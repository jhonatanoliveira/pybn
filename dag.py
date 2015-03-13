from ordered_set import OrderedSet

class DAG:
	def __init__(self):
		self.nodes = OrderedSet()
		self.edges = OrderedSet()

	def addNode(self,node):
		self.nodes.add(node)

	def addEdge(self,edge):
		self.edges.add(edge)

	def add(self,node1, node2):
		if node1 not in self.nodes:
			self.addNode(node1)
		if node2 not in self.nodes:
			self.addNode(node2)
		self.addEdge((node1,node2))

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

	def ancestors(self, variables, includeVariables = False):
		if type(variables) == str:
			variables = OrderedSet([variables])
		parentsOfVariable = self.parents(variables)
		ancestors = parentsOfVariable.copy()
		toCheck = parentsOfVariable.copy()
		while toCheck.__len__() > 0:
			variable = toCheck.pop()
			if variable not in ancestors:
				ancestors.add(variable)
			toCheck = toCheck.union(self.parents(variable))
		if includeVariables:
			ancestors = ancestors.union(variables)
		return ancestors

	def descendants(self,variables):
		if type(variables) == str:
			variables = OrderedSet([variables])
		descendants = OrderedSet()
		for v in self.nodes:
			Anv = self.ancestors(v)
			if Anv.intersection(variables).__len__() > 0:
				descendants.add(v)
		return descendants

	def vstructures(self):
		vstructures = OrderedSet()
		for v in self.nodes:
			if self.parents(v).__len__() > 1:
				vstructures.add(v)
		return vstructures

	def isVstructure(self):
		isVstructure = False
		if self.parents(v).__len__() > 1:
			isVstructure = True
		return isVstructure
