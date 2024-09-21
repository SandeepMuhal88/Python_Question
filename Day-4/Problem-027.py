# Q27. how to create attributes as (public, protected, private)?
# Public
class Demo:
    def __init__(self,name,location):
        self.__name=name
        self._location=location
        print(f"Name:-{self.__name}")
        print(f"Location:-{self._location}")

    def info(self):
        print("I am from Demo class and public function:))")

obj=Demo("Sandeep","Ajmer")
obj.info()
