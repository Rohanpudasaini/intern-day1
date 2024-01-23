# 4. Write a Python program to get a single string from two given strings, separated 
# by a space and swap the first two characters of each string. 
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz' 


string = input("Enter two strings (seperated by comma as abc,def):  ").split(",")
# print(string)
# result = string[1][:2]+ string[0][2:] + " " + string[0][:2] + string[1][2:]
print(f"{string[1][:2]}{string[0][2:]} {string[0][:2]}{string[1][2:]}")
