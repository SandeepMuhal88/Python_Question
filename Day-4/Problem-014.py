# Q14. explain multilevel inheritance ?
class Additation:
    def add(self,x,y):
        print(f"Sum of two numbers:- {x+y}")

class Substraction(Additation):
    def sub(self,x,y):
        print(f"Subtract two number= {x-y}")

class Multiply(Substraction):
    def mul(self,x,y):
        print(f"Multiply two number:-{x*y}")


obj=Multiply()
a=int(input("Enter first value:-"))
b=int(input("Enter second value:-"))
obj.mul(a,b)
obj.sub(a,b)
obj.add(a,b)


