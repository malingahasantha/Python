"""
Q6. Write a program to left rotation of a list?
input:
N = 2
L = [100,200,300,400,500]

output : [300,400,500,100,200]
"""

input_list  = [100,200,300,400,500]
rotate_number = 2

def left_rotate(il,rn):
    n = len(il)
    rn = rn % n

    output_list = il[rn:] + il[:rn]
    return output_list

rotated_list = left_rotate(input_list,rotate_number)
print(rotated_list)