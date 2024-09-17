# Q21. explain Hybrid Inheritance ?


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

class MUL:
    
        def Multiply(self,v1,v2):
            print(f"Multiply of two number:-{v1*v2}")
class Devide(SUB,MUL):
     def Devi(self,v1,v2): 
          print(f"Devide the value:-{v1/v2}")



obj=Devide()
obj.Addition(12,52)
obj.Substract(15,3)
obj.Devi(12,2)
obj.Multiply(22,22)
# concept    3

# hybrid = multiple + herichal:

# hybrid = combination of multiple and herichal
