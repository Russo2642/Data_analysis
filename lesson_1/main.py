print('Heelo World')

# type узннать тип данных
# str() превращение данных в строчку
# str() + str() конкатинация строк
# - % показывает отстаток
# 3**2 степени
# bool все значение не равные 0 true



print('Добро пожаловать в ситему')
name = input('укажи имя: ')
age = int(input("сколько тебе лет: "))
phone = input("номер телефона: ")

name= 'тебя зовут' + name
age =  age + 1
print(f"""
Имя : {name}
Возраст : {age}
Номер : {phone}
""")

answear = (input("Данные заполнены верно ?\n "))
if answear == 'y':
    print('спасибо')
elif answear == 'N':
    print ('введите данные еще раз')