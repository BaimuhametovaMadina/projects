def textinput():
	text = list(input("Введите текст: "))
	for i in text:
		if i.isupper():
			i = i.lower()
		elif i.isspace():
			text.pop(text.index(i))
	return text

def typechoose():
	print("""Выберите действие: 
	1. Зашифровать текст;
	2. Расшифровать текст;
	3. Завершить программу\n""")
	return int(input("Ваш выбор: "))

def check(key, cyr):
	flag = False
	if len(key) != 0:
		for i in key:
			if i not in cyr:
				flag = True
				break
	if flag == True or len(key) == 0:
		return False
	else:
		return True

def maincrypt(text, type):
	cyrillic = list("абвгдежзийклмнопрстуфхцчшщъыьэюя")
	key = list(input("Введите ключ шифра: "))
	checkflag = check(key, cyrillic)
	while checkflag == False:
		if len(key) == 0:
			while len(key) == 0:
				print("Ваш ключ пуст.")
				key = list(input("Введите ключ шифра: "))
		else:
			print("Ключ состоит не только из русских букв.")
			key = list(input("Введите ключ шифра: "))
		checkflag = check(key, cyrillic)
	keylen = len(key)
	for i in range(len(text)):
		key.append(key[i % keylen])
	
	if type == 1:
		encrypt(text, key, cyrillic)
	elif type == 2:
		decrypt(text, key, cyrillic)

def encrypt(text, key, cyrillic):
	newtext = []
	for i in range(len(text)):
		index = (cyrillic.index(text[i]) + cyrillic.index(key[i])) % 33
		newtext.append(cyrillic[index])
	print("Зашифрованный текст: ", ''.join(newtext))

def decrypt(text, key, cyrillic):
	newtext = []
	for i in range(len(text)):
		index = (cyrillic.index(text[i]) + 33 - cyrillic.index(key[i])) % 33
		newtext.append(cyrillic[index])
	print("Зашифрованный текст: ", ''.join(newtext))
	
string = textinput()
choice = typechoose()
while choice != 3:
	if choice == 1:
		maincrypt(string, 1)
	elif choice == 2:
		maincrypt(string, 2)
	else:
		print("Произошла ошибка! Такого действия нет. Попробуйте заново.\n")
	textinputflag = input("Хотите сменить текст? (y/n)\n")
	while textinputflag != 'y' and textinputflag != 'n':
		print("Вы ввели неверное действие. Попробуйте заново.\n")
		textinputflag = input("Хотите сменить текст? (y/n)\n")
	if textinputflag == 'y':
		string = textinput()
	typechooseflag = input("Хотите сменить действие с текстом? (y/n)\n")
	while typechooseflag != 'y' and typechooseflag != 'n':
		print("Вы ввели неверное действие. Попробуйте заново.\n")
		typechooseflag = input("Хотите сменить текст? (y/n)\n")
	if typechooseflag == 'y':
		choice = typechoose()
print("Программа завершена. Хорошего дня!")