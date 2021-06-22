

    

answ = ['python', 'true', 'int']
dic = {1:'python', 2:'true', 3:'int'}

print('Играем в загадки')
q = input('Загадка 1 \nКакой язык мы изучаем?:  ')
if dic[1] == q.lower():
    print('Правильно')
    a = 1
else:
    print('Неправильно')
print('Идём дальше')
q = input('Загадка 2 \nTrue+True= ?')
if q.lower() in answ:
    print('Правильно')
    a = a + 1
else:
    print('Неправильно')
print('Идём дальше')
q = input('Загадка 3 \n Data type for numbers ?')
if q.lower() in answ:
    print('Правильно')
    a = a + 1
else:
    print('Неправильно')
print(' Правильных ответов - ',a)