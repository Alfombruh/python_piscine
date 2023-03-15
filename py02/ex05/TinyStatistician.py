class TinyStatistician():
	def mean(self, x):
		total = 0
		sum = 0
		for i in range(len(x)):
			if isinstance(x[i], list):
				for j in range(len(x[i])):
					sum += x[i][j]
					total += 1
			else:
				sum += x[i]
				total += 1
		return sum / total

	def median(self, x):
		ret = []
		sort = []
		for i in range(len(x)):
			if isinstance(x[i], list):
				sort = sorted(x[i])
				if (len(sort) % 2 == 0):
					ret.append(sort[(int)(len(sort) - 1 / 2)])
				else:
					ret.append(sort[(int)(len(sort) / 2)])
			else:
				sort = sorted(x)
				if (len(sort) % 2 == 0):
					ret.append(sort[(int)(len(sort) - 1 / 2)])
					return ret
				else:
					ret.append(sort[(int)(len(sort) / 2)])
					return ret
		return ret
	
	def quartile(self, x):
		ret = []
		sort = []
		for i in range(len(x)):
			if isinstance(x[i], list):
				sort = sorted(x[i])
				if (len(sort) % 2 == 0):
					ret.append(sort[(int)(len(sort) - 1 / 4)])
					ret.append(sort[(int)(len(sort) * (3 / 4) - 1)])
				else:
					ret.append(sort[(int)(len(sort) * 3 / 4 )])
					ret.append(sort[(int)(len(sort) / 4)])
			else:
				sort = sorted(x)
				if (len(sort) % 2 == 0):
					ret.append(sort[(int)(len(sort) - 1 / 4)])
					ret.append(sort[(int)(len(sort) * (3 / 4) - 1)])
					return ret
				else:
					ret.append(sort[(int)(len(sort) / 4)])
					ret.append(sort[(int)(len(sort) * 3 / 4)])
					return ret
		return ret
	
	def sqrt(self, x):
		guess = x
		while abs(guess - x/guess) > 0.0001:
			guess = (guess + x/guess) / 2
		return guess


	def var(self, x):
		flat = []
		for i in range(len(x)):
			if isinstance(x[i], list):
				for j in range(len(x[i])):
					flat.append(x[i][j])
			else:
				flat.append(x[i])
		if len(flat) == 0:
			return None
		total = 0
		for item in flat:
			total += item
		mean = total / len(flat)
		sqrdiff = 0
		for item in flat:
			sqrdiff += (item - mean)
		if len(flat) == 0:
			return None
		return sqrdiff / len(flat)
	
	def std(self, x):
		return self.var(x) ** 0.5

if __name__ == "__main__":
	tstat = TinyStatistician()
	a = [1, 42, 300, 10, 59]
	print(tstat.mean(a))    # Output: 82.4
	b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	print(tstat.mean(b))    # Output: 5.0
	print(tstat.median(b))
	print(tstat.median(a))
	print(tstat.quartile(b))
	print(tstat.quartile(a))
	print(tstat.var(a))
	print(tstat.var(b))
	print(tstat.std(a))
		
