from pydag.core.dag import DAG
from pydag.core.ordered_set import OrderedSet

def loadBif(bifFilePath):
	
	dag = DAG()

	bifFile = open(bifFilePath)
	for line in bifFile:
		if line.find("probability") == 0:
			splitLine = line.replace(",","").split()
			head = []
			tail = []
			headFlag = False
			tailFlag = False
			for term in splitLine:
				if headFlag:
					head.append(term)
				elif tailFlag:
					tail.append(term)

				if term == "(":
					headFlag = True
				elif term == "|":
					head.pop()
					headFlag = False
					tailFlag = True
				elif term == ")":
					if len(tail) != 0:
						tail.pop()
					headFlag = False
					tailFlag = False
			
			# add edge in BN
			if len(tail) != 0:
				for parent in tail:
					for child in head:
						dag.add(parent,child)
	dag.preLoadTransitiveClosure()
	return dag