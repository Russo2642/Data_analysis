extension = ['png', 'jperg', 'ppt', 'gif']

user_input = input('введите название файла: ')
splited = user_input.split('.')
if splited[-1] in extension:
    print ('ok')
else:
    print('нет такого')



