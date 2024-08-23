"""
Q21. Binary Search

Criteria:
1. Find the mid value
2. If your value is equal to mid value return it
3. If your value is higher than mid value, change the lower value
4. If your value is lower than mid value, change the upper value

Use:
1. Functions
2. User Input
3. f.string
"""

pos = -1

def binary_search(list, n):
    lower = 0
    upper = len(list)-1 

    while lower <= upper:
        mid  = (lower + upper) // 2

        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        elif list[mid] < n:
                lower = mid + 1
        else:
                upper = mid - 1

    return False


list = [4,7,8,12,45,99]
n = int(input('Please enter a value: '))

if binary_search(list,n):
    print(f"Found at: {pos + 1}")
else:
    print("Not Found")