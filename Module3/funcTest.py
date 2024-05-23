def print_params(a=1, b='строка', c=True):
    print('Вывод:', a, b, c)


print_params()  #  Вывод: 1 строка True

print_params('читаемость', c='значение')  #  Вывод: читаемость строка значение

print_params(b=25)  #  Вывод: 1 25 True

print_params(c=[1, 2, 3])  #  Вывод: 1 строка [1, 2, 3]

values_list = ['cat', 'dog', 'bat']
values_dict = {'a': 'BMW', 'b': 'Lada', 'c': 'Nissan'}

print_params(*values_list)  #  Вывод: cat dog bat
print_params(**values_dict)  #  Вывод: BMW Lada Nissan

values_list_2 = ['moon', 'sun']
print_params(*values_list_2, 42) #  Вывод: moon sun 42
