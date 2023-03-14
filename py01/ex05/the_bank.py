class Account(object):

	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount


class Bank:
	def __init__(self):
		self.accoutns = []

	def	checkFix(self, new_account):
		''' Checks if the acount need to be fixed
			returns True if it needs to be fixed False otherwise
		'''
		check = 0
		if len(new_account.__dict__.keys()) % 2 == 0:
			print('Even nuumber of variables')
			return True
		for atribute in new_account.__dict__.keys():
			print(f'{atribute}')
			if atribute == "name" or atribute == "id" or atribute == "value":
				check = 1
		if check == 0:
			print(f"{new_account.name} fails in the name, id and atribute check")
			return True
		for atribute in new_account.__dict__.keys():
			if atribute == "zip" or atribute == "addr":
				check = 0
		if check != 0:
			print(f"{new_account.name} fails in the addr or zip check")
			return True
		for atribute, value in new_account.__dict__.items():
			if atribute[0] == 'b':
				print(f"{new_account.name} b check")
				return True
			if atribute == "name" and not isinstance(value, str):
				print(f"{new_account.name} name string check")
				return True
			if atribute == "id" and not isinstance(value, int):
				print(f"{new_account.name} id int check")
				return True
			if atribute == "value" and not (isinstance(value, float) or isinstance(value, int)):
				print(f"{new_account.name} value int or float check")
				return True
			print(f'{atribute} : {value}')
		
	
	def	add(self, new_account):
		""" Add new_account in the Bank
			@new_account: Account() new account to append
			@return True if success, False if an error occured
		"""
		self.checkFix(new_account)
		#if new_account.name in self.accoutns:
			#return  False
		self.accoutns.append(new_account)
	
	def	transfer(self, origin, dest, amount):
		""" Perform the fund transfer
			@origin: str(name) of the first account
			@dest: str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return True if success, False if an error occured
		"""
		if amount < 0 or dest.value < amount:
			return
		origin.transfer(-amount)
		dest.transfer(amount)
		

	def fix_account(self, name):
		""" fix account associated to name if corrupted
			@name: str(name) of the account
			@return True if success, False if an error occured
		"""
		for elem in self.accoutns:
			if elem.name == name:
				toFix = elem.name #we will have to fix this account
		return False

if __name__ == "__main__":
	bank = Bank()
	bank.add(Account('Smith Jane', zip='911-745', value=1000.0, ref='1044618427ff2782f0bbece0abd05f31'))
	print('here!')
	bank.add(Account('William John', zip='100-064', value=6460.0, ref='58ba2b9954cd278eda8a84147ca73c87', info=None))