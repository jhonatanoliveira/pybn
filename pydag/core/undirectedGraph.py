from pydag.core.dag import DAG
from pydag.core.graph import Graph


class UndirectedGraph(Graph):

    """
    Represents an undirected graph.
    """

    def __init__(self, *args):
        """
        Input: (None)
        Output: (None)
        Description: An undirected graph can be constructed from a DAG.
        """
        Graph.__init__(self)

        if len(args) == 1:
            if isinstance(args[0], DAG):
                self.setVariables(args[0].getVariables().copy())
                self.setEdges(args[0].getEdges().copy())

    def hasEdge(self, edge):
        """
        Input: edge (tuple(Variable,Variable))
        Output: variableNeighbors (Boolean)
        Description: Check if given edge is in UndirectedGraph.
        """
        return (edge in self.getEdges()) or ((edge[1], edge[0]) in self.getEdges())

    def copy(self):
        """
        Input: (None)
        Output: copiedDag (DAG)
        Description: Make a copy of this DAG by copying the variables and edges.
        """
        copiedUndirectedGraph = UndirectedGraph()
        copiedUndirectedGraph.setVariables(self.getVariables().copy())
        copiedUndirectedGraph.setEdges(self.getEdges().copy())
        return copiedUndirectedGraph
