"""
Q3. Rotate a list to the right by k places, where k is non-negative. 
Example: input:[1,2,3,4,5], k=2 Output:[4,5,1,2,3]
"""


def rotate_list(input_list, k):
    n = len(input_list)
    k = k % n

    return input_list[-k:] + input_list[:-k] # --> [4,5]+[1,2,3] = [4,5,1,2,3]

input_list = [1,2,3,4,5]
k = 2

rotated_list = rotate_list(input_list,k)
print(rotated_list)

"""
[-k:] -> -2 to end range and [:-k] -> 0 to -2 range

k = k % n
If k is larger than the length of the list, the % operator reduces it to a valid range. 
For example, if the list has 5 elements and k is 7, rotating the list 7 times to the right is the 
same as rotating it 2 times (7 % 5 = 2).


In the expression 2 % 5, you're finding the remainder when 2 is divided by 5.

Since 2 is less than 5, 5 cannot go into 2 even once.
Therefore, the remainder is simply 2, because 2 divided by 5 results in 0 with a remainder of 2.
So, 2 % 5 = 2.
"""



