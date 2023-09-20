

# file = open("test.txt", mode='r')
# deta = file.readline()
# print(deta)
# file.close()


# with open("newfile.txt" , mode="r") as file:
#     date = file.readline()
#     print(date)


# ? to create file one line
# with open('newfile.txt' , mode='w') as file:
#     file.write("Hello there My name Hazem")


# # ? to create file multie lines
# with open('newfile.txt', mode='w') as file:
#     file.writelines(["Hello there My name Hazem",
#                     "\nHello there My name Hazem", 
#                     "\nHello there My name Hazem"])


# # ? to repet file change mode to 'a'
# with open('newfile.txt', mode='a') as file:
#     file.writelines(["\nHello2 there My name Hazem",
#                     "\nHello there My name Hazem", 
#                     "\nHello there My name Hazem"])
                    

# # ? to exception file  

# try :
#     with open('dd/newfile.txt', mode='a') as file:
#         file.writelines(["\nHello there My name Hazem",
#                         "\nHello there My name Hazem", 
#                        "\nHello there My name Hazem"])
# except  FileNotFoundError as e :
#     print("Error" , e)



# import random
# f = open("petnames.txt", "r")
# f_content= f.read()
# f_content_list = f_content.split("\n")
# print(random.choice(f_content_list))


# import random

# f_name = input('Type the file name: ')

# f = open(f_name,'r') # "r" omitted as it's the default
# f_content = f.read()
# f_content_list = f_content.split("\n")
# print(random.choice(f_content_list))


import random

f_name = input("Taye thr file name : " )
f = open(f_name,'r')
f_content = f.read()
f_content_list = f_content.split("\n")

print(random.choice(f_content_list))
