# Q find sum up to n numbers ?
num=int(input("Enter a number:-"))
# x=0
# for i in range(1,num+1):
#     x+=i

# print("Sum of nubers:-",x)
# Using a function
def sum_of_n_No(n):
    x=0
    for i in range(1,n+1):
         x+=i
    return f"Sum of N numbers:-{x}"

print(sum_of_n_No(num))