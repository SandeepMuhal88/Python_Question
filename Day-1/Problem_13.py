# Q tuple with first and last element
element = int(input("Enter number of elements in list :"))
l1 = []
for i in range(element):
    value = int(input("enter value : "))
    l1.append(value)
t1=tuple(l1)
print("The tupls:-",t1)
# Using slicing
# print(t1[0])
# print(t1[-1])
print(t1[0],t1[-1])