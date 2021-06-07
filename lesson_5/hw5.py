# **Задачи на обработку ошибок:
# 1.Пользователь вводит число, если оно четное - выбрасываем исключение ValueError,
# если оно меньше 0 - TypeError, если оно больше 10 - IndexError. Обрабатываем ошибку, говорим пользователю, в чем его ошибка
vvod = input('Введите любое число:')
n = int(vvod)
try:
    if n < 0:
        raise TypeError ('Число меньше нуля')
    if n > 10:
        raise IndexError ('Число больше десяти')
    if n % 2 == 0:
        raise ValueError ('Число четное')
except TypeError :
    print('Число меньше нуля')
except IndexError :
    print('Число больше десяти')
except ValueError :
    print('Число четное')


# 2. Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть. Если все хорошо - 
# пишите объект в консоль. Если нет - обработайте возмозможные ошибки и скажите ему, что не так
x1 = [1, 2, 3, '4', '5']
y = int(input('Enter index for list with 5 values: '))
try:
    y < 4
    print(x1[y])
except:
    print('there is no such index')

# **Задачи на закрепление функций:
# 1.Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму.
# Если оба меньше - разность. Если знаки разные - возвращаем 0

def function(x,y):
    if x > 0 and y > 0:
        return x + y
    if x < 0 and y < 0:
        return x - y
    if x < 0 and y > 0:
        return 0
    if x > 0 and y < 0:
        return 0
print(function(7,-8))

# 2.Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль

def function(x,y,z):
    lst = [x,y,z]
    lst.sort()
    print(lst[1],lst[2])
function(8,5,10)

# 3.Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. 
# Если флаг действителен - возвращаем новый список с нечетными числами из входного списка,
# если флаг отрицателен - возвращаем новый список с четными числами из входного списка




# **Материалы:
# 1. Что такое ошибка? https://docs.python.org/3.6/tutorial/errors.html
# 2. Какие бывают ошибки? https://docs.python.org/3/library/exceptions.html
# 3. В чем разница между except и except Exception? https://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e-in-python
# 4. Что такое функция? https://www.tutorialspoint.com/python/python_functions.htm
# 5. Что значит - вызвать функцию? https://stackoverflow.com/questions/19130958/what-does-it-mean-to-call-a-function-in-python
# 6. Что такое *args и **kwargs: https://lancelote.gitbooks.io/intermediate-python/content/book/args_and_kwargs.html


