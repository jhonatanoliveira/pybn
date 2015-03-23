from pydag.core.orderedSet import OrderedSet

class EliminationOrdering:
	"""
	This class implements tools to help finding good elimination orderings. Besically, a greedy algorithm scores the variables currently in the Graph, pick one, removing it, and score the graph again.
	"""

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

	def weightedMinFill(self,variable):
		edges = self.edgesNeededToBeAdded(variable)
		sumWeight = 0
		for edge in edges:
			sumWeight = sumWeight + len(edge[0].getDomain()) * len(edge[1].getDomain())
		return sumWeight

	def minNeighbors(self,variable):
		return len(self.undirectedGraph.neighbors(variable))

	def minWeight(self,variable):
		product = 1
		for neighbor in self.undirectedGraph.neighbors(variable):
			product = product * len(neighbor.getDomain())
		return product

	def minFill(self,variable):
		return len(self.undirectedGraph.neighbors(variable))

	def findEliminationOrdering(self,costFunc,variables):
		ordering = []
		while variables:
			scorings = [{"variable": v, "score": costFunc(v)} for v in variables]
			sortedScorings = sorted(scorings, key=lambda k: k['score'])
			ordering.append(sortedScorings[0]["variable"])
			variables.remove(sortedScorings[0]["variable"])
		return ordering