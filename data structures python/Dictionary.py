# Properties of Dictionary
# 1. Duplicate keys are not allowed 

dict1 = {'Name': 'Ram', 'RollNumber': 4, 3: [1, 2, 3]}

# Printing dictionary
print(dict1)

# Accessing value corresponding to a key
print(dict1['Name'])
print(dict1[3])  
print(dict1.get('RollNumber'))

# Printing length of dictionary
print(len(dict1))

# Printing all the keys of dictionary 
print(dict1.keys())

# Printing all the values 
print(dict1.values())

# Adding a key in dictionary 
dict1['a'] = 1

# Deleting a key in python 
dict1.pop('RollNumber')
print(dict1)

# Iterating on dictionary 
for key in dict1:
    print(key, dict1[key])
