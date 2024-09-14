import datetime

import matplotlib.pyplot as plt
import numpy as np
import requests
import pprint
from bs4 import BeautifulSoup

"""
Данный код парсит погодные данные с сайта https://meteoinfo.ru с помощью библиотеки "requests"
и выводит в графическом представления изменения параметров погоды на ближайшие 2 дня с помощью библиотеки matplotlib
"""


class Cloud:
    """
    Класс для хранения параметров погоды
    """

    def __init__(self):
        self.days_temp = [0, 0, 0]  # 0 - today, 1 - tomorrow, 2 - after tomorrow
        self.nights_temp = [0, 0, 0]
        self.wind = [0, 0, 0]
        self.days_press = [0, 0, 0]
        self.nights_press = [0, 0, 0]
        self.data = datetime.date.today()


def add_to_base(description: list) -> Cloud:
    """
    Функция, которая выбирает из блока текста значения параметров погоды и возвращает в виде объекта класса Cloud
    """
    cloud_param = Cloud()
    for i in range(1, 4):
        data_list = description[i].replace('°', " °").split(' ')
        for c in range(len(data_list)):
            if data_list[c - 1] == 'ночью' and '°' in data_list[c + 1]:  # Выборка из текста температуры ночь
                cloud_param.nights_temp[i - 1] = int(data_list[c])
            if data_list[c - 1] == 'днём' and '°' in data_list[c + 1]:  # Выборка из текста температуры день
                cloud_param.days_temp[i - 1] = int(data_list[c])
            if ',' in data_list[c - 1] and 'м/с' in data_list[c + 1]:  # Выборка из текста скорости ветра
                cloud_param.wind[i - 1] = int(data_list[c])
            if data_list[c - 1] == 'ночью' and 'мм' in data_list[c + 1]:  # Выборка из текста давление ночь
                cloud_param.nights_press[i - 1] = int(data_list[c])
            if data_list[c - 1] == 'днём' and 'мм' in data_list[c + 1]:  # Выборка из текста давление день
                cloud_param.days_press[i - 1] = int(data_list[c])
    return cloud_param


URL = 'https://meteoinfo.ru/rss/forecasts/index.php'  # Рессур получения погодных данных
data = requests.get(URL, params={'s': '28440'})  # Записываем данные в переменную
print(f'Код состояния HTTP рессурса: {data.status_code}. //Примечание - Ожидается ответ 200')

# pprint.pprint(data.text) # Дежурная команда проверки полного пакета данных

soup = BeautifulSoup(data.text, 'xml')  # извлекаем данные

descr = soup.find_all('description')  # Выбираем из данных (из раздела <description>) нужные блоки данных с параметрами
cloud_descr = []
for i in range(0, 4):  # Преобразуем данные из формата TAG в формат Str
    cloud_descr.append(str(descr[i]))

c_param = add_to_base(cloud_descr)
print(
    f'Изменение температуры на ближайшие 2 дня \nTemp_day: {c_param.days_temp}, Temp_night: {c_param.nights_temp}, TODAY: {c_param.data}')

# Выводим визуальное изображение прогнозного изменеия температуры
fig, ax = plt.subplots()  # Create a figure containing a single Axes.
ax.plot([str(c_param.data), 'tomorrow', 'after tomorrow'], c_param.nights_temp, label='Nights_temp С°')
ax.plot([str(c_param.data), 'tomorrow', 'after tomorrow'], c_param.days_temp, label='Days_temp С°')
ax.set_title("Изменение температуры")

fig2, ax2 = plt.subplots()
ax2.plot([str(c_param.data), 'tomorrow', 'after tomorrow'], c_param.nights_press, label='Nights_pressure мм рт.ст.')
ax2.plot([str(c_param.data), 'tomorrow', 'after tomorrow'], c_param.days_press, label='Days_pressure мм рт.ст.')
ax2.set_title("Изменение атмосферного давления")

fig3, ax3 = plt.subplots()
ax3.plot([str(c_param.data), 'tomorrow', 'after tomorrow'], c_param.wind, label='Wind_speed м/с')
ax3.set_title("Изменение скорости ветра")

ax.legend()
ax2.legend()
ax3.legend()
plt.show()  # Show the figure.
