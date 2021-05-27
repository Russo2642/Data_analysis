# два вида цикла - for и while

# цикл for 

# for i in 'Hello': # перебирает значения в слове Hello 
#     print(i)


# for i in 'Hello':
#     if i == 'H':
#         print(i)


# a = input('Слово: ')

# if 'п' in a.lower(): # .lower() - к нижнему регистру , .upper() - к верхнему регистру
#     print('Есть такая буква')

# else:
#     print('Такой буквы нет')



# for i in range(20, 10, -2):# range(n, m, k) - n начальное число, m итоговое число, k шаг
#     print(i)


# a = 0

# while a < 5:
#     print(a)
#     if a == 3:
#         break
#     a += 1



for i in ['asd', 'qwe', 'zxc']:
    if i == 'qwe':
        break
    print(i)
    