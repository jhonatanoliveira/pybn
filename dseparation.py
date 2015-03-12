class dSeparation:

	def __init__(self,X,Y,Z,dag,debug=False):
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
		self.debug = debug

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
		### DEBUG
		if self.debug:
			print
			print "### Running REACHABLE ###"
			print
		### -- DEBUG
		numberOfChecks = 0
		while L.__len__() > 0:
			(d,v) = L.pop()
			numberOfChecks = numberOfChecks + 1
			### DEBUG
			if self.debug:
				print "--- Loop ---"
				print "Select:"
				print (d,v)
				print "L:"
				print L
			### -- DEBUG
			if (d,v) not in V:
				if v not in self.Y:
					R.add(v)
					### DEBUG
					if self.debug:
						print "R:"
						print R
					### -- DEBUG
				V.add((d,v))
				### DEBUG
				if self.debug:
					print "V:"
				### -- DEBUG
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
			### DEBUG
			if self.debug:
				print "L:"
				print L
			### -- DEBUG
		return {"R": R, "numberOfChecks": numberOfChecks}

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
		### DEBUG
		if self.debug:
			print
			print "### Running i-REACHABLE ###"
			print
		### -- DEBUG
		# Phase I: insert all ancestors of Y into A
		AnY = self.dag.ancestors(self.Y)
		A = AnY.union(self.Y)

		# Phase II: insert all inaugurals in I
		Is = self.inaugurals()
		### DEBUG
		if self.debug:
			print "Is:"
			print Is
		### -- DEBUG

		# Phase III: traverse active trails starting from X
		L = set()
		for v in self.X:
			L = L.union( set([ ("up",v) ]) )
		V = set()
		R = set()
		numberOfChecks = 0
		while L.__len__() > 0:
			(d,v) = L.pop()
			numberOfChecks = numberOfChecks + 1
			### DEBUG
			if self.debug:
				print "--- Loop ---"
				print "Select:"
				print (d,v)
				print "L:"
				print L
			### -- DEBUG
			if (d,v) not in V:
				V.add((d,v))
				### DEBUG
				if self.debug:
					print "V:"
					print V
				### -- DEBUG
				if v not in self.Y:
					if v in Is:
						continue
					R.add(v)
					### DEBUG
					if self.debug:
						print "R:"
						print R
					### -- DEBUG
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
			### DEBUG
			if self.debug:
				print "L:"
				print L
			### -- DEBUG
		return {"R": R, "numberOfChecks": numberOfChecks}
