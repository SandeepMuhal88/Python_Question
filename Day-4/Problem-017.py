# Q17. what is "method resoultion order(MRO)" ?

# concept 1 (bases)


# class A:
#     pass


# class B:
#     pass


# class C(A, B):
#     pass


# obj = B()
# print(C.__bases__)

class Person:
    def __init__(Self):
        print("I am from Person class:--))")
        super().__init__()


class Human(Person):
    def __init__(self):
       print("I am from Human class")
       super().__init__()



class Man(Person):

    def __init__(self):
       print("I am from Man class")
       super().__init__()
   



class God(Human,Man):
    def __init__(self):
        print("I am from God class:))")
        super().__init__()



obj=God()
# print(God.mro())
# print(Man.__base__)


# class A:
#     def __init__(self):
#         print("class A")
#         super().__init__()


# class B(A):
#     def __init__(self):
#         print("class B")
#         super().__init__()


# class C(A):
#     def __init__(self):
#         print("class C")
#         super().__init__()


# class D(B, C):

#     def __init__(self):
#         print("class D")
#         super().__init__()


# obj = D()