# 35. Write a Python program to iterate over dictionaries using for loops. 

dict1 = {"Name": "Rohan",
        "Surname": "Pudasaini",
        "Laptop": "HP",
         }
for item, value in dict1.items():
    print(f"Key: {item} have value: {value}")