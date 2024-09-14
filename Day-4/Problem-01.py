# Q1. what is a class ?

# 1. variables (attributes)
# 2. methods (function)

# myth  => class consist of variable or methods (this will always not true)
# class is a blue print for creating object.

# concept 1

# 1. variable = small letters
# 2. class = first word must be capital

class Student:
    def info(self):
        Name="Sandeep"
        Address="Karani Nagar,Bikaner"
        age=20
        print(f"Name:-{Name}\nAddress:{Address}\n Age:{age}")
    def add(self,a,b):
        print(f"Sum:-{a+b}")

# Create a object that 
obj=Student()
obj.info()
x=int(input("Enter a number:-"))
y=int(input("Enter a number:-"))

obj.add(x,y)