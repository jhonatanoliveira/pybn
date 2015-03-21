class CPT:

	def __init__(self):
		self.head = [] # A list with Variable
		self.tail = []
		self.table = {} # A dictionary with keys as tuples of combination of domain values and values as float number

	def __str__(self):
		printStr = ""
		printHead  = ""
		for v in self.getHead():
			printHead = printHead + v.__str__() + " "
		printHead.strip()
		printTail  = ""
		for v in self.getTail():
			printTail = printTail + v.__str__() + " "
		printTail.strip()
		printStr = printStr + "P (" + printHead + "| " + printTail + ")"
		printStr = printStr + "\n"
		table = ""
		for key in self.getTable():
			table = table + key.__str__() + " => " + self.getTable()[key].__str__()
			table = table + "\n"
		printStr = printStr + table
		return printStr

	def __len__(self):
		return len(self.getTable())

	def copy(self):
		copiedCPT = CPT()
		copiedCPT.head = self.getHead()[:]
		copiedCPT.tail = self.getTail()[:]
		copiedCPT.table = self.getTable().copy()
		return copiedCPT

	def add(self,key,value):
		self.table[key] = value

	def get(self,key):
		return self.getTable()[key]

	def setHead(self,head):
		self.head = head

	def getHead(self):
		return self.head

	def getHeadAsVarsTuple(self):
		return tuple( [v.getName() for v in self.getHead()] )

	def setTail(self,tail):
		self.tail = tail

	def getTail(self):
		return self.tail

	def getProbability(self,key):
		return self.getTable()[key]

	def getVariables(self):
		return self.getHead() + self.getTail()

	def getTable(self):
		return self.table

	def setTable(self,table):
		self.table = table

	def getColumnIndex(self,variable):
		"""
		Input: 'variable' is a 'Variable' type
		Output: a 'int'
		Return the index of a variable on the table, that is the index after putting head and tail variables together.
		For example: if head is 'a' and tail is 'b','c', the index of 'b' is 1.
		"""
		result = -1
		try:
			result = self.getVariables().index(variable)
		except ValueError:
			pass
		return result

	def __mul__(self,other):
		"""
		Multiply two CPTs.
		"""
		# find matching columns (common variables)
		matchingVarIndexes = [(self.getVariables().index(v), other.getVariables().index(v)) for v in self.getVariables() if v in other.getVariables()]
		matchingOtherHeadVarIndexes = [other.getHead().index(v) for v in other.getHead() if ((v in self.getHead()) or (v in self.getTail())) ]
		matchingOtherTailVarIndexes = [len(other.getHead()) + other.getTail().index(v) for v in other.getTail() if ((v in self.getHead()) or (v in self.getTail())) ]
		# construct the resultant cpt
		cptResult = CPT()
		# multiply each row that has matching domain values for all matching variable columns
		for selfRow in self.getTable():
			for otherRow in other.getTable():
				if len(matchingVarIndexes) > 0:
					# verify if tables has common variables, if yes, just multiply on common rows. If not, multiply them all
					allMatchingVarsHasSameValue = True
					for matchingVarIndex in matchingVarIndexes:
						allMatchingVarsHasSameValue = allMatchingVarsHasSameValue and (selfRow[ matchingVarIndex[0] ] == otherRow[ matchingVarIndex[1] ])
					if allMatchingVarsHasSameValue:
						newKeyAndValue = self.constructNewKeyAndValueTable(other,selfRow,otherRow,matchingOtherHeadVarIndexes,matchingOtherTailVarIndexes)
						cptResult.add(newKeyAndValue["newKey"], newKeyAndValue["newValue"])
				else:
					newKeyAndValue = self.constructNewKeyAndValueTable(other,selfRow,otherRow,matchingOtherHeadVarIndexes,matchingOtherTailVarIndexes)
					cptResult.add(newKeyAndValue["newKey"], newKeyAndValue["newValue"])
		# reorganize the head and tail variables
		newHeadAndTail = self.constructNewHeadAndTailForMult(other)
		cptResult.setHead( newHeadAndTail["newHead"] )
		cptResult.setTail( newHeadAndTail["newTail"] )
		return cptResult

	def constructNewHeadAndTailForMult(self,other):
		newHead = self.getHead() + other.getHead()
		newTailSelf = [v for v in self.getTail() if v not in newHead]
		newTailOther = [v for v in other.getTail() if ((v not in newHead) and (v not in newTailSelf))]
		newTail = newTailSelf + newTailOther
		return {"newHead": newHead, "newTail": newTail}

	def constructNewHeadAndTailForDiv(self,other):
		newHead = [v for v in self.getHead() if v not in other.getHead()]
		newTailSelf = [v for v in (self.getHead() + self.getTail()) if v not in newHead]
		newTailOther = [v for v in (other.getHead() + other.getTail()) if ((v not in newHead) and (v not in newTailSelf))]
		newTail = newTailSelf + newTailOther
		return {"newHead": newHead, "newTail": newTail}

	def constructNewKeyAndValueTable(self,other,selfRow,otherRow,matchingOtherHeadVarIndexes,matchingOtherTailVarIndexes):
		# construct new key (re-organizing the order of tuple, if necessary)
		listSelfRow = list(selfRow)
		listOtherRow = list(otherRow)

		newKey = [listSelfRow[i] for i in range(0, len(self.getHead()) ) ]
		newKey.extend( [listOtherRow[i] for i in range(0, len(other.getHead()) ) if i not in matchingOtherHeadVarIndexes ] )

		newKey.extend( [listSelfRow[i] for i in range( len(self.getHead()), len(self.getHead()) + len(self.getTail()) ) ] )
		newKey.extend( [listOtherRow[i] for i in range( len(other.getHead()), len(other.getHead()) + len(other.getTail()) ) if i not in matchingOtherTailVarIndexes ] )

		newKey = tuple(newKey)

		newValue = self.getTable()[selfRow] * other.getTable()[otherRow]
		return {"newKey": newKey, "newValue": newValue}

	def __div__(self,other):
		tempDivCpt = CPT()
		tempDivCpt.setHead( other.getHead() )
		tempDivCpt.setTail( other.getTail() )
		# divide other rows by 1
		for key in other.getTable():
			newValue = 0
			if other.getTable()[key] != 0:
				newValue = 1.0 / other.getTable()[key]
			tempDivCpt.add(key,newValue)
		cptResult = self * tempDivCpt
		# reorganize the head and tail variables
		newHeadAndTail = self.constructNewHeadAndTailForDiv(other)
		cptResult.setHead( newHeadAndTail["newHead"] )
		cptResult.setTail( newHeadAndTail["newTail"] )
		return cptResult

	def marginalize(self,variables):
		if type(variables) != list:
			variables = [variables]
		cptResult = self.copy()
		sumOutVars = [v for v in self.head if v not in variables]
		for v in sumOutVars:
			vInd = cptResult.getColumnIndex(v)
			newTable = {}
			for row in cptResult.getTable():
				listRow = list(row)
				listRow.remove( listRow[vInd] )
				tupleRow = tuple(listRow)
				if newTable.has_key(tupleRow):
					newTable[tupleRow] = newTable[tupleRow] + cptResult.get(row)
				else:
					newTable[tupleRow] = cptResult.get(row)
			cptResult.setTable(newTable)
			# re construct the head variables
			newHead = cptResult.getHead()
			newHead.remove( v )
			cptResult.setHead( newHead )
		return cptResult
