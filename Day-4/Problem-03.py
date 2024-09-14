# can we assign variable to empty class ?
# it is possible
# When python in program we can crete a class that both create dictionary
class Demo:
    pass

obj=Demo()
obj.Name="Sandeep"
# Obj.age=20
obj.age=200
print(obj.Name)
print(obj.age)
print(obj.__dict__)


class Students:
    pass


obj = Students()
print(obj)
obj.Name = "sandeep"  # dynamically
print(obj.__dict__)
obj.age = 20
print(obj.age)

# Concept class is empty then we can assign only variable
# That run time empty class is create a dictionary dynamically