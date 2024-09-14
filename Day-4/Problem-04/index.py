# Q4. why "Type of class " include "__main__" ?

import Demo 

obj01=Demo.Student()
obj01.info()
obj01.add(12,63)
print(type(obj01))


class Person:
    pass


obj = Person()

print(type(obj))
