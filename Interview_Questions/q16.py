"""
Q16. Given list is : [1,2,3,4,5,6,7,8,9]
The output should be: [2,4,6,8]

Example: "How are you" --> 3

Use:
1. List Comprehension
2. f.string
"""

numbers = [10,11,12,13,14,15,16,17,18,19]

filtered_list = [num for num in numbers if num % 2 == 0]

print(f"Filtered list is ", filtered_list)

### new_list = [new_item for item in list] ###

# new_item - the item with the calculation on it
# item - tme (can be anything)
# list - the list

"""
Double the given list.
list is : [1,2,3,4]
The output should be: [2,4,6,8]

Use:
1. List Comprehension
3. f.string
"""

number_list = [1,2,3,4,5]

doubled_list = [num*2 for num in number_list]

print(f'Doubled list is: ', doubled_list)