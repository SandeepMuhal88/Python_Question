# Q. Program to add to numbers

# MEthod first
# x=int(input("Enter first number:- "))
# y=int(input("Enter ssecond number:- "))
# print("Sum of two Numbers:-",x+y)

# Method second
# x,y=map(int, input("Enter two numbers:- ").split())
# print("Sum of two numbers:-",x+y)

# MEthod third
x,y=map(int, input("Enter two numbers:- ").split(","))
print("Sum of two numbers:-",x+y)

name="My name is sandeep Muhal"
print(name.split("e"))
print(type(name.split()))