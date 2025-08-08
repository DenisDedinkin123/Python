import math


def square(side_length):
    area = side_length ** 2
    if not isinstance(side_length, int):
        area = math.ceil(area)
    return area


side = int(input("Введите сторону квадрата: "))
print(f"Площадь квадрата со стороной {side} равна {square(side)}")
