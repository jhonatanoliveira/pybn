from dag import DAG
from dseparation import dSeparation
from plotReachabilityResult import *
from loadBif import *
from random import *
import csv

def runBenchmarkCsv():
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
		dag = loadBif("datasets/" + dataset + ".bif")

		for i in range(0,100):
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

			dsepDag = dSeparation(set([varX]),set([varY]),set([varZ]),dag, debug)
			result["test"] = "I(" +varX+ "," +varY+ "," +varZ+ ")"
			result["inaugurals"] = dsepDag.inaugurals().__len__()
			numberOfChecksReachable = dsepDag.reachable()["numberOfChecks"]
			numberOfChecksIReachable = dsepDag.iReachable()["numberOfChecks"]
			result["d-sep"] = numberOfChecksReachable
			result["i-sep"] = numberOfChecksIReachable
			percentage = round(float(numberOfChecksIReachable)/float(numberOfChecksReachable), 4)
			percentage = percentage * 100
			result["saving"] = format(percentage,".2f")

			results.append(result)

	# Save the CSV file
	with open(csvName + '.csv', 'w') as csvfile:
		fieldnames = ['name', 'test', 'inaugurals', 'd-sep', 'i-sep', 'saving']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(results)