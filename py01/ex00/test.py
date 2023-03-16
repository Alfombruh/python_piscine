from book import Book
from recipe import Recipe

def test():
	tourte = Recipe("Zapatos", 2, 10, ["cuero", "cordones", "suela", "costura"], "lunch","Pues eso, unos zapatos bien wapos")
	estrin = str(tourte)
	print(estrin)

if __name__ == "__main__":
	rBook = Book("EL libro secreto de las secretas secreatas recetas secretas")
	Tarta = Recipe("Tarta", 5, 120, ["harina", "huevos", "leche", "azucar"], "dessert", "Tarta puta madre")
	Lasaña = Recipe("Lasaña", 5, 60, ["Laminas", "carne picada", "nata", "tomate"], "starter", "Foca!")
	Pesto = Recipe("Pasta Pesto", 5, 120, ["Pasta", "Pesto"], "lunch", "Pasta Pesto")

	rBook.add_recipe(Tarta)
	rBook.add_recipe(Lasaña)
	rBook.add_recipe(Pesto)
	print(str(rBook.get_recipe_by_name("Tarta")))
	print(str(rBook.get_recipe_by_name("Pasta Pesto")))
	print(str(rBook.get_recipe_by_name("Lasaña")))
	lst = rBook.get_recipe_by_type("starter")
	for elem in lst:
		print(str(elem))