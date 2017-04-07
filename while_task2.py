def ask_user():
	while True:
		print('Как дела?')
		user_say = input("Ваш ответ: ")
		if user_say == "Хорошо":
			break


ask_user()