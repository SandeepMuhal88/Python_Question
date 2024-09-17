# Q18. what will happen when two class have same function and they inherits their properties to other class ?
class ADD:
    def Addition(self,Name):
        self.x=Name
        print(f"Add th number:-{self.x+Name}")

class SUB:
    def Addition(self,Name):
        self.x=Name
        print(f"Add SUB class number:-{self.x+Name}")


class Other(ADD,SUB):
    pass

obj=Other()
obj.Addition("Hetua")