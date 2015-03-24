from pydag.core.orderedSet import OrderedSet
from pydag.core.dseparation import dSeparation


class InferenceEngine:

    def __init__(self, bn):
        self.BN = bn
        self.originalBN = bn.copy()
        self.queryVariables = OrderedSet()
        self.evidenceVariables = OrderedSet()

    def run(self):
        pass

    def getBN(self):
        return self.BN

    def setBN(self, bn):
        self.BN = bn

    def setQueryVariables(self, queryVariables):
        self.queryVariables = queryVariables

    def getQueryVariables(self):
        return self.queryVariables

    def setEvidenceVariables(self, evidencesVariables):
        self.evidencesVariables = evidencesVariables

    def getEvidenceVariables(self):
        return self.evidencesVariables

    def beliefUpdate(self, evidences):
        pass

    def getBarrenVariables(self):
        result = OrderedSet()
        for leaf in self.BN.getDAG().leaves():
            if (leaf not in self.getQueryVariables()) and (leaf not in self.getEvidenceVariables()):
                result.add(leaf)
        return result

    def getIndependentByEvidenceVariables(self):
        independentVariables = OrderedSet()
        for variable in self.getBN().getDAG().getVariables():
            if (variable not in self.getQueryVariables()) and (variable not in self.getEvidenceVariables()):
                dSep = dSeparation(variable, self.getEvidenceVariables(), self.getQueryVariables())
                if dSep.test():
                    independentVariables.add(variable)
        return independentVariables
