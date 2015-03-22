class InferenceEngine:

	def __init__(self,cpts):
		self.cpts = cpts.copy()
		self.originalCpts = cpts.copy()
		self.queryVariables = []
		self.evidencesVariables = []

	def run(self):
		pass

	def setQueryVariables(self,queryVariables):
		self.queryVariables = queryVariables

	def setEvidencesVariables(self,evidencesVariables):
		self.evidencesVariables = evidencesVariables