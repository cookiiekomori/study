immutable_var = (1, 2, 3, True, 'name', [4, 5])
print(type(immutable_var)) 
print(immutable_var)
# immutable_var[0] = 3 
# Элементы кортежа неизменяемы, так как в некоторых ситуациях это необходимо, это для уверенности, что какой-то элемент может случайно смениться
mutable_list = [1, 2, 3, True, 'name']
print(type(mutable_list)) 
print(mutable_list)
mutable_list[4] = 'John'
print(mutable_list)