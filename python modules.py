# Importing built-in modules
import datetime
import math
import random
import os

# Using datetime module to get current date and time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Using math module to calculate square root
number = 25
square_root = math.sqrt(number)
print("Square root of", number, "is:", square_root)

# Using random module to generate a random number between 1 and 100
random_number = random.randint(1, 100)
print("Random Number:", random_number)

# Using os module to get current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)
