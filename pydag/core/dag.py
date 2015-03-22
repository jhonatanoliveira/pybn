from pydag.core.graph import Graph
from pydag.core.variable import Variable
from ordered_set import OrderedSet
from bitarray import bitarray

class DAG(Graph):
	"""
	A Directed Acyclic Graph (DAG) is here represented by a (ordered) set of variables and a (ordered) set of edges (tuples). This implementation also does common operations on a DAG, like computing ancestors, topological sort, finding all v-structures, among other.
	"""
	def __init__(self):
		"""
		Input: (None)
		Output: (None)
		Description: The *variables* are a *OrderedSet* of *Variable*. The *edges* are a *OrderedSet* of *tuples* of size two. This tuple has two *Variable*, indicating a direct connection with the variables with respective name. The *transitiveClosureDict* is to save one possible Topological Sort (or Ordering). The *transitiveClosureDict* is to save the Transitive Closure of the DAG.
		"""
		Graph.__init__(self)
		# Members to save recurrent properties of the DAG (that is, they're used to save something that is intrinsic of the DAG and can be reused later - a kind of precomputation).
		self.topologicalSortList = []
		self.transitiveClosureDict = {}

	def copy(self):
		"""
		Input: (None)
		Output: copiedDag (DAG)
		Description: Make a copy of this DAG by copying the variables and edges.
		"""
		copiedDag = DAG()
		copiedDag.setVariables(self.getVariables().copy())
		copiedDag.setEdges(self.getEdges().copy())
		return copiedDag

	def parents(self,variables):
		"""
		Input: variables (list[Variable])
		Output: parents (OrderedSet(Variable))
		Description: Return a set with all parents of all variables in *variables*.
		"""
		if isinstance(variables,Variable):
			variables = OrderedSet([variables])
		parents = OrderedSet()
		for variable in variables:
			for edge in self.edges:
				if edge[1] == variable:
					parents.add(edge[0])
		return parents

	def children(self,variables):
		"""
		Input: variables (list[Variable])
		Output: children (OrderedSet(Variable))
		Description: Return a set with all children of all variables in *variables*.
		"""
		if isinstance(variables,Variable):
			variables = OrderedSet([variables])
		children = OrderedSet()
		for variable in variables:
			for edge in self.edges:
				if edge[0] == variable:
					children.add(edge[1])
		return children

	def ancestors(self, variables):
		"""
		Input: variables (list[Variable])
		Output: result (OrderedSet(Variable))
		Description: Return a set with all ancestors for each given variable.
		"""
		if type(variables) == str:
			variables = OrderedSet([variables])
		if len(self.allAncestors) == 0:
			self.loadAllAncestors()
		result = OrderedSet()
		for variable in variables:
			tmp = self.allAncestors[variable]
			result = result.union( tmp )
		return result

	def descendants(self,variables):
		"""
		Input: variables (list[Variable])
		Output: descendants (OrderedSet(Variable))
		Description: Return a set with all descendants for each given variable.
		"""
		if type(variables) == str:
			variables = OrderedSet([variables])
		descendants = OrderedSet()
		for v in self.variables:
			Anv = self.ancestors(v)
			if len(Anv.intersection(variables)) > 0:
				descendants.add(v)
		return descendants

	def loadTransitiveClosure(self):
		"""
		Input: (None)
		Output: (None)
		Description: A function to do pre-computation, that is, load in advance the transitive closure of the DAG.
		"""
		self.transitiveClosureDict = self.transitiveClosure()

	def loadAllAncestors(self):
		"""
		Input: (None)
		Output: (None)
		Description: A function to do pre-computation, that is, load in advance all ancestors for each variable of the DAG.
		"""
		if len(self.transitiveClosureDict) == 0:
			self.transitiveClosureDict = self.transitiveClosure()
		results = {}
		for variable in self.variables:
			varInd = self.topologicalSortList.index(variable)
			l = [key for key in self.transitiveClosureDict if (key != variable and self.transitiveClosureDict[key][varInd] == True)]
			results[variable] = OrderedSet(l)
		self.allAncestors = results

	def transitiveClosure(self):
		"""
		Input: (None)
		Output: result (dict[Variable] = bitarray)
		Description: Compute the inversed transitive closure of a DAG. In simple words, the transitive closure for each variable in the DAG tells to which ancestors variables it has a connection (via directed edge). This is done by transitivity. For example, if a -> b -> c, then a -> c. This transitive closure is inversed because it start from the bottom (leafes) up (roots). This implementation uses arrays of bits for optimizing the computation.
		"""
		if len(self.topologicalSortList) == 0:
			self.topologicalSortList = self.topologicalSort()
		numVar = len(self.variables)
		# initializing variables
		result = {}
		for i in range(0,numVar):
			tmp = bitarray(numVar)
			tmp.setall(False)
			tmp[i] = True
			result[self.topologicalSortList[i]] = tmp
		# for each variable in the DAG (inversed topological sort)
		for variable in self.topologicalSortList:
			for parent in self.parents(variable):
				result[parent] = result[parent] | result[variable]
		return result

	def roots(self):
		"""
		Input: (None)
		Output: roots (OrderedSet(Variable))
		Description: Return a set with all root variables in a DAG. Root variables are those without directed edge to them.
		"""
		left = []
		right = []
		for edge in self.edges:
			left.append(edge[0])
			right.append(edge[1])
		roots = OrderedSet()
		for variable in self.variables:
			if variable not in right:
				roots.add(variable)
		return roots

	def topologicalSort(self):
		"""
		Input: (None)
		Output: L (OrderedSet(Variable))
		Description: Compute one possible topological sort (or ordering) for the DAG. Algorithm took from Wikipedia. A topological sort of a DAG G is an ordering of the vertices of G such that for every edge (vi, vj) of G we have i < j. This implementation was first described by Kahn (1962).
		"""
		L = []
		S = self.roots()
		allEdges = self.edges.copy()
		while S:
			n = S.pop()
			L.append(n)
			l1 = [(n1,m1) for (n1,m1) in allEdges if n1==n]
			for (n,m) in l1:
				allEdges.remove((n,m))
				incomingToM = [(n2,m2) for (n2,m2) in allEdges if m2==m]
				if len(incomingToM) == 0:
					S.add(m)
		if len(allEdges) > 0:
			print "Error: graph has at least one cycle"
		L.reverse()
		return L

	def vstructures(self):
		"""
		Input: (None)
		Output: vstructures (OrderedSet(Variable))
		Description: Return all v-structures of a DAG. A variable is a v-structure if it has more than one parent.
		"""
		vstructures = OrderedSet()
		for v in self.variables:
			if len(self.parents(v)) > 1:
				vstructures.add(v)
		return vstructures

	def isVstructure(self,variable):
		"""
		Input: variable (Variable)
		Output: result (Boolean)
		Description: Verify if a given variable is a v-structure. A variable is a v-structure if it has more than one parent.
		"""
		result = False
		if len(self.parents(variable)) > 1:
			result = True
		return result

	def moralize(self):
		"""
		Input: (None)
		Output: moralizedDag (DAG)
		Description: Returns the moralized DAG, created by adding edges between parents of v-structures (variables with more than one parents). The moralized DAG is a exactly copy of this DAG, but with (possibly) more edges.
		"""
		moralizedDag = self.copy()
		allVstructures = moralizedDag.vstructures()
		for v in allVstructures:
			parentsOfVstructure = moralizedDag.parents(v)
			moralizedDag.addEdge((parentsOfVstructure[0],parentsOfVstructure[1]))
		return moralizedDag
