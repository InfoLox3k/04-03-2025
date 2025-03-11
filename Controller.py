from Model import *
from View import *

# Controller (Контроллер) - управляет логикой и связывает модель с представлением
def main():
    choice = display_menu()
    num_list = Num()

    if choice == '1':
        try:
            result = sum_num(num_list)
            Result(result)
        except:
            BeNormal()
    elif choice == '2':
        try:
            result = min_num(num_list)
            Result(result)
        except:
            BeNormal()
    elif choice == '3':
        try:
            result = mult_num(num_list)
            Result(result)
        except:
            BeNormal()
    elif choice == '4':
        # try:
            result = div_num(num_list)
            Result(result)
        # except:
        #     BeNormal()

    elif choice == '0':
        Goodbye()
    else:
        BeNormal()

main()
