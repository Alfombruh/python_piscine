import string
import sys

class Recipe:
	def __init__(self, name = None, cooking_lvl = None , cooking_time = None, ingredients = None, recipe_type = None, description = None):
		if name == None or cooking_lvl == None or cooking_time == None or ingredients == None or recipe_type == None:
			sys.exit('All values besides the desciption must be filled')
		if recipe_type != 'starter' and recipe_type != 'lunch' and recipe_type != 'dessert':
			sys.exit("Recipe type has to be ['starter' or 'lunch' or 'dessert']")
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time =  cooking_time
		self.ingredients = ingredients
		self.recipe_type = recipe_type
		self.description = description
	
	def __str__(self):
		txt = self.description
		return txt