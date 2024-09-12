# Q Is enterd number is a prime numebr ?
# Eg:- 1,2,3,5,7,11,13,17,19,23
num=int(input("Enter a number:-"))
if(num<=2):
    print(f"{num} Number is prime))")
elif(num>2):
    for i in range(2,num):
        if(num%i==0):
            print(f"{num} is not prime because number is divided by {i}")
            break
        else:
            print(f"{num} is prime)))")
            break
else:
    print("Invalid input:::::")
