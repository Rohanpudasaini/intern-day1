# 18. Write a Python program to get the largest number from a list. 

list1 = [1,2,3,51,6,7,8,9]
maxm = 0
for item in list1:
    if item > maxm:
        maxm = item
    
print(maxm)