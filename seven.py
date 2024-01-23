# 7. Write a Python function that takes a list of words and returns the length of the 
# longest one. 

def getMaxLength(words:list) -> int:
    max = 0
    for word in words:
        if len(word) > max:
            max = len(word)
    
    return max
    
words = ["hello", "hi", "hello2", "testing", "123456789000000000"]
print(getMaxLength(words))