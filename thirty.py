# 30. Write a Python script to check whether a given key already exists in a dictionary. 
dict1 = {"name": "Rohan",
         "Title": "Intern",
         "laptop": "HP", 
         }

def check_exsist(dict1:dict, key) -> bool:
    if key in dict1.keys():
        return True
    else:
        return False
    
print(check_exsist(dict1, "laptop1"))
