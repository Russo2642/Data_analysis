# Создать лист из 6 любых чисел. Отсортировать его по возрастанию

numbers = [15, 22, 23, 0.698, 1802, -16, -0.523]
print('list of number ', numbers)
numbers.sort()
print('sort by increase ', numbers)

# Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно

slovar = {1:'one', 2:'2', 3:'three', 6:'6', 21:'twenty one'}
for pary, value in slovar.items():
    print(pary, value)

# Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем

tuple = (2.22, 0.25436, 32.12456, 15.112, 567.234, 123.1987, 7.1231, -0.0012312, 7897.136, 1.5)
print('max in в Tuple ', max(tuple))
print('min in Tuple ', min(tuple))

# Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,          # !
# чтобы получилось: 'Earth -> Russia -> Moscow'
slova = ['Earth', 'Russia', 'Moscow']
print(" -> ".join(slova))

# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
str1 = '/bin:/usr/bin:/usr/local/bin'
print(str1.split(':'))

# Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет

print([i for i in range(1,100) if i%7 == 0])

# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

matrix = [[10,9,8],
          [7,6,5],
          [4,3,2],
          [1,0,-1]]

print('Выводим строки\n')
for mat in range(len(matrix)):
    print('\n')
    for string in range(len(matrix[mat])):
        print(matrix[mat][string], end = ' ')

print('Выводим колонки\n')
for string in range(len(matrix[mat])):
    print('\n')
    for mat in range(len(matrix)):
        print(matrix[mat][string], end = ' ')

# Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс                  # !

object_list = [15, 'router', {41:'bread'}, (6,70,15)]
for i in object_list:
    print(i, ' ', object_list.index(i))

# Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'

x1 = ['1','to-delete','2','to-delete','3','4','to-delete','5']
print('list before clear ', x1 )
x1 = [data for data in x1 if data !='to-delete']
print('list after clear: ', x1)

# Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
for y1 in range(10,0,-1):
    print(y1, end = ' ')
print('')