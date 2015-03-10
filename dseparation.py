class dSeparation:

	def __init__(self,X,Y,Z,dag):
		if type(X) is not set:
			self.X = set([X])
		else:
			self.X = X
		if type(Y) is not set:
			self.Y = set([Y])
		else:
			self.Y = Y
		if type(Z) is not set:
			self.Z = set([Z])
		else:
			self.Z = Z
		self.dag = dag

	def reachable(self):
		# Phase I: insert all ancestors of Y into A
		AnY = self.dag.ancestors(self.Y)
		A = AnY.union(self.Y)

		# Phase II: traverse active trails starting from X
		L = set()
		for v in self.X:
			L = L.union( set([ ("up",v) ]) )
		V = set()
		R = set()
		while L.__len__() > 0:
			print "L => " + L.__str__()
			(d,v) = L.pop()
			if (d,v) not in V:
				if v not in self.Y:
					R.add(v)
				V.add((d,v))
				if d == "up" and v not in self.Y:
					for p in self.dag.parents(v):
						L.add(("up",p))
					for c in self.dag.children(v):
						L.add(("down",c))
				elif d == "down":
					if v not in self.Y:
						for c in self.dag.children(v):
							L.add(("down",c))
					if v in A:
						for p in self.dag.parents(v):
							L.add(("up",p))
		return R

	def inaugurals(self):
		# Inaugural variables
		I = set()
		vstructures = self.dag.vstructures()
		XYZ = self.X.union( self.Y.union(self.Z) )
		AnXYZ = self.dag.ancestors(XYZ)
		V = vstructures - AnXYZ.union(XYZ)
		for v in V:
			Anv = self.dag.ancestors(v)
			if Anv.intersection(V).__len__() == 0:
				I.add(v)
		# Descendants of Inaugural variables
		DeI = self.dag.descendants(I)
		return I.union(DeI)
		
	def iReachable(self):
		# Phase I: insert all ancestors of Y into A
		AnY = self.dag.ancestors(self.Y)
		A = AnY.union(self.Y)

		# Phase II: insert all inaugurals in I
		Is = self.inaugurals()

		# Phase III: traverse active trails starting from X
		L = set()
		for v in self.X:
			L = L.union( set([ ("up",v) ]) )
		V = set()
		R = set()
		while L.__len__() > 0:
			print "L => " + L.__str__()
			(d,v) = L.pop()
			if (d,v) not in V:
				V.add((d,v))
				if v not in self.Y:
					if v in Is:
						continue
					R.add(v)
				if d == "up" and v not in self.Y:
					for p in self.dag.parents(v):
						if p not in Is:
							L.add(("up",p))
					for c in self.dag.children(v):
						if c not in Is:
							L.add(("down",c))
				elif d == "down":
					if v not in self.Y:
						for c in self.dag.children(v):
							if c not in Is:
								L.add(("down",c))
					if v in A:
						for p in self.dag.parents(v):
							if p not in Is:
								L.add(("up",p))
		return R
