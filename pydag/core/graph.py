from pydag.core.orderedSet import OrderedSet


class Graph:

    """
    A general graph implementation, with set of variables an edges. It is used to define specific graphs like Directed Acyclic Graphs (DAGs) or Undirected Graphs.
    """

    def __init__(self):
        """
        Input: (None)
        Output: (None)
        Description: The *variables* are a *OrderedSet* of *Variable*. The *edges* are a *OrderedSet* of *tuples* of size two. This tuple has two *Variable*, indicating a direct connection with the variables with respective name.
        """
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

    def setVariables(self, variables):
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

    def setEdges(self, edges):
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

    def addVariable(self, variable):
        """
        Input: variable (Variable)
        Output: (None)
        Description: Add one variable to the set of variables.
        """
        self.variables.add(variable)

    def addEdge(self, edge):
        """
        Input: edge (tuple(Variable,Variable))
        Output: (None)
        Description: Add one edge to the set of edges.
        """
        self.edges.add(edge)

    def add(self, variable1, variable2):
        """
        Input: variable1 (Variable), variable2 (Variable)
        Output: (None)
        Description: A shortcut to add variables and edges simultaneously.
        """
        if variable1 not in self.variables:
            self.addVariable(variable1)
        if variable2 not in self.variables:
            self.addVariable(variable2)
        self.addEdge((variable1, variable2))

    def neighbors(self, variable):
        """
        Input: variable (Variable)
        Output: variableNeighbors (OrderedSet)
        Description: Return variables being neighbors (has an edge to) variable.
        """
        variableNeighbors = OrderedSet()
        for e in self.edges:
            if e[0] == variable:
                variableNeighbors.add(e[1])
            elif e[1] == variable:
                variableNeighbors.add(e[0])
        return variableNeighbors

    def hasEdge(self, edge):
        """
        Input: edge (tuple(Variable,Variable))
        Output: variableNeighbors (Boolean)
        Description: Check if given edge is in Graph.
        """
        return edge in self.getEdges()

    def removeVariable(self, variable):
        """
        Input: variable (Variable)
        Output: (None)
        Description: Remove a variable from a graph, including all edges involving this variable.
        """
        self.variables.remove(variable)
        for e in self.getEdges():
            if (e[0] == variable or e[1] == variable):
                self.edges.remove(e)

    def removeVariables(self, variables):
        """
        Input: variables ([Variable])
        Output: (None)
        Description: Remove all variables from the graph, including all edges involving those variables.
        """
        for v in variables:
            self.removeVariable(v)
