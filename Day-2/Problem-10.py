# Q find factorial of a number without recursion ?
# 0!=1
def factoriyal(num):
    fact=1
    if(num<0):
        print(f"{num} Not defined")
    elif(num==0):
        print(f"factoriyal is :-{num}")
    else:
        while(num!=0):
            fact*=num
            num-=1
        print(f"Factoriyal:- {fact}")

factoriyal(6)

