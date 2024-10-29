def textin():
	hideword = input("Введите слово/текст, который требуется зашифровать: ").encode('cp1251')
	binary = ''
	for i in range(len(hideword)):
		binary += str(bin(hideword[i]))
	binary = binary.replace('0b', '')
	return list(binary)

def spacetxt(text):
	count = 0
	for i in text:
		if i == ' ':
			count+=1
	return count

def to32160(text, binary):
	print("Все единицы в бинарной записи шифруемого текста заменяются неразрывным пробелом, все нули - обычным.")
	count = 0
	array32160 = text
	for i in range(len(array32160)):
		if array32160[i] == ' ' and count < len(binary):
			if binary[count] == '1':
				array32160[i] = chr(160)
			count += 1
		if count >= len(binary):
			break
	return array32160

def secondspace(text, binary):
	print("Все единицы в бинарной записи шифруемого текста заменяются двойным пробелом, все нули - одинарным")
	count = 0
	doubledot = text
	for i in range(len(doubledot)):
		if doubledot[i] == ' ':
			if binary[count] == '1':
				doubledot[i] = '  '
			count += 1
		if count >= len(binary):
			break
	print("Полученный текст: ", ''.join(doubledot))

def exchange(text, binary):
	similar = {'a' : 'а', 'e' : 'е', 'y' : 'у', 'o' : 'о', 'p' : 'р', 'x' : 'х', 'c' : 'с', 'E' : 'Е', 'T' : 'Т', 'O' : 'О', 'A' : 'А', 'H' : 'Н', 'K' : 'К', 'X' : 'Х', 'C' : 'С', 'B' : 'В', 'M' : 'М'}
	extext = text
	count, i = 0, 0
	while count < len(binary):
		if extext[i] in similar:
			if binary[count] == "1":
				extext[i] = similar.get(extext[i])
			count += 1
		i += 1
	print("", "".join(extext))

text = list('Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.')
binary = textin()
if spacetxt(text) < len(binary):
	print("В исходном тексте недостаточно пробелов для шифровки!")
else:
	print(binary)
	choice = int(input('''Выберите тип шифра: 
1. Обычные и неразрывные пробелы
2. Одинарные и двойные пробелы
3. Замена букв на такие же в латинице
Ваш выбор:
'''))
	if choice == 1:
		print("Полученный текст: ", ''.join(to32160(text, binary)))
	elif choice == 2:
		secondspace(text, binary)
	elif choice == 3:
		exchange(text, binary)