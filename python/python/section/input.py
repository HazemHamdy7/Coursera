# num = input('please enter fristnum : ')
# num2 = input('please enter second num : ')

# print(type(num))

# result = int(num) + int(num2)
# print(result)


# str1 = input('please enter frist name: ')
# str2 = input('please enter second name : ')



# result = str1 + ' ' + str2
# print('Hello' , result)
# print('Hello {} {}'.format(str1 , str2))


# # Using explicit type conversion, change the following 
# # inputs so the types match with the following below
# #  
# # name = type string
# # age = type int
# # height = type float
# # loyalty = type boolean

# # Modify the line below
# name = input('What is your name? ')

# print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# # Modify the line below
# age = input('What is your age? ')

# print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# # Modify the line below
# height = input('What is your height in meters? ')

# print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# # Modify the line below
# loyalty = input('Are you part of our loyalty program? ')

# print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")



# # The below script will ask for 3 inputs. Each input will be based
# # on the price of the items - the price is determined by you. The output
# # should print the total of the 3 inputs rounded to 2 decimal places e.g
# #
# #   1 coffee @ $ 2.00
# #   1 sandwich @ $ 4.99
# #   1 cake @ $ 2.75
# #
# #   Your total bill is $ 9.74

# # Modify the line below
# coffee = input('1 coffee @: $ ')

# # Modify the line below
# sandwich = input('1 sandwich @: $ ')

# # Modify the line below
# cake = input('1 cake @: $ ')

# bill_total = float(coffee) + float(sandwich) + float(cake)

# print('Your total bill is $', bill_total)


# Input prices for coffee, sandwich, and cake
coffee_price = 2.00
sandwich_price = 4.99
cake_price = 2.75

# Get quantities from the user
coffee_quantity = int(input('How many coffees would you like to order? '))
sandwich_quantity = int(input('How many sandwiches would you like to order? '))
cake_quantity = int(input('How many cakes would you like to order? '))

# Calculate the total bill
total_bill = (coffee_quantity * coffee_price) + (sandwich_quantity * sandwich_price) + (cake_quantity * cake_price)

# Print the bill rounded to 2 decimal places
print(f'Your total bill is ${total_bill:.2f}')
