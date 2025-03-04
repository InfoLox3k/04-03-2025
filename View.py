# View (Представление) - отвечает за отображение и ввод данных
def display_menu():
    print("\nВыбери действие: 1 - решить выражение, 0 - выход")
    choice = input("Введи номер действия: ")

    return choice

def ZeroDivision():
    print('На ноль делить НЕЛЬЗЯ')
def Goodbye():
    print('Пока')
def BeNormal():
    print('Сейчас пойду за шваброй... Пиши НОРМАЛЬНО')

def Result(result):
    print(result)