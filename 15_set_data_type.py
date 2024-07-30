#set data type is un ordered data type, so we cannot use indexing here. data is not in an order in a set. We cannot keep duplicate values in set data type. we can only keep unique values.
# we can add multiple data types in set data type as well.

my_list = ['Kamal', 24, True, 'Kandy', 76.5, 24]
my_tuple = ('Kamal', 24, True, 'Kandy', 76.5, 24)
my_set = {'Kamal', 24, True, 'Kandy', 76.5, 24}

print(my_set)
print(type(my_set))
#duplicate value will ignore and retun output not in order

print("\n---------------------add() method------------------------------")
#add values
my_set.add(546)
print(my_set)

#in here below data will add as a tuple
my_set.add(('saman','sunil'))
print(my_set)

print("\n-------------------------update() method-------------------------")
#if we need to add multiple values to a set we can use update() method. we can add as a tuple or as a list as well.
my_set.update(('675', False))
print(my_set)
my_set.update(['Ratnapura', 678.45])
print(my_set)

print("\n---------------------remove() method---------------------------")
#remove values
my_set.remove('Kamal')
print(my_set)

#discard() method
my_set.discard('Ratnapura')
print(my_set)

#-------------------------------------------------------------------#
print("\n----------------------union, intersection and difference-------------------------")

A = {1,2,3,5,7}
B = {5,7,9,10,11}

print(A.union(B))
print(B.union(A))
print(A.intersection(B))
print(B.intersection(A))
print(A.difference(B))
print(B.difference(A))