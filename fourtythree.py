# 43. Write a Python program to remove an item from a tuple. 
tuple1 = ("Rohan", "Pudasaini","HP")

# tuple2 = list(tuple1)[:-1]
# print(tuple2)

item_to_remove = "Pudaasaini"
new_list = []
for item in list(tuple1):
    if item == item_to_remove:
        continue
    new_list.append(item)

if len(tuple1) == len(new_list):
    print("Nothing is removed")
tuple(new_list)
print(new_list)
