class InferenceEngine:

    def __init__(self, bn):
        self.BN = bn
        self.originalBN = bn.copy()
        self.queryVariables = []
        self.evidenceVariables = []

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
        result = []
        for leaf in self.BN.getDAG().leaves():
            if (leaf not in self.getQueryVariables()) and (leaf not in self.getEvidenceVariables()):
                result.append(leaf)
        return result
