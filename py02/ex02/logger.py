import time
from random import randint
import os
#... define log decorator...
def log(function):
	''' @function is the argument function it takes
		@return nothing, writes in the machine.log file what happends
	'''
	with open("machine.log", "w") as file:
		file.write("")
	def wrapper(*args):
		start = time.time()
		ret = function(*args)
		end = time.time()
		with open("machine.log", "a") as file:
			file.write("(jofernan)Running: " + "{:<19}".format(function.__name__.replace("_", " ").title()) + "[ exec-time = " + "{:.3f} {}".format(end - start, "s" if (end - start) > 1 else "ms") + " ]\n")
		return ret  
	return wrapper
		

class CoffeeMachine():
	water_level = 100
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffe is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if  __name__ == "__main__":

	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)