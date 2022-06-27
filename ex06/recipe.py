#!/usr/bin/python

def	flavor_town():
	print("Welcome to Flavor Town! What do you want to do?")
	print("1 : Add recipe")
	print("2 : Delete recipe")
	print("3 : Print a recipe")
	print("4 : Print the cookbook")
	print("5 : Quit")

def print_only_recipe(recipe):
	print(cookbook.get(recipe, None))

def print_available_recipes():
	keys = cookbook.keys()
	print("The available recipes are :")
	for x in keys:
		print("-" + str(x))

def add_recipe(name: str, ingredients: tuple, meal: str, prep_time: int):
	cookbook.update({name : {"ingredients" : ingredients, "meal" : meal, "prep_time" : prep_time}})

def delete_recipe(recipe):
	cookbook.pop(recipe, None)

cookbook = {
	"sandwich" : {
		"ingredients" : ["Ham", "Bread", "Cheese", "Tomatoes"],
		"meal" : "Lunch",
		"prep_time" : 10
	},
	"cake" : {
		"ingredients" : ["Flour", "Sugar", "Eggs"],
		"meal" : "Dessert",
		"prep_time" : 60
	},
	"salad" : {
		"ingredients" : ["Avocado", "Arugula", "Tomatoes", "Spinach"],
		"meal" : "Lunch",
		"prep_time" : 15
	}
}
flavor_town()