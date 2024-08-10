import multiprocessing
from datetime import datetime

from Module11.module_11_1 import WarehouseManager


def read_info(name):
    print(name)
    all_data = list()
    with open(name, 'r', encoding='UTF-8') as file:
        all_data.append(file.readlines())


filenames = [f'file {numbers}.txt' for numbers in range(1, 5)]

# Линейный вызов
# start = datetime.now()
# list(map(read_info, filenames))
# end = datetime.now()
# print(end - start, 'линейный')

# Итоговый результат линейный: 0:00:13.883998


# Многопроцессный
if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        list(pool.map(read_info, filenames))

    end = datetime.now()
    print(end - start, 'Многопроцессный')
# Итоговый результат многопроцессный: 0:00:05.274009