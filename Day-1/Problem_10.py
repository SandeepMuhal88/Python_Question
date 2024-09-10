# Q how to reverse a list
element=int(input("Enter a lenth of list:- "))
l1=[]
for i in range(element):
    value=input("Enter value:- ")
    l1.append(value)
print(l1)
print("Reverse List :))-",l1[::-1])