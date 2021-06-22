# Напечайтайте о каждом из друзей такое сообщение ""(Имя друга) живет в городе (название города)

frineds = {'Arsen':'Almaty', 'Atlet':'Astana', 'Nikolay':'Shymkent'}
for i, value in frineds.items():
    print(i,'живет в городе', value)

# в этой задаче вам дан словарь, в котором ключи имена друзей, а значения списки любимых песен каждого другаю

# напечатайте  кол-во любимых песен димы
#все любимые песни сони через запятую и пробел

pesni = {'Dima':['Ramstein', 'Nirvana'] , 'Sonya':['Ranetki','KISH','Zveri']}
print('Nikolay loves',len(pesni['Dima']), 'song')
print(' ,' .join(pesni['Sonya']))

