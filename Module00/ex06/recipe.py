################## Exercise 06 - recipe.py #######################
##################################################################

cookbook = {"recipes": {'Sandwich': {'ingredients': ["ham", "bread", "cheese", "tomatoes"], "meal": "lunch", "prep_time": 10},
						'Cake': {'ingredients': ["flour", "sugar", "eggs"], "meal": "dessert", "prep_time": 60},
						'Salad': {'ingredients': ["avocado", "arugula", "tomatoes", "spinach"], "meal": "lunch", "prep_time": 15}}}


# def recipes_book(book):
# 	for name in book['recipes']:
# 		print(name)

def print_recipes(cook_book,recipe):
	print("Recipe for {}:\n Ingredients list: {}\n To be eaten for {}.\n Takes {} minutes of cooking.\n".format(recipe, cook_book['recipes'][recipe]['ingredients'], cook_book['recipes'][recipe]['meal'], cook_book['recipes'][recipe]['prep_time']))

def delete_recipe(cook_book, recipe):
	if recipe in cook_book['recipes']:
			cook_book['recipes'].pop(recipe)

def add_recipe(cook_book):
	name = input(">>> Enter a name:\n")
	tmp = {"ingredients": []}
	cook_book[name] = tmp
	ing = input(">>> Enter ingredients:\n")
	cook_book[name]['ingredients'].append(ing)
	while ing:
		ing = input("")
		cook_book[name]['ingredients'].append(ing)
	meal = input(">>> Enter a meal type:\n")
	cook_book[name]['meal'] = meal
	prep_time = int(input(">>> Enter a preparation time:\n"))
	cook_book[name]['prep_time'] = prep_time
	#remove the empty list element
	for i in cook_book[name]['ingredients']:
		if i == '':
			cook_book[name]['ingredients'].remove(i)
	return cook_book

def print_cookbook(cook_book):
	for rec in cook_book['recipes']:
		print("Recipe for {}:\n Ingredients list: {}\n To be eaten for {}.\n Takes {} minutes of cooking.".format(rec, cook_book['recipes'][rec]['ingredients'], cook_book['recipes'][rec]['meal'], cook_book['recipes'][rec]['prep_time']))
		print("#-------------------------------------------------------------------#\n")



def menu(cook_book):
	print("Welcome to the Python Cookbook !\nList of available option:")
	print(" 1: Add a recipe\n 2: Delete a recipe\n 3: Print a recipe\n 4: Print the cookbook\n 5: Quit")
	promt = input("Please select an option:\n>> ")
	while promt != '5':
		if promt == '1':
			add_recipe(cook_book)
			#menu(cook_book)
		elif promt == '2':
			recipe_name = input("Enter the name of the recipe to delete:\n")
			delete_recipe(cook_book, recipe_name)
		elif promt == '3':
			rec_details = input("Please enter a recipe name to get its details:\n")
			print_recipes(cook_book, rec_details)
			menu(cook_book)
		elif promt == '4':
			print_cookbook(cook_book)
			menu(cook_book)
	else:
		print("Sorry, this option does not exist.")


menu(cookbook)