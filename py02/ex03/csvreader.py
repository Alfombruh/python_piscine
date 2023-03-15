class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
		#trycatch
		self.file = open(self.filename, "r")
		self.data = self.file.readlines()
		
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type:
			print("exc_type")
		self.file.close()

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
			Return:
			nested list (list(list, list, ...)) representing the data.
		"""
		if self.header and len(self.data) > 1:
			return self.data[::1]
		return self.data

	def getheader(self):
		""" Retrieves the header from csv file.
			Returns:
			list: representing the data (when self.header is True).
			None: (when self.header is False).
		"""
		if self.header:
			return self.data[0]
		return False

if __name__ == "__main__":
	with CsvReader('good.csv', ';', True) as file:
		data = file.getdata()
		header = file.getheader()
		print(header)
		print(data)