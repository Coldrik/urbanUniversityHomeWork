def test_function():
    def inner_fuction():
        print('Я в области видимости функции test_function')

    inner_fuction()


test_function()  #  Я в области видимости функции test_function

#NameError: name 'inner_fuction' is not defined:
#print('Вызов функции inner_function вне функции test_function: ', inner_fuction())
