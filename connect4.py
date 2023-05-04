# File created by: Ryan Anil

import pygame as pg
import math
import sys 
import numpy as np
 
BLUE = (0,0,255)
BLACK =(0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# dimensions
ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board,row,col,piece):
    board[row][col]= piece

def is_valid_location(board,col):
    # if this condition is true let the use drop piece.
    # if not true col is not vacant
    return board[5][col]==0

def get_next_open_row(board,col):
    for r in range (ROW_COUNT):
        if board[r][col]==0:
            return r
        
def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):
    # Check horizontal locatons for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board [r][c+1] == piece and board [r][c+2] == piece and board [r][c+3] == piece:
                return True 
    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board [r+1][c+1] == piece and board [r+2][c+2] == piece and board [r+3][c+3] == piece:
                return True 
    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board [r-1][c+1] == piece and board [r-2][c+2] == piece and board [r-3][c+3] == piece:
                return True 
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pg.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
            pg.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            if board[r][c] == 1:
                pg.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pg.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pg.display.update()

#initialize board
board = create_board()
#We will initialize the game_over as False.
game_over = False
turn = 0

# initialize pygame
pg.init()

# define screen size
SQUARESIZE = 100

# dimensions of board
width = COLUMN_COUNT*SQUARESIZE
height = (ROW_COUNT+1)*SQUARESIZE

size = (width/height)

RADIUS = int(SQUARESIZE/2-5)

screen = pg.display.set_mode(size)
# Calling Functions draw_board again
draw_board(board)
pg.display.update()

myfont = pg.font.SysFont("arial", 75)

while not game_over:
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
 
        if event.type == pg.MOUSEMOTION:
            pg.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pg.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else: 
                pg.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pg.display.update()
 
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            #print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
 
                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

    print_board(board)
    draw_board(board)

    turn += 1
    turn = turn % 2

    if game_over:
        pg.time.wait(3000)


