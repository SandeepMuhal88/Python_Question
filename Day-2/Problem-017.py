# Q what is high order function. Explain with example ?
def double(value):
    return value*2

def add(double,a,b):
    result=a+b
    print("Sum of two number:-",result)
    print("After sum double value",double(result))

a=int(input("Enter first number:- "))
b=int(input("Enter second value:-"))

add(double,a,b)