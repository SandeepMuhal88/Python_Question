# Q finding factorial of a number
# 0!=1
#1!=1
# -1!=undefined
n=int(input("Enter a number:- "))
fact =1
# if(n==0):
#     print(f"{n} factoriyal is 1")
# elif(n<0):
#     print(f"{n} factoriyal is not defined_)))")
# else:
#     for i in range(1,n+1):
#          fact*=i
#    print(fact)
#  print(fact)

for i in range(1,n+1):
    fact*=i
print(fact)
    