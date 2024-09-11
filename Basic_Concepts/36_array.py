#in python array does not come as default. we should import array. we are importing array package.

import array

x = array.array('I',[2,3,4,5,6])
y = array.array('i',[2,-3,4,5,6])
#we can store both + and - values, if we use capital I we only can store + values.

print(x)
print(y)

print(x[2])
print(y[1:3])

print("\n")
x.append(9)
print(x)
#append can only add one value.

x.extend([9,10,88])
print(x)
#extend can add more than one value.

x.insert(2,75)
print(x)
#insert can add a value to any position we want.

print("\n")
#join array. to join both arrays should be in one form.
o = array.array('i',[2,3,4,5,6])
p = array.array('i',[7,8,9,10,11])

z = o+p
print(z)