# Q28. how to create methods as (public, protected, private)?

class Arithmetic:
    def __Add(self,x,y):
        # Private Method
        self.k=x
        self.l=y
        print(f"Sum of two number:-{self.l+self.k}")

    def _Sub(self,x,y):
        # Protected Method
        self.k=x
        self.l=y
        print(f"Substract of two number:-{self.l-self.k}")

    def Mul(self,x,y):
        # Protected Method
        self.k=x
        self.l=y
        print(f"Multiply of two number:-{self.l*self.k}")

obj=Arithmetic()
# obj.__Add(45,63)
obj._Sub(45,12)
obj.Mul(45,2)