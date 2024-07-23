class Recipe(object):
    
    all_ingredients = []

    #Initialization method eith name and cooking time
    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None

    #Getter and Setter methods to get and modify recipe name/cooking time
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
    
    def add_ingredients(self, *ingredients):
        for ingredient in ingredients: 
            self.ingredients.append(ingredient)
        self.update_all_ingredients()

    def get_ingredients(self):
        print("\nIngredients: ")
        print("--------------\n")
        for ingredient in self.ingredients:
            print(str(ingredient))
    
    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty
    
    #sets difficulty attribute based on number of ingredients and cooking time
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    #Checks if ingredient is in the recipe:
    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False

    #updates all_ingredients list 
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    #a string representation that prints the recipe
    def __str__(self):
    #    return f"Recipe Name: {self.name}\nIngredients: {', ' .join(self.ingredients)}\nCooking Time(minutes): {self.cooking_time}\nDifficulty: {self.get_difficulty()}\n"
        
        output = "Name: " + self.name + "\nCooking Time (minutes): " + str(self.cooking_time) + \
        "\nIngredients: " + str(self.ingredients) + \
        "\nDifficulty: " + str(self.difficulty) + \
        "\n--------------------"
        #for ingredient in self.ingredients:
        #    output += "- " + ingredient + "\n"
        return output
        
#a method to search a recipe that contains a specific ingredient
def recipe_search(data, search_term):
    # Search for recipes containing a specific ingredient
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


#create instances of the Recipe class and add ingredients
tea = Recipe("Tea", "5")
tea.add_ingredients("Water", "Tea Leaves", "Sugar")
print(tea)

coffee = Recipe("Coffee", "5")
coffee.add_ingredients("Coffee powder", "Water", "Milk")
print(coffee)

cake = Recipe("Cake", "50")
cake.add_ingredients("Flour", "Sugar", "Eggs", "Milk", "Butter", "Vanilla Essence")
print(cake)

banana_smoothie = Recipe("Banana Smoothie", "5")
banana_smoothie.add_ingredients("Banana", "Milk", "Sugar", "Ice")
print(banana_smoothie)       

#create a list of all recipes
recipes_list = [tea, coffee, cake, banana_smoothie]

#using the recipe_search function to find recipes with specific ingredients
print("Recipes containg Water: ")
recipe_search(recipes_list, "Water")

print("Recipes containg Sugar: ")
recipe_search(recipes_list, "Sugar")

print("Recipes containg Bananas: ")
recipe_search(recipes_list, "Banana")

#for recipe in recipes_list:
#    print(recipe)

# Search for recipes that contain certain ingredients
#for ingredient in ["Water", "Sugar", "Bananas"]:
#    recipe_search(recipes_list, ingredient)       
