def ask_user():
	while True:
		user_say = input("я вопрос пользователя ")
		get_answer(user_say)
		if user_say == "Пока!":
			break



def get_answer(user_say):
	if user_say == '1':
		print('1')
	elif user_say == '2':
		print(user_say)


ask_user()

