import queue
from random import random
from threading import Thread
from time import sleep


class Table:

    def __init__(self, num):
        self.num = num
        self.guest = None


    def __call__(self):
        return self.not_busy


class Cafe:

    def __init__(self, *tables):
        self.guests = []
        self.q = queue.Queue()
        self.tables = [*tables]


    def busy_tables(self):
        check = False
        for t in self.tables:
            if t.guest is not None:
                check = True
        return check

    def guest_arrival(self, *guests):
        for i in guests:  # Добавляем всех пришедших гостей в общий список на входе
            print(i.name_of_guest)
            self.guests.append(i)

        free_table = []
        for check_table in self.tables:  # Проверяем свободные столы
            if check_table.guest is None:
                free_table.append(check_table)

        for t in free_table:  # Рассаживаем гостей за свободные столы, запускается процесс
            t.guest = self.guests.pop(0)
            t.guest.start()
            print(f'{t.guest.name_of_guest} сел(-а) за стол номер {t.num}')

        while len(self.guests) > 0:  # Гости, не попавшие за стол, становятся в очередь
            next_guest = self.guests.pop(0)
            self.q.put(next_guest)
            print(f'{next_guest.name_of_guest} в очереди')

        print('Всех рассадили')


    def discuss_guests(self):
        num_table = 0
        while not self.q.empty() or self.busy_tables():
            for t in self.tables:

                if t.guest is None and not self.q.empty():
                    t.guest = self.q.get()
                    print(f'{t.guest.name_of_guest} вышел(-ла) из очереди и сел(-а) за стол номер {t.num}')
                    t.guest.start()
                if t.guest is not None and not t.guest.is_alive():
                    print(f'{t.guest.name_of_guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {t.num} свободен')
                    t.guest = None



class Guest(Thread):
    def __init__(self, name_of_guest):
        super().__init__()
        self.name_of_guest = name_of_guest
        self.num_of_table = None

    def run(self):
        # print(f'{self.name_of_guest}: Ням-Ням-Ням.')
        sleep(random() * 7 + 3)
        # print(f'{self.name_of_guest}: Спасибо, я поел.')



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
