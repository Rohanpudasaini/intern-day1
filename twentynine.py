# 29. Write a Python script to concatenate following dictionaries to create a new 
# one. 
# Sample Dictionary : 
# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60} 
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
# new_dict = {}
# def merge(dic1:dict, dic2:dict) -> dict:
#     for key, value in 


dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={4:40,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)