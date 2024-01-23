dict1 = {x:x*x for x in range(1,4)}
# {1: 1, 2: 4, 3: 9}
mul = 1
for item in dict1.values():
    mul *=item
print(mul)