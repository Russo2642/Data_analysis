# -*- coding: utf-8 -*-

import random

EQ_X = "X"
EQ_O = "O"
EMPTY = " "
COUNT = 9

board = range(1,10)

def write_board(board):
    print("-" * 13)
    for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)


def add_board():
    """
    Создание игральной доски
    :return: доска для игры
    """
    board = []
    for i in range(COUNT):
        board.append(EMPTY)
    return board
    
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

def take_input(move):
    valid = False
    while not valid:
        player_move = input("Твой ход " + move+"? ")
        try:
            player_move = int(player_move)
        except:
            print("Не правильный ход. введи число?")
            continue
        if player_move >= 1 and player_move <= 9:
            if (str(board[player_move-1]) not in "XO"):
                board[player_move-1] = move
                valid = True
            else:
                print("Эта клетка занята")
        else:
            print("Не правильный ход. Введи число от 1 до 9 ")

def main(board):
    moves = 0
    win = False
    while not win:
        write_board(board)
        if moves % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        moves += 1
        if moves > 4:
            if winner(board):
                print("выиграл!")
                win = True
                break
        if moves == 9:
            print("Ничья!")
            break
    write_board(board)

if __name__ == '__main__':
    main()