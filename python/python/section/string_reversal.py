# trial='reversal'
# new_trial=trial[::-1]
# print(new_trial)


# def string_reverse(str):
#     if len(str)==0:
#         return str
#     else:
#         return string_reverse(str[1:]) + str[0]

# str = "reversal"
# reverse= string_reverse(str)

# print(reverse)

# =========================================#

# menu = ['espresso' , 'mosha', 'latte', 'cappuccino' , 'corado' , 'americano']

# def find_coffee(coffee):
#     if coffee[0]=='e':
#         return coffee

# map_coffee = map(find_coffee , menu)
# print(map_coffee)

# for x in map_coffee:
#     print(x)

# menu = ['espresso', 'mosha', 'latte', 'cappuccino', 'corado', 'americano']


# def find_coffee(coffee):
#     if coffee[0] == 'm':
#         return coffee
# ? To find items
# map_coffee = map(find_coffee , menu)
# print(map_coffee)


# for x in map_coffee:
#     print(x)
# ? To filter items
# filter_coffee = filter(find_coffee, menu)
# print(filter_coffee)

# for x in filter_coffee:
#     print(x)


# data = [2,3,5,7,11,13,17,19,23,29,31]

# # Ex1: List comprehension: updating the same list
# data = [x+3 for x in data]
# print("Updating the list: ", data)

# # Ex2: List comprehension: creating a different list with updated values
# new_data = [x*2 for x in data]
# print("Creating new list: ", new_data)

# # Ex3: With an if-condition: Multiples of four:
# fourx = [x for x in new_data if x%4 == 0 ]
# print("Divisible by four", fourx)

# # Ex4: Alternatively, we can update the list with the if condition as well
# fourxsub = [x-1 for x in new_data if x%4 == 0 ]
# print("Divisible by four minus one: ", fourxsub)

# # Ex5: Using range function:
# nines = [x for x in range(100) if x%9 == 0]
# print("Nines: ", nines)


def sum (n):
    if n ==1:
        return 0
    return n + sum(n-1)

a= sum(5)
print(a)