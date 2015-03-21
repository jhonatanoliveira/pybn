from ordered_set import OrderedSet
from time import time
from dseparation import dSeparation

class iSeparation(dSeparation):
	"""
	This class inherits from dSeparation. Basically, it overrides the reachable alorithm.
	Implements an alternative test of d-separation, called i-separation (Butz, Oliveira, dos Santos, 2015). The idea is to avoid paths doomed to be blocked by looking for inaugural variables.
	"""

	def inaugurals(self):
		"""
		Input: (None)
		Output: (OrderedSet)
		Description: Given the test of independence, return a set with all inaugural variables on the DAG.
		"""
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
		"""
		Input: variable (Variable), anXYZandXYZ (OrderedSet)
		Output: result (Boolean)
		Description: Test if a variable, given all ancestors of XYZ (including XYZ), is inaugural.
		"""
		result = False
		if variable not in anXYZandXYZ:
			if self.dag.isVstructure(variable):
				result = True
		return result

	def reachable(self):
		"""
		Input: (None)
		Output: (dict[str] = OrderedSet/int/float)
		Description: This algorithm (Butz, Oliveira, dos Santos, 2015) tests the if Z is reachable from X, given some blocking rules (as described in Darwiche-2009, a sequential, divergent or convergent variables), including inaugural variables.
		"""
		# Phase I: ancestors of Y
		AnY = self.dag.ancestors(self.Y)
		AnY = AnY.union(self.Y)

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