


# if 1 > 0 :  # == True
#     print(1 + 1)
# elif 1 == 1:
#     print('Второе условие сработало')
# else:
#     print('Oops....')


print("""
    Добро пожаловать в систему!
Прежде чем пройти дальше, тебе нужно оставить свои личные данные
""")
user_name = input('Ваше имя: ')
user_age = input('Ваш возраст: ')
user_phone = input('Ваш номер: ')
# Возраст                             к возрасту прибавить + 1
# Сотовый

print('Проверьте правильность заполнения ваших данных')

print(f"""
    Имя : {user_name}
    Возраст : {user_age}
    Номер : {user_phone}
""")


user_answer = input('Данные заполнены правильно ?\n')


if user_answer.lower() == 'да':
    print('Спасибо за сотрудничество')
elif user_answer.upper() == 'НЕТ':
    print('Заполните данные ещё раз')
else:
    print('???')
# Два варианта ответа : Да или Нет 

# Если пользователь отвечат Да, то вывовдим "Спасибо за сотрудничество"

# Если пользователь отвечает Нет, то выводим "Заполните данные ещё раз"


if 1 > 0:
    if user_answer.lower() == 'да':
        print('Спасибо за сотрудничество')
    else:
        print('Ничего не вышло')
else:
    print('не работает')
    