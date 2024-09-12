# Q Write a function to print table of a given number
# def table(*num):
#     for j in num:   
#       for i in range(1,11):
#         print(f"{j}x{i}={j*i}")

# n=int(input("Enter a number:-"))
# m=int(input("Enter a number:-"))
# k=int(input("Enter a number:-"))
def table(num):
      for i in range(1,11):
        print(f"{num}x{i}={num*i}")

n=int(input("Enter a number:-"))
table(n)