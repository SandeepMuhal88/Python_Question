# Q26. what is Encapsulation?

# Encapsulation is a fundamental concept in object-oriented programming (OOP) that refers
# to bundling the data (attributes) and the methods (functions) that operate on the data into a single unit or class. 
# It also involves restricting direct access to some of the object’s components, 
# which is typically done to protect the integrity of the data and hide its internal implementation from outside interference.

# Key feature of Encapsulation
# Data hiding
# Controlled Access
# Improved Security


# private = __(double underscrow)
# protected = _(single underscrow)


# Example:-
class Car:
    def __init__(self, make, model):
        self._make = make     # protected attribute
        self.__model = model  # private attribute

    def get_model(self):      # Getter method for model
        return self.__model

    def set_model(self, model):  # Setter method for model
        if model:
            self.__model = model

# Usage
car = Car("Toyota", "Camry")
print(car._make)            # Accessible, but by convention, this is "protected"
print(car.get_model())       # Accessing private attribute via getter

car.set_model("Corolla")     # Modifying private attribute via setter
print(car.get_model())
