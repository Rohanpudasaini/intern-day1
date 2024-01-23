# 24. Write a Python program to clone or copy a list. 
list1 = [1,2,3,4,5]
list2 = []
list2 = list1
# list2 = [2,3,4,5]
# print(id(list2))
print(id(list1))
# list2 = list1.copy()
print(id(list2))
# print(list2)