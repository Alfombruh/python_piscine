import datetime
from recipe import Recipe

class Book:
	def __init__(self, name):
		self.name = name
		self.creation_date = datetime.datetime.now()
		self.last_update = self.creation_date
		self.recipes_list = {"starter":[], "lunch":[], "dessert":[]}
	

	def	get_recipe_by_name(self, name):
		'''Prints the recipe name with \texttt{name} and returns the instance'''
		for elem in self.recipes_list:
			for recipe in self.recipes_list[elem]:
				if recipe.name == name:
					return recipe


	def get_recipe_by_type(self, Recipe_type):
		'''Returns all the recipes of the recipe_type'''
		if Recipe_type in self.recipes_list:
			return self.recipes_list[Recipe_type]
		else:
			print(f"there are no {Recipe_type} recipes ")


	def	add_recipe(self, recipe):
		'''Adds a new recipe to the book and updates last_update'''
		self.recipes_list[recipe.recipe_type].append(recipe)
