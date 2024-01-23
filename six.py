# 6. Write a Python program to find the first appearance of the substring 'not' and 
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' 
# substring with 'good'. Return the resulting string. 
# Sample String : 'The lyrics is not that poor!' 
# 'The lyrics is poor!' 
# Expected Result : 'The lyrics is good!' 
# 'The lyrics is poor!' 


string = input("Enter a string: ")
if "not" not in string and "poor" not in string:
    print(string)
    exit()
not_index = string.index("not")
poor_index = string.index("poor")

if not_index < poor_index:
    new_string = string[:not_index] + "good" + string[poor_index+4:]
else:
    print(string)
    exit()
print(new_string)
