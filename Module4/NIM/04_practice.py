from nim_engine import get_bunches, put_stones, is_gameover, take_from_bunch
from termcolor import cprint

put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color="green")
    cprint(get_bunches(), color="green")
    user_color = 'blue' if user_number == 1 else "yellow"
    print('Ход игрока {}'.format(user_number))
    pos = input('Откуда берем?')
    qua = input('Сколько берем?')
    take_from_bunch(position=int(pos), quantity=int(qua))
    if is_gameover():
        break
    user_number = 2 if user_number == 1 else 1

print('Выйграл игрок номер', user_number)

