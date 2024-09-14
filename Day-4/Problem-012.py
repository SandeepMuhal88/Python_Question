# Q12. how to overrides method ?

class Person:
    def diplay(self):
        print(f"Good morning !!")
        print("I from Class person!!")

class Human(Person):
    def diplay(self):
        print("Good Night bro!!")
        print("I from class Human")
        super().diplay()
 
obj=Human()
obj.diplay()








class A:
    def method(self):
        print("class A")


class B(A):
    def method(self):
        print("class B")
        super().method()


obj = B()

obj.method()