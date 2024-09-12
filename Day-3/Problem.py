# 1. name = "yourName"

# 2. function => "python"
# 3. function => odd / even
# 4. function => table print
# Table printing
name="Sandeep Muhal"

def table(num):
      for i in range(1,11):
        print(f"{num}x{i}={num*i}")

# Even odd
def evenodd(n):
    if(n%2==0):
        print(f"{n} is even !!")
    else:
        print(f"{n} odd number!!")
print(evenodd(52))
