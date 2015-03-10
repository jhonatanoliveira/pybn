from dag import DAG
from dseparation import dSeparation

print
print
print "---------------- BEGIN ----------------"
print

dag = DAG()

dag.add("a","c")
dag.add("a","d")
dag.add("b","d")
dag.add("b","e")
dag.add("c","i")
dag.add("c","f")
dag.add("d","f")
dag.add("d","g")
dag.add("e","f")
dag.add("e","g")
dag.add("i","j")
dag.add("i","h")
dag.add("f","h")
dag.add("g","h")

print "*** Example 1 ***"
print "Using the DAG in Figure 1 for testing I(a,de,g)."
print

dsepDag = dSeparation("a",set(["d","e"]),"g",dag)

print "Reachable variables from X:"
print "   " + dsepDag.reachable().__str__()

print "Inaugural variables and its descendants:"
print "   " + dsepDag.inaugurals().__str__()

print "Reachable variables from X using i-Separation"
print "   " + dsepDag.iReachable().__str__()

subDag = DAG()

subDag.add("a","c")
subDag.add("a","d")
subDag.add("b","d")
subDag.add("b","e")
subDag.add("c","i")
subDag.add("d","g")
subDag.add("e","g")
subDag.add("i","j")

print
print "*** Example 2 ***"
print "Using the sub-DAG in Figure 4 for testing I(a,de,g)."
print

dsepDag = dSeparation("a",set(["d","e"]),"g",subDag)

print "Reachable variables from X:"
print "   " + dsepDag.reachable().__str__()

print "Inaugural variables and its descendants:"
print "   " + dsepDag.inaugurals().__str__()

print "Reachable variables from X using i-Separation"
print "   " + dsepDag.iReachable().__str__()

print
print "---------------- END ----------------"
print
print