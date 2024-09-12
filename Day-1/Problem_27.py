# Q find maximum from three numbers. ?
a=int(input("Enter first number:-"))
b=int(input("Enter second number:-"))
c=int(input("Enter third number:-"))
if(a>b and a>c):
    print(f"{a} is greatest")
elif(b>c):
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")