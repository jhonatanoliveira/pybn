from dag import DAG
from dseparation import dSeparation
from iseparation import iSeparation
from plotReachabilityResult import *
from loadBif import *
from random import *
from ordered_set import OrderedSet

# *** Kjaerulff ***

dag = DAG()
dag.add("a","c")
dag.add("a","d")
dag.add("a","f")
dag.add("b","d")
dag.add("b","e")
dag.add("c","f")
dag.add("d","g")
dag.add("e","f")
dag.add("e","g")
dag.add("f","h")
dag.add("g","h")

# result = {"title": "Kjaerulff","reachable": [], "i-reachable": [], "test": []}

# print
# print "Testing I(c,,g)"
# dSep = dSeparation("c",OrderedSet([]),"g",dag)
# iSep = iSeparation("c",OrderedSet([]),"g",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(c,{},g)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(c,,e)"
# dSep = dSeparation("c",OrderedSet([]),"e",dag)
# iSep = iSeparation("c",OrderedSet([]),"e",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(c,{},e)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(c,g,e)"
# dSep = dSeparation("c",OrderedSet(["g"]),"e",dag)
# iSep = iSeparation("c",OrderedSet(["g"]),"e",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(c,g,e)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(a,de,g)"
# dSep = dSeparation("a",OrderedSet(["d","e"]),"g",dag)
# iSep = iSeparation("a",OrderedSet(["d","e"]),"g",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,de,g)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(a,d,g)"
# dSep = dSeparation("a",OrderedSet(["d"]),"g",dag)
# iSep = iSeparation("a",OrderedSet(["d"]),"g",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

print dag.transitiveClosure()

# plotReachabilityResult(result)

# *** Darwiche ***

# dag = DAG()
# dag.add("a","c")
# dag.add("a","d")
# dag.add("b","d")
# dag.add("b","e")
# dag.add("c","f")
# dag.add("d","f")
# dag.add("e","h")
# dag.add("f","g")
# dag.add("f","h")

# result = {"title": "Darwiche","reachable": [], "i-reachable": [], "test": []}

# print
# print "Testing I(,,)"
# iSep = iSeparation("a",OrderedSet(["b","h"]),"e",dag)
# dSep = dSeparation("a",OrderedSet(["b","h"]),"e",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["test"].append("I(a,bh,e)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(,,)"
# iSep = iSeparation("g","d","e",dag)
# dSep = dSeparation("g","d","e",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["test"].append("I(g,d,e)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(,,)"
# iSep = iSeparation(OrderedSet(["a","b"]),"f",OrderedSet(["g","h"]),dag)
# dSep = dSeparation(OrderedSet(["a","b"]),"f",OrderedSet(["g","h"]),dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["test"].append("I(ab,f,gh)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# # plotReachabilityResult(result)

# # *** Castillo ***

# dag = DAG()
# dag.add("a","c")
# dag.add("a","d")
# dag.add("b","d")
# dag.add("c","f")
# dag.add("c","g")
# dag.add("d","g")
# dag.add("d","h")
# dag.add("e","h")

# result = {"title": "Castillo","reachable": [], "i-reachable": [], "test": []}

# print
# print "Testing I(,,)"
# iSep = iSeparation("e",OrderedSet([]),"g",dag)
# dSep = dSeparation("e",OrderedSet([]),"g",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["test"].append("I(e,{},g)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(,,)"
# iSep = iSeparation("c",OrderedSet([]),"d",dag)
# dSep = dSeparation("c",OrderedSet([]),"d",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["test"].append("I(c,{},d)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(,,)"
# iSep = iSeparation("c","g","d",dag)
# dSep = dSeparation("c","g","d",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["test"].append("I(c,g,d)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(,,)"
# iSep = iSeparation("b","a","c",dag)
# dSep = dSeparation("b","a","c",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["test"].append("I(b,a,c)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(,,)"
# iSep = iSeparation(OrderedSet(["c","d"]),OrderedSet([]),"e",dag)
# dSep = dSeparation(OrderedSet(["c","d"]),OrderedSet([]),"e",dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["test"].append("I(cd,{},e)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(,,)"
# iSep = iSeparation("f",OrderedSet(["a"]),OrderedSet(["e","h"]),dag)
# dSep = dSeparation("f",OrderedSet(["a"]),OrderedSet(["e","h"]),dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["test"].append("I(f,a,eh)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# print
# print "Testing I(,,)"
# iSep = iSeparation(OrderedSet(["a","c"]),OrderedSet(["d"]),OrderedSet(["h","e"]),dag)
# dSep = dSeparation(OrderedSet(["a","c"]),OrderedSet(["d"]),OrderedSet(["h","e"]),dag)
# dSepAns = dSep.test()
# iSepAns = iSep.test()
# print "d-Sep answer: " + str(dSepAns)
# print "i-Sep answer: " + str(iSepAns)
# if dSepAns == iSepAns:
# 	print "Correct answer!"
# else:
# 	print "Incorrect answer"
# result["test"].append("I(a,d,g)")
# result["test"].append("I(ac,d,he)")
# result["reachable"].append(dSep.reachable()["numberOfChecks"])
# result["i-reachable"].append(iSep.reachable()["numberOfChecks"])

# plotReachabilityResult(result)