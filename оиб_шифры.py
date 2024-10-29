from time import sleep
from math import gcd


# text input func
def textinput(x):
	if x == 1:
		sleep(0.2)
		address = input("Введите адрес файла в формате C:\...\filename.txt: ")
		file = open(address, 'r', encoding='UTF-8')
		text = list(file.read().lower())
		file.close()
	elif x == 2:
		sleep(0.2)
		text = list(input("Введите или вставьте из буфера обмена текст, который необходимо обработать: ").lower())
	return text



# main atbash func
def atbash(y):
	sleep(0.2)
	if y == 1 or y == 2:
		cryptext = []
		for i in range(len(text)):
			if text[i] in rusal:
				cryptext.append(rusal[32 - rusal.index(text[i])])
			elif text[i] in latal:
				cryptext.append(latal[25 - latal.index(text[i])])
			else:
				cryptext.append(text[i])
		return ("Полученный текст:\n" + ''.join(cryptext))
	else:
		return "Такого действия нет. Выберите другое..."
	sleep(0.5)



# main caesar func
def caesar(y):
	sleep(0.2)
	if y == 1:
		b = int(input("Введите сдвиг: "))
		return affcaecrypt(1, b)
	elif y == 2:
		absurd = 0
		while absurd != 1:
			b = (int(input("Введите сдвиг (если не известен, введите случайный): ")))
			return affcaecrypt(1, -b)
			absurd = int(input("Расшифрованный текст имеет смысл?\n1. Да\n2. Нет"))
	else:
		return "Такого действия нет. Выберите другое..."
	sleep(0.5)



# main aff func
def aff(y):
	sleep(0.2)
	if y == 1:
		a, b = map(int, input("Введите числа а и b, являющиеся ключом шифра: ").split())
		if gcd(a, 26) == 1 and gcd(33, a) == 1:
			print(affcaecrypt(a, b))
		else:
			while gcd(a, 26) != 1 and gcd(33, a) != 1:
				if gcd(a, 26) != 1:
					print("Число а и длина латинского алфавита не являются взаимно простыми!")
					a = int(input("Введите новое число а: "))
				elif gcd(a, 33) != 1:
					print("Число а и длина русского алфавита не являются взаимно простыми!")
					a = int(input("Введите новое число а: "))
			print(affcaecrypt(a, b))

	if y == 2:
		key = int(input("Вам известен ключ расшифровки?\n1. Да\n2. Нет\n"))
		if key == 1:
			a = 1
			x, b = map(int, input("Введите числа а и b, являющиеся ключом шифра: "))
			if gcd(x, 26) == 1 and gcd(33, x) == 1:
				while (a * x) % 26 != 1 and (a * x) % 33 != 1:
					a += 1
				b = -b * a
				print(affcaecrypt(a, b))
			else:
				while gcd(a, 26) != 1 and gcd(33, a) != 1:
					if gcd(a, 26) != 1:
						print("Число а и длина латинского алфавита не являются взаимно простыми!")
						a = int(input("Введите новое число а: "))
					elif gcd(a, 33) != 1:
						print("Число а и длина русского алфавита не являются взаимно простыми!")
						a = int(input("Введите новое число а: "))
				print(affcaecrypt(a, b))

		else:
			print("Данная программа может только посчитать, \nсколько раз конкретная буква встречается в тексте, \nи вывести это значение на экран. \nЗаменять значения вам придется самостоятельно.")
			freqchoice = int(input("Вы согласны?\n1. Да\n2. Нет\n"))
			if freqchoice==1:
				print(frequen())
			else:
				print("Выберите следующее действие...")

# inner aff func & inner caesar func
def affcaecrypt(a, b):
	cryptext = []
	for i in range(len(text)):
		if text[i] in rusal: # russian
			cryptext.append(rusal[(a * rusal.index(text[i]) + b) % 33])
		elif text[i] in latal: # english
			cryptext.append(latal[(a * latal.index(text[i]) + b) % 26])
		else:
			cryptext.append(text[i])
	return ("Полученный текст:\n" + ''.join(cryptext))

# frequency analysis
def frequen():
	pukpuk = []
	for i in range(len(text)):
		if text[i] not in pukpuk and (text[i] in rusal or text[i] in latal):
			c = text.count(text[i])
			pukpuk.append(text[i])
			print("Буква {} встречается в тексте {} раз".format(text[i], c))


#alphabets
rusal = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
latal = list("abcdefghijklmnopqrstuvwxyz")


# text input
tinchoice = int(input("Выберите способ считывания текста:\n1. Из файла\n2. Из буфера обмена или с клавиатуры\n"))
text = textinput(tinchoice)
print(text)


# choose cipher
sleep(0.5)
print("Выберите шифр: ")
cipherchoice = int(input("1. Атбаш\n2. Шифр Цезаря\n3. Аффинный шифр\n4. Завершить программу\n"))


choice = 0
# main func
while cipherchoice != 4:
	# choose operation
	sleep(0.5)
	print("Выберите действие с текстом: ")
	choice = int(input("1. Зашифровать\n2. Расшифровать\n3. Завершить программу\n"))
	if choice == 3:
		break

	if cipherchoice == 1: # atbash
		print(atbash(choice))
	elif cipherchoice == 2: # caesar
		print(caesar(choice))
	elif cipherchoice == 3: # aff
		print(aff(choice))
	else:
		print("Ошибка! Такого шифра нет в базе. Попробуйте другой.")

	# check for new text
	sleep(0.5)
	nulling = int(input("Хотите ввести новый текст?\n1. Да\n2. Нет\n"))
	if nulling == 1:
		sleep(0.2)
		tinchoice = int(input("Выберите способ считывания текста:\n1. Из файла\n2. Из буфера обмена или с клавиатуры\n"))
		text = textinput(tinchoice)

	# choose cipher
	sleep(0.5)
	print("Выберите следующий шифр: ")
	cipherchoice = int(input("1. Атбаш\n2. Шифр Цезаря\n3. Аффинный шифр\n4. Завершить программу\n"))
print("Программа завершена. Хорошего дня!")