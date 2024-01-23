# 19. Write a Python program to get the smallest number from a list. 

list1 = [1,2,3,-51,6,7,8,9]
minim = 1000000
for item in list1:
    if item < minim:
        minim = item
    
print(minim)