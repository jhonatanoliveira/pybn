from ordered_set import OrderedSet

class dSeparation:

	def __init__(self,X,Y,Z,dag,debug=False):
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
		self.debug = debug

	def inaugurals(self):
		# Inaugural variables
		I = OrderedSet()
		vstructures = self.dag.vstructures()
		XYZ = self.X.union( self.Y.union(self.Z) )
		AnXYZ = self.dag.ancestors(XYZ)
		V = vstructures - AnXYZ.union(XYZ)
		for v in V:
			Anv = self.dag.ancestors(v)
			if Anv.intersection(V).__len__() == 0:
				I.add(v)
		return I
		
	def reachable(self, consideringInaugurals = False):
		### DEBUG
		if self.debug:
			print
			print "### Running REACHABLE ###"
			print
		### -- DEBUG
		# Phase I: insert all ancestors of Y into A
		A = self.dag.ancestors(self.Y, True)

		if consideringInaugurals:
			# Phase II: insert all inaugurals in I
			I = self.inaugurals()
			### DEBUG
			if self.debug:
				print "I: (" + str(I.__len__()) + ")"
				print I
			### -- DEBUG
			DeI = self.dag.descendants(I) # Descendants of Inaugural variables
			Is = I.union(DeI) # Union
			### DEBUG
			if self.debug:
				print "Is: (" + str(Is.__len__()) + ")"
				print Is
			### -- DEBUG

		# Phase III: traverse active trails starting from X
		L = OrderedSet()
		for v in self.X:
			L.add(("up",v))
		V = OrderedSet()
		R = OrderedSet()
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
					if consideringInaugurals and (v in Is): #TODO: remove
						continue
						### DEBUG
						if self.debug:
							print ">>> Is this used?"
						### -- DEBUG
					R.add(v)
					### DEBUG
					if self.debug:
						print "R:"
						print R
					### -- DEBUG
				if d == "up" and v not in self.Y:
					for p in self.dag.parents(v):
						if consideringInaugurals:
							if p not in Is:
								L.add(("up",p))
						else:
							L.add(("up",p))
					for c in self.dag.children(v):
						if consideringInaugurals:
							if p not in Is:
								L.add(("down",c))
						else:
							L.add(("down",c))
				elif d == "down":
					if v not in self.Y:
						for c in self.dag.children(v):
							if consideringInaugurals:
								if p not in Is:
									L.add(("down",c))
							else:
								L.add(("down",c))
					if v in A:
						for p in self.dag.parents(v):
							if consideringInaugurals:
								if p not in Is:
									L.add(("up",p))
								else:
									### DEBUG
									if self.debug:
										print ">>> Is this used? 2"
									### -- DEBUG
							else:
								L.add(("up",p))
			### DEBUG
			if self.debug:
				print "L:"
				print L
			### -- DEBUG
		### DEBUG
		if self.debug:
			print "R:"
			print R
		### -- DEBUG
		return {"R": R, "numberOfChecks": numberOfChecks}
