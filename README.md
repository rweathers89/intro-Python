# Achievement 1

## Exercise 1.1

## Install and Setup Python

- First, install Python 3.8.7 on your system. Check your Python version by using the command `python --version` from your terminal.

- Set up a new virtual environment named “cf-python-base”.

- Create a Python script named “add.py”. This script will take two numbers from the user input, add them, and print the result.

- Set up an IPython shell in the virtual environment "cf-python-base". An IPython shell is similar to the regular Python REPL with additional features like syntax highlighting, auto-indentation, and robust auto-complete features. Install it using pip.

### Export a Requirements File
- Generate a “requirements.txt” file from your source environment by running `pip freeze > requirements.txt` in the terminal. In this case the source environment is "cf-python-base"

- Create a new virtual environment titled "cf-python-copy". 

- Copy the requirements.txt file to the new environment using the command `copy requirements.txt path\to\new\project`


- Activate the new environment using `./Activate.ps1` and then install packages from the "requirements.txt" using pip `pip install -r requirements.txt`

## Exercise 1.2

### Task

Create a structure that contains a set of attributes related to a specific recipe, and several of these “recipe structures” need to be stored sequentially in another outer structure.

The initial structure will be a dictionary titled "recipe_1" and contain the following keys:
- **name (str):** Contains the name of the recipe
- **cooking_time (int):** Contains the cooking time in minutes
- **ingredients (list):** Contains a number of ingredients, each of the str data type

The subsequent list structure will be titled "all_recipes", where I will add dictionaries including the "recipe_1" dictionary.

### Reasoning for Data Types

I chose to use a dictionary for my recipes as I want to be able to store more types of data such as lists and tuples. Doing so will allow for more veriety of the information that can be stored for each recipe.

The list type is appropriate for the "all_recipes" structure as it will allow for quick searches, where multiple recipes can be stored and modified as required.