# Q8. how many types of variables are there in python class ?

# there are two types of variables

# 1. instance variable = variable which inside a constructor are instance variables
# 2. class variable (static variable) = variable which outside of a constructor

class Person:
    name="xyz"
    PoneNo=78780000000
    lang="Python"
    def __init__(vari,name,age):
        vari.name=name
        vari.age=age
    def info(self):
        print("I am from Person class and info function")


obj=Person("Anuj Rati",200)
obj.info()
obj.age=21
print(obj.age)