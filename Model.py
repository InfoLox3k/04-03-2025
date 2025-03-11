# Model (Модель) - отвечает за данные и логику работы с ними
def sum_num(num_list):
    summ = 0
    for item in num_list:
        summ += item
    return summ

def min_num(num_list):
    minn = 0
    for item in num_list:
        minn -= item
    return minn

def mult_num(num_list):
    multt = 0
    i = 0

    for item in num_list:
        if i == 0:
            multt = item
        else:
            multt *= item
        i += 1
    return multt

def div_num(num_list):
    div = 0
    i = 0

    for item in num_list:
        if i == 0:
            div = item
        else:
            div /= item
        i += 1
    return div

import math

def square_area(a):
    """Вычисляет площадь квадрата."""
    return a ** 2

def rectangle_area(a, b):
    """Вычисляет площадь прямоугольника."""
    return a * b

def triangle_area(base, height):
    """Вычисляет площадь треугольника."""
    return 0.5 * base * height

def circle_area(r):
    """Вычисляет площадь круга."""
    return math.pi * r ** 2

def parallelogram_area(base, height):
    """Вычисляет площадь параллелограмма."""
    return base * height

def trapezoid_area(a, b, height):
    """Вычисляет площадь трапеции."""
    return (a + b) * height / 2

def rhombus_area(d1, d2):
    """Вычисляет площадь ромба."""
    return (d1 * d2) / 2

# def area_of_cube(num_list):
#     area = 6 * (num_list[0]**2)
#     return area
#
# def area_of_box(num_list):
#     area = 2 * (num_list[0]*num_list[1] + num_list[0]*num_list[2] + num_list[1]*num_list[2])
#     return area
#
# def area_of_box(num_list):
#     area = 2 * (num_list[0]*num_list[1] + num_list[0]*num_list[2] + num_list[1]*num_list[2])
#     return area

