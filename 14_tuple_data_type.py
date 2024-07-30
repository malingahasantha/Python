my_tuple = ('Kamal', 25, 'Ratnapura', True, 48.9)
#only different in tuple from list is tuple is a immutable data type. we cannot change tuple in runtime.

tpl1 = ()
tpl2 = tuple()

print(type(tpl1))
print(type(tpl2))

tpl3 = (23, 54, 75, 87, 34, 'Kamal', 54, 54)
tpl4 = tuple((23, 54, 75, 87, 34, 'Kamal'))

print(tpl3)
print(tpl4)

print(tpl3[2])
print(tpl4[-1])

print(tpl4[1:])
print(tpl4[1:4])

print(tpl3.count(54))


print("----------------------\nConvert list into tuple--------------------------")
lst6 = (23, 54, 75, 87, 34, 'Kamal', 52.3, 'Kumara')
print(type(lst6))

tpl = tuple(lst6)
print(type(lst6))