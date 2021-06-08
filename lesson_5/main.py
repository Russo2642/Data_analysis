"""
1.Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0
"""

def func(a, b):
    if a > 0 and b > 0:
        return a + b
    elif a < 0 and b < 0:
        return a - b
    else:
        return 0


# print(func(int(input('Введите число a: ')), int(input('Введите число b: '))))


"""
3.Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. 
Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, если флаг отрицателен -
 возвращаем новый список с четными числами из входного списка
"""


def func(list_, Flag=True):
    new_list_che = []
    if Flag:
        for x in list_:
            if x % 2 != 0:
                new_list_che.append(x)
    return new_list_che


def func1(lst, Flag=False):
    new_list_neche = [x for x in lst if x % 2 == 0]
    return new_list_neche


list_ = [10, 2, 50, 5, -1, 0, 123]
print(func(list_))

print(func1(list_))