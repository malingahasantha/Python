#two methods of creating a list. below you can see both lst1 and lst2 are identified as lists.
lst1 = []
lst2 = list()

print(type(lst1))
print(type(lst2))


# ---------------------------------------------- #

lst3 = [20, 30, 10, 60]
lst4 = list((34, 56,98, 108))

print(lst3)
print(lst4)


# Access elements in a list using index values

my_list = ['Kamal', 20, False, 'kandy', 23.5]
#in a list we can store several data types in one list.

print(my_list[0])
print(my_list[-4])
print(my_list[1])
print(my_list[-2])

print(my_list)
print(my_list[:])
print(my_list[1:])
print(my_list[1:4])


#store a list in a list and we can return that list using index. The list in the list is identify as a one index.
my_list1 = ['Kamal', 20, False, 'kandy', 23.5, [4,5,6]]

print(my_list1[5])

#return a value in the list inside list. Two dimentional list.
print(my_list1[5][1])

print("-----------------change values in a list in runtime-----------------")
#change values in a list in runtime
print(my_list1)

my_list1[3] = 'colombo'

print(my_list1)


print("-----------------add new elements to a list-----------------")

#append() method - with this method we can add only one value
my_list1.append("Saman")

print(my_list1)

#extend() method
my_list1.extend(["Sunil", 43, 55.6])
print(my_list1)

#insert() method - with this method we can add value to any place in the list. We just have to mention the index value and the value we are going to add.
my_list1.insert(0, 'hello')
print(my_list1)

my_list1.insert(2, 'world')
print(my_list1)

print("-----------------\nremove new elements to a list-----------------")

#pop() method
my_list1.pop(2)
print(my_list1)

#remove() method - here we should provide value instead of the index value.
my_list1.remove(55.6)
print(my_list1)

#clear() with this method we can clear whole list.
my_list1.clear()
print(my_list1)