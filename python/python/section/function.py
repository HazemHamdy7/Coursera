# coffees= ['Espresso' , 'Latte', 'Cappuccino','Macchiato']

# print(sorted(coffees))



# coffees= ['Espresso' , 'Latte', 'Cappuccino','Macchiato']

# def revrse(str):
#     return str[::-1]
# reversed_coffees = map(revrse, coffees)

# for x in reversed_coffees:

#     print(x)




# my_list= [1,2,3]

# def add_to_list(item):
#     return my_list.append(item)


# add_to_list(6)
# print(my_list)


def calculate_tex(bill , tex):
    return round((bill * tex) /100.00 , 2 )

print("Total bii" , calculate_tex(175.00 ,15))
print("Total bii" , calculate_tex(163.00 ,25))

