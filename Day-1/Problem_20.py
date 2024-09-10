# give even number up to n
n=int(input("Enter a number:-"))
for i in range(n):
    if(i%2==0):
        print(i)
if(i%2!=0):
    print()