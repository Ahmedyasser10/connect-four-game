import numpy as np
import pygame
from math import floor
pygame.init()
ROW = 6
RED = (250, 0, 0)
YELLOW = (250, 250, 0)
COLUM = 7
blue = (0, 0, 255)
black = (0, 0, 0)

def create_board():
    board = np.zeros((6, 7))

    return board
board = create_board()


def valid_colum(board, c):
    if board[0][c] == 0:
        return True
    else:
        return False



def empty_row(board, c):
    for r in range(ROW-1, -1, -1):
        if board[r][c] == 0:
            return r
def update_board(board, r, c, player ):
    if player == "player 1":
        board[r][c] = 1
    else:
        board[r][c] = 2
    print(board)

def is_winner(board):
   # check_horizental
    for r in range(ROW):
        for c in range(COLUM-3):
            if board[r][c] == 1 and board[r][c+1] == 1 and board[r][c+2] == 1 and board[r][c+3] == 1:
                return "player 1"
            elif board[r][c] == 2 and board[r][c+1] == 2 and board[r][c+2] == 2 and board[r][c+3] == 2:
                return "player 2"

    # check_vertical
    for c in range(COLUM):
        for r in range (ROW-3):
            if board[r][c] == 1 and board[r+1][c] == 1 and board[r+2][c] == 1 and board[r+3][c] == 1:

                return "player 1"
            elif  board[r][c] == 2 and board[r+1][c] == 2 and board[r+2][c] == 2 and board[r+3][c] == 2:
                return "player 2"

    # check_positive_slope
    for c in range(COLUM-3):
        for r in range(ROW-1, 3, -1):
            if board[r][c] == 1 and board[r-1][c+1] == 1 and board[r-2][c+2] == 1 and board[r-3][c+3] == 1:
                return "player 1"
            elif board[r][c] == 2 and board[r-1][c+1] == 2 and board[r-2][c+2] == 2 and board[r-3][c+3] == 2:
                return "player 2"

    #negative slope
    for c in range(COLUM-3):
        for r in range(ROW-3):
            if board[r][c] == 1 and board[r+1][c+1] == 1 and board[r+2][c+2] == 1 and board[r+3][c+3] == 1:
                return "player 1"
            elif board[r][c] == 2 and board[r+1][c+1] == 2 and board[r+2][c+2] == 2 and board[r+3][c+3] == 2:
                return "player 2"



def draw_board(board):
    for c in range (COLUM):
        for r in range(ROW):
            pygame.draw.rect(screen, blue, (c*SQUARE, r*SQUARE+SQUARE, SQUARE, SQUARE ))
            if board[r][c] == 0:
                pygame.draw.circle(screen, black, (int(c*SQUARE+SQUARE/2), int(r*SQUARE+SQUARE+SQUARE/2)),radius)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARE + SQUARE / 2), int(r * SQUARE + SQUARE + SQUARE / 2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARE + SQUARE / 2), int(r * SQUARE + SQUARE + SQUARE / 2)), radius)
icon = pygame.image.load("connect-four.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Connect Four Game")


print(board)
game_over = False
turn = 0

SQUARE = 100
radius = (SQUARE/2)-2
width = COLUM * SQUARE
height = ROW * SQUARE
screen = pygame.display.set_mode((700, 700))
pygame.display.update()
game_over = False

draw_board(board)

font = pygame.font.SysFont("freesansbold.ttf",32)
game = 0
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos = event.pos[0]

            if turn % 2 == 0:
                print(event.pos[0])
                colum = int(floor(x_pos/100))
                if valid_colum(board, colum):
                    row = empty_row(board, colum)
                    update_board(board, row, colum, "player 1")
                    game +=1

            else:
                colum = int(floor(x_pos/100))
                if valid_colum(board, colum):
                    row = empty_row(board, colum)
                    update_board(board, row, colum, "player 2")
                    game +=1



            turn += 1
            if is_winner(board) == "player 1":
                wining = font.render("Player 1 has won!!!", True, (250, 0, 0))
                screen.blit(wining,(250, 10) )
                game_over = True

            if is_winner(board) == "player 2":
                wining = font.render("Player 2 has won!!!", True, (250, 250, 0))
                screen.blit(wining, (250, 10))
                game_over = True
            if game == 42:
                draw = font.render("Draw ", True, (250, 250, 250))
                screen.blit(draw, (250, 10))
                game_over = True

    draw_board(board)
    pygame.display.update()
    if game_over:
        pygame.time.wait(3000)



