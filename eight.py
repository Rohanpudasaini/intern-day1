# 8. Write a Python program to remove the nth index character from a nonempty string. 
string = input("Enter a non empty string: ")
try:
    index = int(input("Enter the index that you want to remove, i.e 1 for first and 2 for second: "))
except ValueError:
    print("Cant convert to int")
    exit()
print(f"{string[:index]}{string[index+1:]}")