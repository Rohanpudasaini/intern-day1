# 15. Write a Python function to insert a string in the middle of a string. 
# Sample function and result : 
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]] 
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}} 

def insert_string(string1:str, string2:str) -> str:
    mid = int(len(string1)/2)
    return f'{string1[:mid:]}{string2}{string1[mid::]}'

print(insert_string("{{{{}}}}", "rohan"))