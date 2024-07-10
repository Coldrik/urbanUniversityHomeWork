from math import pi


class Figure:
    def __init__(self, color, *sides, sides_count=0):
        self.__color = list([255, 255, 255])
        self.__sides = [*sides]
        self.filled = True
        self.sides_count = sides_count
        if self.__is_valid_color(list(color)):
            self.set_color(color[0], color[1], color[2])
        else:
            print('неверно введен формат цвета')
            pass

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        if len(color) == 3 and isinstance(color, list):
            for i in range(3):
                check = 256 > color[i] >= 0
                if not check:
                    return False
        else:
            return False
        return True

    def set_color(self, r, g, b):
        color = [r, g, b]
        if self.__is_valid_color(color):
            iterator = 0
            for i in color:
                self.__color[iterator] = i
                iterator += 1
        else:
            print('неверно введен формат цвета')
            pass

    def __if_valid_sides(self, *sides):
        sides_counter = 0
        for i in list(*sides):
            if isinstance(i, int) and i > 0:
                sides_counter += 1
            else:
                return False
        print('side_counter= ', sides_counter, '     self.sides_count= ', self.sides_count)
        return True if sides_counter == self.sides_count else False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        sum = 0
        for i in self.__sides:
            sum += i
        return sum

    def set_sides(self, *sides):
        if len(sides) == self.sides_count:
            self.__sides = [*sides]
        else:
            print("Некорректно заданы размеры сторон")


class Circle(Figure):
    def __init__(self, color, side1):
        super().__init__(color, side1, sides_count=1)
        self.__radius = self.get_sides()[0] / (2 * pi)
        # print('Radius: ', self.__radius) #  вывод информации о радиусе
        # print('Square: ', self.get_square()) #  вывод информации о площади

    def get_square(self):
        return pi * (self.__radius ** 2)


class Triangle(Figure):

    def __init__(self, color, side1, side2, side3):
        super.__init__(color, side1, side2, side3, sides_count=3)


class Cube(Figure):
    def __init__(self, color, side1):
        super().__init__(color, side1, sides_count=1)

    def get_sides(self):
        return self._Figure__sides * 12

    def get_volume(self):
        for i in self._Figure__sides:
            return i ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
