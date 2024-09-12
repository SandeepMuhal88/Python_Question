# find minimum from three numbers
a=int(input("Enter first number:-"))
b=int(input("Enter second number:-"))
c=int(input("Enter third number:-"))
if(a<b and a<c):
    print(f"{a} is minimum")
elif(b<c):
    print(f"{b} is minimum")
else:
    print(f"{c} is minimum")