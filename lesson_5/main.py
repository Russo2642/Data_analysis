def function_with_default_value(name, age=0, needs_stars=True):
    message = '{} is {} years old!'.format(name, age)
    print(message)

    if needs_stars:
        print('*****')

function_with_default_value('Nikita')
function_with_default_value('Alex', age=19)
function_with_default_value('Bob', age=40, needs_stars=False)