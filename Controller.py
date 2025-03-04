from Model import *
from View import *

# Controller (Контроллер) - управляет логикой и связывает модель с представлением
def main():
    while True:
        choice = display_menu()

        if choice == '1':
            try:
                result = sum_num()
                Result(result)
            except:
                BeNormal()
        elif choice == '2':
            try:
                result = min_num()
                Result(result)
            except:
                BeNormal()
        elif choice == '3':
            try:
                result = mult_num()
                Result(result)
            except:
                BeNormal()
        elif choice == '4':
            try:
                result = div_num()
                Result(result)
            except:
                BeNormal()

        elif choice == '0':
            Goodbye()
            break
        else:
            BeNormal()

main()

# # Запуск программы
# if __name__ == "__main__":
#     main()
