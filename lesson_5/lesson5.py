# посмотреть про return



x = int(input('enter ur number: '))
if x % 2 != 0:
    try: 
        x % 3 > 0
        print('Cool') 
except:
    print('ValueEror ')
if x > 10:
    raise Exception('TypeEror')
    



x1 = [1, 2, 3, '4', '5']
y = int(input('Enter index for list with 5 values: '))
try:
    y < 4
    print(x1[y])
except:
    print('there is no such index')

#рандом библеотека шафл
