# def sum_of(a, b):
#     return a + b
# print(sum_of(4, 5))


# def sum_of(**kwargs):
#     sum = 0
#     for k , v in kwargs.items():
#         sum += v
#     return round(  sum , 3)    

     
# print(sum_of(coffee = 2.99 , tea = 4.55 , huice = 2.99))


employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id]


print(get_employee_from_dict(12458))