from pybn.core.undirectedGraph import UndirectedGraph
from pybn.core.orderedSet import OrderedSet
from pybn.inference.inferenceEngine import InferenceEngine
from pybn.inference.eliminationOrdering import EliminationOrdering
from time import time


class VariableElimination(InferenceEngine):

    def __init__(self, bn):
        InferenceEngine.__init__(self, bn)
        self.eliminationOrdering = OrderedSet()

    def setEliminationOrdering(self, elimnOrd):
        self.eliminationOrdering = elimnOrd

    def run(self):
        originalRoots = self.getBN().getDAG().roots()  # save roots for later
        # Remove barren variables
        self.removeBarrenVariables()
        # Remove independen by evidence variables
        self.removeIndependenceByEvidenceVariables()
        # Build 1(v) for all current roots which were not root in the original BN
        currentRoots = self.getBN().getDAG().roots()
        newRoots = currentRoots - originalRoots
        self.constructOneVariable(newRoots)
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
        finalResult = (finalProduct / divCPT)
        return finalResult

    def beliefUpdate(self, evidences):
        evidenceVars = OrderedSet()
        for var in evidences:
            evidenceVars.add(var)
            relevantCPTs = self.BN.getCPTs().getCPTsByVariable(var)
            for cpt in relevantCPTs:
                cpt.keepRows({var: evidences[var]})
        self.setEvidenceVariables(evidenceVars)

    def setOneEliminationOrdering(self):
        moralizedDAG = self.BN.getDAG().moralize()
        ud = UndirectedGraph(moralizedDAG)
        e = EliminationOrdering(ud)
        elimVars = self.BN.getDAG().getVariables() - (self.getQueryVariables() + self.getEvidenceVariables())
        elimOrd = e.findEliminationOrdering(e.weightedMinFill, elimVars)
        self.setEliminationOrdering(elimOrd)

    def removeIndependenceByEvidenceVariables(self):
        indepVars = self.getIndependentByEvidenceVariables()
        self.BN.getCPTs().removeCPTsByAllHeadVariables(indepVars)
        self.BN.getDAG().removeVariables(indepVars)

    def removeBarrenVariables(self):
        barren = self.getBarrenVariables()
        while barren:
            # remove CPTs of barren variables
            self.BN.getCPTs().removeCPTsByAllHeadVariables(barren)
            # remove barren variables from the DAG
            self.BN.getDAG().removeVariables(barren)
            barren = self.getBarrenVariables()

    def constructOneVariable(self, variables):
        oldCpts = self.getBN().getCPTs().getCPTsByHeadVariables(variables)
        for variable in variables:
            for cpt in oldCpts:
                varIndices = OrderedSet()
                for t in cpt.getTail():
                    varIndices.add(cpt.getGlobalReferenceVarInd(t))
                    cpt.removeTailVariable(t)
                cpt.removeColumns(varIndices)
                for row in cpt.getTable():
                    cpt.set(row, 1.0)
