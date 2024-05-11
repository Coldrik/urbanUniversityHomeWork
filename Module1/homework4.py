immunable_var = (1, 'string', [0, 0], True)
# immunable_var[0] = 2 #элементы кортежа являются неизменяемыми
# immunable_var[2][0] = 2 #сам элемен кортежа не может быть изменен,
# а его компоненты могут быть изменены, если объект является изменяемым
print(immunable_var)
mutable_list = [1, 'string', [0, 0], True]
mutable_list[0] = 0
print(mutable_list)
