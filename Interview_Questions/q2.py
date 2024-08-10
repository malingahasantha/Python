"""
Q2. Given an array, find all the duplicates in this array? 
For example: input: [1,2,3,1,3,6,5] output:[1,3]
"""

import array

arr1 = [1,2,3,1,3,6,5,5,5,8,8]

unique=[]
duplicates=[]

for num in arr1:
    if num not in unique:
        unique.append(num)
    elif num not in duplicates:
        duplicates.append(num)

print(duplicates)   
print(unique)  


print("\n----------------------- method 2 -------------------------------------")


def find_duplicates(input_arr):
    counts={}       #create empty dictionary
    duplicates=[]   #create empty list

    for num in input_arr:   #for loop to check array, num--> is the variable assigning array elements
        if num in counts:
            counts[num] += 1 #if counts[num] is in counts dictionary, it's value increase by 1
        else:
            counts[num] = 1
        #dictionary output --> {1:2, 2:1, 3:2, 6:1, 5:3, 8:2}
    
    for key, value in counts.items():
        if value > 1:
            duplicates.append(key)
    
    return duplicates
    
result = find_duplicates(arr1)
print(result)


