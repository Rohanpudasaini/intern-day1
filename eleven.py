# 11. Write a Python program to count the occurrences of each word in a given 
# sentence. 

string = input("Enter a sentence: ").split(" ")
lists = {}
for word in string:
    if word not in lists:
        lists[word] = 1
    else:
        lists[word] +=1
print(lists)
