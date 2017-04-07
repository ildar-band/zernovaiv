def ask_user():
	try:
		while True:
			print('Как дела?')
			user_say = input("Ваш ответ: ")
			if user_say == "Хорошо":
				break
	except KeyboardInterrupt:
		print("ПОка")

ask_user()