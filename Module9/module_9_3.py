first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i[0]) - len(i[1]) for i in zip (first, second) if not len(i[0]) == len(i[1]))
print(list(first_result))

second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))
print (list(second_result))