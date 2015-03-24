from pydag.core.orderedSet import OrderedSet
from time import time


class dSeparation:

    """
    This class implements algorithms used to test d-Separation (Pearl,1988) in a DAG, denoted I(X,Y,Z). Basically, a algorithm test for reachability from X to Z, given some blocking rules (sequential, divergent and convergente variables).
    """

    def __init__(self, X, Y, Z, dag):
        """
        Input: X (OrderedSet or str), Y (OrderedSet or str), Z (OrderedSet or str), dag (DAG)
        Output: (None)
        Description: Initialize one test of d-Separation, that is if X is independent of Z given Y.
        """
        if type(X) is not OrderedSet:
            self.X = OrderedSet([X])
        else:
            self.X = X
        if type(Y) is not OrderedSet:
            self.Y = OrderedSet([Y])
        else:
            self.Y = Y
        if type(Z) is not OrderedSet:
            self.Z = OrderedSet([Z])
        else:
            self.Z = Z
        self.dag = dag

    def reachable(self):
        """
        Input: (None)
        Output: (dict[str] = OrderedSet/int/float)
        Description: This algorithm (Koller,09) tests the if Z is reachable from X, given some blocking rules (as described in Darwiche-2009, a sequential, divergent or convergent variables).
        """
        # Phase I: ancestors of Y
        _timeAnY0 = time()
        AnY = self.dag.ancestors(self.Y)
        A = AnY.union(self.Y)
        _timeAnY1 = time()
        _timeAnY = _timeAnY1 - _timeAnY0

        # Phase II: traverse active paths starting from X
        L = OrderedSet()
        for v in self.X:
            L.add(("up", v))
        V = OrderedSet()
        R = OrderedSet()
        _numberOfChecks = 0
        while L.__len__() > 0:
            (d, v) = L.pop()
            _numberOfChecks = _numberOfChecks + 1
            if (d, v) not in V:
                if v not in self.Y:
                    R.add(v)
                V.add((d, v))
                if d == "up" and (v not in self.Y):
                    for vi in self.dag.parents(v):
                        L.add(("up", vi))
                    for vi in self.dag.children(v):
                        L.add(("down", vi))
                elif d == "down":
                    if v not in self.Y:
                        for vi in self.dag.children(v):
                            L.add(("down", vi))
                    if v in A:
                        for vi in self.dag.parents(v):
                            L.add(("up", vi))

        return {"reachables": R, "numberOfChecks": _numberOfChecks, "timeAnY": _timeAnY}

    def test(self):
        """
        Input: (None)
        Output: result (Boolean)
        Description: After running the reachability on the DAG, the test checks if Z is in all possible reachable variables from X.
        """
        result = False
        reachables = self.reachable()["reachables"]
        if reachables.intersection(self.Z).__len__() > 0:
            result = False
        else:
            result = True
        return result
