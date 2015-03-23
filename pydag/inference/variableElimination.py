from pydag.core.undirectedGraph import UndirectedGraph
from pydag.core.orderedSet import OrderedSet
from pydag.inference.inferenceEngine import InferenceEngine
from pydag.inference.eliminationOrdering import EliminationOrdering

class VariableElimination(InferenceEngine):

	def __init__(self,bn):
		InferenceEngine.__init__(self,bn)
		self.eliminationOrdering = []

	def setEliminationOrdering(self,elimnOrd):
		self.eliminationOrdering = elimnOrd

	def run(self):
		if len(self.eliminationOrdering) == 0:
			self.setOneEliminationOrdering()
		copiedCPTs = self.BN.getCPTs().copy()
		for v in self.eliminationOrdering:
			relevantCPTs = copiedCPTs.getCPTsByVariable(v)
			copiedCPTs.removeCPTs(relevantCPTs)
			if len(relevantCPTs) > 0:
				product = relevantCPTs[0]
				for i in range(1,len(relevantCPTs)):
					product *= relevantCPTs[i]
				marginalizeVars = product.getHead()
				marginalizeVars.remove(v)
				product = product.marginalize( marginalizeVars )
				copiedCPTs.add(product)
		finalProduct = None
		if len(copiedCPTs) > 1:
			finalProduct = copiedCPTs[0]
			for i in range(1,len(copiedCPTs)):
				finalProduct *= copiedCPTs[i]
		else:
			finalProduct = copiedCPTs[0]
		divCPT = finalProduct.marginalize( self.getEvidenceVariables() )
		print finalProduct / divCPT

	def beliefUpdate(self,evidences):
		evidenceVars = []
		for var in evidences:
			evidenceVars.append(var)
			relevantCPTs = self.BN.getCPTs().getCPTsByVariable(var)
			for cpt in relevantCPTs:
				cpt.removeRows({var: evidences[var]})
		self.setEvidenceVariables(evidenceVars)

	def setOneEliminationOrdering(self):
		moralizedDAG = self.BN.getDAG().moralize()
		ud = UndirectedGraph( moralizedDAG )
		e = EliminationOrdering(ud)
		elimVars = self.BN.getDAG().getVariables() - OrderedSet( self.getQueryVariables() + self.getEvidenceVariables() )
		elimOrd = e.findEliminationOrdering(e.weightedMinFill, elimVars )
		self.setEliminationOrdering( elimOrd )