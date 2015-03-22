from pydag.core.ordered_set import OrderedSet

class EliminationOrdering:

	def __init__(self,elimVariables,moralizedDAG):
		self.variables = elimVariables
		self.moralizedDAG = moralizedDAG

	def edgesNeededToBeAdded(self,variable):
		edges = OrderedSet()
		allEdgesInvolvingVariable = [e for e in self.moralizedDAG.getEdges() if (e[0] == variable) or (e[1] == variable)]
		for edge in allEdgesInvolvingVariable:
			for otherEdge in allEdgesInvolvingVariable:
				if edge != otherEdge:
					try:
						variableInd1 = edge.index(variable)
					except ValueError:
						variableInd1 = -1
					try:
						variableInd2 = otherEdge.index(variable)
					except ValueError:
						variableInd2 = -1
					for i in range(0,len(edge)):
						if i != variableInd1:
							for i2 in range(0,len(otherEdge)):
								if i2 != variableInd2:
									if edge[i] != otherEdge[i2]:
										pass

		return len(allEdgesInvolvingVariable)
