from dag import DAG
from dseparation import dSeparation
from plotReachabilityResult import *
from loadBif import *
from random import *
from time import time
from ordered_set import OrderedSet

## CONTROL ##
# datasets = ["alarm","asia","cancer","barley","diabetes","hepar2","pathfinder","win95pts","munin"]
datasets = ["barley"]
debug = True
saveFigure = False

# *** Benchmark ***

for dataset in datasets:
	dag = loadBif("datasets/" + dataset + ".bif")

	result = {"title": dataset.capitalize(),"reachable": [], "i-reachable": [], "tests": [], "inaugurals": []}

	for i in range(0,1):
		allNodes = [node for node in dag.nodes]

		varX = "nedbarea"
		# varX = choice(allNodes)
		# allNodes.remove(varX)
		varY = "markgrm"
		# varY = choice(allNodes)
		allNodes.remove(varY)
		varZ = "dgv5980"
		# varZ = choice(allNodes)
		allNodes.remove(varZ)

		dsepDag = dSeparation(OrderedSet([varX]),OrderedSet([varY]),OrderedSet([varZ]),dag, debug)
		result["tests"].append("I(" +varX+ "," +varY+ "," +varZ+ ")")
		result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
		result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

	plotReachabilityResult(result,saveFigure)
