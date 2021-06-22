import random


EQ_X = "X"
EQ_O = "O"
EMPTY = " "
COUNT = 9


def add_board():
    """
    Создание игральной доски
    :return: доска для игры
    """
    board = []
    for i in range(COUNT):
        board.append(EMPTY)
    return board


def write_board(board):
    """
    Отрисовка игральной доски
    :param board: доска
    :return: None
    """
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

    
def winner(board):
    """
    Определение победителя
    :param board: доска
    :return: победитель
    """
    WAYS_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
    

