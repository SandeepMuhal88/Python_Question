# Q delete a character by its position

# 1. string = immutable ( not change )
name=input("Enter somthing:- ")
position=int(input("Enter Position:-"))
char=name[position-1]
print(name.replace(char,""))