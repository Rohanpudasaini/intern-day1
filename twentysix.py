# 26. Write a Python program to insert a given string at the beginning of all items in 
# a list. 
# Sample list : [1,2,3,4], string : emp 
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

sample_list = [1,2,3,4]
sample_string  = 'test'
new_list = []
for item in sample_list:
    new_string = sample_string + str(item)
    new_list.append(new_string)
print(new_list)
