from dag import DAG
from dseparation import dSeparation
from plotReachabilityResult import *
from loadBif import *
from random import *
from time import *
import csv
from ordered_set import OrderedSet

## CONTROL ##
results = []
# datasets = ["alarm","barley","child","hailfinder","insurance","mildew","water"] # Medium
# csvName = "benchmarkDSepISep_medium"
# datasets = ["hepar2","win95pts"] # Large
# csvName = "benchmarkDSepISep_large"
datasets = ["andes","diabetes","link","pathfinder","pigs"] # Very Large
csvName = "benchmarkDSepISep_very_large"
# datasets = ["munin"] # Massive
# csvName = "benchmarkDSepISep_massive"
debug = False

# *** Benchmark ***

for dataset in datasets:

	### DEBUG
	print
	print "Initializing " + dataset + " ..."
	print
	### --- DEBUG

	dag = loadBif("datasets/" + dataset + ".bif")

	for i in range(0,500):
		### DEBUG
		print "Testing independence #" + str(i)
		### --- DEBUG

		result = {}
		result["name"] = dataset.capitalize()

		allNodes = [node for node in dag.nodes]
		# varX = "nedbarea"
		varX = choice(allNodes)
		allNodes.remove(varX)
		# varY = "markgrm"
		varY = choice(allNodes)
		allNodes.remove(varY)
		# varZ = "dgv5980"
		varZ = choice(allNodes)
		allNodes.remove(varZ)

		dsepDag = dSeparation(OrderedSet([varX]),OrderedSet([varY]),OrderedSet([varZ]),dag, debug)
		result["test"] = "I(" +varX+ "," +varY+ "," +varZ+ ")"
		dSepTime0 = time()
		numberOfChecksReachable = dsepDag.reachable()["numberOfChecks"]
		dSepTime1 = time()
		iSepTime0 = time()
		numberOfChecksIReachable = dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"]
		iSepTime1 = time()
		result["d-sep"] = numberOfChecksReachable
		result["i-sep"] = numberOfChecksIReachable
		percentage = round(float(numberOfChecksIReachable)/float(numberOfChecksReachable), 4)
		percentage = percentage * 100
		result["saving"] = format(percentage,".2f")
		result["dSepTime"] = dSepTime1 - dSepTime0
		result["iSepTime"] = iSepTime1 -iSepTime0

		results.append(result)

# Save the CSV file
with open("results/	" + csvName + '.csv', 'w') as csvfile:
    fieldnames = ['name', 'test', 'd-sep', 'i-sep', 'saving', 'dSepTime', 'iSepTime']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)
