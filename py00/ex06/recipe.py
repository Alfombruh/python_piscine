import sys


def printNames(cookbook):
    print("My recipies are:")
    for elem in cookbook:
        print(f"\t{elem}")


def printRecipe(cookbook):
    res = 0
    while True:
        res = input("Select a recipe:")
        if res in cookbook:
            break
        print("input no valid")
    rec = cookbook[res]
    print(f'Ingredients list: {rec["ingredients"]}')
    print(f'To be eater for {rec["meal"]}.')
    print(f'Takes {rec["prep_time"]} minutes of cooking.')


def deleteRecipe(cookbook):
    name = input('Which one you want to delete?:')
    del cookbook[name]

def addRecipe(cookbook):
    name = input('Recipe Name: ')
    ing = input('Ingredients: ')
    ing.split(', ')
    mealtype = input('Meal Type: ')
    cooktime = input('Time to cook: ')
    cookbook[name] = {"ingredients" : ing, "meal" : mealtype, "prep_time" : cooktime}

def printOptions():
    print("List of aviable option:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")

if __name__ == "__main__":
    sandwichRecipe = {
        "ingredients": ["jamon", "pan", "queso", "tomate"],
        "meal": "almuerzo",
        "prep_time": "10",
    }
    cakeRecipe = {
        "ingredients": ["harina", "azucar", "huevos"],
        "meal": "postre",
        "prep_time": "10",
    }
    saladRecipe = {
        "ingredients": ["aguacate", "rucula", "tomate", "espinacas"],
        "meal": "almuerzo",
        "prep_time": "60",
    }
    cookbook = {
        "bocadillo de jamon": sandwichRecipe,
        "tarta": cakeRecipe,
        "ensalada": saladRecipe,
    }
    print("Welcome to the Python Cookbook !")
    printOptions()
    while True:
        try:
            res = int (input("Select an option:\n>>"))
        except ValueError:
            print('Sorry, this option is not aviable')
            printOptions()
            res = 6
        if res == 1:
            addRecipe(cookbook)
        if res == 2:
            deleteRecipe(cookbook)
        if res == 3:
            printRecipe(cookbook)
        if res == 4:
            printNames(cookbook)
        if res == 5:
            sys.exit("SO LONG KING BOWSER!")
