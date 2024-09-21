# Q25. what is duck typing ?

class M1:
    def info(self):
        print("class M1")


class B:
    def info(self):
        print("class b")


class C:
    def info(self):
        print("class c")


class D:
    def info(self):
        print("class d")


def function(*a):
    for i in a:
        obj = i()
        obj.info()


function(M1, B, C, D)


# duck typing = it is a function which calls same method of different class