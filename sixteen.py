# 16. Write a Python program to sum all the items in a list. 

list1 = [1,2,3,5,6,7,8,9]

def get_sum(list1:list) -> int:
    sum = 0
    for item in list1:
        sum+=item
    return sum

print(get_sum(list1))