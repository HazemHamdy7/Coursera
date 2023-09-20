# def divide_by(a, b):
#     return a/b

# ? Frist
# try:
#     ans = divide_by(40, 0)

# except Exception as e:
#     print("sorry we are not read ..", e)


# ? Second

# try:
#     ans = divide_by(40, 0)

# except Exception as e:
#     print("sorry we are not read ..", e)
#     print(e.__class__)


# #? third

# try:
#     ans = divide_by(40, 0)

# except ZeroDivisionError as e:
#     print("something error we are not read ..", e)
#     print(e.__class__)


# ? Forth


# try:
#     ans = divide_by(40, 0)

# except ZeroDivisionError as e:
#     print("something error we are not read ..", e)
# except Exception as e:
#     print("We are not opening sorry")

# ======================================================= ##
items = [1,2,3,4,5]

try:
   item = items[6]
except:
   print("soory i cant run code ..")




# Starter code
# def divide_by(a, b):
#     return a / b
# try:
#     ans = divide_by(40, 0)
# except ZeroDivisionError as e:
#    print("soory i cant run code222 ..")

# except Exception as e :
#        print("soory i cant run 33333 ..")


# def divide_by(a, b):
#    try:
#       return a/b 
#    except ZeroDivisionError :
#       return 0
#    except Exception as e :
#       print(e,"Something error")
# ans =divide_by(10,0)      
# print(ans)

with open('file_does_not_exist.txt', 'r') as file:
    print(file.read())


try:
   with open('file_does_not_exist.txt', 'r') as file:
       print(file.read)
 
except:
    print("i cant read file ")

