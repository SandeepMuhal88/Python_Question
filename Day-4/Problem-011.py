# Q11. what is the use of super keyword.

class Person:
    def __init__(self,Name,Age,Location):
        self.naam=Name
        self.umr=Age
        self.loac=Location
        print("I am calling from Person class")
    
    def info(self,name):
        self.name=name
        print(f"Good morning!! {name}")

class Human(Person):
    def __init__(self,x,y):
        super().__init__("Rahul",89,"Ajmer jahfj")
        self.value=x
        self.value1=y
        print(f"Sum of two Number:-{x+y}")
       
obj=Human(12,63)
print(obj.__init__)
xyz=input("Enter your name:-")
obj.info(xyz)

# class Students:
#     # lang = "python"
#     def __init__(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location
#         print("calling from constructor")

#     def info(self):
#         print(f"name : {self.name}")


# class Person(Students):

#     def __init__(self, name, lang):

#         super().__init__(name, age=None, location=None)
#         self.lang = lang

#     def jp(self):
#         print("calling from person class")


# obj = Person("jp", "java")
# obj.info()