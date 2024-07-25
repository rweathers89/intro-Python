import mysql.connector

# initialze the connection object
conn = mysql.connector.connect(
  host='localhost', 
  user='cf-python', 
  passwd= 'password')

# initialize cursor object from conn
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
               id INT PRIMARY KEY AUTO_INCREMENT,
               name VARCHAR(50),
               ingredients VARCHAR(255),
               cooking_time INT,
               difficulty VARCHAR(20))''' )

# main menu function
def main_menu(conn, cursor):
    choice = ""
    while(choice!= "quit"):
        print("Main Menu")
        print("-------------")
        print("Pick a choice:")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)

def create_recipe(conn, cursor):
    recipe_ingredients = []
    name = str(input("Enter Recipe Name: "))
    cooking_time = int(input("Enter the cooking time (minutes): "))
    ingredients = str(input("Enter the ingredients: "))
    recipe_ingredients.append(ingredients)
    difficulty = calculate_difficulty(cooking_time, ingredients)
    # converts ingredients to a string
    recipe_ingredients_str = ", ".join(recipe_ingredients)
   
    # SQL statment
    sql = 'INSER INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (name, recipe_ingredients_str, cooking_time, difficulty)
    
    # execute SQL statment to insert recipe into table
    cursor.execute(sql, val)
    
    # commit changes to the table
    conn.commit()
    print("Recipe saved into database.")

def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    if cooking_time < 10 and len(ingredients) >= 4: 
        return "Medium"
    if cooking_time >= 10 and len(ingredients) < 4: 
        return "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        return "Hard"
    


def search_recipe(conn, cursor):
    all_ingredients = []
    # fetch ingredients from the table
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    # Loop through results
    for ingredients_list in results:
        for recipe_ingredients in ingredients_list:
            recipe_ingredients_list = recipe_ingredients.split(", ")
            all_ingredients.extend(recipe_ingredients_list)
   
    #Remove duplicates from list
    all_ingredients = list(dict.fromkeys(all_ingredients))

    #Show available ingredients
    all_ingredients_list = list(enumerate(all_ingredients))

    print("All Ingredients: ")
    for index, ingredient in enumerate(all_ingredients_list):
        print(f"{index}.{ingredient}")
    
    try:
        ingredient_choice = input("Select the number of the ingredient you want to search for: ")
        ingredient_index = int(ingredient_choice)
        search_ingredient = all_ingredients[ingredient_index]
        print("You selectd: ", search_ingredient)
    except:
        print("An unexpected error occured.")
    else:
        print("The recipe(s) below include the selected ingredient: ")


    # search for recipes containing the selected ingredient
    sql = "SELECT name, ingredients, cooking_time, difficulty FROM Recipes WHERE ingredients LIKE %s)"
    val = ("%" + search_ingredient + "%")

    cursor.execute(sql, val)
    search_results = cursor.fetchall()
    print("Recipes containing the ingredient: ")
    for row in search_results:
        print(row)


def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    print("Available Recipes")
    for row in results: 
        ingredients_list = row[0].split(", ")
        ingredients_list_str = ", ".join(ingredients_list)

        print(f"ID: {row[0]} | Name: {row[1]}")
        print(f"Ingredients: {ingredients_list_str} | Cooking Time: {row[3]} | Difficulty: {row[4]}")

    while True:
        try:
            print()
            recipe_id = int(input("Enter the ID of the recipe to update: "))
            print()

            cursor.execute("SELECT COUNT(*) FROM Recipes WHERE id = %s", (recipe_id,))
            if cursor.fetchone()[0] == 0:
                print("No recipe found with the entered ID. Please try again.\n")
            else:
                break
        except ValueError:
            print()
            print("Invalid input. Please enter a numeric value.\n")

    selected_recipe = next((recipe for recipe in results if recipe[0] == recipe_id), None)
    if selected_recipe:
        print(f"Which field would you like to update for '{selected_recipe[1]}'?")
    else:
        print("Recipe not found.")
        return
    print(" - Name")
    print(" - Cooking Time")
    print(" - Ingredients\n")

    update_field = input("Enter your choice: ").lower()
    print()

    if update_field == "cooking time":
        update_field = "cooking_time"

    if update_field not in ["name", "cooking_time", "ingredients"]:
        print("Invalid field. Please enter 'name', 'cooking_time', or 'ingredients'.")
        return
    
    if update_field == "cooking_time" or update_field == "cooking time":
        while True:
            try:
                new_value = int(input("Enter the new cooking time (in minutes): "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for cooking time.")
    else:
        new_value = input(f"Enter the new value for {update_field}: ")

    update_query = f"UPDATE Recipes SET {update_field} = %s WHERE id = %s"
    cursor.execute(update_query, (new_value, recipe_id))

    if update_field in ["cooking_time", "ingredients"]:
        cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        updated_recipe = cursor.fetchone()
        new_difficulty = calculate_difficulty(int(updated_recipe[0]), updated_recipe[1].split(", "))

        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (new_difficulty, recipe_id))


    conn.commit()

def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    print("Available Recipes")
    recipe_to_delete = int(input("Enter the ID of the recipe you want to delete: "))
    # Delete the recipe
    cursor.execute("DELETE FROM Recipes WHERE id = (%s)", (recipe_to_delete))
    
    conn.commit()
    print("Recipe deleted")


conn.close()