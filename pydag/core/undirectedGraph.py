from pydag.core.dag import DAG
from pydag.core.graph import Graph

class UndirectedGraph(Graph):

	def __init__(self,*args):
		Graph.__init__(self)

		if len(args) == 1:
			if isinstance(args[0],DAG):
				self.setVariables(args[0].getVariables().copy())
				self.setEdges(args[0].getEdges().copy())

	def hasEdge(self,edge):
		"""
		Input: edge (tuple(Variable,Variable))
		Output: variableNeighbors (Boolean)
		Description: Check if given edge is in UndirectedGraph.
		"""
		return (edge in self.getEdges()) or ((edge[1],edge[0]) in self.getEdges())