# n1 = input('First number is: ')
# n2 = input('Second number is: ')
# user_sum = float(n1) + float(n2)
# print("The sum of " + str(n1) + " and " + str(n2) + " is " + str(user_sum))


# bill_total = 210

# discount1 = 10
# discount2 = 20

# if bill_total > 100 and bill_total < 200:
#     print("Bill is greater than 100")
#     bill_total = bill_total - discount1
# elif bill_total > 200:
#     bill_total = bill_total - discount2
#     print("Bill is less than 200")
# else:
#     print("Bill is less than 100")


# print("Total bill " + str(bill_total))


# http_status=200

# if http_status ==200 or http_status ==201:
#     print('Success')
# elif http_status ==400 :
#     print('Bad requset')
# elif http_status == 404 :
#     print('Not Error')
# elif http_status == 500:
#     print('Server Error')

# Match and Case
# match http_status:
#     case 200 | 201 :
#         print('Seccess')
#     case 400 :
#         print('Bad')
#     case 500:
#         print('Servers')
#     case _:
#         print('UnKnown')

# Starter Code
# Starter Code
# favorites = ['Creme Brulee', 'Apple', 'Churros', 'Tiramisú', 'Chocolate Cake']

# for dessert in favorites:
#     if dessert == 'Apple':
#         pass
#     print('Other desserts I like are', dessert)


# faverites =['Hazem' , 'Hamdy' , 'Abdallah' , 'Hassan']


# for idx, item in enumerate(faverites):
#     print(id,item)

# for item in faverites:
#     print('Looping ..',item)

# count = 0
# while count < len(faverites) :
#    print('My name is ' ,faverites[count])
#    count+=1
# import time
# start_time=time.time()
# num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
# count = 0
# for  x ,num in enumerate(num_list):
#     count += 1
#     if num == 77:
 
#         print('Number found at ' , x)
#         break
# print(count)
 


# print(round((time.time() - start_time),2))   

# def calculate_tax(bill, tax):
#     return round((bill * tax) / 100.00,2)

# print("Total is " , calculate_tax(175.00 ,15))
# print("Total is " , calculate_tax(100.00 ,15))

# my=100

# def fn1():
#     enclosed = 8
#     def fn2():
#         lacal_v = 5
#         print("Access " , my)
#         print("Access " , enclosed)
#     fn2()    
# fn1()    


# list1 =[1,2,3,4,5]
# print(list1 , sep=" ")

# list1.insert(len(list1), 6)
# list1.append (6)
# list1.extend([6,7,8,9])
# list1.pop(2) # to remove item
# del list1[2]

# print(list1 )

# for x in list1:
#     print('Value :' ,x)


list1 =[1,2,3,4,5]


print(list1, sep= "" )

for i in list1:
    print("Value :" ,i)