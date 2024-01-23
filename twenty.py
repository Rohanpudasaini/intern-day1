# 20. Write a Python program to count the number of strings where the string 
# length is 2 or more and the first and last character are same from a given list of 
# strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221'] 
# Expected Result : 2 
list1 = ['abc', 'xyz', 'aba', '1221', "121", "asdsa"]
same = 0
for item in list1:
    if str(item)[0] == str(item)[-1]:
        same +=1
print(same)