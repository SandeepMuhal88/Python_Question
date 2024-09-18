# Q22. what is Polymorphism?
# concept 1
# ploy = many
# morphism = forms

# Polymorphism can be achieved in Python in several ways, mainly through:

# Method Overriding (in Inheritance)
# Duck Typing
# Operator Overloading
# concept2
# 1.method overloading
# 2. method overriding
class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

class Cat(Animal):
    def speak(self):
        print("The cat meows.")

# Creating objects of the classes
animals = [Dog(), Cat()]

# Looping through the list of animals
for animal in animals:
    animal.speak()  # Polymorphism in action
