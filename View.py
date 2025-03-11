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
    print("\nВыбери действие: 1 - Куб, 2 - Параллелепипед, 3 - Сфера, 4 - Цилиндр, 5 - Конус, 6 - Пирамида, 0 - выход")
    choice3 = input("Введи номер действия: ")
    return choice3

def Num():
    while True:
        num = float(input('Введите число: '))
        if num == 0:
            return num_list
        else:
            num_list.append(num)

def Num_2D():
    for i in range(3):
        num = float(input('Введите число: '))
        if num == 0:
            return num_list
        else:
            num_list.append(num)

# def Num_of_cube_area():
#     lengh = float(input('Введите длину: '))
#
#     return lengh
#
# def Num_of_box_area():
#     lengh = float(input('Введите длину: '))
#     width = float(input('Введите ширину: '))
#     height = float(input('Введите высоту: '))
#     info_list = [lengh, width, height]
#
#     return info_list

def ZeroDivision():
    print('На ноль делить НЕЛЬЗЯ')
def Goodbye():
    print('Пока')
def BeNormal():
    print('Сейчас пойду за шваброй... Пиши НОРМАЛЬНО')

def Result(result):
    print(result)
