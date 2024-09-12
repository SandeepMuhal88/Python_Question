name="Sandeep Muhal"
Age=20
Adress="Karani nagar"

def factoriyal(n):
    if(n==0):
        # Base case
        return 1
    elif(n<0):
        return "Factroiyal is not defined"
    else:
        return factoriyal(n-1)*n
    
def add(a, b):
    return a + b


def subtract_two_numbers(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "undefined"
    else:
        return a / b