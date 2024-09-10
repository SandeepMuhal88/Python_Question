# Q insert element at particuler index (without insert method)
element = int(input("Enter number of elements in list :"))
l1 = []
for i in range(element):
    value = int(input("enter value : "))
    l1.append(value)

l2 = l1.copy()

ins = int(input("enter a index :"))
value = input("enter a value :")
l1[ins] = value

print(l1)

for i in range(ins + 1, len(l1) + 1):
    l1[i] = l2[i - 1]

print(l1)