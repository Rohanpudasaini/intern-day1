# 32. Write a Python script to generate and print a dictionary that contains a 
# number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) : 
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

num = int(input("Enter the number:"))
dict1 = {x: x*x for x in range(1,num+1)}
print(dict1)