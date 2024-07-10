class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}\n'

class Shop:

    check_list = set()
    def __init__(self):
        self.__file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name, 'r')
        list_of_product = file.read()
        file.close()
        return list_of_product

    def add(self, *products: Product):
        '''
        *products - объекты класса Product
        '''

        file = open(self.__file_name, 'a')
        for i in products:
            if i.name in self.check_list or i.name in str(self.get_products()):
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                self.check_list.add(i.name)
                file.write(str(i))
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())