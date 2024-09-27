my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

m_list = 0
while m_list < len(my_list):
	a = int(my_list[m_list])
	if a > 0:
		print(a)
	elif a == 0:
		pass
	else:
		break
	m_list += 1