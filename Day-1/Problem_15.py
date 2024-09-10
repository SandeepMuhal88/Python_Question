# number is divisible by which number
num=int(input("Enter a value:- "))
n=int(num/2)
l1=[]
for i in range(1,n):
    if(n%i==0):
        l1.append(i)
l1.append(n)
l1.append(num)
print("The value you entered Divisol Thease number :-",l1)

