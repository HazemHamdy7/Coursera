def divide(a,b):
    return a / b
try:
    nn= divide(40 , 0)
except Exception as e:
    print("someinfg error" , e)   
    print( e.__class__) 