my_dict = {
	'John': 2010,
	'Sasha': 1998,
	'Max': 2001,
	'Elena': 1999
}
print(my_dict)

print('-----------------------------------')

print(my_dict.get('Elena'))
print(my_dict.get('Harry'))

print('-----------------------------------')

my_dict.update({
	'Alex': 2008,
	'Vladimir': 1992
	})
print(my_dict)

print('-----------------------------------')

a = my_dict.pop('John')
print(a)
print(my_dict)

print('-----------------------------------')

my_set = {1, 2, 2, 3, 1, 3, 6, 4, 6, 4, 5, 5}
print(my_set)
my_set.add(7)
my_set.add(8)
print(my_set)

print('-----------------------------------')

my_set.discard(2)
print(my_set)