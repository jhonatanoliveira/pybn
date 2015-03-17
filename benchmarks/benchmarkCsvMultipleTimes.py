from dag import DAG
from dseparation import dSeparation
from iseparation import iSeparation
from plotReachabilityResult import *
from loadBif import *
from random import *
from time import time
import csv
from ordered_set import OrderedSet

## CONTROL ##
# datasets = ["alarm","barley","child","hailfinder","insurance","mildew","water"] # Medium
# csvName = "benchmarkDSepISep_medium"
# datasets = ["hepar2","win95pts"] # Large
# csvName = "benchmarkDSepISep_large"
datasets = ["andes","link","pathfinder","pigs"] # Very Large
csvName = "benchmarkDSepISep_very_large"
# datasets = ["munin"] # Massive
# csvName = "benchmarkDSepISep_massive"
# datasets = ["diabetes"] # Diabetes
# csvName = "benchmarkDSepISep_diabetes"
# numExperiments = 50
experiments = [10,20,50,100,500,1000]
# *** Benchmark ***

for numExperiments in experiments:
	results = []
	for dataset in datasets:

		### DEBUG
		# print
		# print "Initializing " + dataset + " ..."
		# print
		### --- DEBUG

		dag = loadBif("datasets/" + dataset + ".bif")

		sumInaugurals = 0
		sumDsep = 0
		sumTimeAnY = 0
		sumTimeDsep = 0
		sumIsep = 0
		sumTimeAnXYZ = 0
		sumTimeIsep = 0

		for i in range(0,numExperiments):
			### DEBUG
			# print "Testing independence #" + str(i)
			### --- DEBUG

			result = {}
			result["name"] = dataset.capitalize()

			allVariables = [node for node in dag.variables]
			# varX = "nedbarea"
			varX = choice(allVariables)
			allVariables.remove(varX)
			# varY = "markgrm"
			varY = choice(allVariables)
			allVariables.remove(varY)
			# varZ = "dgv5980"
			varZ = choice(allVariables)
			allVariables.remove(varZ)



			# Testing independence
			dSep = dSeparation(OrderedSet([varX]),OrderedSet([varY]),OrderedSet([varZ]),dag)

			# d-Separation
			dSepTime0 = time()
			dSep = dSep.reachable()
			dSepTime1 = time()
			result["dSepTime"] = dSepTime1 - dSepTime0
			result["d-sep"] = dSep["numberOfChecks"]
			result["timeAnY"] = dSep["timeAnY"]


			# Testing independence
			iSep = iSeparation(OrderedSet([varX]),OrderedSet([varY]),OrderedSet([varZ]),dag)
			
			# i-Separation
			iSepTime0 = time()
			iSep = iSep.reachable()
			iSepTime1 = time()
			result["iSepTime"] = iSepTime1 -iSepTime0
			result["i-sep"] = iSep["numberOfChecks"]
			result["timeAnXYZ"] = iSep["timeAnXYZ"]
			


			# Comparisons between them
			result["%% check saving"] = (1 - float(iSep["numberOfChecks"])/float(dSep["numberOfChecks"])) * 100
			result["%% time saving"] = result["iSepTime"]/result["dSepTime"]

			# Inaugurals
			# result["inaugurals"] = dSep.inaugurals().__len__()
			result["inaugurals"] = 0



			# Sum values
			sumInaugurals = sumInaugurals + result["inaugurals"]
			sumDsep = sumDsep + result["d-sep"]
			sumTimeAnY = sumTimeAnY + result["timeAnY"]
			sumTimeDsep = sumTimeDsep + result["dSepTime"]
			sumIsep = sumIsep + result["i-sep"]
			sumTimeAnXYZ = sumTimeAnXYZ + result["timeAnXYZ"]
			sumTimeIsep = sumTimeIsep + result["iSepTime"]

			# results.append(result)

		results.append({"name": dataset.capitalize(),
	    				"inaugurals": float(sumInaugurals)/numExperiments,
	    				"d-sep": sumDsep,
	    				"timeAnY": sumTimeAnY,
	    				"dSepTime": sumTimeDsep,
	    				"i-sep": sumIsep,
	    				"timeAnXYZ": sumTimeAnXYZ,
	    				"iSepTime": sumTimeIsep,
	    				"%% check saving": round((1 - float(sumIsep)/float(sumDsep)) * 100),
	    				"%% time saving": round((1 - float(sumTimeIsep)/float(sumTimeDsep)) * 100)
	    			})

	# Save the CSV file
	with open("results/multiples/%s-%d.csv" %(csvName,numExperiments), "w") as csvfile:
	    fieldnames = ["name", "inaugurals", "d-sep", "timeAnY", "dSepTime", "i-sep", "timeAnXYZ", "iSepTime", "%% check saving", "%% time saving"]
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    writer.writeheader()
	    writer.writerows(results)