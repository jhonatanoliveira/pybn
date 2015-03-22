from pydag.core.orderedSet import OrderedSet

class EliminationOrdering:

	def __init__(self,undirectedGraph):
		self.variables = OrderedSet()
		self.undirectedGraph = undirectedGraph

	def edgesNeededToBeAdded(self,variable):
		edges = OrderedSet()
		neighbors = self.undirectedGraph.neighbors(variable)
		for neighbor1 in neighbors:
			for neighbor2 in neighbors:
				if neighbor1 != neighbor2:
					if (not self.undirectedGraph.hasEdge((neighbor1,neighbor2))) and ((neighbor1,neighbor2) not in edges) and ((neighbor2,neighbor1) not in edges):
						edges.add((neighbor1,neighbor2))
		return edges
