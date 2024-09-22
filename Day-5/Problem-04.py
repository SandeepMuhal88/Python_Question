# Q4. working with append mode ?
# concept 1
# append = data write

with open("demo.txt", "a") as file:
    file.write("I am write for useng append method")


# 1. write()
# 2. writelines()

# Writelines()

k1=[
 "There is denote Week name:-\n"
 "Sunday,Monday,Tuesday\n"
 "Wednesday,Thrusday.\n"
 "Filday Saturday!!"
]
with open("demo.txt", "a") as file:
    file.writelines(k1)

# concept 2
# if file does not exist then it will create a new file
#
#
# with open("radha.py", "a") as file:
#     file.write("radha")