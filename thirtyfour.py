# 34. Write a Python script to merge two Python dictionaries. 
dict1 = {"Name": "Rohan",
        "Surname": "Pudasaini",
        "Laptop": "HP",
         }

dict2 = {
    "Favourite_drink": "Tea",
    "Mobile": "Samsung",
}

dict1.update(dict2)
print(f"The merged dict is: {dict1}")