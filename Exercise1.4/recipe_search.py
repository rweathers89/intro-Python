import pickle

#function to display recipe details
def display_recipe(recipe):
    print("Recipe: ", recipe["name"])
    print("Cooking Time (minutes): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty: ", recipe["difficulty"])
    print()

#function to search for an ingredient
def search_ingredient(data):
    print("Available Ingredients:")

    for index, ingredient in enumerate(data["all_ingredients"], start=1):
        print(str(index) + ". " + ingredient)
    
    try:
        ingredient_searched = data["all_ingredients"][
            int(input("Enter the number of the ingredient you want to search for: "))
        ]
    except ValueError:
        print("Only numbers are allowed")
    except:
      print("Oops! Your input does not match any ingredient. Please try again.")
    else:
        # search for recipes containing the ingredient
        recipes_found = []
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                recipes_found.append(recipe)
        # display the recipes found
        for recipe in recipes_found:
            display_recipe(recipe)

#name of file containing the recipes
filename = input("Enter the filename where you've stored your recipes: ")

try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print("File does not exist")
else: 
    search_ingredient(data)
finally:
    print("Goodbye!")
    file.close()