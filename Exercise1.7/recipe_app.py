from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

# Connecting to SQAlchemy with database "task_database"
engine = create_engine("mysql://cf-python:password@localhost/task_database")
#Create declarative base
Base = declarative_base()

# create session object that will bind to the engine 
# session object will be used to make changes to the database
Session = sessionmaker(bind=engine)
session = Session()


# Recipe class using the declaritive Base class
class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Show a quick representation of the recipe
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + str(self.difficulty) + ">"
    
    # Print a well-formatted version of the recipe
    def __str__(self):
        return "<Recipe: " + str(self.name)

    # Calculate the difficulty of a recipe based on the number of ingredients and cooking time
    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients.split(", "))
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        if self.cooking_time < 10 and num_ingredients >= 4: 
            self.difficulty = "Medium"
        if self.cooking_time >= 10 and num_ingredients< 4: 
            self.difficulty = "Intermediate"
        if self.cooking_time >= 10 and num_ingredients >= 4:
            self.difficulty = "Hard"
    
    def return_ingredients_as_list(self):
        if self.ingredients == "": return []
        return self.ingredients.split(", ")
    
# Create the corresponding table on the database
Base.metadata.create_all(engine)

# --- Main Menu Functions --- #

# Function to add a new recipe
def create_recipe():
    # collect recipe details
    while True:
        name = str(input("Enter the name of the recipe: "))
        if len(name) > 50:
            print("Recipe name is too long, please enter a name with a maximum of 50 characters including spaces.")
        else: break
    
    while True: 
        cooking_time_input = input("enter the cooking time of the recipe (minutes): ")
        if not cooking_time_input.isnumeric():
            print("This is not a number. Please enter cook time minutes as a number")
        else:
            cooking_time = int(cooking_time_input)
            break
    
    ingredients_list = []
    #ingredient = input("Enter the ingredients of the recipe (separated by comma): ").split(", ")
    #for i in range(ingredient):
    #    ingredient = input(f"\nEnter ingredient {i+1} or type 'done' to finish: ")   
    
    while True:
        ingredients_input = input("  Enter the recipe's ingredients, separated by a comma: ").strip()
        if ingredients_input:
            break
        else:
            print("Please enter at least one ingredient.\n")
    #    ingredient = input("Enter the ingredients of the recipe (separated by comma): ").split(", ")
    #    if ingredient != "done":
    #        ingredients_list.append(ingredient)
    #    else: break
    ingredients = ", ".join(ingredients_list)

    # Create new object from the Recipe model
    recipe_entry = Recipe(name=name, ingredients=ingredients, cooking_time=cooking_time)
    # Generate difficulty attribute for this recipe
    recipe_entry.calculate_difficulty()
    # add to the database and commit changes
    session.add(recipe_entry)
    session.commit()

# Function to view recipes
def view_all_recipes():
    all_recipes = session.query(Recipe).all()
    # if no recipes in database, inform user and exit function
    if len(all_recipes) == 0:
        print("There are not recipes")
        # to exit the function
        return None
    else: 
        print("Here are all the recipes in the database:")
    for recipe in all_recipes:
        print(recipe)

# Function to search recipes by ingredient
def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("There are no recipes in the database")
        return None
    # Get ingredients from database
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    for result in results:
        ingredients = result[0].split(", ")
        for ingredient in ingredients:
            if not ingredient in all_ingredients:
                all_ingredients.append(ingredient)
    # Print all ingredients
    print("Here are all ingredients in the database:")
    for count, ingredient in enumerate(all_ingredients):
        print(count, ingredient)
    search_ingredient = input("Enter the numbers of the ingredients you want to search for(separate by space): ").split()
    for i in search_ingredient:
        if not i.isnumeric() or int(i) > len(all_ingredients):
            print("Please enter a valid number")
            return None
    # Search for recipes containing the desired ingredients
    search_ingredient = [all_ingredients[int(i) - 1] for i in search_ingredient]
    conditions = []
    for ingredient in search_ingredient:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))
    recipes = session.query(Recipe).filter(*conditions).all()
    for recipe in recipes:
        print(recipe)

