# Q write a function to check (number is prime or not)
def checkprime(num):
    if(num<=2):
        print(f"{num}  is not prime: ")
    elif(num>2):
        for i in range(2,num):
            if(num%i==0):
                 print(f"{num} is not a prime number because is divided by {i}")
                 break
            else:
                 print(f"{num}  is prime: ")
                 break
    else:
        print("Invaild input")


number=int(input("Enter a number:-"))
checkprime(number)