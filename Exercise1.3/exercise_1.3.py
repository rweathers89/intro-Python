# empty lists for recipes and ingredients
recipes_list = []
ingredients_list = []

#function to take user recipe input
def take_recipe(): 
    name = str(input("Recipe Name: "))
    cooking_time = int(input("Cooking Time (minutes): "))
    ingredients = list(input("Ingredients").split(", "))
    recipe = {
        "name": name, 
        "cooking_time": cooking_time, 
        "ingredients": ingredients
        }
    return recipe
#END take_recipe function

#initial prompt for user
n = int(input("How many recipes would you like to enter? "))

#for loop: number of recipes given
for i in range(n):
    recipe = take_recipe()

    #checks if ingredient should be added to a given list
    for ingredient in recipe["ingredients"]:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

#determines recipe difficulty
for recipe in recipes_list:
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Intermediate"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Hard"

#display all information of recipe from recipe_list
for recipe in recipes_list:
    print("Recipe: ", recipe["name"])
    print("Cooking Time (minuntes): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty: ", recipe["difficulty"])

#display all ingredients from all recipes in alphabetcal order
def all_ingredients():
    ingredients_list.sort()
    print("Ingredients Avaialable Across All Recipes")
    print("=======================================")
    for ingredient in ingredients_list:
        print(ingredient)

all_ingredients()