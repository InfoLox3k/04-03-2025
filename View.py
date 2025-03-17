# View (Представление) - отвечает за отображение и ввод данных
num_list = []


def display_menu():
    print("\nВыбери действие: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление, 5 - вычисление площади, 0 - выход")
    choice = input("Введи номер действия: ")
    return choice

def display_menu_of_area():
    print("\nВыбери действие: 1 - 2D, 2 - 3D, 0 - выход")
    choice2 = input("Введи номер действия: ")
    return choice2

def display_menu_of_2D_area():
    print("\nВыбери действие: 1 - квадрат, 2 - Прямоугольник, 3 - Треугольник, 4 - Круг, 5 - Параллелограмм, 6 - Трапеция, 7 - Ромб, 0 - выход")
    choice4 = input("Введи номер действия: ")
    return choice4

def display_menu_of_3D_area():
    print("\nВыбери действие: 1 - Куб, 2 - Сфера, 3 - Параллелепипед, 4 - Цилиндр, 5 - Конус, 6 - Пирамида, 7 - Призма, 0 - выход")
    choice3 = input("Введи номер действия: ")
    return choice3

def Num():
    while True:
        num = float(input('Введите число: '))
        if num == 0:
            break
        else:
            num_list.append(num)
    return num_list

def Num_2D():

    num1 = float(input('Введите длину: '))
    num2 = float(input('Введите ширину: '))
    num3 = float(input('Введите высоту: '))

    num_list.append(num)
    return num_list

def Num_of_cube_area():
    length = float(input('Введите длину: '))
    return length

def Num_of_circle_area():
    radius = float(input('Введите радиус: '))
    return radius

def Num_of_box_area():
    length = float(input('Введите длину: '))
    width = float(input('Введите ширину: '))
    height = float(input('Введите высоту: '))
    info_list = [lengh, width, height]

    return info_list

def Num_of_cylinder_area():
    radius = float(input('Введите радиус: '))
    height = float(input('Введите высоту: '))
    info_list = [radius, height]
    return info_list

def Num_of_cone_area():
    radius = float(input('Введите радиус: '))
    length = float(input('Введите длину: '))
    info_list = [radius, length]
    return info_list

def Num_of_pyramid_area():
    A = float(input('Введите площадь основания: '))
    P = float(input('Введите периметр основания: '))
    l = float(input('Введите высоту боковой грани: '))
    info_list = [A, P, l]
    return info_list

def Num_of_prism_area():
    A = float(input('Введите площадь основания: '))
    P = float(input('Введите периметр основания: '))
    h = float(input('Введите высоту призмы: '))
    info_list = [A, P, h]
    return info_list


def ZeroDivision():
    print('На ноль делить НЕЛЬЗЯ')
def Goodbye():
    print('Пока')
def BeNormal():
    print('Сейчас пойду за шваброй... Пиши НОРМАЛЬНО')

def Result(result):
    print(result)

def ThatLevelAgain():
    again = input('Продолжим?(Да/Нет): ')
    return again
