# 13. Write a Python program that accepts a comma separated sequence of words 
# as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black 
# Expected Result : black, green, red, white,red 

string = input("Enter a comma seperated string: ").split(',')
string.sort()
new_list = []
# print(type(string))
# print(string)
for item in string:
    if item in new_list:
        continue
    new_list.append(item)
print(new_list)

