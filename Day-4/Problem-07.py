# Q7. what are the three properties of object ?


# 1. object can have variables
# 2. object can have methods
# 3. two object have different unique id

# id = (variable , function , class) provides unique value

# myth = id does not denotes memory address
# name = "radha"
# print(id(name))
# name="Rama"
# print(id(name))
# dono ki id will be change
# But
# two object will always have different id


class Student:
    def __init__(self,name,age,loaction,group):
        self.name=name
        self.age=age
        self.loacation=loaction
        self.group=group
        # print("I am calling from constructor class")

    def info(self):
        Name="Rahul"
        Address="Karani Nagar,Bikaner"
        age=20
        print(f"Name:-{Name}\nAddress:{Address}\n Age:{age}")


obj=Student("Sandeep","2000","Ajmer rajsthan","Teja group")
obj1=Student("Rahul","500","Sikhar","Monster")

print(id(obj))
print(id(obj1))


# We use assignment then it will same id
x=90
print(id(x))
y=x
print(id(y))