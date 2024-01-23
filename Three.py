# 3. Write a Python program to get a string from a given string where all 
# occurrences of its first char have been changed to '$', except the first char itself. 
# Sample String : 'restart' 
# Expected Result : 'resta$t' 



string = input("Enter a string: ")
# string = (string.lower()).strip()
lead = string[0].lower()
new_string =''
for num, chr in enumerate(string):
    test_chr = chr.lower()
    if num == 0:
        new_string = new_string + chr
        continue
    if test_chr == lead:
        # print("true")
        new_string = new_string + "$"
        continue
    new_string = new_string + chr
    # new_string = new_string + chr
    
print(new_string)
