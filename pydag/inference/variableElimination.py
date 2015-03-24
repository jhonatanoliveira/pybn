from pydag.core.undirectedGraph import UndirectedGraph
from pydag.core.orderedSet import OrderedSet
from pydag.inference.inferenceEngine import InferenceEngine
from pydag.inference.eliminationOrdering import EliminationOrdering


class VariableElimination(InferenceEngine):

    def __init__(self, bn):
        InferenceEngine.__init__(self, bn)
        self.eliminationOrdering = []

    def setEliminationOrdering(self, elimnOrd):
        self.eliminationOrdering = elimnOrd

    def run(self):
        # Remove barren variables
        self.removeBarrenVariables()
        # Find one elimination ordering
        if len(self.eliminationOrdering) == 0:
            self.setOneEliminationOrdering()
        # Eliminate each variable
        for v in self.eliminationOrdering:
            relevantCPTs = self.BN.getCPTs().getCPTsByVariable(v)
            self.BN.getCPTs().removeCPTs(relevantCPTs)
            if len(relevantCPTs) > 0:
                product = relevantCPTs[0]
                for i in range(1, len(relevantCPTs)):
                    product *= relevantCPTs[i]
                marginalizeVars = product.getHead()
                marginalizeVars.remove(v)
                product = product.marginalize(marginalizeVars)
                self.BN.getCPTs().add(product)
        finalProduct = None
        if len(self.BN.getCPTs()) > 1:
            finalProduct = self.BN.getCPTs()[0]
            for i in range(1, len(self.BN.getCPTs())):
                finalProduct *= self.BN.getCPTs()[i]
        else:
            finalProduct = self.BN.getCPTs()[0]
        divCPT = finalProduct.marginalize(self.getEvidenceVariables())
        return (finalProduct / divCPT)

    def beliefUpdate(self, evidences):
        evidenceVars = []
        for var in evidences:
            evidenceVars.append(var)
            relevantCPTs = self.BN.getCPTs().getCPTsByVariable(var)
            for cpt in relevantCPTs:
                cpt.keepRows({var: evidences[var]})
        self.setEvidenceVariables(evidenceVars)

    def setOneEliminationOrdering(self):
        moralizedDAG = self.BN.getDAG().moralize()
        ud = UndirectedGraph(moralizedDAG)
        e = EliminationOrdering(ud)
        elimVars = self.BN.getDAG().getVariables() - \
            OrderedSet(self.getQueryVariables() + self.getEvidenceVariables())
        elimOrd = e.findEliminationOrdering(e.weightedMinFill, elimVars)
        self.setEliminationOrdering(elimOrd)

    def removeBarrenVariables(self):
        barren = self.getBarrenVariables()
        while barren:
            # remove CPTs of barren variables
            self.BN.getCPTs().removeCPTsByAllHeadVariables(barren)
            # remove barren variables from the DAG
            self.BN.getDAG().removeVariables(barren)
            barren = self.getBarrenVariables()
