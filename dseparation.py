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

	def isInauguralInActivePath(self,variable,anXYZandXYZ):
		result = False
		if variable not in anXYZandXYZ:
			if self.dag.isVstructure(variable):
				result = True
		return result
		
	def reachable(self, consideringInaugurals = False):
		### DEBUG
		# if self.debug:
		# 	print
		# 	if consideringInaugurals:
		# 		print "### Running i-REACHABLE for I(" + self.X.map.keys().__str__() + ", " + self.Y.map.keys().__str__() + "," + self.Z.map.keys().__str__() + ") ###"
		# 	else:
		# 		print "### Running REACHABLE for I(" + self.X.map.keys().__str__() + ", " + self.Y.map.keys().__str__() + "," + self.Z.map.keys().__str__() + ") ###"
		# 	print
		### -- DEBUG
		# Phase I: insert all ancestors of Y into A
		A = self.dag.ancestors(self.Y, True)
		if consideringInaugurals:
			anXZ = self.X.union(self.Z)
			anXZandXZ = self.dag.ancestors(anXZ,True)
			anXYZandXYZ = anXZandXZ.union(A)
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
			# if self.debug:
			# 	print "--- Loop ---"
			# 	print "Select:"
			# 	print (d,v)
			# 	print "L:"
			# 	print L
			### -- DEBUG
			if (d,v) not in V:
				V.add((d,v))
				### DEBUG
				# if self.debug:
				# 	print "V:"
				# 	print V
				### -- DEBUG
				if v not in self.Y:
					R.add(v)
					### DEBUG
					# if self.debug:
					# 	print "R:"
					# 	print R
					### -- DEBUG
				if d == "up" and v not in self.Y:
					for p in self.dag.parents(v):
						if consideringInaugurals:
							if not self.isInauguralInActivePath(p,anXYZandXYZ):
								L.add(("up",p))
						else:
							L.add(("up",p))
					for c in self.dag.children(v):
						if consideringInaugurals:
							if not self.isInauguralInActivePath(c,anXYZandXYZ):
								L.add(("down",c))
						else:
							L.add(("down",c))
				elif d == "down":
					if v not in self.Y:
						for c in self.dag.children(v):
							if consideringInaugurals:
								if not self.isInauguralInActivePath(c,anXYZandXYZ):
									L.add(("down",c))
							else:
								L.add(("down",c))
					if v in A:
						for p in self.dag.parents(v):
							L.add(("up",p))
			### DEBUG
			# if self.debug:
			# 	print "L:"
			# 	print L
			### -- DEBUG
		### DEBUG
		# if self.debug:
		# 	print "Final R (" + str(R.__len__()) + "): "
		# 	print R
		### -- DEBUG
		return {"R": R, "numberOfChecks": numberOfChecks}
