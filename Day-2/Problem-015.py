# Q can a function return multiple values ? if so, how ?


def factoriyal(n):
    if(n==0):
        return 1
        # Base case
    elif(n<0):
        return "Factroiyal is not defined"
    else:
        return factoriyal(n-1)*n
num =int(input("Enter number:-"))
print("Factoriyal usin recursive:- ",factoriyal(num))

