from threading import Thread
from time import sleep


class Knight(Thread):


    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100


    def run(self):
        print(f'{self.name}, на нас напали!')
        sec = 0
        while self.enemy > 0:
            sleep(1)
            sec += 1
            self.enemy -= self.power
            print(f'{self.name}, сражается {sec} день(дня)..., осталось {self.enemy} воинов.' + '\n')
        print(f'{self.name} одержал победу спустя {sec} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
first_knight.start()

second_knight = Knight('Sir Galahad', 20)
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
