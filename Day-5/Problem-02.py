# Q2. working with read mode ?


# Method -01
# defulat Mode(Read mode)
# file=open("demo.txt")
# for i in file:
#     print(i)


# print("That task read method")
# with open("demo.txt") as dirc:
#     print(dirc.read(26))

# 1. read(indexing) = it will give data(Start 1)
# 2. readline() = it will give only first line
# 3. readlines() = it will also give data and convert into in list

# print("That task readline method")
# with open("demo.txt") as dirc:
#     print(dirc.readline(25))

# print("That task readlines method")
# with open("demo.txt") as dirc:
#     print(dirc.readlines(2))

# with open("demo.txt") as file:
#     a = file.readlines()
#     for i in a:
#         print(i, end="")




# if we give indexing in readline it will print line
# with open("jp.txt") as file:
#     print(file.readlines(18))



try:
    with open("day.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not Found!!!")

try:
    with open("demo.txt") as a:
        print(a.read())
except FileNotFoundError:
    print("Error:\nFile not found!!")

try:
    with open("day.txt") as file:
        print(file.read())
except:
    print("File not Found!!!")

try:
    with open("day.txt") as file:
        print(file.read())
except Exception as e:
    print(f"Error:-{e}")