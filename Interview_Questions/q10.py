"""
Q9. Draw Pyramid using python.
"""

print('   *')
print('  ***')
print(' *****')
print('*******')


row_count = 10

for item in range(1, row_count+1):
    print(' '*(row_count-1), end='')
    print('*'*((2*item)-1))
    row_count = row_count - 1