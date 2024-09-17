
# Q19.If class B overrides method of class A and class C inherits properties from class B . can we access method of class A from C's object.



class ADD:
    def Addition(self,Value):
        self.x=Value
        print(f"Add th number:-{self.x+Value}")

class SUB(ADD):
    def Addition(self,Value):
        self.x=Value
        super().Addition(self.x)
        print(f"Add SUB class number:-{self.x-Value}")

class C(SUB):
    def Method(self):
        print("I am Forom class C")


obj=C()
obj.Addition(45)


# concept 1
# 1. method = ()
# 2. varibale = .
# class A:

#     def info(self):
#         print("class A")


# class B(A):

#     def info(self):
#         print("class B")
#         super().info()


# class C(B):

#     def m1(self):
#         print("class C")
#         super().info()


# obj = C()
# obj.m1()
