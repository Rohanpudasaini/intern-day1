# 27. Write a Python program to replace the last element in a list with another list. 
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8] 
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

list1 = [1,2,3,4,5,25]
list2 = [3,5,7,8]
list1.pop(-1)
print(list1 + list2)
