# 38. Write a Python program to remove a key from a dictionary. 
dict1 = {x:x*x for x in range(1,4)}
# {1: 1, 2: 4, 3: 9}
dict1.pop(1)
print(dict1)