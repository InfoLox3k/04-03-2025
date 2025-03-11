# View (Представление) - отвечает за отображение и ввод данных
num_list = []


def display_menu():
    print("\nВыбери действие: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление, 0 - выход")
    choice = input("Введи номер действия: ")

    return choice

def Num():
    while True:
        num = float(input('Введите число: '))
        if num == 0:
            return num_list
        else:
            num_list.append(num)

def ZeroDivision():
    print('На ноль делить НЕЛЬЗЯ')
def Goodbye():
    print('Пока')
def BeNormal():
    print('Сейчас пойду за шваброй... Пиши НОРМАЛЬНО')

def Result(result):
    print(result)
