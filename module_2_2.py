first = int(input('1. Введите целое число: '))
second = int(input('2. Введите целое число: '))
third = int(input('3. Введите целое число: '))

if first == second == third:
	print('3 числа равны <3')
elif first == second or first == third or second == third:
	print('2 числа равны <3')
else:
	print('0, все числа не равны (')
