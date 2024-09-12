# Q how to access key and values from a dictionary using for loop
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
for keys,values in dict.items():
    print(f"{keys}:{values}")