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
