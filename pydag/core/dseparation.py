from ordered_set import OrderedSet
from time import time

class dSeparation:

	def __init__(self,X,Y,Z,dag):
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
		# Phase I: ancestors of Y
		_timeAnY0 = time()
		AnY = self.dag.ancestors(self.Y)
		A = AnY.union(self.Y)
		_timeAnY1 = time()
		_timeAnY = _timeAnY1 - _timeAnY0

		# Phase II: traverse active paths starting from X
		L = OrderedSet()
		for v in self.X:
			L.add(("up",v))
		V = OrderedSet()
		R = OrderedSet()
		_numberOfChecks = 0
		while L.__len__() > 0:
			(d,v) = L.pop()
			_numberOfChecks = _numberOfChecks + 1
			if (d,v) not in V:
				if v not in self.Y:
					R.add(v)
				V.add((d,v))
				if d == "up" and (v not in self.Y):
					for vi in self.dag.parents(v):
						L.add(("up",vi))
					for vi in self.dag.children(v):
						L.add(("down",vi))
				elif d == "down":
					if v not in self.Y:
						for vi in self.dag.children(v):
							L.add(("down",vi))
					if v in A:
						for vi in self.dag.parents(v):
							L.add(("up",vi))

		return {"reachables": R, "numberOfChecks": _numberOfChecks, "timeAnY": _timeAnY}

	def test(self):
		result = False
		reachables = self.reachable()["reachables"]
		if reachables.intersection(self.Z).__len__() > 0:
			result = False
		else:
			result = True
		return result
