# Using explicit type conversion, change the following 
# inputs so the types match with the following below
#  
# name = type string
# age = type int
# height = type float
# loyalty = type boolean

# Modify the line below
# Using explicit type conversion to match the expected types

# For name (string)
name = input('What is your name? ')
print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# For age (int)
age_str = input('What is your age? ')
age = int(age_str)
print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# For height (float)
height_str = input('What is your height in meters? ')
height = float(height_str)
print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# For loyalty (boolean)
loyalty_str = input('Are you part of our loyalty program? ')
loyalty = loyalty_str.lower() == 'yes'  # Convert to boolean (True/False)
print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")
