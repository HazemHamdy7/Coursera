

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

try :
    with open('dd/newfile.txt', mode='a') as file:
        file.writelines(["\nHello there My name Hazem",
                        "\nHello there My name Hazem", 
                       "\nHello there My name Hazem"])
except  FileNotFoundError as e :
    print("Error" , e)