# Edit a recipe in the database
def edit_recipe():
    if session.query(Recipe).count() < 1:
        print("There are no recipes in the database")
        return None
    # Get all recipe names and IDs from database
    results = session.query(Recipe.id, Recipe.name).all()
    print("Here are the recipes in the database")
    for result in results:
        print(result[0], result[1])
    recipe_id = input("Enter the number of the recipe you want to edit: ")
    while not recipe_id.isnumeric() or int(recipe_id) > len(results):
        print("Please enter a valid number")
        recipe_id = input("Enter the number of the recipe you want to edit: ")
    recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).first()
    print("Please edit: " + str(recipe_to_edit))
    print("Which part of the recipe would you like to edit?")
    print("1. Name")
    print("2. Ingredients")
    print("3. Cooking time")
    attribute = input("Enter the number of the recipe attribute you want to edit: ")
    while not attribute.isnumeric() or int(attribute) > 3:
        print()
        print("Please enter a valid number")
        attribute = input("Enter the number of the recipe attribute you want to edit: ")
    if attribute == "1":
        print()
        new_name = input("Enter the new name: ")
        while not new_name.isalnum() or len(new_name) > 50:
            print()
            print(
                "Please enter a recipe name that is alphanumeric and less than 50 characters"
            )
            new_name = input("Enter the new name: ")
        recipe_to_edit.name = new_name
    elif attribute == "2":
        print()
        #num_ingredients = input("How many ingredients do you want to add? ")
        ingredients_list = []
        while True:
            ingredient = str(input("Enter new ingredient: "))
            if ingredient != "":
                ingredients_list.append(ingredient)
            else: break
        ingredients = ", ".join(ingredients_list)
        recipe_to_edit.ingredients = ingredients
        recipe_to_edit.calculate_difficulty()
        
        #for i in range(int(num_ingredients)):
        #    print()
        #    ingredient = input(f"Enter ingredient {i+1} or type 'done' to finish: ")
        #    #fix this line
        #    while not ingredient.isalpha(ingredient) and ingredient != "done":
        #        print()
        #        print(
        #            "Please enter an ingredient using only letters, spaces or hyphens"
        #        )
        #        ingredient = input(f"Enter ingredient {i+1} or type 'done' to finish: ")
        #        if ingredient != "done":
        #            new_ingredients.append(ingredient)
        #new_ingredients = ", ".join(new_ingredients)
        #recipe_to_edit.ingredients = new_ingredients
    elif attribute == "3":
        print()
        new_cooking_time = input("Enter the new cooking time in minutes: ")
        while not new_cooking_time.isnumeric():
            print()
            print("Please enter a cooking time that is numeric")
            new_cooking_time = input("Enter the new cooking time in minutes: ")
        recipe_to_edit.cooking_time = int(new_cooking_time)
    recipe_to_edit.calculate_difficulty()
    session.commit()
    print()
    print("Recipe edited successfully!")
    print()

    # Delete recipe
def  delete_recipe():
    # Check if any recipes exist on database
    if session.query(Recipe).count() < 1:
        print("There are no recipes in the database!")
        return
    # Get all recipe names and IDs from database
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    # Print recipe IDs and names
    ids = []
    for recipe in results:
        print(recipe[0], recipe[1])
        ids.append(recipe[0])
    # Get ID of recipe from user
    try:
        id = int(input("Please enter the ID of the recipe that you want to delete and hit enter: "))
    except:
        print("Input is invalid! Going back to main menu.")
        return
    # Check ID
    if not id in ids:
        print("ID not found! Going back to main menu.")
        return
    recipe_to_delete = session.query(Recipe).filter(Recipe.id == id).one()
    print(recipe_to_delete)
    answer = input("Are you sure to delete this recipe? (If yes, enter 'yes' and hit enter): ")
    if answer == "yes":
        session.delete(recipe_to_delete)
        session.commit()
        print("Deleted!")

### --- MAIN LOOP --- ###

choice = ""
while (choice != "quit"):
    print("\nMAIN MENU")
    print("=" * 50)
    print("Pick a choice:")
    print("\t1. Create a new recipe")
    print("\t2. View all recipes")
    print("\t3. Search for a recipe by ingredients")
    print("\t4. Update an existing recipe")
    print("\t5. Delete a recipe")
    print("\tType 'quit' to exit the program")
    choice = input("Your choice: ")

    if choice == "1": create_recipe()
    elif choice == "2": view_all_recipes()
    elif choice == "3": search_by_ingredients()
    elif choice == "4": edit_recipe()
    elif choice == "5": delete_recipe()
    elif choice != "quit": print("Invalid input!")

# End: Closing session and database
session.close()
engine.dispose()