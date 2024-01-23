# 41. Write a Python program to convert a tuple to a string. 
tuple1 = ("Rohan", "Pudasaini","HP")
# tuple1 = str(tuple1)
# print(type(tuple1))
string = ""
for item in tuple1:
    string  = string + item + " "
print(string)