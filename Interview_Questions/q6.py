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


print("\n------------------------- 2nd method -------------------------")

def left_rotation(l,n):
    for i in range(n):      # range n means 0:1 --> 0 to 1
        t = l[0]            # t = 100
        for j in range(len(l)-1):  # 0,1,2,3 --> 0:4 0 to 4
            l[j] = l[j+1]   # l[0] = l[1], l[1] = l[2], l[2] = l[3], l[3] = l[4]
            l[len(l)-1] = t # l[4] = 100 --> 200 --> in 2nd rotation t becoms 200
    return l

rotated_left = left_rotation(input_list,rotate_number)
print(rotated_left)