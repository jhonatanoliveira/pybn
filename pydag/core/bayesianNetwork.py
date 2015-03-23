class BayesianNetwork:

	def setCPTs(self,cpts):
		self.CPTs = cpts

	def getCPTs(self):
		return self.CPTs

	def setDAG(self,dag):
		self.DAG = dag

	def getDAG(self):
		return self.DAG