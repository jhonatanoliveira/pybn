class Variable:

	def __init__(self):
		self.name = ""
		self.domain = []

	def setName(self,varName):
		self.name = varName

	def addDomain(self,domain):
		self.domain.append(domain)

	def removeDomain(self,domain):
		self.domain.remove(domain)

	def getName(self):
		return self.name

	def getDomain(self):
		return self.domain