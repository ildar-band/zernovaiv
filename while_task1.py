Name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

def find_person(name):
	while True:
		if Name_list.pop() == name:
			print(name, " нашелся")
			break
				


find_person('Вася')