Name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']


while True:
	name = Name_list.pop()
	print(name)
	if name != 'Валера':
		pass
	else:
		print(name, " нашелся")
		break
	
