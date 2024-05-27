my_dict = {'Alexander': 1999, 'Vasya': 1975, 'Egor': 1986}
print(my_dict)
print(my_dict.get('Alexander'))
print(my_dict.get('Kamila'))
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1980
deleted_value = my_dict.pop('Egor')
print(deleted_value)
print(my_dict)

my_set = {1, 'Яблоко', 42.314, 1, 1}
print(my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.remove(1)
print(my_set)
