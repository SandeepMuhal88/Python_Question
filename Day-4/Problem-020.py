# Q20. explain Hierarchical Inheritance ?
# 
# In Python, hierarchical inheritance is a type of inheritance where multiple child classes inherit from the same base 
# or parent class. This means that the parent class is at the top of the hierarchy,
#  and multiple child classes are below it, inheriting its properties and methods.

class ADD:
    def Addition(self,value1,value2):
        self.x=value1
        self.y=value2
        print(f"Sum od two number:-{self.x+self.y}")

class SUB(ADD):
    def Substract(self,v1,v2):
        self.x=v1
        self.y=v2
        print(f"Substract of two number:-{self.x-self.y}")

class MUL(ADD):
    
        def Multiply(self,v1,v2):
            print(f"Multiply of two number:-{v1*v2}")
            
            
"""That is provide multipy of two number"""

obj=MUL()
print(MUL.mro())
obj.Addition(12,52)
obj.Multiply(2,5)
obj1=SUB()
obj1.Substract(45,25)