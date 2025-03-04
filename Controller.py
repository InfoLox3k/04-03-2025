from Model import *
from View import *

# Controller (Контроллер) - управляет логикой и связывает модель с представлением
def main():
    while True:
        choice = display_menu()

        if choice == '1':
            try:
                result = expression()
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
