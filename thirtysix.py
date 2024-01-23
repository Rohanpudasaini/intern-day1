dict1 = {x:x*x for x in range(1,5)}
# {1: 1, 2: 4, 3: 9, 4: 16}
total_sum = 0
for item in dict1.values():
    total_sum +=item
print(total_sum)