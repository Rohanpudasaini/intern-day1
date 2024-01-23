# 31. Write a Python program to iterate over dictionaries using for loops. 

dict1 = {"name": "Rohan",
         "Title": "Intern",
         "laptop": "HP", 
         }

for item, value in dict1.items():
    print(f"Key: {item} have value: {value}")
