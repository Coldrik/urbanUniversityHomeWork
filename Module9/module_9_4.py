import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
a = list(map(lambda x, y: x == y, first, second))
print(a)


def get_advanced_writer(file_name):
    file = open(file_name, 'w', encoding='utf-8')
    def write_everything(*data_set):
        for i in data_set:
            file.writelines(f'{i}\n')
        file.close()
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *lines):
        self.words = set()
        for i in lines:
            self.words.add(i)
    def __call__(self, *args, **kwargs):
        return random.choice(tuple(self.words))

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())