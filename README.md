# Exercise 1

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
