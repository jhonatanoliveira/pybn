from ordered_set import OrderedSet
from time import time
from dseparation import dSeparation
from threading import Thread

class iSeparation(dSeparation):

	def inaugurals(self):
		I = OrderedSet()
		vstructures = self.dag.vstructures()
		XYZ = self.X.union( self.Y.union(self.Z) )
		AnXYZ = self.dag.ancestors(XYZ)
		V = vstructures - AnXYZ.union(XYZ)
		for v in V:
			Anv = self.dag.ancestors(v)
			if Anv.intersection(V).__len__() == 0:
				I.add(v)
		return I.union(self.dag.descendants(I))

	def isInaugural(self,variable,anXYZandXYZ):
		result = False
		if variable not in anXYZandXYZ:
			if self.dag.isVstructure(variable):
				result = True
		return result

	def reachable(self):

		# _timeAnY0 = time()
		# _timeAnXYZ0 = time()

		# AnX = []
		# t1 = Thread(target = self.dag.ancestorsInParallel, args=(self.Y,AnX))
		# t1.start()
		# _timeAnY1 = time()
		# _timeAnY = _timeAnY1 - _timeAnY0

		# AnY = []
		# t2 = Thread(target = self.dag.ancestorsInParallel, args=(self.Y,AnY))
		# t2.start()

		# AnZ = []
		# t3 = Thread(target = self.dag.ancestorsInParallel, args=(self.Y,AnZ))
		# t3.start()

		# t1.join()
		# t2.join()
		# t3.join()

		# _timeAnY1 = time()
		# _timeAnY = _timeAnY1 - _timeAnY0
		# _timeAnXYZ1 = time()
		# _timeAnXYZ = _timeAnXYZ1 - _timeAnXYZ0

		# AnX = AnX[0]
		# AnY = AnY[0]
		# AnZ = AnZ[0]
		# anXYZ = AnX.union(AnY.union(AnZ))

		# Phase I: ancestors of Y
		# _timeAnY0 = time()
		AnY = self.dag.ancestors(self.Y)
		AnY = AnY.union(self.Y)
		# _timeAnY1 = time()
		# _timeAnY = _timeAnY1 - _timeAnY0

		# Phase II: ancestors of XYZ
		_timeAnXYZ0 = time()
		XZ = self.X.union(self.Z)
		anXZ = self.dag.ancestors(XZ)
		anXYZ = anXZ.union(AnY)
		_timeAnXYZ1 = time()
		_timeAnXYZ = _timeAnXYZ1 - _timeAnXYZ0
			
		# Phase III: traverse active paths starting from X
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
				V.add((d,v))
				# Is v serial?
				if v not in self.Y:
					R.add(v)
					if d == "up":
						for vi in self.dag.parents(v):
							if not self.isInaugural(vi,anXYZ):
								L.add(("up",vi))
						for vi in self.dag.children(v):
							if not self.isInaugural(vi,anXYZ):
								L.add(("down",vi))
					else:
						for vi in self.dag.children(v):
							if not self.isInaugural(vi,anXYZ):
								L.add(("down",vi))
				# Is v convergent?
				if d == "down" and (v in AnY):
					for vi in self.dag.parents(v):
						L.add(("up",vi))

		return {"reachables": R, "numberOfChecks": _numberOfChecks, "timeAnXYZ": _timeAnXYZ}