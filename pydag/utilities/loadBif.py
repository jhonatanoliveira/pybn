from pydag.core.dag import DAG
from pydag.core.ordered_set import OrderedSet
from pydag.core.variable import Variable
from pydag.core.cpt import CPT

def loadBif(bifFilePath):
	"""
	Input: bifFilePath (str)
	Output: (dict[str] = DAG/OrderedSet(CPT))
	Description: Given the a string with the path for a bif file, return the DAG and CPTs within a set.
	"""
	
	dag = DAG()
	cpts = OrderedSet()

	bifFile = open(bifFilePath)

	# Control flags
	getVarFlag = False
	getCptFlag = False

	# Temp vars
	tempVar = Variable()
	tempVars = {}
	tempCpt = CPT()
	tempCpts = {}

	for line in bifFile:

		# Construct the DAG
		if getCptFlag or line.find("probability") == 0:
			if not getCptFlag:
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
						else:
							head.pop()
						headFlag = False
						tailFlag = False
				
				# add edge in BN
				if len(tail) != 0:
					for parent in tail:
						for child in head:
							dag.add(tempVars[parent],tempVars[child])

				# Save head and tail to temporary CPT
				headVars = []
				for headVar in head:
					headVars.append( tempVars[headVar] )
				tempCpt.setHead(headVars)
				tailVars = []
				for tailVar in tail:
					tailVars.append( tempVars[tailVar] )
				tempCpt.setTail(tailVars)

				getCptFlag = True

			else:
				# Construct the table while } is not found
				if line.find("}") == -1:
					splitLine = line.strip()
					domainSplit = []
					probabilitiesSplit = []

					if splitLine.find("table") == 0:
						probabilitiesSplit = splitLine.replace("table ","").replace(";","").split(",")
					else:
						domainSplit = splitLine.split(")")[0].replace("(","").split(",")
						domainSplit = [s.strip() for s in domainSplit]
						probabilitiesSplit = splitLine.split(")")[1].replace("(","").replace(";","").split(",")

					probabilitiesSplit = [float(s.strip()) for s in probabilitiesSplit]

					for headVar in tempCpt.getHead():
						counter = 0
						for domainValue in headVar.getDomain():
							tableKey = [domainValue] + domainSplit
							tableValue = probabilitiesSplit[counter]
							tempCpt.add(tuple(tableKey), tableValue)
							counter = counter + 1
				else:
					tempCpts[tempCpt.getHeadAsVarsTuple()] = tempCpt
					tempCpt = CPT()
					getCptFlag = False

		# Construct domain of Variables
		elif getVarFlag or line.find("variable") == 0:
			splitLine = line.split()
			if not getVarFlag:
				varName = ""
				controlFlag = False
				for term in splitLine:
					if controlFlag:
						varName = varName + term

					if term == "variable":
						controlFlag = True
					elif term == "{":
						varName = varName.replace("{","")
						controlFlag = False
				tempVar.setName(varName)
				getVarFlag = True
			else:
				if line.find("  type discrete") == 0:
					controlFlag = False
					for term in splitLine:
						if controlFlag:
							tempVar.addDomain( term.replace(",","") )

						if term == "{":
							controlFlag = True
						elif term == "};":
							tempVar.removeDomain("};")
							controlFlag = False
					tempVars[tempVar.getName()] = tempVar
					tempVar = Variable()
					getVarFlag = False
				else:
					print "ERROR! Not discrete variable!"


	return {"DAG": dag, "CPTs": tempCpts}