class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides):
        self.__sides = list(__sides)
        self.__color = list(__color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for x in (r, g, b):
            if 0 <= x <= 255:
                return r, g, b

    def set_color(self, new_r, new_g, new_b):
        self.new_r = new_r
        self.new_g = new_g
        self.new_b =new_b
        if 0 < self.new_r <=255 and 0 < self.new_g <=255 and 0 < self.new_b <=255:
            self.__color = [new_r, new_g, new_b]
        else:
            return self.__color

    def __is_valid_sides(self, *new_sides):
        for x in new_sides:
            if isinstance(x, int) and x > 0 and x == len(self.__sides):
                self.filled = True

            else:
                self.filled = False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        self.new_sides = list(new_sides)
        if len(new_sides) != self.sides_count:
            return self.__sides
        else:
            self.__sides = list(new_sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, length):
        super().__init__(__color, length)
        self.__radius = length / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        s = sum(self.get_sides()) / 2
        return (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, side):
        super().__init__(__color)
        self.side = side

    def get_sides(self):
        set_side_lst = []
        for element in range(self.sides_count):
            set_side_lst.append(self.side)
        self.__sides = set_side_lst
        return self.__sides

    def get_volume(self):
        return self.side ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
