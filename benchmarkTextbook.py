from dag import DAG
from dseparation import dSeparation
from plotReachabilityResult import *
from loadBif import *
from random import *
from ordered_set import OrderedSet

# *** Kjaerulff ***

dag = DAG()
dag.add("a","c")
dag.add("a","d")
dag.add("b","d")
dag.add("b","e")
dag.add("c","f")
dag.add("d","g")
dag.add("e","f")
dag.add("e","g")
dag.add("f","h")
dag.add("g","h")

result = {"title": "Kjaerulff","reachable": [], "i-reachable": [], "tests": []}

dsepDag = dSeparation("c",OrderedSet([]),"g",dag)
result["tests"].append("I(c,{},g)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation("c",OrderedSet([]),"e",dag)
result["tests"].append("I(c,{},e)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation("c",OrderedSet(["g"]),"e",dag)
result["tests"].append("I(c,g,e)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation("a",OrderedSet(["d","e"]),"g",dag)
result["tests"].append("I(a,de,g)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation("a",OrderedSet(["d"]),"g",dag)
result["tests"].append("I(a,d,g)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

plotReachabilityResult(result)


# *** Darwiche ***

dag = DAG()
dag.add("a","c")
dag.add("a","d")
dag.add("b","d")
dag.add("b","e")
dag.add("c","f")
dag.add("d","f")
dag.add("e","h")
dag.add("f","g")
dag.add("f","h")

result = {"title": "Darwiche","reachable": [], "i-reachable": [], "tests": []}

dsepDag = dSeparation("a",OrderedSet(["b","h"]),"e",dag)
result["tests"].append("I(a,bh,e)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation("g","d","e",dag)
result["tests"].append("I(g,d,e)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation(OrderedSet(["a","b"]),"f",OrderedSet(["g","h"]),dag)
result["tests"].append("I(ab,f,gh)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

plotReachabilityResult(result)

# *** Castillo ***

dag = DAG()
dag.add("a","c")
dag.add("a","d")
dag.add("b","d")
dag.add("c","f")
dag.add("c","g")
dag.add("d","g")
dag.add("d","h")
dag.add("e","h")

result = {"title": "Castillo","reachable": [], "i-reachable": [], "tests": []}

dsepDag = dSeparation("e",OrderedSet([]),"g",dag)
result["tests"].append("I(e,{},g)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation("c",OrderedSet([]),"d",dag)
result["tests"].append("I(c,{},d)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation("c","g","d",dag)
result["tests"].append("I(c,g,d)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation("b","a","c",dag)
result["tests"].append("I(b,a,c)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation(OrderedSet(["c","d"]),OrderedSet([]),"e",dag)
result["tests"].append("I(cd,{},e)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation("f",OrderedSet(["a"]),OrderedSet(["e","h"]),dag)
result["tests"].append("I(f,a,eh)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

dsepDag = dSeparation(OrderedSet(["a","c"]),OrderedSet(["d"]),OrderedSet(["h","e"]),dag)
result["tests"].append("I(ac,d,he)")
result["reachable"].append(dsepDag.reachable()["numberOfChecks"])
result["i-reachable"].append(dsepDag.reachable(consideringInaugurals = True)["numberOfChecks"])

plotReachabilityResult(result)