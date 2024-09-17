# Q16. access constructor of parent class in child class (multiple inheritance)?

class Personal:
    def __init__(self,Name,Address,Hoby,PhoneNO):
        self.temp=Name
        self.temp1=Address
        self.tem2=Hoby
        # print(f"I am calling from Personal class))")
        super().__init__(PhoneNO)
        
    def Detail_print(self):
        print(f"Name:-{self.temp}")
        print(f"Address:-{self.temp1}")
        print(f"Hoby:-{self.tem2}")

class Public:
    def __init__(self,phoneNo):
        self.No=phoneNo
        print("I am calling from Public class")

    def Print(self):
        print(f"Phone Number:- {self.No}")

class Customer(Personal,Public):
    def __init__(self,Name,Address,Hoby,PhoneNo):
        print("I am from Customer class:-")
        super().__init__(Name,Address,Hoby,PhoneNo)


obj=Customer("Sandep","Ajmer","Book",7878496344)
obj.Detail_print()
obj.Print()



# class A:

#     def __init__(self, name, age):
#         self.name = name
#         print(f"name : {self.name}")
#         super().__init__(age)


# class B:

#     def __init__(self, age):
#         self.age = age
#         print(f"age : {self.age}")


# class C(A, B):

#     def __init__(self, location, name, age):
#         self.location = location
#         print(f"location : {self.location}")
#         super().__init__(name, age)


# obj = C("Ajmer", "jp", 21)


# concept 1
# 1. constructor has no return type
# 2. constructor makes instance variable
# 3. class => object => constructor will called


# concept 2
# class A:
#     pass


# obj = A()
# obj.name = "jp"
# obj.age = 21

# print(obj.name)
# print(obj.__dict__)