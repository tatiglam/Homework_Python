import math


def square(side):

    # Вычисляем площадь
    area = side * side

    # Если сторона была не целой, округляем вверх
    if not isinstance(side, int):
        area = math.ceil(area)

    return area


# Примеры использования:
side1 = 5
side2 = 5.5
side3 = 3.2

print(f"Площадь квадрата со стороной {side1}: {square(side1)}")
print(f"Площадь квадрата со стороной {side2}: {square(side2)}")
print(f"Площадь квадрата со стороной {side3}: {square(side3)}")
