class InferenceEngine:

	def __init__(self,bn):
		self.BN = bn
		self.queryVariables = []
		self.evidenceVariables = []

	def run(self):
		pass

	def setQueryVariables(self,queryVariables):
		self.queryVariables = queryVariables

	def getQueryVariables(self):
		return self.queryVariables

	def setEvidenceVariables(self,evidencesVariables):
		self.evidencesVariables = evidencesVariables

	def getEvidenceVariables(self):
		return self.evidencesVariables

	def beliefUpdate(self,evidences):
		pass
