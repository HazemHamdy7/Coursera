# with open('hhh.txt' , mode ='r') as file:
#     date = file.readline()
#     print(date)


# with open('test.txt' ,  'w') as file:
#     file.writelines  (["This is a new file create!" , "\nAHazm hamdy"])

try:
    with open(' test.txt' ,  'w') as file:
        file.writelines  (["\nThis is a new file create!" , "\nAHazm hamdy"])   
except FileNotFoundError as e:
  print("Errorrrrrrrrr",e )  