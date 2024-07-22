import pickle

#function to take a recipe from the user
def take_recipe():
    name = str(input("Enter the recipe: "))
    cooking_time = int(input("Enter the cooking time (minutes): "))
    ingredients = [
        ingredient.strip().capitalize()
        for ingredient in input("Enter the ingredients separated by a comma: ").split(",")
    ]

#creates recipe dictionary
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    # calculate the difficulty level for the recipe
    difficulty = calc_difficulty(recipe)
    # add the difficulty level to the recipe dictionary
    recipe["difficulty"] = difficulty
    return recipe

#function to calculate recipe difficulty
def calc_difficulty(recipe):
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        difficulty = "Medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"
    return difficulty

#User enters the name of the file
filename = input("Enter the filename where your recipes are stored: ")

# Try to open the file, if it doesn't exist, creat a new file
try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
        print("File loaded successfully!")

#Error: If file does NOT exist, creates new dictionary
except FileNotFoundError:
    print("File does not exist - creating new file")
    data = {"recipes_list": [], "all_ingredients": []}

#Error: general error is something goes wrong
except:
    print("Oops! Something went wrong. Try again.")
    data = {"recipes_list": [], "all_ingredients": []}

#close the file
else:
    file.close()
#extracts data into 2 variables
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

#prompts the user to input the number of recipes to add
n = int(input("How many recipes would you like to add? "))

#take recipes from user and add to recipes_list
for i in range(n):
    recipe = take_recipe()

    #update all_ingredients with new ingredients
    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

    #add recipe to recipes_list
    recipes_list.append(recipe)

#Save the recipe_list and all_ingredients to a dictionary
data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

#Save the dictionary to a user-specified file
filename = input("Enter the filename where you'd like to store your recipes: ")
with open(filename, "wb") as file:
    pickle.dump(data, file)
    print("Recipes saved successfully!")
    file.close()