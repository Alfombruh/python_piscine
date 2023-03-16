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
		for elem in self.accoutns:
			if elem == new_account.name:
				print ('Account name is already chosen')
				return 
		#self.checkFix(new_account)
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
		self.fix_account(origin)
		self.fix_account(dest)
		print("bot accounts are gud!")
		origin.transfer(-amount)
		dest.transfer(amount)
		print(f"Transfer has been done from {origin.name} to {dest.name}")
		

	def fix_account(self, name):
		""" fix account associated to name if corrupted
			@name: str(name) of the account
			@return True if success, False if an error occured
		"""
		check = 0

		for elem in self.accoutns:
			print (f'name is {elem.name} and we are looking for {name.name}')
			if elem.name == name.name:
				print('for loop')
				if not isinstance(elem.name, str):
					print('Account name is int')
					return False
				toFix = elem #we will have to fix this account
				for key in toFix.__dict__.keys(): #checks there are none keys that start with 'b'
					if key[0] == 'b':
						del toFix[key]
				for atribute in toFix.__dict__.keys(): #checks if atribute has value, name or id
					if atribute == "name" or atribute == "id" or atribute == "value":
						check = 1
				if check != 1: #checks if no atribute in name id or value
					i = 0
					for elem in self.accoutns:
						if elem.name == 'Default' + str(i):
							i += 1
					toFix.__dict__['name'] == 'Default' + str(i)
				for atribute in toFix.__dict__.keys(): #checks if atribute has zip or addr
					if atribute == "zip" or atribute == "addr":
						check = 2
				if check != 2: # adds a new atribute to fix account if not zip or addr
					i = 0
					for elem in self.accoutns:
						if elem.name == 'DefaultAddr' + str(i):
							i += 1
					toFix.__dict__['addr'] == 'DefaultAddr' + str(i)
				for key, value in toFix.__dict__.items(): #for key that casts name id or value in case of error
					if key == 'name' and not isinstance(value, str):
						value = (str)(value)
					if key == 'id' and not isinstance(value, int):
						value = (int)(value)
					if key == 'value' and not (isinstance(value, int) or isinstance(value, float)):
						value = (float)(value)
				print('im somewhere')
				if len(toFix.__dict__.keys()) % 2 == 0: #checks the number of atributes isnt even and deletes one atribute if so
					for key in toFix.__dict__.keys():
						if (key != "name" or key != 'id' or key != 'value') and (key != "zip" or key != "addr"):
							del toFix.__dict__[key]
							print('sex')
							break
				print("Account FIXED!!!")
		return False

if __name__ == "__main__":
	bank = Bank()
	bank.add(Account('Smith Jane', zip='911-745', value=1000.0, ref='1044618427ff2782f0bbece0abd05f31'))
	bank.add(Account('Smith Jone', zip='911-745', value=1000.0, ref='1044618427ff2782f0bbece0abd05f31'))
	bank.add(Account('Smith June', zip='911-745', value=1000.0, ref='1044618427ff2782f0bbece0abd05f31'))
	bank.add(Account('Smith Jene', zip='911-745', value=1000.0, ref='1044618427ff2782f0bbece0abd05f31'))
	bank.transfer(bank.accoutns[0], bank.accoutns[1], 10)
	print('Account is valid!!')
	bank.add(Account('William John', zip='100-064', value=6460.0, ref='58ba2b9954cd278eda8a84147ca73c87', info=None))
	bank.fix_account(bank.accoutns[4])