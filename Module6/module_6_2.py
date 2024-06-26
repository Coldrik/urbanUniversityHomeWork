class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        if color.lower() in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            print("Проверьте цвет автомобиля")
            self.__color = None

    def get_model(self):
        return print(f'Модель: {self.__model}')

    def get_horsepower(self):
        return print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return print(f'Цвет:  {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, color):
        if color.lower() in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            return print(f'Невозможно покрасить в {color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue1', 500)

# Изначальные свойства
vehicle1.print_info()
vehicle1.__color = 'black'  # нет прав на изменение цвета, только через метод set_color!

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
