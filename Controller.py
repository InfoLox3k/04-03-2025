from Model import *
from View import *

# Controller (Контроллер) - управляет логикой и связывает модель с представлением
def main():
    choice = display_menu()


    if choice == '1':
        num_list = Num()
        try:
            result = sum_num(num_list)
            Result(result)
        except:
            BeNormal()
    elif choice == '2':
        num_list = Num()
        try:
            result = min_num(num_list)
            Result(result)
        except:
            BeNormal()
    elif choice == '3':
        num_list = Num()
        try:
            result = mult_num(num_list)
            Result(result)
        except:
            BeNormal()
    elif choice == '4':
        num_list = Num()
        try:
            result = div_num(num_list)
            Result(result)
        except:
            BeNormal()

    elif choice == '5':
        # try:
            choice2 = display_menu_of_area()
            if choice2 == '1':
                num_list = Num_2D()
                choice4 = display_menu_of_2D_area()
                if choice4 == '1':
                    result = square_area(num_list[0])
                elif choice4 == '2':
                    result = rectangle_area(num_list[0], num_list[1])
                elif choice4 == '3':
                    result = triangle_area(num_list[0], num_list[2])
                elif choice4 == '4':
                    result = circle_area(num_list[0])
                elif choice4 == '5':
                    result = parallelogram_area(num_list[0], num_list[2])
                elif choice4 == '6':
                    result = trapezoid_area(num_list[0], num_list[1], num_list[2])
                elif choice4 == '7':
                    result = rhombus_area(num_list[0], num_list[1])
                
            # elif choice2 == '2':
            #     choice3 = display_menu_of_3D_area()
            #     if choice3 == '1':
            #         lenghth = Num_of_cube_area()
            #         result = area_of_cube(lenghth)
            Result(result)
        # except:
        #     BeNormal()

    elif choice == '0':
        Goodbye()
    else:
        BeNormal()

main()
