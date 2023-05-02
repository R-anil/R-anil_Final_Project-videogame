# File created by: Ryan Anil

import pygame as pg
import math
import sys 
import numpy as np
 


ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board,row,col,piece):
    board[row][col]= piece

def is_valid_location(board,col):
    for r in range (ROW_COUNT):
        if board[r][col]==0:
            return r

def print_board(board):
    print(np.flip(board,0))

#initialize board
board = create_board()
#We will initialize the game_over as False.
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        selection = int(input("Player 1, Make your selection(0,6):"))

        # Ask for player 2 input
    else:
        selection = int(input("Player 2, Make your selection(0,6):"))
    print_board(board)

    turn += 1
    turn = turn % 2


