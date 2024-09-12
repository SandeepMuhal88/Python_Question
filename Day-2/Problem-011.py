# Q find factorial using recursion ?


# concept 1

# recursion = function ke ander function call hoga
def factoriyal(n):
    if(n==0):
        # Base case
        return 1
    elif(n<0):
        return "Factroiyal is not defined"
    else:
        return factoriyal(n-1)*n
num =int(input("Enter number:-"))
print("Factoriyal usin recursive:- ",factoriyal(num))