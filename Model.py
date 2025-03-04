# Model (Модель) - отвечает за данные и логику работы с ними
def sum_num():
    summ = 0
    for item in num_list:
        summ += item
    return summ

def min_num():
    minn = 0
    for item in num_list:
        minn -= item
    return minn

def mult_num():
    multt = 0
    for item in num_list:
        multt *= item
    return multt

def div_num():
    div = 0
    for item in num_list:
        div /= item
    return div
