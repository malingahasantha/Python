""" 
Q1. Given two arrays, write a python function to return the intersection of the two? 
For example, x = [1,5,9,0] and y = [3,0,2,9] it should return [0,9]
"""
import array

def intersect_arr(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    sets = set1.intersection(set2)
    return sets

x = array.array('I',[1,5,9,0])
y = array.array('I',[3,0,2,9])

intersect = intersect_arr(x,y)
print(intersect)



