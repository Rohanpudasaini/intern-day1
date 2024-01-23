# 10. Write a Python program to remove the characters which have odd index 
# values of a given string. 

string = input("Enter a string: ")
new_string = ""
for index, char in enumerate(string):
    if index %2 == 0:
        new_string = new_string+char
print(new_string)   