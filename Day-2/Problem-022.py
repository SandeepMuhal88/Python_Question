# how to access element from nested dictionary
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
print(dict["Eduction"]["Borad"])
print(dict["Eduction"]["Branch"])