class Vector:
	def __init__(self, vec, shape = False):
		self.values = vec
		self.shape = (len(self.values[0]), len(self.values))

	def dot(self, vec):
		ret = 0
		for i in range(len(self.values)):
			for j in range(len(self.values[0])):
				ret += self.values[i][j] * vec.values[i][j]
		return ret

	def T(self):
		new = []
		for j in range(len(self.values[0])):
			row = []
			for i in range(len(self.values)):
				row.append(self.values[i][j])
			new.append(row)
		return(Vector(new))
	
	def __add__(self, vec):
		new = []
		for i in range(len(self.values)):
			row = []
			for j in range(len(self.values[0])):
				row.append(self.values[i][j] + vec.values[i][j])
			new.append(row)
		return(Vector(new))
	
	def __radd__(self, vec):
		new = []
		for i in range(len(self.values)):
			row = []
			for j in range(len(self.values[0])):
				row.append(self.values[i][j] + vec.values[i][j])
			new.append(row)
		return(Vector(new))

	def __sub__(self, vec):
		new = []
		for i in range(len(self.values)):
			row = []
			for j in range(len(self.values[0])):
				row.append(self.values[i][j] - vec.values[i][j])
			new.append(row)
		return(Vector(new))
	
	def __rsub__(self, vec):
		new = []
		for i in range(len(self.values)):
			row = []
			for j in range(len(self.values[0])):
				row.append(self.values[i][j] - vec.values[i][j])
			new.append(row)
		return(Vector(new))
	
	def __mul__(self, num):
		new = []
		for i in range(len(self.values)):
			row = []
			for j in range(len(self.values[0])):
				row.append(self.values[i][j] * num)
			new.append(row)
		return(Vector(new))
	
	def __rmul__(self, num):
		new = []
		for i in range(len(self.values)):
			row = []
			for j in range(len(self.values[0])):
				row.append(self.values[i][j] * num)
			new.append(row)
		return(Vector(new))
	
	def __rmul__(self, num):
		new = []
		for i in range(len(self.values)):
			row = []
			for j in range(len(self.values[0])):
				row.append(self.values[i][j] / num)
			new.append(row)
		return(Vector(new))

	def __truediv__(self, num):
		new = []
		for i in range(len(self.values)):
			row = []
			for j in range(len(self.values[0])):
				row.append(self.values[i][j] / num)
			new.append(row)
		return(Vector(new))
	
	def __rtruediv__(self, num):
		new = []
		for i in range(len(self.values)):
			row = []
			for j in range(len(self.values[0])):
				row.append(self.values[i][j] / num)
			new.append(row)
		return(Vector(new))
	
	def __str__(self):
		return f'{self.values}'
	
	def __repr__(self):
		return f'{self.values}'
