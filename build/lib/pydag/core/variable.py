class Variable:

	def __init__(self, name = ""):
		self.name = name
		self.domain = [] # Can be a list with strings, for instance

	def __str__(self):
		return self.name

	def __eq__(self,other):
		return self.name == other.name

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
