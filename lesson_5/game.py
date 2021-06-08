# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    random.shuffle(field)
    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    param_field = list(range(1, 16))
    param_field.append(EMPTY_MARK)

    return field == param_field

def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    index = field.index('x')
    move = MOVES[key]
    if key == 'w' and index <= 3:
        raise IndexError('you cant move up')
    elif key == 's' and index >= 12:
        raise IndexError('you cant move down')
    elif key == 'a' and (index % 4) == 0:
        raise IndexError('you cant move left')
    elif key == 'd' and (index % 4) == 3:
        raise IndexError('you cant move right')
    

    new_index = index + move
    field[index], field[new_index] = field[new_index], field[index]

    return field
    

def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    step = input('Ход: ')
    while not step in MOVES.keys():
        step = input('Введите WASD.\nХод: ')
    return step


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()
    print_field(field)
    while not is_game_finished(field):
        key = handle_user_input()
        try:
            perform_move(field, key)
        except IndexError as e:
            print(e)
        print_field(field)

if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()

