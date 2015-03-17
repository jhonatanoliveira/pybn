from ordered_set import OrderedSet
from bitarray import bitarray

class DAG:
	def __init__(self):
		self.variables = OrderedSet()
		self.edges = OrderedSet()
		self.transitiveClosureMap = {}

	def addVariable(self,variable):
		self.variables.add(variable)

	def addEdge(self,edge):
		self.edges.add(edge)

	def add(self,variable1, variable2):
		if variable1 not in self.variables:
			self.addVariable(variable1)
		if variable2 not in self.variables:
			self.addVariable(variable2)
		self.addEdge((variable1,variable2))

	def parents(self,variables):
		if type(variables) == str:
			variables = OrderedSet([variables])
		parents = OrderedSet()
		for variable in variables:
			for edge in self.edges:
				if edge[1] == variable:
					parents.add(edge[0])
		return parents

	def children(self,variables):
		if type(variables) == str:
			variables = OrderedSet([variables])
		children = OrderedSet()
		for variable in variables:
			for edge in self.edges:
				if edge[0] == variable:
					children.add(edge[1])
		return children

	def ancestors(self, variables):
		if len(self.transitiveClosureMap) == 0:
			self.transitiveClosureMap = self.transitiveClosure()
		results = []
		for variable in variables:
			varInd = self.transitiveClosureMap["topologicalSort"].index(variable)
			l = [key for key in self.transitiveClosureMap["maps"] if (key != variable and self.transitiveClosureMap["maps"][key][varInd] == True)]
			results.extend(l)
		return OrderedSet(results)

	def ancestorsInParallel(self,variables,result):
		result.append(self.ancestors(variables))

	def preLoadTransitiveClosure(self):
		self.transitiveClosureMap = self.transitiveClosure()

	def transitiveClosure(self):
		topoSort = self.topologicalSort()
		topoSort.reverse()
		numVar = len(self.variables)
		# initializing variables
		result = {}
		for i in range(0,numVar):
			tmp = bitarray(numVar)
			tmp.setall(False)
			tmp[i] = True
			result[topoSort[i]] = tmp
		# for each variable in the DAG (inversed topological sort)
		for variable in topoSort:
			for parent in self.parents(variable):
				result[parent] = result[parent] | result[variable]

		return {"maps": result, "topologicalSort": topoSort}

	def roots(self):
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
		First described by Kahn (1962), Wikipedia
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
		return L

	def descendants(self,variables):
		if type(variables) == str:
			variables = OrderedSet([variables])
		descendants = OrderedSet()
		for v in self.variables:
			Anv = self.ancestors(v)
			if Anv.intersection(variables).__len__() > 0:
				descendants.add(v)
		return descendants

	def vstructures(self):
		vstructures = OrderedSet()
		for v in self.variables:
			if self.parents(v).__len__() > 1:
				vstructures.add(v)
		return vstructures

	def isVstructure(self,variable):
		result = False
		if self.parents(variable).__len__() > 1:
			result = True
		return result
