from ordered_set import OrderedSet

class Graph:

	def __init__(self):
		self.variables = OrderedSet()
		self.edges = OrderedSet()

	def __str__(self):
		"""
		Input: (None)
		Output: (None)
		Description: How to print a Graph.
		"""
		toPrint = ""
		toPrint = toPrint + "Variables: \n"
		for v in self.getVariables():
			toPrint = toPrint + v.__str__() + ","
		toPrint = toPrint[0:-1]
		toPrint = toPrint + "\n"
		toPrint = toPrint + "Edges: \n"
		for e in self.getEdges():
			toPrint = toPrint + "("
			for v in e:
				toPrint = toPrint + v.__str__() + ","
			toPrint = toPrint[0:-1]
			toPrint = toPrint + ")"
			toPrint = toPrint + " "
		toPrint = toPrint + "\n"
		return toPrint

	def setVariables(self,variables):
		"""
		Input: variables (OrderedSet(Variable))
		Output: (None)
		Description: set all variables in this Graph.
		"""
		self.variables = variables

	def getVariables(self):
		"""
		Input: (None)
		Output: (None)
		Description: Return all variables.
		"""
		return self.variables

	def setEdges(self,edges):
		"""
		Input: edges (OrderedSet(tuple(Variable,Variable)))
		Output: (None)
		Description: set all edges in this Graph.
		"""
		self.edges = edges

	def getEdges(self):
		"""
		Input: (None)
		Output: (None)
		Description: Return all edges.
		"""
		return self.edges

	def addVariable(self,variable):
		"""
		Input: variable (Variable)
		Output: (None)
		Description: Add one variable to the set of variables.
		"""
		self.variables.add(variable)

	def addEdge(self,edge):
		"""
		Input: edge (tuple(Variable,Variable))
		Output: (None)
		Description: Add one edge to the set of edges.
		"""
		self.edges.add(edge)

	def add(self,variable1, variable2):
		"""
		Input: variable1 (Variable), variable2 (Variable)
		Output: (None)
		Description: A shortcut to add variables and edges simultaneously.
		"""
		if variable1 not in self.variables:
			self.addVariable(variable1)
		if variable2 not in self.variables:
			self.addVariable(variable2)
		self.addEdge((variable1,variable2))