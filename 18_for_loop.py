# Access values in a list or tuple using for loop

x = [1,2,3,4,5]

for num in x:
    print(num)

print("\n ------------------------- Access values in a dictionary --------------------------")
# Access values in a dictionary using for loop

x = {'name':'Kamal', 
     'age':40,
     'gender':'male'} 

print("\n ------------------------- Return keys in the dictionary --------------------------")
# Return keys in the dictionary
for i in x.keys():
    print(i)

print("\n ------------------------- Return values in the dictionary --------------------------")
# Return values in the dictionary
for j in x.values():
    print(j)

print("\n ------------------------- Return items in the dictionary --------------------------")
# Return items in the dictionary, both key and value
for k in x.items():
    print(k)

for l,m in x.items():
    print(l,m)

for o in range(4):
    print(o)