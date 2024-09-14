# Q how to create a constructor ?
class Student:
    def __init__(self,name,age,loaction,group):
        self.name=name
        self.age=age
        self.loacation=loaction
        self.group=group
        print("I am calling from constructor class")

obj=Student(name="Sandeep",age="2000",loaction="Ajmer rajsthan",group="Teja group")
print(obj.age)
print(obj.name)
print(obj.loacation)
print(obj.group)
print(obj.name)

# Self is the using variable and that conncet to us with class 
# varible.name=parameter
# name=argument



