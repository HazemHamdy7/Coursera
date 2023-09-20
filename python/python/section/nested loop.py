# list1= [ 1,2,3,4,5]
# list2= [ 6,7,8,9,10]

# for x in list1:
#     print(x)
#     for y in list2:
#
#         print(y)


# import time
# start_time =time.time()

# for i in range(100):
#     for x in range(10000):
#         print(0, end=" ")
#     print()
# print(round((time.time() - start_time) , 2))

num_list = [33, 42, 5, 66, 77, 22, 16, 79,36, 62, 78, 43, 88, 39, 53, 67, 89, 11]


# for num in num_list:
#     if num > 45:
#         print('Over 45')
#     else:
#         print('Uder 45')

count  = 0
for x ,num in enumerate( num_list):
    count +=1

    if num ==36:
        print("Number found at " , x)
        break
 
print(count)

