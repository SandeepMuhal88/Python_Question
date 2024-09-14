# Q10. how to override a constructor ?
# Diffrent paramenters and method name same
class Person:
    def __init__(self,Name,Age,Location):
        self.naam=Name
        self.age=Age
        self.loac=Location
        print("I am calling from Person class")
    
    def info(self,name):
        name= input("Enter your Name:")
        self.name=name
        print(f"Good morning!! {name}")

class Human(Person):
    def __init__(self,x,y):
        self.value=x
        self.value1=y
        print(f"Sum og two Number:-{x+y}")

obj=Human(12,63)
obj.info("Sandeep")