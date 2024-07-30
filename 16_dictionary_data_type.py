#in ditionary one element define as pair of key and value.

my_dict = {'name':'Malinga', 'age':25, 'city':'Ratnapura'}
students = {80:'kamal', 81:'saman', 82:'sunil'}

print(my_dict)
print(type(my_dict))

print("\n ------------------------------ access values -------------------------------")
#access vales using the key
print(my_dict['age'])
print(my_dict.get('name'))

my_dict['name'] = 'Hasantha'
print(my_dict)

print("\n ------------------------------ add values -------------------------------")
#add data
my_dict['is married'] = False
print(my_dict)

#add multiple values
my_dict.update({'gender':'male', 'job':'Computer Engineer'})
print(my_dict)

print("\n ------------------------------ remove values -------------------------------")
#remove values
del my_dict['age']
my_dict.pop('name')
print(my_dict)

print(my_dict.pop('city'))

print("\n ------------------------------ clear dictionary -------------------------------")
#clear whole dictionary
my_dict.clear()
print(my_dict)
