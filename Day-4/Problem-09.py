# Q9 what is inheritance


# 1. single level
# 2. multilevel
# 3. multiple
# 4. herichal
# 5. hybrid
class Person:
    name="xyz"
    PoneNo=78780000000
    lang="Python"
    def __init__(vari,x,y):
        # vari.name=name
        # vari.age=age
        vari.x=x
        vari.y=y
        print(f"Sum of two number:- {x+y}")
        

    def info(self):
        print("I am from Person class and info function")

class Inherit(Person):
    def demo(self):
        print("I am calling from Inherit class")

obj=Inherit(12,3)
obj.info()
obj.demo()