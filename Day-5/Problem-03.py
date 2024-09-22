# Q3. working with write mode ?

# write mode

# concept 1
# if file open with write mode
# 1. file alrady exist = data will be override
 
# with open("demo.txt",'w') as d:
#     # print(d.write())
#     pass


# concept -2
# If file open with write mode then file will be created
# with open("day.txt",'w') as file:
#   pass


#  Write data into file that will start 
# with open("day.txt",'w') as file:
#     file.write("Sunday is good day\nMonday is very beatuful day\nTuesday is fast day for me")


# There are manyTypes
# write()
# writelines()

# Using write method to wirtten data into file
with open("xyz.txt",'w') as F:
    F.write("My Name Sandeep Muhal.\n")
    F.write("I am from Ajmer Rajsathan.\n")
    F.write("I am a software Engineering.")
    F.write("Current time i am studying at bikaner.")

# There before data exit in day.txt then we will run that then data is override 
# with open("day.txt",'w') as F:
#     F.write("My Name Sandeep Muhal.\n")
#     F.write("I am from Ajmer Rajsathan.\n")
#     F.write("I am a software Engineering.")
#     F.write("Current time i am studying at bikaner.")



k1=[
 "There is denote Week name:-\n"
 "Sunday,Monday,Tuesday\n"
 "Wednesday,Thrusday.\n"
 "Filday Saturday!!"
]
# writelines()
with open("temp.txt",'w') as F:
    F.writelines(k1)


# with open("jp.py", "w") as f:
#     f.write("this is some random data \n")
#     f.write("this is some random data \n")
#     f.write("this is some random data \n")
#     f.write("this is some random data \n")
#     f.write("this is some random data \n")


# l1 = [
#     "this is first line \n",
#     "this is first line \n",
#     "this is first line \n",
#     "this is first line \n",
# ]

# with open("jp.py", "w") as file:
#     file.writelines(l1)