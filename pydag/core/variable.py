class Variable:
	"""
	Represent a variable in a DAG or a CPT. A variable depends almost completly on its name (a string). A variable is equal to another if they have the same name and it is hashable by the hash of its name (a hash of a string).
	"""

	def __init__(self, name = ""):
		"""
		Input: name (str)
		Output: (None)
		Description: A variable can be created with a given name or no name.
		"""
		self.name = name
		self.domain = [] # Can be a list with strings, for instance

	def __str__(self):
		"""
		Input: (None)
		Output: (None)
		Description: A special function in Python, called when "print" is called on an object of this class. Prints the name of the variable.
		"""
		return self.name

	def __eq__(self,other):
		"""
		Input: other (Variable)
		Output: (None)
		Description: Two variables are equal if they have the same name.
		"""
		return self.name == other.name

	def __hash__(self):
		"""
		Input: (None)
		Output: (None)
		Description: The hash of a variable is the hash of its name.
		"""
		return hash(self.name)

	def addDomain(self,domain):
		"""
		Input: domain (str/int)
		Output: (None)
		Description: Add a domain (integer or string) to the variable.
		"""
		self.domain.append(domain)

	def removeDomain(self,domain):
		"""
		Input: domain (str/int)
		Output: (None)
		Description: Remove a domain (integer or string) of the variable.
		"""
		self.domain.remove(domain)

	def getDomain(self):
		"""
		Input: (None)
		Output: (list[str/int])
		Description: Return the whole list with domain values of the variable.
		"""
		return self.domain

	def setName(self,varName):
		"""
		Input: varName (str)
		Output: (None)
		Description: Set the name of the variable.
		"""
		self.name = varName

	def getName(self):
		"""
		Input: (None)
		Output: (str)
		Description: Return the name of the variable.
		"""
		return self.name

