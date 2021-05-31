

import random
x = random.randint(0, 100)
i = 0

answ = input('Wanna play with me Y/N?:')
if answ.lower() == 'n':
    exit()
elif answ.lower() == 'y':
    while i < 8:
        ui = int(input('Guess my number from 0 to 100: '))
        if x == ui:
            print('You win, my number', x)
            i += 1
            exit()
        elif x > ui:
            print('Ur num smaller')
            i += 1
        elif x < ui:
            print('ur mum bigger')
            i += 1    

if i == 8:
    print('U loose, my nubmer:', x)


# a.split('.') 
# '.'.join.(a)
#Doanwload git file