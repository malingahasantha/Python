"""
Q20. Linear Search

Criteria:

Use:
1. Functions
2. User Input
3. f.string
"""
pos = -1

def linear_search(list,n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1
    return False

list = [4,7,8,9,12,45,99]
n = int(input('Please enter a value: '))

if linear_search(list,n):
    print(f'Found at: {pos}')
else:
    print("Not Found")