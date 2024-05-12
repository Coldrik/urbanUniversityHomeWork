my_list = ['яблоко', 'груша', 'мандарин', 'манго', 'арбуз']
print('List: ' + str(my_list))
print('First element: ' + my_list[0] + '\nLast element: ' + my_list[-1])
print('Sublist: ' + str(my_list[2: 5]))
my_list[2] = 'киви'
print('Modified list: ' + str(my_list))
my_dict = {'собака': 'dog', 'кошка': 'kat', 'орел': 'eagle'}
print('\nDictionary: ' + str(my_dict))
print('Translation: ' + my_dict['собака'])
my_dict['волк'] = 'wolf'
print('Modified dictionary: ' + str(my_dict))