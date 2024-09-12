# how to delete element in dictionary
# del=that is key word in python language
dict={
    "Name":"Sandeep Muhal",
    "Age" : 19,
    "Mobile No.":7878446678,
    "Address": "Ajmer",
    "Eduction" :{
        "Borad":"RBSE",
        "Collage":"BTU",
        "Branch":"CSE"
    }

}
del dict["Mobile No."]
print(dict)