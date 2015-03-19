class CPT:

	def __init__(self):
		self.head = []
		self.tail = []
		self.table = {}

	def add(self,key,value):
		self.table[key] = value

	def setHead(self,head):
		self.head = head

	def getHead(self):
		return self.head

	def setTail(self,tail):
		self.tail = tail

	def getProbability(self,key):
		return self.table[key]