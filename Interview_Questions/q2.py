"""
Q2. Given an array, find all the duplicates in this array? 
For example: input: [1,2,3,1,3,6,5] output:[1,3]
"""

import array

arr1 = [1,2,3,1,3,6,5,5,5]

unique=[]
duplicates=[]

for num in arr1:
    if num not in unique:
        unique.append(num)
    elif num not in duplicates:
        duplicates.append(num)

print(duplicates)   
print(unique)  