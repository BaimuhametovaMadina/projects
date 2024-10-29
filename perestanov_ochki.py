import random

def horizontal(string):
	for i in range(0, len(text)):
        temp_text += text[i]
        if i % len(key) == 0:
            temp_text += " "

    a = list(temp_text.split())

    for i in range(len(text) // (len(key))):
        matrix.append(list(a[i]))

    key_matrix = list(key)

    for i in range(len(text) // len(key)):
        temp = ''.join(matrix[i])
        for j in range(len(key)):
            matrix[i][j] = temp[int(key[j]) - 1]

    print("Зашифрованный текст: ")
    for i in range(len(matrix)):
        print(*matrix[i], end = '', sep = '')

def textinput():
	helpstring = list(input("Введите текст:\n"))
	string = []
	for i in range(len(helpstring)):
		if helpstring[i].isalpha(): string.append(helpstring[i])
	helpstring = []
	print(string)
	return string

def choose():
	print("""Выберите тип перестановки:
	1. Горизонтальная (зашифровка);
	2. Вертикальная (зашифровка);
	3. Горизонтальная (расшифровка);
	4. Вертикальная (расшифровка);
	5. Завершить программу.
	""")
	return int(input("Ваш выбор: "))

string = textinput()
choice = choose()
while choice != 3:
	if choice == 1 or choice == 3:
		horizontal(string)
	elif choice == 2 or choice == 4:
		vertical(string)
	elif choice > 5:
		print("Такого действия нет! Попробуйте заново.")
	textchangeflag = input("Хотите сменить текст? (y/n)")
	if textchangeflag == 'y':
		string = textinput()
	cipherchangeflag = input("Хотите сменить тип перестановки или выйти из программы? (y/n/exit)")
	if cipherchangeflag == 'y':
		choice = choose()
	elif cipherchangeflag == 'exit':
		break
print("Программа завершена. Хорошего дня!")
