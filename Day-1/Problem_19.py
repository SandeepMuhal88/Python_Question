# Q. number of unique combination on two dice
count=0
for i in range(1,7):
    for j in range(i,7):
        print(i,j)
        count+=1
print("Numbers of :-",count)
