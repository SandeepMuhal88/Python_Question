# check string is a palindrom or not
# Input string
string = input("Enter a string: ")
print(string)
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
