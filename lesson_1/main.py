
# Типы данных : 
# type() - узнать тип данных

# str() - Превращение данных в строку

# str() + str() - конкатинация (объединение) двух и более строк

# int() - Превращение в число 

# bool() - Логический тип данных (True/False)

# !!! Складывать два разных типа дынных НЕЛЬЗЯ

# Вывод в консоль - print()


# print(type(int(input("Введите ваш возраст: "))))



# Варианты написания переменных : 

    # 1) user_input 

    # 2) UserInput

# ----------------------------------------------------------------------------------------------------                                          
                                # быстрый коммент - ctrl + /

user_name = input("Введите ваше имя: ")

user_age = input("Введите ваш возраст: ")

print("\tВаше имя: ", user_name, "\n\tВаш возраст: ", user_age)

print(f"\tВаше имя: {user_name}\n\tВаш возраст: {user_age}")

print("\tВаше имя: {}\n\tВаш возраст: {} \n\tВаш пол: {}".format(user_name, user_age, "Мужской"))

print(f"""
    Привет, меня зовут {user_name}.
    Мне 22 года.
    Я программист
""")






# Выведите в консоль информацию о пользователе, запросив у него данные



print("""
    Добро пожаловать в систему!
Прежде чем пройти дальше, тебе нужно оставить свои личные данные
""")



user_name = input('Ваше имя: ')
# Возраст                             к возрасту прибавить + 1
# Сотовый


print('Проверьте правильность заполнения ваших данных')

user_age = int(input('возраст: '))

print(f"Имя : Руслан, Возраст: {user_age + 1}")


