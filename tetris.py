import sys, pygame
from pygame.locals import *
from sys import exit
import random

# Initialize Pygame
pygame.init()
pygame.font.init()

# Set caption

pygame.display.set_caption('Tetris by David Campbell Columbia College')

# Music/sound

music = pygame.mixer.music.load("Tetris Music video by 2pm.mp3")#"Tetris Music video by 2pm.mp3")

lock_set = pygame.mixer.Sound("tetrissoundeffects/button-9.wav")
lock_set.set_volume(0.3)

#movement = pygame.mixer.Sound("tetrissoundeffects/button-16.wav")
#movement.set_volume(0.05)

single_cap = pygame.mixer.Sound("tetrissoundeffects/button-14.wav")
single_cap.set_volume(0.6)

double_cap = pygame.mixer.Sound("tetrissoundeffects/button-1.wav")

triple_cap = pygame.mixer.Sound("tetrissoundeffects/button-5.wav")

tetris_cap = pygame.mixer.Sound("tetrissoundeffects/button-8.wav")

#go_exp = pygame.mixer.Sound("tetrissoundeffects/ex-fl-2.wav")

#fail = pygame.mixer.Sound("tetrissoundeffects/GAME-OVER-SOUND-EFFECT.wav")


# Sound pics

music_on = pygame.image.load("images/soundon.gif")
music_off = pygame.image.load("images/soundoff.gif")



# Set surface to 680x480
BLACK = (0, 0, 0)
DIM_GRAY = (100, 100, 100)
DIMMER_GRAY = (45, 45, 45)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 128)
PINK = (255, 20, 147)
YELLOW = (255, 255, 0) 
TURQUOISE = (64, 224, 208)
SKY_BLUE = (135, 206, 250)
DODGER_BLUE = (30, 144, 255)
FIREBRICK = (142, 35, 35)
ORANGE = (255, 165, 0)
GREEN = (0, 100, 0)
PURPLE = (160, 32, 240)
LIGHT_PINK = (255, 182, 193)
SLATE_BLUE = (106,90,205)
STEEL_BLUE4 = (54,100,139)
MEDIUM_ORCHID = (147,112,219)
DIMMERER_GRAY = (30,30,30)

BACKGROUND = (135, 206, 250)


# Size of tiles

TILE = 30

# Change in the goal sign y value

d_go_y = 0


# Goal and Score Number

goal_number = '10'
score = '0'
level = '0'

# Board width and height

B_WIDTH = 10
B_HEIGHT = 20


# Border widths

L_BORDER = 90
R_BORDER = 40
TOP_BORDER = 60
B_BORDER = 40


# Width of line encompassing each tile

LINE_WIDTH = 1

# Set WIDTH and HEIGHT

WIDTH = TILE * B_WIDTH + TILE * B_WIDTH / 2 + L_BORDER + R_BORDER
HEIGHT = TILE * B_HEIGHT + TOP_BORDER + B_BORDER
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

TWENTY = WIDTH / 22
TEN = WIDTH / 44
TFIVE = WIDTH / 17.6
FORTY = WIDTH / 11
FIFTEEN = 3 * WIDTH / 88
THREE = 3 * WIDTH / 440
NINETEEN = int(WIDTH / 23)
FIVE = WIDTH / 88
SEVENTY = int(440 / 6.29)
SFIVE = int(440 / 6.76)







# Background shapes etc.

back_color = BLACK
back_vertices = [[L_BORDER - TEN, TOP_BORDER - FIFTEEN],[L_BORDER + B_WIDTH * TILE + THREE, TOP_BORDER - NINETEEN], \
                 [L_BORDER + B_WIDTH * TILE + THREE, HEIGHT - B_BORDER + FIVE],[L_BORDER - FIVE, HEIGHT - B_BORDER + FIFTEEN]]

hold_area_color = back_color
hold_area_vertices = [[back_vertices[0][0] - SEVENTY, back_vertices[0][1] + FIVE], [back_vertices[0][0], back_vertices[0][1]], \
                      [back_vertices[0][0], back_vertices[0][1] + SEVENTY], [back_vertices[0][0] - SFIVE, back_vertices[0][1] + SEVENTY]]

next_area_color = back_color
next_area_vertices = [[back_vertices[1][0],back_vertices[1][1]],[back_vertices[1][0] + SEVENTY,back_vertices[1][1] + FIVE], \
                      [back_vertices[1][0] + SEVENTY,back_vertices[1][1] + SEVENTY],[back_vertices[1][0],back_vertices[1][1] + SEVENTY]]

side_back_color = DODGER_BLUE
side_back_vertices = [[next_area_vertices[1][0] + FIVE, TEN],[WIDTH - TEN, TWENTY], \
                      [WIDTH - NINETEEN, HEIGHT - TEN],[L_BORDER + B_WIDTH * TILE \
                        + SEVENTY + TEN, HEIGHT - TWENTY]]

ha_layer_color = DIMMER_GRAY
ha_layer_vertices = [[hold_area_vertices[0][0] + TEN, hold_area_vertices[0][1] + TEN],[hold_area_vertices[1][0] + TEN,hold_area_vertices[1][1] + TEN], \
                     [hold_area_vertices[2][0] + TEN,hold_area_vertices[2][1] - TEN],[hold_area_vertices[3][0] + TEN,hold_area_vertices[3][1] - TEN]]

b_layer_color = ha_layer_color
b_layer_vertices = [[ha_layer_vertices[1][0],ha_layer_vertices[1][1]],[next_area_vertices[0][0] - TEN,next_area_vertices[0][1] + FIVE], \
                    [back_vertices[2][0] - FIVE,back_vertices[2][1] - FIVE],[back_vertices[3][0] + FIVE,back_vertices[3][1] - FIVE]]

na_layer_color = ha_layer_color
na_layer_vertices = [[b_layer_vertices[1][0],b_layer_vertices[1][1]],[next_area_vertices[1][0] - TEN,next_area_vertices[1][1] + FIVE], \
                     [next_area_vertices[2][0] - FIVE,next_area_vertices[2][1] - FIVE],[next_area_vertices[3][0] - TEN, next_area_vertices[3][1] - FIVE]]

goal_area_color = back_color
goal_area_vertices = [[back_vertices[2][0],back_vertices[2][1] - FORTY - THREE],[back_vertices[2][0] + FORTY, back_vertices[2][1] - FORTY], \
                      [back_vertices[2][0] + FORTY,back_vertices[2][1] + THREE],[back_vertices[2][0],back_vertices[2][1]]]

ga_layer_color = ha_layer_color
ga_layer_vertices = [[goal_area_vertices[0][0] - FIVE,goal_area_vertices[0][1] + FIVE],[goal_area_vertices[0][0] + FORTY - FIVE,goal_area_vertices[0][1] + TEN], \
                     [goal_area_vertices[2][0] - FIVE, goal_area_vertices[2][1] - FIVE],[goal_area_vertices[3][0] - FIVE, goal_area_vertices[3][1] - FIVE]]

score_area_color = back_color
score_area_vertices = [[back_vertices[0][0] + SEVENTY + TWENTY, back_vertices[0][1] - TWENTY],[back_vertices[1][0] - TWENTY - TEN, back_vertices[1][1] - TWENTY], \
                       [back_vertices[1][0] - TWENTY, back_vertices[1][1] + TEN],[back_vertices[0][0] + TWENTY, back_vertices[0][1]]]

la_layer_color = ha_layer_color
la_layer_vertices = [[score_area_vertices[0][0] + THREE, score_area_vertices[0][1] + TEN],[score_area_vertices[1][0] - TEN, score_area_vertices[1][1] + TEN], \
                     [score_area_vertices[2][0] + TEN, score_area_vertices[2][1] + TEN],[score_area_vertices[3][0] - TEN, score_area_vertices[3][1] + TEN]]

pause_back_color = DIMMERER_GRAY
pause_back_vertices = [[L_BORDER - TEN - (SEVENTY * FIVE) - SEVENTY, TOP_BORDER - TEN],[L_BORDER + (TILE * B_WIDTH) + TEN - (SEVENTY * FIVE) - SEVENTY,TOP_BORDER - TEN], \
                       [L_BORDER + (TILE * B_WIDTH) + TEN - (SEVENTY * FIVE) - SEVENTY, HEIGHT - B_BORDER + TEN],[L_BORDER - TEN - (SEVENTY * FIVE) - SEVENTY, HEIGHT - B_BORDER + TEN]]

pause_layer_color = back_color
pause_layer_vertices = [[pause_back_vertices[0][0] + TEN, pause_back_vertices[0][1] + TEN + FIVE],[pause_back_vertices[1][0] - TEN, pause_back_vertices[1][1] + TEN], \
                       [pause_back_vertices[2][0] - TEN, pause_back_vertices[2][1] - TEN - FIVE],[pause_back_vertices[3][0] + TEN, pause_back_vertices[3][1] - TEN - FIVE]]

resume_back_color = pause_back_color
resume_back_vertices = [[R_BORDER + FORTY + TWENTY - (SEVENTY * FIVE) - SEVENTY, (HEIGHT / 2) - SEVENTY],[WIDTH - R_BORDER - SEVENTY - SEVENTY - TWENTY - (SEVENTY * FIVE) - SEVENTY, (HEIGHT / 2) - SEVENTY], \
                        [WIDTH - R_BORDER - SEVENTY - SEVENTY - TWENTY - (SEVENTY * FIVE) - SEVENTY, HEIGHT / 2 + TWENTY - SEVENTY],[R_BORDER + FORTY + TWENTY + FIVE - (SEVENTY * FIVE) - SEVENTY, HEIGHT / 2 + TWENTY - SEVENTY]]

quit_back_color = pause_back_color
quit_back_vertices = [[resume_back_vertices[3][0], resume_back_vertices[3][1] + TWENTY],[resume_back_vertices[2][0], resume_back_vertices[2][1] + TWENTY], \
                      [resume_back_vertices[2][0],resume_back_vertices[2][1] + FORTY],[resume_back_vertices[0][0], resume_back_vertices[3][1] + FORTY]]

for_sure_color = pause_back_color
for_sure_vertices = [[-365,221],[-107,221],[-107,357],[-359,357]]





# This portion of the code helps position and render the text used in the game

# Text

font = pygame.font.Font(pygame.font.match_font(('impact')), 20)
lit_smaller_font = pygame.font.Font(pygame.font.match_font(('impact')), 13)
go_font = pygame.font.Font(pygame.font.match_font(('impact')), 90)
pause_tetris_font = pygame.font.Font(pygame.font.match_font(('impact')), SEVENTY)

# Render the text
next_piece = font.render('NEXT\nPIECE', True, FIREBRICK, BACKGROUND)
hold = font.render('HOLD', True, FIREBRICK, BACKGROUND)
goal = font.render('GOAL', True, FIREBRICK, BACKGROUND)
goal_no = font.render(goal_number, True, FIREBRICK, DIMMER_GRAY)
score_number = font.render(score, True, FIREBRICK, DIMMER_GRAY)
level_number = font.render(level, True, FIREBRICK, BACKGROUND)
level_text = font.render("LEVEL", True, FIREBRICK, BACKGROUND)
game_over = go_font.render("GAME OVER!", True, FIREBRICK, BLACK)
t = pause_tetris_font.render("T", True, DIMMERER_GRAY, BLACK)
e = pause_tetris_font.render("E", True, DIMMERER_GRAY, BLACK)
t2 = pause_tetris_font.render("T", True, DIMMERER_GRAY, BLACK)
are = pause_tetris_font.render("R", True, DIMMERER_GRAY, BLACK)
i = pause_tetris_font.render("I", True, DIMMERER_GRAY, BLACK)
s = pause_tetris_font.render("S", True, DIMMERER_GRAY, BLACK)
resume_play = font.render("RESUME", True, FIREBRICK, DIMMERER_GRAY)
quit_play = font.render("QUIT", True, FIREBRICK, DIMMERER_GRAY)
for_sure = lit_smaller_font.render("ARE YOU SURE YOU WANT TO QUIT?", True, FIREBRICK, DIMMERER_GRAY)
data_lost = font.render("ALL DATA WILL BE LOST", True, FIREBRICK, DIMMERER_GRAY)
yes_answer = font.render("YES", True, FIREBRICK, DIMMERER_GRAY)
no_answer = font.render("NO", True, FIREBRICK, DIMMERER_GRAY)

# Create a rectangle
next_pieceRect = next_piece.get_rect()
holdRect = hold.get_rect()
goalRect = goal.get_rect()
goal_noRect = goal_no.get_rect()
score_numberRect = score_number.get_rect()
level_numberRect = level_number.get_rect()
level_textRect = level_text.get_rect()
game_overRect = game_over.get_rect()
tRect = t.get_rect()
eRect = e.get_rect()
t2Rect = t2.get_rect()
areRect = are.get_rect()
iRect = i.get_rect()
sRect = s.get_rect()
resume_playRect = resume_play.get_rect()
quit_playRect = quit_play.get_rect()
for_sureRect = for_sure.get_rect()
data_lostRect = data_lost.get_rect()
yes_answerRect = yes_answer.get_rect()
no_answerRect = no_answer.get_rect()

# Center the rectangle
next_pieceRect.centerx = back_vertices[1][0] + ((next_area_vertices[1][0] - back_vertices[1][0]) / 2)
next_pieceRect.centery = back_vertices[1][1] / 2

holdRect.centerx = hold_area_vertices[0][0] + ((hold_area_vertices[1][0] - hold_area_vertices[0][0]) / 2)
holdRect.centery = next_pieceRect.centery

goalRect.centerx = next_pieceRect.centerx - ((goal_area_vertices[2][1] - goal_area_vertices[1][1])/ 4)
goalRect.centery = HEIGHT - ((goal_area_vertices[2][1] - goal_area_vertices[1][1])/ 2) + ((goal_area_vertices[2][1] - goal_area_vertices[1][1])/ 2) / 2

goal_noRect.centerx = goalRect.centerx + THREE
goal_noRect.centery = goalRect.centery - FORTY + FIVE

score_numberRect.centerx = WIDTH / 2 + TWENTY
score_numberRect.centery = TWENTY + TEN

level_numberRect.centerx = WIDTH / 2
level_numberRect.centery = HEIGHT - TEN

level_textRect.centerx = level_numberRect.centerx - SEVENTY
level_textRect.centery = level_numberRect.centery

game_overRect.centerx = WIDTH / 2
game_overRect.centery = d_go_y

tRect.centerx = WIDTH / 2  - (SEVENTY * FIVE) - SEVENTY
tRect.centery = TOP_BORDER + TWENTY + TEN + FIVE

eRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
eRect.centery = tRect.centery + SEVENTY + TWENTY

t2Rect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
t2Rect.centery = eRect.centery + SEVENTY + TWENTY

areRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
areRect.centery = t2Rect.centery + SEVENTY + TWENTY

iRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
iRect.centery = areRect.centery + SEVENTY + TWENTY

sRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
sRect.centery = iRect.centery + SEVENTY + TWENTY 

resume_playRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY - SEVENTY#resume_back_vertices[0][0]
resume_playRect.centery = HEIGHT / 2 - SEVENTY + TEN

quit_playRect.centerx = resume_playRect.centerx
quit_playRect.centery = resume_playRect.centery + TWENTY + TWENTY

for_sureRect.centerx = WIDTH / 2 - TWENTY - TEN - FIVE - (SEVENTY * FIVE) - SEVENTY
for_sureRect.centery = HEIGHT / 2 - SEVENTY - TWENTY - TEN

data_lostRect.centerx = WIDTH / 2 - TWENTY - TEN - FIVE - (SEVENTY * FIVE) - SEVENTY
data_lostRect.centery = HEIGHT / 2 - FORTY - TWENTY

yes_answerRect.centerx = WIDTH / 2 - FORTY + TEN - (SEVENTY * FIVE) - SEVENTY
yes_answerRect.centery = HEIGHT / 2 - TWENTY - TEN

no_answerRect.centerx = WIDTH / 2 - FORTY + TEN - (SEVENTY * FIVE) - SEVENTY
no_answerRect.centery = HEIGHT / 2 - TEN










# Graph of board

intro_squares = []

for y in range(0, B_HEIGHT):
    x = 0
    while x < B_WIDTH:
        intro_squares.append([((x * TILE + L_BORDER), (y * TILE + TOP_BORDER)), ((x * TILE + L_BORDER), (y * TILE + TILE + TOP_BORDER)), \
                              ((x * TILE + TILE + L_BORDER), (y * TILE + TILE + TOP_BORDER)), ((x * TILE + TILE + L_BORDER), (y * TILE + TOP_BORDER))])
        x += 1
    y += 1

circles_in_grid = []

for y in range(0, len(intro_squares)):
    circles_in_grid.append(intro_squares[y][0])
    circles_in_grid.append(intro_squares[y][1])
    circles_in_grid.append(intro_squares[2][0])
    circles_in_grid.append(intro_squares[y][3])








    

# Set all values in the board array to zero (signifying empty tile)

board = list(range(0, B_WIDTH))

for x in range(0, B_WIDTH):
    board[x] = list(range(0, B_HEIGHT))
    for y in range(0, B_HEIGHT):
        board[x][y] = 0








        

# Print the board (text-based)

def print_board():
    for y in range(0, B_HEIGHT):
        for x in range(0, B_WIDTH):
            if x != B_WIDTH - 1:
                print(board[x][y], end=' ')
            else:
                print(board[x][y])
    print(' ')
    print(' ')

    








# Define reset_board() function which makes all values in the array
# set to zero

def reset_board():
    for x in range(0, B_WIDTH):
        for y in range(0, B_HEIGHT):
            board[x][y] = 0







            

# Define the 4x4 piece array which will fill appropriately according to
# which piece is being played

piece = list(range(0, 4))

for x in range(0, 4):
    piece[x] = list(range(0, 4))
    for y in range(0, 4):
        piece[x][y] = 0










# This function will update the board with the occupied spaces
# Call whenever the gamepiece moves

def update_board(x_value, y_value):
    reset_board()

    for y in range(0, B_HEIGHT):
        for x in range(0, B_WIDTH):
            for m in range(0, len(stacked_piece)):
                if x == stacked_piece[m][0] and y == stacked_piece[m][1]:
                    board[x][y] = 1
    if x_value >= 0:# and y_value < 0:
        for y in range(0, B_HEIGHT):
            x = 0
            while x < B_WIDTH:
                if y == piece_pos[1] and x == piece_pos[0]:
                    if piece[0][0] == 2:
                        board[x][y] = piece[0][0]
                    if piece[1][0] == 2:
                        board[x + 1][y] = piece[1][0]
                    if piece[2][0] == 2:
                        board[x + 2][y] = piece[2][0]
                    if piece[3][0] == 2:
                        board[x + 3][y] = piece[3][0]
    
                    x += 4
                if y == piece_pos[1] + 1 and x == piece_pos[0]:
                    if piece[0][1] == 2:
                        board[x][y] = piece[0][1]
                    if piece[1][1] == 2:
                        board[x + 1][y] = piece[1][1]
                    if piece[2][1] == 2:
                        board[x + 2][y] = piece[2][1]
                    if piece[3][1] == 2:
                        board[x + 3][y] = piece[3][1]
    
                    x += 4
                if y == piece_pos[1] + 2 and x == piece_pos[0]:
                    if piece[0][2] == 2:
                        board[x][y] = piece[0][2]
                    if piece[1][2] == 2:
                        board[x + 1][y] = piece[1][2]
                    if piece[2][2] == 2:
                        board[x + 2][y] = piece[2][2]
                    if piece[3][2] == 2:
                        board[x + 3][y] = piece[3][2]
                
                    x += 4
                if y == piece_pos[1] + 3 and x == piece_pos[0]:
                    if piece[0][3] == 2:
                        board[x][y] = piece[0][3]
                    if piece[1][3] == 2:
                        board[x + 1][y] = piece[1][3]
                    if piece[2][3] == 2:
                        board[x + 2][y] = piece[2][3]
                    if piece[3][3] == 2:
                        board[x + 3][y] = piece[3][3]
    
                x += 1

    if y_value >= 0 and x_value < 0:
        for x in range(0, B_WIDTH):
            y = 0
            while y < B_HEIGHT:
                if y == piece_pos[1] and x == piece_pos[0]:
                    if piece[0][0] == 2:
                        board[x][y] = piece[0][0]
                    if piece[0][1] == 2:
                        board[x][y + 1] = piece[0][1]
                    if piece[0][2] == 2:
                        board[x][y + 2] = piece[0][2]
                    if piece[0][3] == 2:
                        board[x][y + 3] = piece[0][3]
    
                    y += 4
                if y == piece_pos[1] and x == piece_pos[0] + 1:
                    if piece[1][0] == 2:
                        board[x][y] = piece[1][0]
                    if piece[1][1] == 2:
                        board[x][y + 1] = piece[1][1]
                    if piece[1][2] == 2:
                        board[x][y + 2] = piece[1][2]
                    if piece[1][3] == 2:
                        board[x][y + 3] = piece[1][3]
    
                    y += 4
                if y == piece_pos[1] and x == piece_pos[0] + 2:
                    if piece[2][0] == 2:
                        board[x][y] = piece[2][0]
                    if piece[2][1] == 2:
                        board[x][y + 1] = piece[2][1]
                    if piece[2][2] == 2:
                        board[x][y + 2] = piece[2][2]
                    if piece[2][3] == 2:
                        board[x][y + 3] = piece[2][3]
                
                    y += 4
                if y == piece_pos[1] and x == piece_pos[0] + 3:
                    if piece[3][0] == 2:
                        board[x][y] = piece[3][0]
                    if piece[3][1] == 2:
                        board[x][y + 1] = piece[3][1]
                    if piece[3][2] == 2:
                        board[x][y + 2] = piece[3][2]
                    if piece[3][3] == 2:
                        board[x][y + 3] = piece[3][3]
    
                y += 1

    if y_value < 0 and x_value < 0:
        if selection == 2:
            for x in range(0, B_WIDTH):
                y = 0
                while y < B_HEIGHT:
                    if y == piece_pos[1] + 1 and x == piece_pos[0] + 2:
                        if piece[2][1] == 2:
                            board[x][y] = piece[2][1]
                        if piece[3][1] == 2:
                            board[x + 1][y] = piece[3][1]
        
                        y += 1
                    if y == piece_pos[1] + 2 and x == piece_pos[0] + 2:
                        if piece[2][2] == 2:
                            board[x][y] = piece[2][2]
                        if piece[3][2] == 2:
                            board[x + 1][y] = piece[3][2]
        
                        y += 1
                    if y == piece_pos[1] + 3 and x == piece_pos[0] + 2:
                        if piece[2][3] == 2:
                            board[x][y] = piece[2][3]
                        if piece[3][3] == 2:
                            board[x + 1][y] = piece[3][3]
                            
                    y += 1
        else:
            for x in range(0, B_WIDTH):
                y = 0
                while y < B_HEIGHT:
                    if y == piece_pos[1] + 1 and x == piece_pos[0] + 1:
                        if piece[1][1] == 2:
                            board[x][y] = piece[1][1]
                        if piece[2][1] == 2:
                            board[x + 1][y] = piece[2][1]
                        if piece[3][1] == 2:
                            board[x + 2][y] = piece[3][1]
        
                        y += 1
                    if y == piece_pos[1] + 2 and x == piece_pos[0] + 1:
                        if piece[1][2] == 2:
                            board[x][y] = piece[1][2]
                        if piece[2][2] == 2:
                            board[x + 1][y] = piece[2][2]
                        if piece[3][2] == 2:
                            board[x + 2][y] = piece[3][2]
        
                        y += 1
                    if y == piece_pos[1] + 3 and x == piece_pos[0] + 1:
                        if piece[1][3] == 2:
                            board[x][y] = piece[1][3]
                        if piece[2][3] == 2:
                            board[x + 1][y] = piece[2][3]
                        if piece[3][3] == 2:
                            board[x + 2][y] = piece[3][3]
                            
                    y += 1







def update_board2(x_value, y_value):
    reset_board()

    for y in range(0, B_HEIGHT):
        for x in range(0, B_WIDTH):
            for m in range(0, len(stacked_piece)):
                if x == stacked_piece[m][0] and y == stacked_piece[m][1]:
                    board[x][y] = 1
    
    if x_value >= 0:
        for y in range(0, B_HEIGHT):
            x = 0
            while x < B_WIDTH:
                if y == piece_pos[1] and x == piece_pos[0]:
                    if piece[0][0] == 2:
                        board[x][y] = piece[0][0]
                    if piece[1][0] == 2:
                        board[x + 1][y] = piece[1][0]
                    if piece[2][0] == 2:
                        board[x + 2][y] = piece[2][0]
                    if piece[3][0] == 2:
                        board[x + 3][y] = piece[3][0]
    
                    x += 4
                if y == piece_pos[1] + 1 and x == piece_pos[0]:
                    if piece[0][1] == 2:
                        board[x][y] = piece[0][1]
                    if piece[1][1] == 2:
                        board[x + 1][y] = piece[1][1]
                    if piece[2][1] == 2:
                        board[x + 2][y] = piece[2][1]
                    if piece[3][1] == 2:
                        board[x + 3][y] = piece[3][1]
    
                    x += 4
                if y == piece_pos[1] + 2 and x == piece_pos[0]:
                    if piece[0][2] == 2:
                        board[x][y] = piece[0][2]
                    if piece[1][2] == 2:
                        board[x + 1][y] = piece[1][2]
                    if piece[2][2] == 2:
                        board[x + 2][y] = piece[2][2]
                    if piece[3][2] == 2:
                        board[x + 3][y] = piece[3][2]
                
                    x += 4
                if y == piece_pos[1] + 3 and x == piece_pos[0]:
                    if piece[0][3] == 2:
                        board[x][y] = piece[0][3]
                    if piece[1][3] == 2:
                        board[x + 1][y] = piece[1][3]
                    if piece[2][3] == 2:
                        board[x + 2][y] = piece[2][3]
                    if piece[3][3] == 2:
                        board[x + 3][y] = piece[3][3]
    
                x += 1

    else:
        for x in range(0, B_WIDTH):
            y = 0
            while y < B_HEIGHT:
                if y == piece_pos[1] and x == piece_pos[0]:
                    if piece[0][0] == 2:
                        board[x][y] = piece[0][0]
                    if piece[0][1] == 2:
                        board[x][y + 1] = piece[0][1]
                    if piece[0][2] == 2:
                        board[x][y + 2] = piece[0][2]
                    if piece[0][3] == 2:
                        board[x][y + 3] = piece[0][3]
    
                    y += 4
                if y == piece_pos[1] and x == piece_pos[0] + 1:
                    if piece[1][0] == 2:
                        board[x][y] = piece[1][0]
                    if piece[1][1] == 2:
                        board[x][y + 1] = piece[1][1]
                    if piece[1][2] == 2:
                        board[x][y + 2] = piece[1][2]
                    if piece[1][3] == 2:
                        board[x][y + 3] = piece[1][3]
    
                    y += 4
                if y == piece_pos[1] and x == piece_pos[0] + 2:
                    if piece[2][0] == 2:
                        board[x][y] = piece[2][0]
                    if piece[2][1] == 2:
                        board[x][y + 1] = piece[2][1]
                    if piece[2][2] == 2:
                        board[x][y + 2] = piece[2][2]
                    if piece[2][3] == 2:
                        board[x][y + 3] = piece[2][3]
                
                    y += 4
                if y == piece_pos[1] and x == piece_pos[0] + 3:
                    if piece[3][0] == 2:
                        board[x][y] = piece[3][0]
                    if piece[3][1] == 2:
                        board[x][y + 1] = piece[3][1]
                    if piece[3][2] == 2:
                        board[x][y + 2] = piece[3][2]
                    if piece[3][3] == 2:
                        board[x][y + 3] = piece[3][3]
    
                y += 1





                

"""

The 'next_move' variable will be used to determine if a move is valid or not. When requesting to move a space,
the spaces on the board that will be occupied if the move is allowed will be stored in 'next_move'. This variable
will then be compared with the 'board' array. If there are found any values on the board that have any of the
same coordinates that the 'next_move' variable holds, the move will not be allowed. Also, if the piece moves
off of the board, the move will not be allowed.

"""


def check_move(direction):
    next_move = []
    if direction == 'DOWN':
        for y in range(0, B_HEIGHT):
            for x in range(0, B_WIDTH):
                if board[x][y] == 2:
                    next_move.append([x, y + 1])

    if direction == 'UP':
        for y in range(0, B_HEIGHT):
            for x in range(0, B_WIDTH):
                if board[x][y] == 2:
                    next_move.append([x, y - 1])

    if direction == 'LEFT':
        for y in range(0, B_HEIGHT):
            for x in range(0, B_WIDTH):
                if board[x][y] == 2:
                    next_move.append([x - 1, y])

    if direction == 'RIGHT':
        for y in range(0, B_HEIGHT):
            for x in range(0, B_WIDTH):
                if board[x][y] == 2:
                    next_move.append([x + 1, y])

    # This for-loop checks to see if the piece is trying to move off the board

    for l in range(0, len(next_move)):
        if next_move[l][0] < 0 or next_move[l][0] >= B_WIDTH \
        or next_move[l][1] < 0 or next_move[l][1] >= B_HEIGHT:
            return "DON'T MOVE"

    # This for-loop checks to see if the piece collides with an occupied space on the board

    for y in range(0, B_HEIGHT):
        for x in range(0, B_WIDTH):
            if board[x][y] == 1:
                for m in range(0, len(next_move)):
                    if x == next_move[m][0] and y == next_move[m][1]:
                        return "DON'T MOVE"

    return "MOVE"










# Use this function to help determine rotations and find collisions

def compare_w_board(selection):

    select_piece(selection)

    test_board = list(range(0, B_WIDTH))

    for x in range(0, B_WIDTH):
        test_board[x] = list(range(0, B_HEIGHT))
        for y in range(0, B_HEIGHT):
            test_board[x][y] = 0




    x_value = piece_pos[0]
    y_value = piece_pos[1]

    if x_value >= 0:
        for y in range(0, B_HEIGHT):
            x = 0
            while x < B_WIDTH:
                if y == piece_pos[1] and x == piece_pos[0]:
                    if piece[0][0] == 2:
                        test_board[x][y] = piece[0][0]
                    if piece[1][0] == 2:
                        test_board[x + 1][y] = piece[1][0]
                    if piece[2][0] == 2:
                        test_board[x + 2][y] = piece[2][0]
                    if piece[3][0] == 2:
                        test_board[x + 3][y] = piece[3][0]
    
                    x += 4
                if y == piece_pos[1] + 1 and x == piece_pos[0]:
                    if piece[0][1] == 2:
                        test_board[x][y] = piece[0][1]
                    if piece[1][1] == 2:
                        test_board[x + 1][y] = piece[1][1]
                    if piece[2][1] == 2:
                        test_board[x + 2][y] = piece[2][1]
                    if piece[3][1] == 2:
                        test_board[x + 3][y] = piece[3][1]
    
                    x += 4
                if y == piece_pos[1] + 2 and x == piece_pos[0]:
                    if piece[0][2] == 2:
                        test_board[x][y] = piece[0][2]
                    if piece[1][2] == 2:
                        test_board[x + 1][y] = piece[1][2]
                    if piece[2][2] == 2:
                        test_board[x + 2][y] = piece[2][2]
                    if piece[3][2] == 2:
                        test_board[x + 3][y] = piece[3][2]
                
                    x += 4
                if y == piece_pos[1] + 3 and x == piece_pos[0]:
                    if piece[0][3] == 2:
                        test_board[x][y] = piece[0][3]
                    if piece[1][3] == 2:
                        test_board[x + 1][y] = piece[1][3]
                    if piece[2][3] == 2:
                        test_board[x + 2][y] = piece[2][3]
                    if piece[3][3] == 2:
                        test_board[x + 3][y] = piece[3][3]
    
                x += 1

    else:
        for x in range(0, B_WIDTH):
            y = 0
            while y < B_HEIGHT:
                if y == piece_pos[1] and x == piece_pos[0]:
                    if piece[0][0] == 2:
                        test_board[x][y] = piece[0][0]
                    if piece[0][1] == 2:
                        test_board[x][y + 1] = piece[0][1]
                    if piece[0][2] == 2:
                        test_board[x][y + 2] = piece[0][2]
                    if piece[0][3] == 2:
                        test_board[x][y + 3] = piece[0][3]
    
                    y += 4
                if y == piece_pos[1] and x == piece_pos[0] + 1:
                    if piece[1][0] == 2:
                        test_board[x][y] = piece[1][0]
                    if piece[1][1] == 2:
                        test_board[x][y + 1] = piece[1][1]
                    if piece[1][2] == 2:
                        test_board[x][y + 2] = piece[1][2]
                    if piece[1][3] == 2:
                        test_board[x][y + 3] = piece[1][3]
    
                    y += 4
                if y == piece_pos[1] and x == piece_pos[0] + 2:
                    if piece[2][0] == 2:
                        test_board[x][y] = piece[2][0]
                    if piece[2][1] == 2:
                        test_board[x][y + 1] = piece[2][1]
                    if piece[2][2] == 2:
                        test_board[x][y + 2] = piece[2][2]
                    if piece[2][3] == 2:
                        test_board[x][y + 3] = piece[2][3]
                
                    y += 4
                if y == piece_pos[1] and x == piece_pos[0] + 3:
                    if piece[3][0] == 2:
                        test_board[x][y] = piece[3][0]
                    if piece[3][1] == 2:
                        test_board[x][y + 1] = piece[3][1]
                    if piece[3][2] == 2:
                        test_board[x][y + 2] = piece[3][2]
                    if piece[3][3] == 2:
                        test_test_board[x][y + 3] = piece[3][3]
    
                y += 1


    for y in range(0, B_HEIGHT):
        for x in range(0, B_WIDTH):
            if board[x][y] == 1 and test_board[x][y] == 2:
                return "DON'T ROTATE"
                
                    
                    

    return "ROTATE"










# Use this function to determine selection piece to be tested for rotation/collision

def test_piece(selection, sub_selection, next_selection):
    if sub_selection == '0':
        if next_selection == 'R':
            if selection == 5:
                selection = 6
            elif selection == 9:
                selection = 10
            elif selection == 13:
                selection = 14
            elif selection == 17:
                selection = 18
            elif selection == 21:
                selection = 22
            elif selection == 25:
                selection = 26
        elif next_selection == 'L':
            if selection == 5:
                selection = 8
            elif selection == 9:
                selection = 12
            elif selection == 13:
                selection = 16
            elif selection == 17:
                selection = 20
            elif selection == 21:
                selection = 24
            elif selection == 25:
                selection = 28
    elif sub_selection == 'R':
        if next_selection == '0':
            if selection == 6:
                selection = 5
            elif selection == 10:
                selection = 9
            elif selection == 14:
                selection = 13
            elif selection == 18:
                selection = 17
            elif selection == 22:
                selection = 21
            elif selection == 26:
                selection = 25
        elif next_selection == '2':
            if selection == 6:
                selection = 7
            elif selection == 10:
                selection = 11
            elif selection == 14:
                selection = 15
            elif selection == 18:
                selection = 19
            elif selection == 22:
                selection = 23
            elif selection == 26:
                selection = 27
    elif sub_selection == '2':
        if next_selection == 'R':
            if selection == 7:
                selection = 6
            elif selection == 11:
                selection = 10
            elif selection == 15:
                selection = 14
            elif selection == 19:
                selection = 18
            elif selection == 23:
                selection = 22
            elif selection == 27:
                selection = 28
        elif next_selection == 'L':
            if selection == 7:
                selection = 8
            elif selection == 11:
                selection = 12
            elif selection == 15:
                selection = 16
            elif selection == 19:
                selection = 20
            elif selection == 23:
                selection = 24
            elif selection == 27:
                selection = 28
    elif sub_selection == 'L':
        if next_selection == '0':
            if selection == 8:
                selection = 5
            elif selection == 12:
                selection = 9
            elif selection == 16:
                selection = 13
            elif selection == 20:
                selection = 17
            elif selection == 24:
                selection = 21
            elif selection == 28:
                selection = 25
        elif next_selection == '2':
            if selection == 8:
                selection = 7
            elif selection == 12:
                selection = 11
            elif selection == 16:
                selection = 15
            elif selection == 20:
                selection = 19
            elif selection == 24:
                selection = 23
            elif selection == 28:
                selection = 27

    return selection










# Use this function to determine what the selection will be if the test that checks collision fails

def failed_test(selection, sub_selection, next_selection):
    if sub_selection == '0':
        if next_selection == 'R':
            if selection == 6:
                selection = 5
            elif selection == 10:
                selection = 9
            elif selection == 14:
                selection = 13
            elif selection == 18:
                selection = 17
            elif selection == 22:
                selection = 21
            elif selection == 26:
                selection = 25
        elif next_selection == 'L':
            if selection == 8:
                selection = 5
            elif selection == 12:
                selection = 9
            elif selection == 16:
                selection = 13
            elif selection == 20:
                selection = 17
            elif selection == 24:
                selection = 21
            elif selection == 28:
                selection = 25
    elif sub_selection == 'R':
        if next_selection == '0':
            if selection == 5:
                selection = 6
            elif selection == 9:
                selection = 10
            elif selection == 13:
                selection = 14
            elif selection == 17:
                selection = 18
            elif selection == 1:
                selection = 2
            elif selection == 25:
                selection = 26
        elif next_selection == '2':
            if selection == 7:
                selection = 6
            elif selection == 11:
                selection = 10
            elif selection == 15:
                selection = 14
            elif selection == 19:
                selection = 18
            elif selection == 23:
                selection = 22
            elif selection == 27:
                selection = 26
    elif sub_selection == '2':
        if next_selection == 'R':
            if selection == 6:
                selection = 7
            elif selection == 10:
                selection = 11
            elif selection == 14:
                selection = 15
            elif selection == 18:
                selection = 19
            elif selection == 22:
                selection = 23
            elif selection == 28:
                selection = 27
        elif next_selection == 'L':
            if selection == 8:
                selection = 7
            elif selection == 12:
                selection = 11
            elif selection == 16:
                selection = 15
            elif selection == 20:
                selection = 19
            elif selection == 24:
                selection = 23
            elif selection == 28:
                selection = 27
    elif sub_selection == 'L':
        if next_selection == '0':
            if selection == 5:
                selection = 8
            elif selection == 9:
                selection = 12
            elif selection == 13:
                selection = 16
            elif selection == 17:
                selection = 20
            elif selection == 21:
                selection = 24
            elif selection == 25:
                selection = 28
        elif next_selection == '2':
            if selection == 7:
                selection = 8
            elif selection == 11:
                selection = 12
            elif selection == 15:
                selection = 16
            elif selection == 19:
                selection = 20
            elif selection == 23:
                selection = 24
            elif selection == 27:
                selection = 28

    return selection







            
# Rotate the pieces

def rotate(selection, sub_selection, next_selection):

    if selection == 1 or selection == 2 or selection == 3 or selection == 4:
        if sub_selection == 'R':
            if next_selection == '0':
                if piece_pos[0] != -2 and piece_pos[0] != B_WIDTH - 3:
                    selection = 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 3 and piece_pos[0] != B_WIDTH - 4 and piece_pos[0] != -2:
                    selection = 1
                    piece_pos[0] += 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 2
                        piece_pos[0] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != -2 and piece_pos[0] != B_WIDTH - 4 and piece_pos[0] != B_WIDTH - 3:
                    selection = 1
                    piece_pos[0] += 1
                    piece_pos[1] -= 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 2
                        piece_pos[0] -= 1
                        piece_pos[1] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 3 and piece_pos[0] != -1 and piece_pos[0] != -2:
                    selection = 1
                    piece_pos[1] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 2
                        piece_pos[1] -= 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != -2 and piece_pos[0] != B_WIDTH - 3  and piece_pos[0] != B_WIDTH - 4:
                    selection = 1
                    piece_pos[0] -= 1
                    piece_pos[1] -= 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 2
                        piece_pos[0] += 1
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])
                        
                        
            elif next_selection == '2':
                if piece_pos[0] != -2 and piece_pos[0] != B_WIDTH - 3:
                    selection = 3

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != -2 and piece_pos[0] != -1 and piece_pos[0] != 0:
                    selection = 3
                    piece_pos[0] -= 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 2
                        piece_pos[0] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])
                        
                elif piece_pos[0] != B_WIDTH - 3 and piece_pos[0] != B_WIDTH - 4 and piece_pos[0] != B_WIDTH - 5:
                    selection = 3
                    piece_pos[0] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 2
                        piece_pos[0] -= 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 4 and piece_pos[0] != -2 and piece_pos[0] != -1 and piece_pos[0] != 0:
                    selection = 3
                    piece_pos[0] -= 1
                    piece_pos[1] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 2
                        piece_pos[1] -= 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 3 and piece_pos[0] != B_WIDTH - 4 and piece_pos[0] != B_WIDTH - 5:
                    selection = 3
                    piece_pos[0] += 2
                    piece_pos[1] -= 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 2
                        piece_pos[0] -= 2
                        piece_pos[1] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])
                    

        elif sub_selection == 'L':
            if next_selection == '0':
                if piece_pos[0] != -1 and piece_pos[0] != B_WIDTH - 2 and piece_pos[0] != B_WIDTH - 3:
                    selection = 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 4
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 2 and piece_pos[0] != B_WIDTH - 3 and piece_pos[0] != B_WIDTH - 4:
                    selection = 1
                    piece_pos[0] += 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 4
                        piece_pos[0] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != -1 and piece_pos[0] != 0 and piece_pos[0] != 1:
                    selection = 1
                    piece_pos[0] -= 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 4
                        piece_pos[0] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != 0 and piece_pos[0] != B_WIDTH - 2 and piece_pos[0] != B_WIDTH - 3 and piece_pos[0] != B_WIDTH - 4:
                    selection = 1
                    piece_pos[0] += 1
                    piece_pos[1] -= 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 4
                        piece_pos[0] -= 1
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != -1 and piece_pos[0] != 0 and piece_pos[0] != 1:
                    selection = 1
                    piece_pos[0] -= 2
                    piece_pos[1] += 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 4
                        piece_pos[0] += 2
                        piece_pos[1] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])
                

            elif next_selection == '2':
                if piece_pos[0] != -1 and piece_pos[0] != B_WIDTH - 2 and piece_pos[0] != B_WIDTH - 3:
                    selection = 3
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 4
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != -1 and piece_pos[0] != 0 and piece_pos[0] != 1:
                    selection = 3
                    piece_pos[0] -= 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 4
                        piece_pos[0] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 2 and piece_pos[0] != B_WIDTH - 3 and piece_pos[0] != B_WIDTH - 4:
                    selection = 3
                    piece_pos[0] += 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 4
                        piece_pos[0] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != 0 and piece_pos[0] != 1:
                    selection = 3
                    piece_pos[0] -= 2
                    piece_pos[1] -= 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 4
                        piece_pos[0] += 2
                        piece_pos[1] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != -1 and piece_pos[0] != B_WIDTH - 3 and piece_pos[0] != B_WIDTH - 2:
                    selection = 3
                    piece_pos[0] += 1
                    piece_pos[1] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 4
                        piece_pos[0] -= 1
                        piece_pos[1] -= 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])
                

        elif sub_selection == '0':
            if next_selection == 'R':
                if piece_pos[1] != B_HEIGHT - 2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = 2
                    piece_pos[0] -= 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 1
                        piece_pos[0] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = 2
                    piece_pos[0] += 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 1
                        piece_pos[0] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != 0 and piece_pos[1] != B_HEIGHT - 2:
                    selection = 2
                    piece_pos[0] -= 2
                    piece_pos[1] -= 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 1
                        piece_pos[0] += 2
                        piece_pos[1] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_WIDTH - 2 and piece_pos[1] != B_WIDTH - 3 and piece_pos[1] != B_HEIGHT - 4 and piece_pos[1] != B_WIDTH - 5:
                    selection = 2
                    piece_pos[0] += 1
                    piece_pos[1] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 1
                        piece_pos[0] -= 1
                        piece_pos[1] -= 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])
                
            elif next_selection == 'L':
                if piece_pos[1] != B_HEIGHT - 2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = 4

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = 4
                    piece_pos[0] -= 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 1
                        piece_pos[0] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = 4
                    piece_pos[0] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 1
                        piece_pos[0] -= 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 2 and piece_pos[1] != B_HEIGHT - 3 and piece_pos[1] != B_HEIGHT - 4:
                    selection = 4
                    piece_pos[0] -= 1
                    piece_pos[1] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 1
                        piece_pos[0] += 1
                        piece_pos[1] -= 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_WIDTH - 2 and piece_pos[1] != B_WIDTH - 3 and piece_pos[1] != B_WIDTH - 4:
                    selection = 4
                    piece_pos[0] += 2
                    piece_pos[1] -= 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 1
                        piece_pos[0] -= 2
                        piece_pos[1] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])
                

        elif sub_selection == '2':
            if next_selection == 'R':
                if piece_pos[1] != -2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 3
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != -2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = 2
                    piece_pos[0] += 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 3
                        piece_pos[0] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != -2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = 2
                    piece_pos[0] -= 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 3
                        piece_pos[0] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != -2 and piece_pos[1] != 0 and piece_pos[1] != 1:
                    selection = 2
                    piece_pos[0] += 1
                    piece_pos[1] -= 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 3
                        piece_pos[0] -= 1
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != -2 and piece_pos[1] != 0 and piece_pos[0] != B_WIDTH - 4:
                    selection = 2
                    piece_pos[0] -= 2
                    piece_pos[1] += 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 3
                        piece_pos[0] += 2
                        piece_pos[1] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

            elif next_selection == 'L':
                if piece_pos[1] != B_HEIGHT - 3 and piece_pos[1] != -2:
                    selection = 4

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 3
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 3 and piece_pos[1] != -2:
                    selection = 4
                    piece_pos[0] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 3
                        piece_pos[0] -= 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 3 and piece_pos[1] != -2:
                    selection = 4
                    piece_pos[0] -= 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 3
                        piece_pos[0] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != -2 and piece_pos[1] != B_HEIGHT - 3 and piece_pos[1] != B_HEIGHT - 4:
                    selection = 4
                    piece_pos[0] += 2
                    piece_pos[1] += 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 3
                        piece_pos[0] -= 2
                        piece_pos[1] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != -2 and piece_pos[1] != 0 and piece_pos[0] != 1:
                    selection = 4
                    piece_pos[0] -= 1
                    piece_pos[1] -= 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = 3
                        piece_pos[0] += 1
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])


            
    elif selection == 5 or selection == 6 or selection == 7 or selection == 8 \
    or selection == 9 or selection == 10 or selection == 11 or selection == 12 \
    or selection == 13 or selection == 14 or selection == 15 or selection == 16 \
    or selection == 17 or selection == 18 or selection == 19 or selection == 20 \
    or selection == 21 or selection == 22 or selection == 23 or selection == 24 \
    or selection == 25 or selection == 26 or selection == 27 or selection == 28:
        if sub_selection == 'R':
            if next_selection == '0':
                if piece_pos[0] != -1:
                    selection = test_piece(selection, sub_selection, next_selection)

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 3 and piece_pos[1] != 0:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1
                    piece_pos[1] -= 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] -= 1
                        piece_pos[1] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[1] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[1] -= 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 3 and piece_pos[1] != B_HEIGHT - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1
                    piece_pos[1] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] -= 1
                        piece_pos[1] -= 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

            elif next_selection == '2':

                if piece_pos[0] != -1:
                    selection = test_piece(selection, sub_selection, next_selection)

                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[0] -= 1
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1
                    piece_pos[1] -= 1

                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[0] -= 1
                        piece_pos[1] += 1
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 3 and piece_pos[1] != B_HEIGHT - 4:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[1] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[1] -= 2
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 3 and piece_pos[1] != B_HEIGHT - 4 and piece_pos[0] != B_WIDTH - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1
                    piece_pos[1] += 2

                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[0] -= 1
                        piece_pos[1] -= 2
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

        elif sub_selection == 'L':
            if next_selection == '0':
                if piece_pos[0] != B_WIDTH - 2:
                    selection = test_piece(selection, sub_selection, next_selection)
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != 0:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[0] += 1
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != 0 and piece_pos[1] != 0:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    piece_pos[1] -= 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[0] += 1
                        piece_pos[1] += 1
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[1] += 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[1] -= 2
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != 0 and piece_pos[1] != B_HEIGHT - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    piece_pos[1] += 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[0] += 1
                        piece_pos[1] -= 2
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

            elif next_selection == '2':
                if piece_pos[0] != B_WIDTH - 2:
                    selection = test_piece(selection, sub_selection, next_selection)
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != 0:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[0] += 1
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != 0:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    pieve_pos[1] -= 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[0] += 1
                        piece_pos[1] += 1
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != B_WIDTH - 2 and piece_pos[1] != B_HEIGHT - 3 and piece_pos[1] != B_HEIGHT - 4:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[1] += 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[1] -= 2
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[0] != 0 and piece_pos[1] != B_HEIGHT - 3 and piece_pos[1] != B_HEIGHT - 4:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    piece_pos[1] += 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        piece_pos[0] += 1
                        piece_pos[1] -= 2
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])
                        
        elif sub_selection == '0':
            if next_selection == 'R':
                if piece_pos[1] != B_HEIGHT - 2:
                    selection = test_piece(selection, sub_selection, next_selection)
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 2:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    piece_pos[1] += 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] += 1
                        piece_pos[1] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != 0 and piece_pos[1] != 1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[1] -= 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != 0 and piece_pos[1] != 1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    piece_pos[1] -= 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] += 1
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])
                        
            elif next_selection == 'L':
                if piece_pos[1] != B_HEIGHT - 2:
                    selection = test_piece(selection, sub_selection, next_selection)
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 2:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 2 and piece_pos[1] != B_HEIGHT - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1
                    piece_pos[1] += 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] -= 1
                        piece_pos[1] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != 0 and piece_pos[1] != 1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[1] -= 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != 0 and piece_pos[1] != 1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1
                    piece_pos[1] -= 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] -= 1
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

        elif sub_selection == '2':
            if next_selection == 'R':
                if piece_pos[1] != -1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != -1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    piece_pos[1] += 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] += 1
                        piece_pos[1] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != -1 and piece_pos[1] != 0 and piece_pos[1] != 1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[1] -= 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != -1 and piece_pos[1] != 0 and piece_pos[1] != 1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] -= 1
                    piece_pos[1] -= 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] += 1
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

            elif next_selection == 'L':
                if piece_pos[1] != -1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != -1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] -= 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != B_HEIGHT - 3:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1
                    piece_pos[1] += 1
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] -= 1
                        piece_pos[1] += 1
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != 0 and piece_pos[1] != -1 and piece_pos[1] != 1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[1] -= 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

                elif piece_pos[1] != 0 and piece_pos[1] != -1 and piece_pos[1] != 1:
                    selection = test_piece(selection, sub_selection, next_selection)
                    piece_pos[0] += 1
                    piece_pos[1] -= 2
                    
                    if compare_w_board(selection) == "DON'T ROTATE":
                        selection = failed_test(selection, sub_selection, next_selection)
                        piece_pos[0] -= 1
                        piece_pos[1] += 2
                        select_piece(selection)
                        update_board(piece_pos[0], piece_pos[1])
                    else:
                        update_board(piece_pos[0], piece_pos[1])

    return selection


    







# Occupy appropriate spots in piece

def select_piece(selection):
    for y in range(0, 4):
        for x in range(0, 4):
            piece[x][y] = 0

    if selection == 1: piece[0][1] = 2; piece[1][1] = 2; piece[2][1] = 2; piece[3][1] = 2

    if selection == 2: piece[2][0] = 2; piece[2][1] = 2; piece[2][2] = 2; piece[2][3] = 2
    
    if selection == 3: piece[0][2] = 2; piece[1][2] = 2; piece[2][2] = 2; piece[3][2] = 2
    
    if selection == 4: piece[1][0] = 2; piece[1][1] = 2; piece[1][2] = 2; piece[1][3] = 2

    if selection == 5: piece[0][0] = 2; piece[0][1] = 2; piece[1][1] = 2; piece[2][1] = 2
    
    if selection == 6: piece[1][0] = 2; piece[2][0] = 2; piece[1][1] = 2; piece[1][2] = 2
    
    if selection == 7: piece[0][1] = 2; piece[1][1] = 2; piece[2][1] = 2; piece[2][2] = 2
    
    if selection == 8: piece[1][0] = 2; piece[1][1] = 2; piece[1][2] = 2; piece[0][2] = 2
    
    if selection == 9: piece[0][1] = 2; piece[1][1] = 2; piece[2][0] = 2; piece[2][1] = 2
    
    if selection == 10: piece[1][0] = 2; piece[1][1] = 2; piece[1][2] = 2; piece[2][2] = 2
    
    if selection == 11: piece[0][1] = 2; piece[1][1] = 2; piece[2][1] = 2; piece[0][2] = 2
    
    if selection == 12: piece[0][0] = 2; piece[1][0] = 2; piece[1][1] = 2; piece[1][2] = 2
    
    if selection == 13: piece[1][0] = 2; piece[2][0] = 2; piece[1][1] = 2; piece[2][1] = 2

    if selection == 14: piece[1][0] = 2; piece[2][0] = 2; piece[1][1] = 2; piece[2][1] = 2

    if selection == 15: piece[1][0] = 2; piece[2][0] = 2; piece[1][1] = 2; piece[2][1] = 2

    if selection == 16: piece[1][0] = 2; piece[2][0] = 2; piece[1][1] = 2; piece[2][1] = 2
    
    if selection == 17: piece[1][0] = 2; piece[2][0] = 2; piece[0][1] = 2; piece[1][1] = 2
    
    if selection == 18: piece[1][0] = 2; piece[1][1] = 2; piece[2][1] = 2; piece[2][2] = 2
    
    if selection == 19: piece[0][2] = 2; piece[1][1] = 2; piece[2][1] = 2; piece[1][2] = 2
    
    if selection == 20: piece[0][0] = 2; piece[0][1] = 2; piece[1][1] = 2; piece[1][2] = 2
    
    if selection == 21: piece[0][1] = 2; piece[1][0] = 2; piece[1][1] = 2; piece[2][1] = 2
    
    if selection == 22: piece[1][0] = 2; piece[1][1] = 2; piece[2][1] = 2; piece[1][2] = 2

    if selection == 23: piece[0][1] = 2; piece[1][1] = 2; piece[2][1] = 2; piece[1][2] = 2
    
    if selection == 24: piece[0][1] = 2; piece[1][0] = 2; piece[1][1] = 2; piece[1][2] = 2
    
    if selection == 25: piece[0][0] = 2; piece[1][0] = 2; piece[1][1] = 2; piece[2][1] = 2
    
    if selection == 26: piece[2][0] = 2; piece[1][1] = 2; piece[2][1] = 2; piece[1][2] = 2
    
    if selection == 27: piece[0][1] = 2; piece[1][1] = 2; piece[1][2] = 2; piece[2][2] = 2
    
    if selection == 28: piece[1][0] = 2; piece[0][1] = 2; piece[1][1] = 2; piece[0][2] = 2









# Occupy appropriate spots in the next pieces

next_piece_help = list(range(0, 4))

for x in range(0, 4):
    next_piece_help[x] = list(range(0, 4))
    for y in range(0, 4):
        next_piece_help[x][y] = 0

def select_next_piece(selection):
    for y in range(0, 4):
        for x in range(0, 4):
            next_piece_help[x][y] = 0

    if selection == 1: next_piece_help[0][1] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2; next_piece_help[3][1] = 2

    if selection == 2: next_piece_help[2][0] = 2; next_piece_help[2][1] = 2; next_piece_help[2][2] = 2; next_piece_help[2][3] = 2
    
    if selection == 3: next_piece_help[0][2] = 2; next_piece_help[1][2] = 2; next_piece_help[2][2] = 2; next_piece_help[3][2] = 2
    
    if selection == 4: next_piece_help[1][0] = 2; next_piece_help[1][1] = 2; next_piece_help[1][2] = 2; next_piece_help[1][3] = 2

    if selection == 5: next_piece_help[0][0] = 2; next_piece_help[0][1] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2
    
    if selection == 6: next_piece_help[1][0] = 2; next_piece_help[2][0] = 2; next_piece_help[1][1] = 2; next_piece_help[1][2] = 2
    
    if selection == 7: next_piece_help[0][1] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2; next_piece_help[2][2] = 2
    
    if selection == 8: next_piece_help[1][0] = 2; next_piece_help[1][1] = 2; next_piece_help[1][2] = 2; next_piece_help[0][2] = 2
    
    if selection == 9: next_piece_help[0][1] = 2; next_piece_help[1][1] = 2; next_piece_help[2][0] = 2; next_piece_help[2][1] = 2
    
    if selection == 10: next_piece_help[1][0] = 2; next_piece_help[1][1] = 2; next_piece_help[1][2] = 2; next_piece_help[2][2] = 2
    
    if selection == 11: next_piece_help[0][1] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2; next_piece_help[0][2] = 2
    
    if selection == 12: next_piece_help[0][0] = 2; next_piece_help[1][0] = 2; next_piece_help[1][1] = 2; next_piece_help[1][2] = 2
    
    if selection == 13: next_piece_help[1][0] = 2; next_piece_help[2][0] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2

    if selection == 14: next_piece_help[1][0] = 2; next_piece_help[2][0] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2

    if selection == 15: next_piece_help[1][0] = 2; next_piece_help[2][0] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2

    if selection == 16: next_piece_help[1][0] = 2; next_piece_help[2][0] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2
    
    if selection == 17: next_piece_help[1][0] = 2; next_piece_help[2][0] = 2; next_piece_help[0][1] = 2; next_piece_help[1][1] = 2
    
    if selection == 18: next_piece_help[1][0] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2; next_piece_help[2][2] = 2
    
    if selection == 19: next_piece_help[0][2] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2; next_piece_help[1][2] = 2
    
    if selection == 20: next_piece_help[0][0] = 2; next_piece_help[0][1] = 2; next_piece_help[1][1] = 2; next_piece_help[1][2] = 2
    
    if selection == 21: next_piece_help[0][1] = 2; next_piece_help[1][0] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2
    
    if selection == 22: next_piece_help[1][0] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2; next_piece_help[1][2] = 2

    if selection == 23: next_piece_help[0][1] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2; next_piece_help[1][2] = 2
    
    if selection == 24: next_piece_help[0][1] = 2; next_piece_help[1][0] = 2; next_piece_help[1][1] = 2; next_piece_help[1][2] = 2
    
    if selection == 25: next_piece_help[0][0] = 2; next_piece_help[1][0] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2
    
    if selection == 26: next_piece_help[2][0] = 2; next_piece_help[1][1] = 2; next_piece_help[2][1] = 2; next_piece_help[1][2] = 2
    
    if selection == 27: next_piece_help[0][1] = 2; next_piece_help[1][1] = 2; next_piece_help[1][2] = 2; next_piece_help[2][2] = 2
    
    if selection == 28: next_piece_help[1][0] = 2; next_piece_help[0][1] = 2; next_piece_help[1][1] = 2; next_piece_help[0][2] = 2

second_piece_help = list(range(0, 4))

for x in range(0, 4):
    second_piece_help[x] = list(range(0, 4))
    for y in range(0, 4):
        second_piece_help[x][y] = 0

def select_second_piece(selection):
    for y in range(0, 4):
        for x in range(0, 4):
            second_piece_help[x][y] = 0

    if selection == 1: second_piece_help[0][1] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2; second_piece_help[3][1] = 2

    if selection == 2: second_piece_help[2][0] = 2; second_piece_help[2][1] = 2; second_piece_help[2][2] = 2; second_piece_help[2][3] = 2
    
    if selection == 3: second_piece_help[0][2] = 2; second_piece_help[1][2] = 2; second_piece_help[2][2] = 2; second_piece_help[3][2] = 2
    
    if selection == 4: second_piece_help[1][0] = 2; second_piece_help[1][1] = 2; second_piece_help[1][2] = 2; second_piece_help[1][3] = 2

    if selection == 5: second_piece_help[0][0] = 2; second_piece_help[0][1] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2
    
    if selection == 6: second_piece_help[1][0] = 2; second_piece_help[2][0] = 2; second_piece_help[1][1] = 2; second_piece_help[1][2] = 2
    
    if selection == 7: second_piece_help[0][1] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2; second_piece_help[2][2] = 2
    
    if selection == 8: second_piece_help[1][0] = 2; second_piece_help[1][1] = 2; second_piece_help[1][2] = 2; second_piece_help[0][2] = 2
    
    if selection == 9: second_piece_help[0][1] = 2; second_piece_help[1][1] = 2; second_piece_help[2][0] = 2; second_piece_help[2][1] = 2
    
    if selection == 10: second_piece_help[1][0] = 2; second_piece_help[1][1] = 2; second_piece_help[1][2] = 2; second_piece_help[2][2] = 2
    
    if selection == 11: second_piece_help[0][1] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2; second_piece_help[0][2] = 2
    
    if selection == 12: second_piece_help[0][0] = 2; second_piece_help[1][0] = 2; second_piece_help[1][1] = 2; second_piece_help[1][2] = 2
    
    if selection == 13: second_piece_help[1][0] = 2; second_piece_help[2][0] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2

    if selection == 14: second_piece_help[1][0] = 2; second_piece_help[2][0] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2

    if selection == 15: second_piece_help[1][0] = 2; second_piece_help[2][0] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2

    if selection == 16: second_piece_help[1][0] = 2; second_piece_help[2][0] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2
    
    if selection == 17: second_piece_help[1][0] = 2; second_piece_help[2][0] = 2; second_piece_help[0][1] = 2; second_piece_help[1][1] = 2
    
    if selection == 18: second_piece_help[1][0] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2; second_piece_help[2][2] = 2
    
    if selection == 19: second_piece_help[0][2] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2; second_piece_help[1][2] = 2
    
    if selection == 20: second_piece_help[0][0] = 2; second_piece_help[0][1] = 2; second_piece_help[1][1] = 2; second_piece_help[1][2] = 2
    
    if selection == 21: second_piece_help[0][1] = 2; second_piece_help[1][0] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2
    
    if selection == 22: second_piece_help[1][0] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2; second_piece_help[1][2] = 2

    if selection == 23: second_piece_help[0][1] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2; second_piece_help[1][2] = 2
    
    if selection == 24: second_piece_help[0][1] = 2; second_piece_help[1][0] = 2; second_piece_help[1][1] = 2; second_piece_help[1][2] = 2
    
    if selection == 25: second_piece_help[0][0] = 2; second_piece_help[1][0] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2
    
    if selection == 26: second_piece_help[2][0] = 2; second_piece_help[1][1] = 2; second_piece_help[2][1] = 2; second_piece_help[1][2] = 2
    
    if selection == 27: second_piece_help[0][1] = 2; second_piece_help[1][1] = 2; second_piece_help[1][2] = 2; second_piece_help[2][2] = 2
    
    if selection == 28: second_piece_help[1][0] = 2; second_piece_help[0][1] = 2; second_piece_help[1][1] = 2; second_piece_help[0][2] = 2

third_piece_help = list(range(0, 4))

for x in range(0, 4):
    third_piece_help[x] = list(range(0, 4))
    for y in range(0, 4):
        third_piece_help[x][y] = 0

def select_third_piece(selection):
    for y in range(0, 4):
        for x in range(0, 4):
            third_piece_help[x][y] = 0

    if selection == 1: third_piece_help[0][1] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2; third_piece_help[3][1] = 2

    if selection == 2: third_piece_help[2][0] = 2; third_piece_help[2][1] = 2; third_piece_help[2][2] = 2; third_piece_help[2][3] = 2
    
    if selection == 3: third_piece_help[0][2] = 2; third_piece_help[1][2] = 2; third_piece_help[2][2] = 2; third_piece_help[3][2] = 2
    
    if selection == 4: third_piece_help[1][0] = 2; third_piece_help[1][1] = 2; third_piece_help[1][2] = 2; third_piece_help[1][3] = 2

    if selection == 5: third_piece_help[0][0] = 2; third_piece_help[0][1] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2
    
    if selection == 6: third_piece_help[1][0] = 2; third_piece_help[2][0] = 2; third_piece_help[1][1] = 2; third_piece_help[1][2] = 2
    
    if selection == 7: third_piece_help[0][1] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2; third_piece_help[2][2] = 2
    
    if selection == 8: third_piece_help[1][0] = 2; third_piece_help[1][1] = 2; third_piece_help[1][2] = 2; third_piece_help[0][2] = 2
    
    if selection == 9: third_piece_help[0][1] = 2; third_piece_help[1][1] = 2; third_piece_help[2][0] = 2; third_piece_help[2][1] = 2
    
    if selection == 10: third_piece_help[1][0] = 2; third_piece_help[1][1] = 2; third_piece_help[1][2] = 2; third_piece_help[2][2] = 2
    
    if selection == 11: third_piece_help[0][1] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2; third_piece_help[0][2] = 2
    
    if selection == 12: third_piece_help[0][0] = 2; third_piece_help[1][0] = 2; third_piece_help[1][1] = 2; third_piece_help[1][2] = 2
    
    if selection == 13: third_piece_help[1][0] = 2; third_piece_help[2][0] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2

    if selection == 14: third_piece_help[1][0] = 2; third_piece_help[2][0] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2

    if selection == 15: third_piece_help[1][0] = 2; third_piece_help[2][0] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2

    if selection == 16: third_piece_help[1][0] = 2; third_piece_help[2][0] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2
    
    if selection == 17: third_piece_help[1][0] = 2; third_piece_help[2][0] = 2; third_piece_help[0][1] = 2; third_piece_help[1][1] = 2
    
    if selection == 18: third_piece_help[1][0] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2; third_piece_help[2][2] = 2
    
    if selection == 19: third_piece_help[0][2] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2; third_piece_help[1][2] = 2
    
    if selection == 20: third_piece_help[0][0] = 2; third_piece_help[0][1] = 2; third_piece_help[1][1] = 2; third_piece_help[1][2] = 2
    
    if selection == 21: third_piece_help[0][1] = 2; third_piece_help[1][0] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2
    
    if selection == 22: third_piece_help[1][0] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2; third_piece_help[1][2] = 2

    if selection == 23: third_piece_help[0][1] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2; third_piece_help[1][2] = 2
    
    if selection == 24: third_piece_help[0][1] = 2; third_piece_help[1][0] = 2; third_piece_help[1][1] = 2; third_piece_help[1][2] = 2
    
    if selection == 25: third_piece_help[0][0] = 2; third_piece_help[1][0] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2
    
    if selection == 26: third_piece_help[2][0] = 2; third_piece_help[1][1] = 2; third_piece_help[2][1] = 2; third_piece_help[1][2] = 2
    
    if selection == 27: third_piece_help[0][1] = 2; third_piece_help[1][1] = 2; third_piece_help[1][2] = 2; third_piece_help[2][2] = 2
    
    if selection == 28: third_piece_help[1][0] = 2; third_piece_help[0][1] = 2; third_piece_help[1][1] = 2; third_piece_help[0][2] = 2

hold_piece_help = list(range(0, 4))

for x in range(0, 4):
    hold_piece_help[x] = list(range(0, 4))
    for y in range(0, 4):
        hold_piece_help[x][y] = 0

def select_hold_piece(selection):
    for y in range(0, 4):
        for x in range(0, 4):
            hold_piece_help[x][y] = 0

    if selection == 1: hold_piece_help[0][1] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2; hold_piece_help[3][1] = 2

    if selection == 2: hold_piece_help[2][0] = 2; hold_piece_help[2][1] = 2; hold_piece_help[2][2] = 2; hold_piece_help[2][3] = 2
    
    if selection == 3: hold_piece_help[0][2] = 2; hold_piece_help[1][2] = 2; hold_piece_help[2][2] = 2; hold_piece_help[3][2] = 2
    
    if selection == 4: hold_piece_help[1][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[1][2] = 2; hold_piece_help[1][3] = 2

    if selection == 5: hold_piece_help[0][0] = 2; hold_piece_help[0][1] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2
    
    if selection == 6: hold_piece_help[1][0] = 2; hold_piece_help[2][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[1][2] = 2
    
    if selection == 7: hold_piece_help[0][1] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2; hold_piece_help[2][2] = 2
    
    if selection == 8: hold_piece_help[1][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[1][2] = 2; hold_piece_help[0][2] = 2
    
    if selection == 9: hold_piece_help[0][1] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][0] = 2; hold_piece_help[2][1] = 2
    
    if selection == 10: hold_piece_help[1][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[1][2] = 2; hold_piece_help[2][2] = 2
    
    if selection == 11: hold_piece_help[0][1] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2; hold_piece_help[0][2] = 2
    
    if selection == 12: hold_piece_help[0][0] = 2; hold_piece_help[1][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[1][2] = 2
    
    if selection == 13: hold_piece_help[1][0] = 2; hold_piece_help[2][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2

    if selection == 14: hold_piece_help[1][0] = 2; hold_piece_help[2][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2

    if selection == 15: hold_piece_help[1][0] = 2; hold_piece_help[2][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2

    if selection == 16: hold_piece_help[1][0] = 2; hold_piece_help[2][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2
    
    if selection == 17: hold_piece_help[1][0] = 2; hold_piece_help[2][0] = 2; hold_piece_help[0][1] = 2; hold_piece_help[1][1] = 2
    
    if selection == 18: hold_piece_help[1][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2; hold_piece_help[2][2] = 2
    
    if selection == 19: hold_piece_help[0][2] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2; hold_piece_help[1][2] = 2
    
    if selection == 20: hold_piece_help[0][0] = 2; hold_piece_help[0][1] = 2; hold_piece_help[1][1] = 2; hold_piece_help[1][2] = 2
    
    if selection == 21: hold_piece_help[0][1] = 2; hold_piece_help[1][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2
    
    if selection == 22: hold_piece_help[1][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2; hold_piece_help[1][2] = 2

    if selection == 23: hold_piece_help[0][1] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2; hold_piece_help[1][2] = 2
    
    if selection == 24: hold_piece_help[0][1] = 2; hold_piece_help[1][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[1][2] = 2
    
    if selection == 25: hold_piece_help[0][0] = 2; hold_piece_help[1][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2
    
    if selection == 26: hold_piece_help[2][0] = 2; hold_piece_help[1][1] = 2; hold_piece_help[2][1] = 2; hold_piece_help[1][2] = 2
    
    if selection == 27: hold_piece_help[0][1] = 2; hold_piece_help[1][1] = 2; hold_piece_help[1][2] = 2; hold_piece_help[2][2] = 2
    
    if selection == 28: hold_piece_help[1][0] = 2; hold_piece_help[0][1] = 2; hold_piece_help[1][1] = 2; hold_piece_help[0][2] = 2


def print_hold():

    print(' ')
    
    for y in range(0, 4):
        for x in range(0, 4):
            if x != 3:
                print(hold_piece_help[x][y], end=' ')
            else:
                print(hold_piece_help[x][y])

    print(' ')






# Lock the piece into place

def lock_board(able_to_hold):
    able_to_hold = True
    
    for y in range(0, B_HEIGHT):
        for x in range(0, B_WIDTH):
            if board[x][y] == 2:
                stacked_piece.append([x, y])

                

                if selection == 1 or selection == 2 or selection == 3 or selection == 5:
                    piece_colors.append(TURQUOISE)
                elif selection == 5 or selection == 6 or selection == 7 or selection == 8:
                    piece_colors.append(BLUE)
                elif selection == 9 or selection == 10 or selection == 11 or selection == 12:
                    piece_colors.append(ORANGE)
                elif selection == 13 or selection == 14 or selection == 15 or selection == 16:
                    piece_colors.append(YELLOW)
                elif selection == 17 or selection == 18 or selection == 19 or selection == 20:
                    piece_colors.append(GREEN)
                elif selection == 21 or selection == 22 or selection == 23 or selection == 24:
                    piece_colors.append(PURPLE)
                elif selection == 25 or selection == 26 or selection == 27 or selection == 28:
                    piece_colors.append(RED)

    update_board(piece_pos[0], piece_pos[1])

    return able_to_hold










def change_the_background(r, g, b, BACKGROUND, dr, dg, db):

    r = BACKGROUND[0]
    g = BACKGROUND[1]
    b = BACKGROUND[2]
    
    r += dr
    g += dg
    b += db

    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0

    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255

    if g == 206:
        g = 215

    BACKGROUND = (int(r), int(g), int(b))

    if BACKGROUND == (255,206,0):
        g = 215
        dg = 0

    if BACKGROUND == (191,23,0):
        r = 192
        dr = 0
        
        g = 0
        dg = 0

    if BACKGROUND == (134,145,174):
        r = 135
        dr = 0

    if BACKGROUND == (135,205,246):
        g = 206
        dg = 0
        
        b = 250
        db = 0

    BACKGROUND = (int(r), int(g), int(b))

    return dr, dg, db, BACKGROUND







high_scores = []
high_score_names = []
high_scores_font = []
high_score_names_font = []
high_scores_fontRect = []
high_score_names_fontRect = []
num_of_scores = 0


# Get the highscores

def get_highscores(num_of_scores):
    file_path = 'highscores/highscores.txt'
    file = open(file_path, "r")


    x = 0
    for line in file:
        if x % 2 == 0:
            high_score_names.append(line)
        else:
            high_scores.append(line)
            num_of_scores = num_of_scores + 1
        x += 1

    file.close()

    if num_of_scores > 5:
        num_of_scores = 5

    # Remove the newline characters from the strings

    for x in range(0, len(high_scores)):
        if high_scores[x][len(high_scores[x]) - 1] == '\n':
            high_scores[x] = high_scores[x][:len(high_scores[x]) - 1]

    for x in range(0, len(high_score_names)):
        if high_score_names[x][len(high_score_names[x]) - 1] == '\n':
            high_score_names[x] = high_score_names[x][:len(high_score_names[x]) - 1]

    # Arrange the order of scores

    start = len(high_scores) - 1
    temp = ''

    """for x in range(0, len(high_scores) - 1):
        while start > 0:
            if int(high_scores[start]) > int(high_scores[start - 1]):
                # Swap the scores

                temp = high_scores[start]
                high_scores[start] = high_scores[start - 1]
                high_scores[start - 1] = temp

                # Swap the names

                temp = high_score_names[start]
                high_score_names[start] = high_score_names[start - 1]
                high_score_names[start - 1] = temp
            
            start -= 1"""

    
    # Get the font for each name and score
    
    for x in range(0, num_of_scores):
        high_scores_font.append(font.render(high_scores[x], True, FIREBRICK, DODGER_BLUE))
        high_score_names_font.append(font.render(high_score_names[x], True, FIREBRICK, DODGER_BLUE))

    # Render the font        

    for x in range(0, num_of_scores):
        high_scores_fontRect.append(high_scores_font[x].get_rect())
        high_score_names_fontRect.append(high_score_names_font[x].get_rect())

    # Position the text

    for x in range(0, num_of_scores):
        high_scores_fontRect[x].centerx = WIDTH - (L_BORDER / 2) - TWENTY + FIVE
        high_score_names_fontRect[x].centerx = WIDTH - (L_BORDER / 2) - TWENTY + FIVE

        high_scores_fontRect[x].centery = TOP_BORDER + SEVENTY + TWENTY + (x * SEVENTY)
        high_score_names_fontRect[x].centery = TOP_BORDER + SEVENTY + (x * SEVENTY)

    return num_of_scores
        








# Determine what the next pieces will be

"""def next_pieces(piece_in_holding, second_piece, third_piece):
    piece_in_holding = second_piece
    second_piece = third_piece
    third_piece = random.choice(select_list)
'
    return next_piece, second_piece, third_piece"""







# Game variables

intro_over = False
intro_timer = 0
d_it = 1
intro_color = (0,0,0)
d_color = 1
r_i = 0
g_i = 0
b_i = 0
initials = ''
ending_intro = False

my_name_dx = 10

key_press = False

timer = 0
dt = 1
INTERVAL = 50
temp_interval = INTERVAL
count = 1
pdy = 1

stacked_piece = []
piece_colors = []
paused = False
pause_timer = 0
d_pt = 0
resume = False

ask_to_quit = False
quitting_timer = 0
d_qt = 0
going_to_quit = False
exited_game = False

music_choice = music_on

mouse_x, mouse_y = (0, 0)

not_playing = False
has_started = False
sound_timer = 0

pygame.mixer.music.play(-1, 0.0)

already_held = False

next_level_timer = 0
next_level = False

orig_goal_number = goal_number

speed_increase_interval = 2

lines_cleared = 0

dr = 0
dg = 0
db = 0

next_color = (255,215,0)

r = 0
g = 0
b = 0

number_times_removed = 0

change_color = True
number_check = 2
number_changed = False

temp_piece = 0
able_to_hold = True

game_over_true = False
game_over_timer = 0
d_go_t = 0
started = False

file_temp = ''





# Determines where piece will be located on the board

piece_pos = [3, -1]
update_board(piece_pos[0], piece_pos[1])

select_list = [1,5,9,13,17,21,25]

piece_in_holding = random.choice(select_list)
second_piece = random.choice(select_list)
third_piece = random.choice(select_list)
hold_piece = 0

select_next_piece(piece_in_holding)
select_second_piece(second_piece)
select_third_piece(third_piece)
select_hold_piece(hold_piece)

selection = random.choice(select_list)
select_piece(selection)

pygame.key.set_repeat(50, 50)
FRAME_RATE = 1000.0 / 60


test_font = pygame.font.Font(pygame.font.match_font(('impact')), 200)
test_font2 = pygame.font.Font(pygame.font.match_font(('impact')), 20)
enter_font = pygame.font.Font(pygame.font.match_font(('impact')), 40)

intro_text = test_font.render('TETRIS', True, intro_color, BLACK)
my_name = test_font2.render('by David Campbell', True, WHITE, BLACK)
enter_name = enter_font.render('ENTER INITIALS', True, WHITE, BLACK)
initial_area = enter_font.render(initials, True, FIREBRICK, BLACK)

intro_textRect = intro_text.get_rect()
my_nameRect = my_name.get_rect()
enter_nameRect = enter_name.get_rect()
initial_areaRect = initial_area.get_rect()

intro_textRect.centerx = WIDTH / 2
intro_textRect.centery = HEIGHT / 2

my_nameRect.centerx = -90
my_nameRect.centery = intro_textRect.centery + SEVENTY + TWENTY

enter_nameRect.centerx = WIDTH / 2
enter_nameRect.centery = HEIGHT + 500

name_area = pygame.Rect(0,0,200,50)

name_area.centerx = -200
name_area.centery = -200

initial_areaRect.centerx = WIDTH / 2 - TWENTY
initial_areaRect.centery = HEIGHT / 2 - FORTY - TEN


# Get the highscores and print them on the screen

num_of_scores = get_highscores(num_of_scores)

#print high_scores
#print high_score_names


while 1:
    
    # Calculate delay

    starttime = pygame.time.get_ticks()


    #print intro_timer
    # Intro

    if intro_over == False:
        surface.fill(BLACK)

        intro_timer += d_it

        r_i += d_color
        g_i += d_color
        b_i += d_color

        intro_color = (r_i, g_i, b_i)

        if r_i >= 255 - d_color:
            d_color = 0
            intro_color = (255,255,255)

        intro_text = test_font.render('TETRIS', True, intro_color, BLACK)

    if intro_timer > 200 and intro_timer < 350:
        my_nameRect.centerx += my_name_dx

    if intro_timer == 250:
        my_name_dx = 8

    if intro_timer == 252:
        my_name_dx = 6

    if intro_timer == 254:
        my_name_dx = 4

    if intro_timer == 256:
        my_name_dx = 2

    if intro_timer == 258:
        my_name_dx = -2

    if intro_timer == 260:
        my_name_dx = -4

    if intro_timer == 262:
        my_name_dx = -6

    if intro_timer == 264:
        my_name_dx = -8

    if intro_timer == 266:
        my_name_dx = -10

    if intro_timer > 266 and my_nameRect.centerx == WIDTH / 2:
        my_name_dx = 0


    if intro_timer > 350:
        my_name_dx = -10

    if enter_nameRect.centery == 380:
        my_name_dx = 0

    if intro_timer > 350 and ending_intro == False:
        d_it = 0
        
        intro_textRect.centery += my_name_dx
        my_nameRect.centery += my_name_dx
        enter_nameRect.centery += my_name_dx

        name_area.centerx = enter_nameRect.centerx
        name_area.centery = enter_nameRect.centery - SEVENTY - TWENTY

        initial_area = enter_font.render(initials, True, FIREBRICK, BLACK)

    if ending_intro == True:
        d_it = 1
        my_name_dx = 10

        if intro_timer > 354:
            my_name_dx = 8

        if intro_timer > 356:
            my_name_dx = 6

        if intro_timer > 358:
            my_name_dx = 4

        if intro_timer > 360:
            my_name_dx = 2

        if intro_timer > 362:
            my_name_dx = -2

        if intro_timer > 364:
            my_name_dx = -4

        if intro_timer > 366:
            my_name_dx = -6

        if intro_timer > 368:
            my_name_dx = -8

        if intro_timer > 370:
            my_name_dx = -10

        initial_areaRect.centery += my_name_dx
        enter_nameRect.centery += my_name_dx
        name_area.centery += my_name_dx

        initial_area = enter_font.render(initials, True, FIREBRICK, BLACK)
        enter_name = enter_font.render('ENTER INITIALS', True, WHITE, BLACK)

        if intro_timer == 475:
            intro_over = True





    
    
    # Loop variables

    number_of_tiles = 0

    if intro_over == True:
        timer += dt
    
    if paused == True or next_level == True:
        pdy = 0
    else:
        pdy = 1


        





    # Pause menu

    if paused == True:
        if pause_timer < 59:
            d_pt = 1
        
        pause_timer += d_pt

        if yes_answerRect.centerx < 0:
            if pause_timer < 25:
                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 16
                    pause_back_vertices[x][0] += 16

                tRect.centerx += 16
                eRect.centerx += 16
                t2Rect.centerx += 16
                areRect.centerx += 16
                iRect.centerx += 16
                sRect.centerx += 16

            if pause_timer >= 25 and pause_timer < 27:
                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 14
                    pause_back_vertices[x][0] += 14

                tRect.centerx += 14
                eRect.centerx += 14
                t2Rect.centerx += 14
                areRect.centerx += 14
                iRect.centerx += 14
                sRect.centerx += 14

            if pause_timer >= 27 and pause_timer < 29:
                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 12
                    pause_back_vertices[x][0] += 12
                    
                tRect.centerx += 12
                eRect.centerx += 12
                t2Rect.centerx += 12
                areRect.centerx += 12
                iRect.centerx += 12
                sRect.centerx += 12

            if pause_timer >= 29 and pause_timer < 31:
                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 10
                    pause_back_vertices[x][0] += 10

                tRect.centerx += 10
                eRect.centerx += 10
                t2Rect.centerx += 10
                areRect.centerx += 10
                iRect.centerx += 10
                sRect.centerx += 10

            if pause_timer >= 31 and pause_timer < 33:
                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 8
                    pause_back_vertices[x][0] += 8

                tRect.centerx += 8
                eRect.centerx += 8
                t2Rect.centerx += 8
                areRect.centerx += 8
                iRect.centerx += 8
                sRect.centerx += 8

            if pause_timer >= 33 and pause_timer < 35:
                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 6
                    pause_back_vertices[x][0] += 6

                tRect.centerx += 6
                eRect.centerx += 6
                t2Rect.centerx += 6
                areRect.centerx += 6
                iRect.centerx += 6
                sRect.centerx += 6

            if pause_timer >= 35 and pause_timer < 37:
                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 4
                    pause_back_vertices[x][0] += 4

                tRect.centerx += 4
                eRect.centerx += 4
                t2Rect.centerx += 4
                areRect.centerx += 4
                iRect.centerx += 4
                sRect.centerx += 4

            if pause_timer >= 37 and pause_timer < 39:
                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 2
                    pause_back_vertices[x][0] += 2

                tRect.centerx += 2
                eRect.centerx += 2
                t2Rect.centerx += 2
                areRect.centerx += 2
                iRect.centerx += 2
                sRect.centerx += 2

            if pause_timer >= 39 and pause_timer < 41:
                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] -= 2
                    pause_back_vertices[x][0] -= 2

                tRect.centerx -= 2
                eRect.centerx -= 2
                t2Rect.centerx -= 2
                areRect.centerx -= 2
                iRect.centerx -= 2
                sRect.centerx -= 2

            if pause_timer >= 41 and pause_timer < 43:
                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] -= 4
                    pause_back_vertices[x][0] -= 4

                tRect.centerx -= 4
                eRect.centerx -= 4
                t2Rect.centerx -= 4
                areRect.centerx -= 4
                iRect.centerx -= 4
                sRect.centerx -= 4


            

        if pause_timer < 30:
            resume_playRect.centerx += 16
            quit_playRect.centerx += 16
            
            for x in range(0, 4):
                resume_back_vertices[x][0] += 16
                quit_back_vertices[x][0] += 16

        if pause_timer >= 30 and pause_timer < 32:
            resume_playRect.centerx += 14
            quit_playRect.centerx += 14
            
            for x in range(0, 4):
                resume_back_vertices[x][0] += 14
                quit_back_vertices[x][0] += 14

        if pause_timer >= 32 and pause_timer < 34:
            resume_playRect.centerx += 12
            quit_playRect.centerx += 12
            
            for x in range(0, 4):
                resume_back_vertices[x][0] += 12
                quit_back_vertices[x][0] += 12

        if pause_timer >= 34 and pause_timer < 36:
            resume_playRect.centerx += 10
            quit_playRect.centerx += 10
            
            for x in range(0, 4):
                resume_back_vertices[x][0] += 10
                quit_back_vertices[x][0] += 10

        if pause_timer >= 36 and pause_timer < 38:
            resume_playRect.centerx += 8
            quit_playRect.centerx += 8
            
            for x in range(0, 4):
                resume_back_vertices[x][0] += 8
                quit_back_vertices[x][0] += 8

        if pause_timer >= 38 and pause_timer < 40:
            resume_playRect.centerx += 6
            quit_playRect.centerx += 6
            
            for x in range(0, 4):
                resume_back_vertices[x][0] += 6
                quit_back_vertices[x][0] += 6

        if pause_timer >= 40 and pause_timer < 42:
            resume_playRect.centerx += 4
            quit_playRect.centerx += 4
            
            for x in range(0, 4):
                resume_back_vertices[x][0] += 4
                quit_back_vertices[x][0] += 4

        if pause_timer >= 42 and pause_timer < 44:
            resume_playRect.centerx += 2
            quit_playRect.centerx += 2
            
            for x in range(0, 4):
                resume_back_vertices[x][0] += 2
                quit_back_vertices[x][0] += 2

        if pause_timer >= 44 and pause_timer < 46:
            resume_playRect.centerx -= 2
            quit_playRect.centerx -= 2
            
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 2
                quit_back_vertices[x][0] -= 2

        if pause_timer >= 46 and pause_timer < 48:
            resume_playRect.centerx -= 4
            quit_playRect.centerx -= 4
            
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 4
                quit_back_vertices[x][0] -= 4

        if pause_timer >= 50 and pause_timer < 52:
            resume_playRect.centerx -= 6
            quit_playRect.centerx -= 6
            
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 6
                quit_back_vertices[x][0] -= 6

        if pause_timer >= 52 and pause_timer < 54:
            resume_playRect.centerx -= 8
            quit_playRect.centerx -= 8
            
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 8
                quit_back_vertices[x][0] -= 8

        if pause_timer >= 54 and pause_timer < 56:
            resume_playRect.centerx -= 10
            quit_playRect.centerx -= 10
            
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 10
                quit_back_vertices[x][0] -= 10

        if pause_timer >= 56 and pause_timer < 58:
            resume_playRect.centerx -= 12
            quit_playRect.centerx -= 12
            
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 12
                quit_back_vertices[x][0] -= 12

        if pause_timer >= 58 and pause_timer < 59:
            resume_playRect.centerx -= 14
            quit_playRect.centerx -= 14
            
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 14
                quit_back_vertices[x][0] -= 14

        if pause_timer == 59:
            d_pt = 0

        if resume == True:
            d_pt = 1

            if pause_timer < 59:                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] -= 10
                    pause_back_vertices[x][0] -= 10

                tRect.centerx -= 10
                eRect.centerx -= 10
                t2Rect.centerx -= 10
                areRect.centerx -= 10
                iRect.centerx -= 10
                sRect.centerx -= 10

            if pause_timer >= 59 and pause_timer < 61:                
                for x in range(0, 4):
                    pause_layer_vertices[x][0] -= 8
                    pause_back_vertices[x][0] -= 8

                tRect.centerx -= 8
                eRect.centerx -= 8
                t2Rect.centerx -= 8
                areRect.centerx -= 8
                iRect.centerx -= 8
                sRect.centerx -= 8

            if pause_timer >= 61 and pause_timer < 63:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] -= 6
                    pause_back_vertices[x][0] -= 6

                tRect.centerx -= 6
                eRect.centerx -= 6
                t2Rect.centerx -= 6
                areRect.centerx -= 6
                iRect.centerx -= 6
                sRect.centerx -= 6

            if pause_timer >= 63 and pause_timer < 65:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] -= 4
                    pause_back_vertices[x][0] -= 4

                tRect.centerx -= 4
                eRect.centerx -= 4
                t2Rect.centerx -= 4
                areRect.centerx -= 4
                iRect.centerx -= 4
                sRect.centerx -= 4

            if pause_timer >= 65 and pause_timer < 67:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] -= 2
                    pause_back_vertices[x][0] -= 2

                tRect.centerx -= 2
                eRect.centerx -= 2
                t2Rect.centerx -= 2
                areRect.centerx -= 2
                iRect.centerx -= 2
                sRect.centerx -= 2

            if pause_timer >= 67 and pause_timer < 69:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 2
                    pause_back_vertices[x][0] += 2

                tRect.centerx += 2
                eRect.centerx += 2
                t2Rect.centerx += 2
                areRect.centerx += 2
                iRect.centerx += 2
                sRect.centerx += 2

            if pause_timer >= 69 and pause_timer < 71:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 4
                    pause_back_vertices[x][0] += 4

                tRect.centerx += 4
                eRect.centerx += 4
                t2Rect.centerx += 4
                areRect.centerx += 4
                iRect.centerx += 4
                sRect.centerx += 4

            if pause_timer >= 71 and pause_timer < 73:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 6
                    pause_back_vertices[x][0] += 6

                tRect.centerx += 6
                eRect.centerx += 6
                t2Rect.centerx += 6
                areRect.centerx += 6
                iRect.centerx += 6
                sRect.centerx += 6

            if pause_timer >= 73 and pause_timer < 75:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 8
                    pause_back_vertices[x][0] += 8

                tRect.centerx += 8
                eRect.centerx += 8
                t2Rect.centerx += 8
                areRect.centerx += 8
                iRect.centerx += 8
                sRect.centerx += 8

            if pause_timer >= 75 and pause_timer < 77:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 10
                    pause_back_vertices[x][0] += 10

                tRect.centerx += 10
                eRect.centerx += 10
                t2Rect.centerx += 10
                areRect.centerx += 10
                iRect.centerx += 10
                sRect.centerx += 10

            if pause_timer >= 77 and pause_timer < 79:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 12
                    pause_back_vertices[x][0] += 12

                tRect.centerx += 12
                eRect.centerx += 12
                t2Rect.centerx += 12
                areRect.centerx += 12
                iRect.centerx += 12
                sRect.centerx += 12

            if pause_timer >= 79 and pause_timer < 81:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 14
                    pause_back_vertices[x][0] += 14

                tRect.centerx += 14
                eRect.centerx += 14
                t2Rect.centerx += 14
                areRect.centerx += 14
                iRect.centerx += 14
                sRect.centerx += 14

            if pause_timer >= 81 and pause_timer < 83:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 16
                    pause_back_vertices[x][0] += 16

                tRect.centerx += 16
                eRect.centerx += 16
                t2Rect.centerx += 16
                areRect.centerx += 16
                iRect.centerx += 16
                sRect.centerx += 16

            if pause_timer >= 83 and pause_timer < 85:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 18
                    pause_back_vertices[x][0] += 18

                tRect.centerx += 18
                eRect.centerx += 18
                t2Rect.centerx += 18
                areRect.centerx += 18
                iRect.centerx += 18
                sRect.centerx += 18

            if pause_timer >= 85 and pause_timer < 87:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 20
                    pause_back_vertices[x][0] += 20

                tRect.centerx += 20
                eRect.centerx += 20
                t2Rect.centerx += 20
                areRect.centerx += 20
                iRect.centerx += 20
                sRect.centerx += 20

            if pause_timer >= 87 and pause_timer < 89:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 22
                    pause_back_vertices[x][0] += 22

                tRect.centerx += 22
                eRect.centerx += 22
                t2Rect.centerx += 22
                areRect.centerx += 22
                iRect.centerx += 22
                sRect.centerx += 22

            if pause_timer >= 89 and pause_timer < 91:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 24
                    pause_back_vertices[x][0] += 24

                tRect.centerx += 24
                eRect.centerx += 24
                t2Rect.centerx += 24
                areRect.centerx += 24
                iRect.centerx += 24
                sRect.centerx += 24

            if pause_timer >= 91 and pause_timer < 93:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 26
                    pause_back_vertices[x][0] += 26

                tRect.centerx += 26
                eRect.centerx += 26
                t2Rect.centerx += 26
                areRect.centerx += 26
                iRect.centerx += 26
                sRect.centerx += 26

            if pause_timer >= 93:
                for x in range(0, 4):
                    pause_layer_vertices[x][0] += 28
                    pause_back_vertices[x][0] += 28

                tRect.centerx += 28
                eRect.centerx += 28
                t2Rect.centerx += 28
                areRect.centerx += 28
                iRect.centerx += 28
                sRect.centerx += 28





                
            if pause_timer < 65:
                resume_playRect.centerx -= 10
                quit_playRect.centerx -= 10
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] -= 10
                    quit_back_vertices[x][0] -= 10

            if pause_timer >= 65 and pause_timer < 67:
                resume_playRect.centerx -= 8
                quit_playRect.centerx -= 8
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] -= 8
                    quit_back_vertices[x][0] -= 8

            if pause_timer >= 67 and pause_timer < 69:
                resume_playRect.centerx -= 6
                quit_playRect.centerx -= 6
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] -= 6
                    quit_back_vertices[x][0] -= 6

            if pause_timer >= 69 and pause_timer < 71:
                resume_playRect.centerx -= 4
                quit_playRect.centerx -= 4
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] -= 4
                    quit_back_vertices[x][0] -= 4

            if pause_timer >= 71 and pause_timer < 73:
                resume_playRect.centerx -= 2
                quit_playRect.centerx -= 2
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] -= 2
                    quit_back_vertices[x][0] -= 2

            if pause_timer >= 73 and pause_timer < 75:
                resume_playRect.centerx += 2
                quit_playRect.centerx += 2
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 2
                    quit_back_vertices[x][0] += 2

            if pause_timer >= 77 and pause_timer < 79:
                resume_playRect.centerx += 4
                quit_playRect.centerx += 4
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 4
                    quit_back_vertices[x][0] += 4

            if pause_timer >= 79 and pause_timer < 81:
                resume_playRect.centerx += 6
                quit_playRect.centerx += 6
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 6
                    quit_back_vertices[x][0] += 6

            if pause_timer >= 81 and pause_timer < 83:
                resume_playRect.centerx += 8
                quit_playRect.centerx += 8
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 8
                    quit_back_vertices[x][0] += 8

            if pause_timer >= 83 and pause_timer < 85:
                resume_playRect.centerx += 10
                quit_playRect.centerx += 10
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 10
                    quit_back_vertices[x][0] += 10

            if pause_timer >= 85 and pause_timer < 87:
                resume_playRect.centerx += 12
                quit_playRect.centerx += 12
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 12
                    quit_back_vertices[x][0] += 12

            if pause_timer >= 87 and pause_timer < 89:
                resume_playRect.centerx += 14
                quit_playRect.centerx += 14
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 14
                    quit_back_vertices[x][0] += 14

            if pause_timer >= 89 and pause_timer < 91:
                resume_playRect.centerx += 16
                quit_playRect.centerx += 16
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 16
                    quit_back_vertices[x][0] += 16

            if pause_timer >= 91 and pause_timer < 93:
                resume_playRect.centerx += 18
                quit_playRect.centerx += 18
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 18
                    quit_back_vertices[x][0] += 18

            if pause_timer >= 93 and pause_timer < 95:
                resume_playRect.centerx += 20
                quit_playRect.centerx += 20
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 20
                    quit_back_vertices[x][0] += 20

            if pause_timer >= 95 and pause_timer < 97:
                resume_playRect.centerx += 22
                quit_playRect.centerx += 22
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 22
                    quit_back_vertices[x][0] += 22

            if pause_timer >= 97 and pause_timer < 99:
                resume_playRect.centerx += 24
                quit_playRect.centerx += 24
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 24
                    quit_back_vertices[x][0] += 24

            if pause_timer >= 99 and pause_timer < 101:
                resume_playRect.centerx += 26
                quit_playRect.centerx += 26
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 26
                    quit_back_vertices[x][0] += 26

            if pause_timer >= 101:
                resume_playRect.centerx += 28
                quit_playRect.centerx += 28
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] += 28
                    quit_back_vertices[x][0] += 28

            if pause_timer == 127:
                resume_playRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY - SEVENTY
                quit_playRect.centerx = resume_playRect.centerx
                
                
                resume_back_vertices = [[R_BORDER + FORTY + TWENTY - (SEVENTY * FIVE) - SEVENTY, (HEIGHT / 2) - SEVENTY],[WIDTH - R_BORDER - SEVENTY - SEVENTY - TWENTY - (SEVENTY * FIVE) - SEVENTY, (HEIGHT / 2) - SEVENTY], \
                        [WIDTH - R_BORDER - SEVENTY - SEVENTY - TWENTY - (SEVENTY * FIVE) - SEVENTY, HEIGHT / 2 + TWENTY - SEVENTY],[R_BORDER + FORTY + TWENTY + FIVE - (SEVENTY * FIVE) - SEVENTY, HEIGHT / 2 + TWENTY - SEVENTY]]
                
                quit_back_vertices = [[resume_back_vertices[3][0], resume_back_vertices[3][1] + TWENTY],[resume_back_vertices[2][0], resume_back_vertices[2][1] + TWENTY], \
                      [resume_back_vertices[2][0],resume_back_vertices[2][1] + FORTY],[resume_back_vertices[0][0], resume_back_vertices[3][1] + FORTY]]
                
                pause_back_vertices = [[L_BORDER - TEN - (SEVENTY * FIVE) - SEVENTY, TOP_BORDER - TEN],[L_BORDER + (TILE * B_WIDTH) + TEN - (SEVENTY * FIVE) - SEVENTY,TOP_BORDER - TEN], \
                       [L_BORDER + (TILE * B_WIDTH) + TEN - (SEVENTY * FIVE) - SEVENTY, HEIGHT - B_BORDER + TEN],[L_BORDER - TEN - (SEVENTY * FIVE) - SEVENTY, HEIGHT - B_BORDER + TEN]]

                pause_layer_vertices = [[pause_back_vertices[0][0] + TEN, pause_back_vertices[0][1] + TEN + FIVE],[pause_back_vertices[1][0] - TEN, pause_back_vertices[1][1] + TEN], \
                       [pause_back_vertices[2][0] - TEN, pause_back_vertices[2][1] - TEN - FIVE],[pause_back_vertices[3][0] + TEN, pause_back_vertices[3][1] - TEN - FIVE]]

                tRect.centerx = WIDTH / 2  - (SEVENTY * FIVE) - SEVENTY
                eRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
                t2Rect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
                areRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
                iRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
                sRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY

                paused = False
                pause_timer = 0
                resume = False
                not_playing = False
                pygame.mixer.music.set_volume(1.0)






    if ask_to_quit == True:# and going_to_quit == False:

        if quitting_timer < 61 and going_to_quit != True:
            d_qt = 1

        quitting_timer += d_qt

        if quitting_timer >= 0 and quitting_timer < 2:
                resume_playRect.centerx -= 10
                quit_playRect.centerx -= 10
                for_sureRect.centerx -= 10
                yes_answerRect.centerx -= 10
                no_answerRect.centerx -= 10
                data_lostRect.centerx -= 10
                
                for x in range(0, 4):
                    resume_back_vertices[x][0] -= 10
                    quit_back_vertices[x][0] -= 10
                    for_sure_vertices[x][0] -= 10

        if quitting_timer >= 2 and quitting_timer < 4:
            resume_playRect.centerx -= 8
            quit_playRect.centerx -= 8
            for_sureRect.centerx -= 8
            yes_answerRect.centerx -= 8
            no_answerRect.centerx -= 8
            data_lostRect.centerx -= 8
                
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 8
                quit_back_vertices[x][0] -= 8
                for_sure_vertices[x][0] -= 8

        if quitting_timer >= 4 and quitting_timer < 6:
            resume_playRect.centerx -= 6
            quit_playRect.centerx -= 6
            for_sureRect.centerx -= 6
            yes_answerRect.centerx -= 6
            no_answerRect.centerx -= 6
            data_lostRect.centerx -= 6
                
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 6
                quit_back_vertices[x][0] -= 6
                for_sure_vertices[x][0] -= 6

        if quitting_timer >= 6 and quitting_timer < 8:
            resume_playRect.centerx -= 4
            quit_playRect.centerx -= 4
            for_sureRect.centerx -= 4
            yes_answerRect.centerx -= 4
            no_answerRect.centerx -= 4
            data_lostRect.centerx -= 4
                
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 4
                quit_back_vertices[x][0] -= 4
                for_sure_vertices[x][0] -= 4

        if quitting_timer >= 8 and quitting_timer < 10:
            resume_playRect.centerx -= 2
            quit_playRect.centerx -= 2
            for_sureRect.centerx -= 2
            yes_answerRect.centerx -= 2
            no_answerRect.centerx -= 2
            data_lostRect.centerx -= 2
               
            for x in range(0, 4):
                resume_back_vertices[x][0] -= 2
                quit_back_vertices[x][0] -= 2
                for_sure_vertices[x][0] -= 2

        if quitting_timer >= 10 and quitting_timer < 12:
            resume_playRect.centerx += 2
            quit_playRect.centerx += 2
            for_sureRect.centerx += 2
            yes_answerRect.centerx += 2
            no_answerRect.centerx += 2
            data_lostRect.centerx += 2
               
            for x in range(0, 4):
                resume_back_vertices[x][0] += 2
                quit_back_vertices[x][0] += 2
                for_sure_vertices[x][0] += 2

        if quitting_timer >= 12 and quitting_timer < 14:
            resume_playRect.centerx += 4
            quit_playRect.centerx += 4
            for_sureRect.centerx += 4
            yes_answerRect.centerx += 4
            no_answerRect.centerx += 4
            data_lostRect.centerx += 4
                
            for x in range(0, 4):
                resume_back_vertices[x][0] += 4
                quit_back_vertices[x][0] += 4
                for_sure_vertices[x][0] += 4

        if quitting_timer >= 14 and quitting_timer < 16:
            resume_playRect.centerx += 6
            quit_playRect.centerx += 6
            for_sureRect.centerx += 6
            yes_answerRect.centerx += 6
            no_answerRect.centerx += 6
            data_lostRect.centerx += 6
                
            for x in range(0, 4):
                resume_back_vertices[x][0] += 6
                quit_back_vertices[x][0] += 6
                for_sure_vertices[x][0] += 6

        if quitting_timer >= 16 and quitting_timer < 18:
            resume_playRect.centerx += 8
            quit_playRect.centerx += 8
            for_sureRect.centerx += 8
            yes_answerRect.centerx += 8
            no_answerRect.centerx += 8
            data_lostRect.centerx += 8
                
            for x in range(0, 4):
                resume_back_vertices[x][0] += 8
                quit_back_vertices[x][0] += 8
                for_sure_vertices[x][0] += 8

        if quitting_timer >= 18 and quitting_timer < 20:
            resume_playRect.centerx += 10
            quit_playRect.centerx += 10
            for_sureRect.centerx += 10
            yes_answerRect.centerx += 10
            no_answerRect.centerx += 10
            data_lostRect.centerx += 10
                
            for x in range(0, 4):
                resume_back_vertices[x][0] += 10
                quit_back_vertices[x][0] += 10
                for_sure_vertices[x][0] += 10

        if quitting_timer >= 20 and quitting_timer < 22:
            resume_playRect.centerx += 12
            quit_playRect.centerx += 12
            for_sureRect.centerx += 12
            yes_answerRect.centerx += 12
            no_answerRect.centerx += 12
            data_lostRect.centerx += 12
                
            for x in range(0, 4):
                resume_back_vertices[x][0] += 12
                quit_back_vertices[x][0] += 12
                for_sure_vertices[x][0] += 12

        if quitting_timer >= 22 and quitting_timer < 24:
            resume_playRect.centerx += 14
            quit_playRect.centerx += 14
            for_sureRect.centerx += 14
            yes_answerRect.centerx += 14
            no_answerRect.centerx += 14
            data_lostRect.centerx += 14
                
            for x in range(0, 4):
                resume_back_vertices[x][0] += 14
                quit_back_vertices[x][0] += 14
                for_sure_vertices[x][0] += 14

        if quitting_timer >= 24 and quitting_timer < 50:
            resume_playRect.centerx += 16
            quit_playRect.centerx += 16
            for_sureRect.centerx += 16
            yes_answerRect.centerx += 16
            no_answerRect.centerx += 16
            data_lostRect.centerx += 16
                
            for x in range(0, 4):
                resume_back_vertices[x][0] += 16
                quit_back_vertices[x][0] += 16
                for_sure_vertices[x][0] += 16

        if quitting_timer >= 50 and quitting_timer < 52:
            #d_qt = 0
            for_sureRect.centerx += 14
            yes_answerRect.centerx += 14
            no_answerRect.centerx += 14
            data_lostRect.centerx += 14

            for x in range(0, 4):
                for_sure_vertices[x][0] += 14

        if quitting_timer >= 52 and quitting_timer < 54:
            for_sureRect.centerx += 12
            yes_answerRect.centerx += 12
            no_answerRect.centerx += 12
            data_lostRect.centerx += 12

            for x in range(0, 4):
                for_sure_vertices[x][0] += 12

        if quitting_timer >= 54 and quitting_timer < 56:
            for_sureRect.centerx += 10
            yes_answerRect.centerx += 10
            no_answerRect.centerx += 10
            data_lostRect.centerx += 10

            for x in range(0, 4):
                for_sure_vertices[x][0] += 10

        if quitting_timer >= 56 and quitting_timer < 58:
            for_sureRect.centerx += 8
            yes_answerRect.centerx += 8
            no_answerRect.centerx += 8
            data_lostRect.centerx += 8

            for x in range(0, 4):
                for_sure_vertices[x][0] += 8

        if quitting_timer >= 58 and quitting_timer < 60:
            for_sureRect.centerx += 6
            yes_answerRect.centerx += 6
            no_answerRect.centerx += 6
            data_lostRect.centerx += 6

            for x in range(0, 4):
                for_sure_vertices[x][0] += 6

        if quitting_timer >= 60 and quitting_timer < 62:
            for_sureRect.centerx += 4
            yes_answerRect.centerx += 4
            no_answerRect.centerx += 4
            data_lostRect.centerx += 4

            for x in range(0, 4):
                for_sure_vertices[x][0] += 4

        if quitting_timer >= 62 and quitting_timer < 64:
            for_sureRect.centerx += 2
            yes_answerRect.centerx += 2
            no_answerRect.centerx += 2
            data_lostRect.centerx += 2

            for x in range(0, 4):
                for_sure_vertices[x][0] += 2

        if quitting_timer >= 64 and quitting_timer < 66:
            for_sureRect.centerx -= 2
            yes_answerRect.centerx -= 2
            no_answerRect.centerx -= 2
            data_lostRect.centerx -= 2

            for x in range(0, 4):
                for_sure_vertices[x][0] -= 2

        if quitting_timer >= 68 and quitting_timer < 70:
            for_sureRect.centerx -= 4
            yes_answerRect.centerx -= 4
            no_answerRect.centerx -= 4
            data_lostRect.centerx -= 4

            for x in range(0, 4):
                for_sure_vertices[x][0] -= 4

        if quitting_timer >= 70 and quitting_timer < 72:
            for_sureRect.centerx -= 4
            yes_answerRect.centerx -= 4
            no_answerRect.centerx -= 4
            data_lostRect.centerx -= 4

            for x in range(0, 4):
                for_sure_vertices[x][0] -= 4

        if quitting_timer >= 74 and quitting_timer < 76:
            for_sureRect.centerx -= 6
            yes_answerRect.centerx -= 6
            no_answerRect.centerx -= 6
            data_lostRect.centerx -= 6

            for x in range(0, 4):
                for_sure_vertices[x][0] -= 6

        if quitting_timer >= 76 and quitting_timer < 78:
            for_sureRect.centerx -= 8
            yes_answerRect.centerx -= 8
            no_answerRect.centerx -= 8
            data_lostRect.centerx -= 8

            for x in range(0, 4):
                for_sure_vertices[x][0] -= 8

        if quitting_timer >= 78 and quitting_timer < 80:
            for_sureRect.centerx -= 10
            yes_answerRect.centerx -= 10
            no_answerRect.centerx -= 10
            data_lostRect.centerx -= 10

            for x in range(0, 4):
                for_sure_vertices[x][0] -= 10

        if quitting_timer >= 80 and quitting_timer < 82:
            for_sureRect.centerx -= 12
            yes_answerRect.centerx -= 12
            no_answerRect.centerx -= 12
            data_lostRect.centerx -= 12

            for x in range(0, 4):
                for_sure_vertices[x][0] -= 12

        if quitting_timer >= 82 and quitting_timer < 83:
            for_sureRect.centerx -= 14
            yes_answerRect.centerx -= 14
            no_answerRect.centerx -= 14
            data_lostRect.centerx -= 14

            for x in range(0, 4):
                for_sure_vertices[x][0] -= 14

        if quitting_timer == 83 and going_to_quit == False:
            d_qt = 0

        if quitting_timer >= 84 and quitting_timer < 205 and going_to_quit != True:
            d_qt = 1

            for_sureRect.centerx += 16
            yes_answerRect.centerx += 16
            no_answerRect.centerx += 16
            data_lostRect.centerx += 16
 
            for x in range(0, 4):
                for_sure_vertices[x][0] += 16

        if paused == False:
            ask_to_quit = False
            quitting_timer = 0
            
            for_sureRect.centerx = WIDTH / 2 - TWENTY - TEN - FIVE - (SEVENTY * FIVE) - SEVENTY
            data_lostRect.centerx = WIDTH / 2 - TWENTY - TEN - FIVE - (SEVENTY * FIVE) - SEVENTY
            
            yes_answerRect.centerx = WIDTH / 2 - FORTY + TEN - (SEVENTY * FIVE) - SEVENTY
            no_answerRect.centerx = WIDTH / 2 - FORTY + TEN - (SEVENTY * FIVE) - SEVENTY

            resume_playRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY - SEVENTY
            quit_playRect.centerx = resume_playRect.centerx

            for_sure_vertices = [[-365,221],[-107,221],[-107,357],[-359,357]]

            pause_back_vertices = [[L_BORDER - TEN - (SEVENTY * FIVE) - SEVENTY, TOP_BORDER - TEN],[L_BORDER + (TILE * B_WIDTH) + TEN - (SEVENTY * FIVE) - SEVENTY,TOP_BORDER - TEN], \
                   [L_BORDER + (TILE * B_WIDTH) + TEN - (SEVENTY * FIVE) - SEVENTY, HEIGHT - B_BORDER + TEN],[L_BORDER - TEN - (SEVENTY * FIVE) - SEVENTY, HEIGHT - B_BORDER + TEN]]

            pause_layer_vertices = [[pause_back_vertices[0][0] + TEN, pause_back_vertices[0][1] + TEN + FIVE],[pause_back_vertices[1][0] - TEN, pause_back_vertices[1][1] + TEN], \
                   [pause_back_vertices[2][0] - TEN, pause_back_vertices[2][1] - TEN - FIVE],[pause_back_vertices[3][0] + TEN, pause_back_vertices[3][1] - TEN - FIVE]]

            tRect.centerx = WIDTH / 2  - (SEVENTY * FIVE) - SEVENTY
            eRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
            t2Rect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
            areRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
            iRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY
            sRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY

        if going_to_quit == True:

            d_qt = 1

            if quitting_timer >= 83 and quitting_timer < 85:
                tRect.centerx -= 10
                eRect.centerx -= 10
                t2Rect.centerx -= 10
                areRect.centerx -= 10
                iRect.centerx -= 10
                sRect.centerx -= 10
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] -= 10
                    pause_layer_vertices[x][0] -= 10

            if quitting_timer >= 85 and quitting_timer < 87:
                tRect.centerx -= 8
                eRect.centerx -= 8
                t2Rect.centerx -= 8
                areRect.centerx -= 8
                iRect.centerx -= 8
                sRect.centerx -= 8
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] -= 8
                    pause_layer_vertices[x][0] -= 8

            if quitting_timer >= 87 and quitting_timer < 89:
                tRect.centerx -= 6
                eRect.centerx -= 6
                t2Rect.centerx -= 6
                areRect.centerx -= 6
                iRect.centerx -= 6
                sRect.centerx -= 6
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] -= 6
                    pause_layer_vertices[x][0] -= 6

            if quitting_timer >= 89 and quitting_timer < 91:
                tRect.centerx -= 4
                eRect.centerx -= 4
                t2Rect.centerx -= 4
                areRect.centerx -= 4
                iRect.centerx -= 4
                sRect.centerx -= 4
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] -= 4
                    pause_layer_vertices[x][0] -= 4

            if quitting_timer >= 91 and quitting_timer < 93:
                tRect.centerx -= 2
                eRect.centerx -= 2
                t2Rect.centerx -= 2
                areRect.centerx -= 2
                iRect.centerx -= 2
                sRect.centerx -= 2
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] -= 2
                    pause_layer_vertices[x][0] -= 2

            if quitting_timer >= 93 and quitting_timer < 95:
                tRect.centerx += 2
                eRect.centerx += 2
                t2Rect.centerx += 2
                areRect.centerx += 2
                iRect.centerx += 2
                sRect.centerx += 2
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] += 2
                    pause_layer_vertices[x][0] += 2

            if quitting_timer >= 95 and quitting_timer < 97:
                tRect.centerx += 4
                eRect.centerx += 4
                t2Rect.centerx += 4
                areRect.centerx += 4
                iRect.centerx += 4
                sRect.centerx += 4
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] += 4
                    pause_layer_vertices[x][0] += 4

            if quitting_timer >= 97 and quitting_timer < 99:
                tRect.centerx += 6
                eRect.centerx += 6
                t2Rect.centerx += 6
                areRect.centerx += 6
                iRect.centerx += 6
                sRect.centerx += 6
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] += 6
                    pause_layer_vertices[x][0] += 6

            if quitting_timer >= 99 and quitting_timer < 101:
                tRect.centerx += 8
                eRect.centerx += 8
                t2Rect.centerx += 8
                areRect.centerx += 8
                iRect.centerx += 8
                sRect.centerx += 8
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] += 8
                    pause_layer_vertices[x][0] += 8

            if quitting_timer >= 101 and quitting_timer < 103:
                tRect.centerx += 10
                eRect.centerx += 10
                t2Rect.centerx += 10
                areRect.centerx += 10
                iRect.centerx += 10
                sRect.centerx += 10
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] += 10
                    pause_layer_vertices[x][0] += 10

            if quitting_timer >= 103 and quitting_timer < 105:
                tRect.centerx += 12
                eRect.centerx += 12
                t2Rect.centerx += 12
                areRect.centerx += 12
                iRect.centerx += 12
                sRect.centerx += 12
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] += 12
                    pause_layer_vertices[x][0] += 12

            if quitting_timer >= 105 and quitting_timer < 107:
                tRect.centerx += 14
                eRect.centerx += 14
                t2Rect.centerx += 14
                areRect.centerx += 14
                iRect.centerx += 14
                sRect.centerx += 14
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] += 14
                    pause_layer_vertices[x][0] += 14
                    
            if quitting_timer >= 107:
                tRect.centerx += 16
                eRect.centerx += 16
                t2Rect.centerx += 16
                areRect.centerx += 16
                iRect.centerx += 16
                sRect.centerx += 16
                
                for x in range(0, 4):
                    pause_back_vertices[x][0] += 16
                    pause_layer_vertices[x][0] += 16


                    

            if quitting_timer >= 89 and quitting_timer < 91:
                for_sureRect.centerx -= 10
                yes_answerRect.centerx -= 10
                no_answerRect.centerx -= 10
                data_lostRect.centerx -= 10
                
                for x in range(0, 4):
                    for_sure_vertices[x][0] -= 10

            if quitting_timer >= 91 and quitting_timer < 93:
                for_sureRect.centerx -= 8
                yes_answerRect.centerx -= 8
                no_answerRect.centerx -= 8
                data_lostRect.centerx -= 8
                    
                for x in range(0, 4):
                    for_sure_vertices[x][0] -= 8

            if quitting_timer >= 93 and quitting_timer < 95:
                for_sureRect.centerx -= 6
                yes_answerRect.centerx -= 6
                no_answerRect.centerx -= 6
                data_lostRect.centerx -= 6
                    
                for x in range(0, 4):
                    for_sure_vertices[x][0] -= 6

            if quitting_timer >= 95 and quitting_timer < 97:
                for_sureRect.centerx -= 4
                yes_answerRect.centerx -= 4
                no_answerRect.centerx -= 4
                data_lostRect.centerx -= 4
                    
                for x in range(0, 4):
                    for_sure_vertices[x][0] -= 4

            if quitting_timer >= 97 and quitting_timer < 99:
                for_sureRect.centerx -= 2
                yes_answerRect.centerx -= 2
                no_answerRect.centerx -= 2
                data_lostRect.centerx -= 2
                   
                for x in range(0, 4):
                    for_sure_vertices[x][0] -= 2

            if quitting_timer >= 101 and quitting_timer < 103:
                for_sureRect.centerx += 2
                yes_answerRect.centerx += 2
                no_answerRect.centerx += 2
                data_lostRect.centerx += 2
                   
                for x in range(0, 4):
                    for_sure_vertices[x][0] += 2

            if quitting_timer >= 103 and quitting_timer < 105:
                for_sureRect.centerx += 4
                yes_answerRect.centerx += 4
                no_answerRect.centerx += 4
                data_lostRect.centerx += 4
                    
                for x in range(0, 4):
                    for_sure_vertices[x][0] += 4

            if quitting_timer >= 107 and quitting_timer < 109:
                for_sureRect.centerx += 6
                yes_answerRect.centerx += 6
                no_answerRect.centerx += 6
                data_lostRect.centerx += 6
                    
                for x in range(0, 4):
                    for_sure_vertices[x][0] += 6

            if quitting_timer >= 111 and quitting_timer < 113:
                for_sureRect.centerx += 8
                yes_answerRect.centerx += 8
                no_answerRect.centerx += 8
                data_lostRect.centerx += 8
                    
                for x in range(0, 4):
                    for_sure_vertices[x][0] += 8

            if quitting_timer >= 113 and quitting_timer < 115:
                for_sureRect.centerx += 10
                yes_answerRect.centerx += 10
                no_answerRect.centerx += 10
                data_lostRect.centerx += 10
                    
                for x in range(0, 4):
                    for_sure_vertices[x][0] += 10

            if quitting_timer >= 115 and quitting_timer < 117:
                for_sureRect.centerx += 12
                yes_answerRect.centerx += 12
                no_answerRect.centerx += 12
                data_lostRect.centerx += 12
                    
                for x in range(0, 4):
                    for_sure_vertices[x][0] += 12

            if quitting_timer >= 117 and quitting_timer < 119:
                for_sureRect.centerx += 14
                yes_answerRect.centerx += 14
                no_answerRect.centerx += 14
                data_lostRect.centerx += 14
                    
                for x in range(0, 4):
                    for_sure_vertices[x][0] += 14

            if quitting_timer >= 119:
                for_sureRect.centerx += 16
                yes_answerRect.centerx += 16
                no_answerRect.centerx += 16
                data_lostRect.centerx += 16
                    
                for x in range(0, 4):
                    for_sure_vertices[x][0] += 16

            if quitting_timer > 150:
                game_over_true = True

                if game_over_timer < 50:
                    d_go_y = 10
                    
                started = False
                d_go_t = 1

            
            
            


    t = pause_tetris_font.render("T", True, DIMMERER_GRAY, BLACK)
    e = pause_tetris_font.render("E", True, DIMMERER_GRAY, BLACK)
    t2 = pause_tetris_font.render("T", True, DIMMERER_GRAY, BLACK)
    are = pause_tetris_font.render("R", True, DIMMERER_GRAY, BLACK)
    i = pause_tetris_font.render("I", True, DIMMERER_GRAY, BLACK)
    s = pause_tetris_font.render("S", True, DIMMERER_GRAY, BLACK)
        
        






    # Game over test

    if piece_pos[1] == -1 and check_move('DOWN') == "DON'T MOVE" and game_over_true == False:
        dt = 0
        if game_overRect.centery < (HEIGHT / 2 - d_go_y):
            d_go_y = 10
        
            game_over_true = True
            
        #pygame.mixer.music.fadeout(2000)

    if game_over_true == True and game_overRect.centery >= (HEIGHT / 2 - d_go_y) and game_overRect.centery <= (HEIGHT / 2 + d_go_y) and started == False:
        #go_exp.play()
        d_go_y = 0
        d_go_t = 1

    game_overRect.centery += d_go_y

    game_over_timer += d_go_t

    if game_over_timer == 50 and game_over_true == True:
        if d_go_y == 0 and started == False:
            #fail.play()
            started = True

            # Record score

            if exited_game != True:
                file_path = 'highscores/highscores.txt'
                file = open(file_path, "a")
                file_temp = initials
                initials = initials + score
                file.write(initials)
                file.close()
                initials = file_temp

            # Holdind piece variables

            already_held = False
            able_to_hold = True

        d_go_t = 0
        
        
        

    



    # Caluculate piece movement

    if check_move('DOWN') == "DON'T MOVE":
        if timer > temp_interval:

            # Lock sound

            if paused != True:
                lock_set.play()
            
            # Lock the piece
            
            able_to_hold = lock_board(able_to_hold)

            # Get the next piece(s)
            
            selection = piece_in_holding
            piece_in_holding = second_piece
            second_piece = third_piece
            third_piece = random.choice(select_list)

            # Select the piece(s)
            
            select_piece(selection)
            select_next_piece(piece_in_holding)
            select_second_piece(second_piece)
            select_third_piece(third_piece)
            
            # Set the piece position based on which piece is being used

            if next_level != True:
                piece_pos = [3, -2] # -2 because the increment is done before this part of the code
            else:
                piece_pos = [3, -3]

        





    if timer > temp_interval:
        timer = 0
        piece_pos[1] += pdy






    # Next level

    if (goal_number == '0' or goal_number == '-1' or goal_number == '-2' \
        or goal_number == '-3' or goal_number == '-4') and next_level_timer == 0:

        next_level = True
        INTERVAL -= 8
        temp_interval = INTERVAL
        speed_incrase_interval = 2

        piece_pos = [3, -2]

    if next_level == True:
        next_level_timer += 1

    if next_level_timer == 100:
        stacked_piece = []

    if next_level_timer == 200:
        
        hold_piece = 0
        select_hold_piece(hold_piece)
        
        next_level = False
        next_level_timer = 0
        level = str(int(level) + 1)
        
        goal_number = '10'

        goal_no = font.render(goal_number, True, FIREBRICK, DIMMER_GRAY)

        # Holding piece variables

        already_held = False
        able_to_hold = True
    




    # Quit the game window
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


        if intro_timer > 350:
            

            if event.type == pygame.KEYDOWN and enter_nameRect.centery == 380:
                if len(initials) < 3:
                    if event.key == K_a:
                        initials += 'A'
                    if event.key == K_b:
                        initials += 'B'
                    if event.key == K_c:
                        initials += 'C'
                    if event.key == K_d:
                        initials += 'D'
                    if event.key == K_e:
                        initials += 'E'
                    if event.key == K_f:
                        initials += 'F'
                    if event.key == K_g:
                        initials += 'G'
                    if event.key == K_h:
                        initials += 'H'
                    if event.key == K_i:
                        initials += 'I'
                    if event.key == K_j:
                        initials += 'J'
                    if event.key == K_k:
                        initials += 'K'
                    if event.key == K_l:
                        initials += 'L'
                    if event.key == K_m:
                        initials += 'M'
                    if event.key == K_n:
                        initials += 'N'
                    if event.key == K_o:
                        initials += 'O'
                    if event.key == K_p:
                        initials += 'P'
                    if event.key == K_q:
                        initials += 'Q'
                    if event.key == K_r:
                        initials += 'R'
                    if event.key == K_s:
                        initials += 'S'
                    if event.key == K_t:
                        initials += 'T'
                    if event.key == K_u:
                        initials += 'U'
                    if event.key == K_v:
                        initials += 'V'
                    if event.key == K_w:
                        initials += 'W'
                    if event.key == K_x:
                        initials += 'X'
                    if event.key == K_y:
                        initials += 'Y'
                    if event.key == K_z:
                        initials += 'Z'
                    
                if event.key == K_BACKSPACE:
                    initials = initials[:len(initials) - 1]


                if len(initials) > 0:
                    if event.key == K_RETURN:
                        ending_intro = True
                        #file_path = 'highscores/highscores.txt'
                        #file = open(file_path, "a")
                        #file.write(initials)
                        #file.close()



        # Muting the music

        if intro_over == True or paused == True:
            if event.type == pygame.MOUSEBUTTONDOWN and event.type != MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos

                if mouse_x > 13 and mouse_x < 67 and mouse_y > 631 and mouse_y < 675:
                    if music_choice == music_on:
                        music_choice = music_off
                        pygame.mixer.music.pause()
                    else:
                        music_choice = music_on                
                        pygame.mixer.music.unpause()

            if event.type == pygame.MOUSEBUTTONDOWN and event.type != MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos

                if mouse_x > 121 and mouse_x < 370 and mouse_y > 283 and mouse_y < 308:
                    if pause_timer >= 58 and resume_playRect.centerx < WIDTH and resume_playRect.centerx > 0:
                        resume = True

                if mouse_x > 120 and mouse_x < 371 and mouse_y > 334 and mouse_y < 361:
                    if quit_playRect.centerx < WIDTH and quit_playRect.centerx > 0:
                        ask_to_quit = True
                        quitting_timer = 0

                        for_sureRect.centerx = WIDTH / 2 - TWENTY - TEN - FIVE - (SEVENTY * FIVE) - SEVENTY
                        data_lostRect.centerx = WIDTH / 2 - TWENTY - TEN - FIVE - (SEVENTY * FIVE) - SEVENTY
                        
                        yes_answerRect.centerx = WIDTH / 2 - FORTY + TEN - (SEVENTY * FIVE) - SEVENTY
                        no_answerRect.centerx = WIDTH / 2 - FORTY + TEN - (SEVENTY * FIVE) - SEVENTY

                        for_sure_vertices = [[-365,221],[-107,221],[-107,357],[-359,357]]


                if mouse_x > 238 and mouse_x < 267 and mouse_y > 304 and mouse_y < 318:
                    if yes_answerRect.centerx < WIDTH and yes_answerRect.centerx > 0:
                        going_to_quit = True
                        exited_game = True

                if mouse_x > 243 and mouse_x < 262 and mouse_y > 330 and mouse_y < 342:
                    if no_answerRect.centerx < WIDTH and no_answerRect.centerx > 0:
                        pause_timer = 0
                        paused = True
                        quitting_timer = 84                    

                        resume_playRect.centerx = WIDTH / 2 - (SEVENTY * FIVE) - SEVENTY - SEVENTY
                        quit_playRect.centerx = resume_playRect.centerx
                            
                            
                        resume_back_vertices = [[R_BORDER + FORTY + TWENTY - (SEVENTY * FIVE) - SEVENTY, (HEIGHT / 2) - SEVENTY],[WIDTH - R_BORDER - SEVENTY - SEVENTY - TWENTY - (SEVENTY * FIVE) - SEVENTY, (HEIGHT / 2) - SEVENTY], \
                                [WIDTH - R_BORDER - SEVENTY - SEVENTY - TWENTY - (SEVENTY * FIVE) - SEVENTY, HEIGHT / 2 + TWENTY - SEVENTY],[R_BORDER + FORTY + TWENTY + FIVE - (SEVENTY * FIVE) - SEVENTY, HEIGHT / 2 + TWENTY - SEVENTY]]
                            
                        quit_back_vertices = [[resume_back_vertices[3][0], resume_back_vertices[3][1] + TWENTY],[resume_back_vertices[2][0], resume_back_vertices[2][1] + TWENTY], \
                              [resume_back_vertices[2][0],resume_back_vertices[2][1] + FORTY],[resume_back_vertices[0][0], resume_back_vertices[3][1] + FORTY]]

            





                    

        # Move and rotate the game piece

            if event.type == pygame.KEYDOWN:
                if event.key == K_p:
                    if paused == False:
                        paused = True
                        not_playing = True
                        pygame.mixer.music.set_volume(0.25)

                #if event.key == K_y:
                    #pygame.mixer.music.pause()

                if event.key == K_DOWN and paused != True and next_level != True:
                    if check_move('DOWN') == "MOVE":
                        #movement.play()
                        piece_pos[1] += 1

                if event.key == K_UP and paused != True and next_level != True:
                    if check_move('UP') == "MOVE":
                        #movement.play()
                        piece_pos[1] -= 1

                if event.key == K_LEFT and paused != True and next_level != True:
                    if check_move('LEFT') == "MOVE":
                        #movement.play()
                        piece_pos[0] -= 1

                if event.key == K_RIGHT and paused != True and next_level != True:
                    if check_move('RIGHT') == "MOVE":
                        #movement.play()
                        piece_pos[0] += 1

                if event.key == K_RALT or event.key == K_LCTRL and paused != True and next_level != True:
                    if selection == 1 or selection == 5 or selection == 9 \
                    or selection == 17 or selection == 21 or selection == 25:
                        selection = rotate(selection, '0', 'L')
                        
                    elif selection == 2 or selection == 6 or selection == 10 \
                    or selection == 18 or selection == 22 or selection == 26:
                        selection = rotate(selection, 'R', '0')

                    elif selection == 3 or selection == 7 or selection == 11 \
                    or selection == 19 or selection == 23 or selection == 27:
                        selection = rotate(selection, '2', 'R')

                    elif selection == 4 or selection == 8 or selection == 12 \
                    or selection == 20 or selection == 24 or selection == 28:
                        selection = rotate(selection, 'L', '2')

                        
                if event.key == K_RCTRL or event.key == K_LALT and paused != True and next_level != True:
                    if selection == 1 or selection == 5 or selection == 9 or selection == 13 \
                    or selection == 17 or selection == 21 or selection == 25:
                        selection = rotate(selection, '0', 'R')
                        
                    elif selection == 2 or selection == 6 or selection == 10 or selection == 14 \
                    or selection == 18 or selection == 22 or selection == 26:
                        selection = rotate(selection, 'R', '2')

                    elif selection == 3 or selection == 7 or selection == 11 or selection == 15 \
                    or selection == 19 or selection == 23 or selection == 27:
                        selection = rotate(selection, '2', 'L')

                    elif selection == 4 or selection == 8 or selection == 12 or selection == 16 \
                    or selection == 20 or selection == 24 or selection == 28:
                        selection = rotate(selection, 'L', '0')

                if event.key == K_RETURN:
                    print_hold()

                if event.key == K_h:
                    if already_held == True and able_to_hold == True:
                        piece_pos = [3, -1]
                        temp_piece = selection
                        selection = hold_piece
                        hold_piece = temp_piece
                        able_to_hold = False
                        
                    elif already_held == False:
                        piece_pos = [3, -1]
                        hold_piece = selection
                        selection = piece_in_holding
                        already_held = True
                        able_to_hold = False

                        piece_in_holding = second_piece
                        second_piece = third_piece
                        third_piece = random.choice(select_list)

                    # Select the piece(s)
                
                    select_piece(selection)
                    select_next_piece(piece_in_holding)
                    select_second_piece(second_piece)
                    select_third_piece(third_piece)
                    select_hold_piece(hold_piece)



                

    # Update board with new position of piece
    
    update_board(piece_pos[0], piece_pos[1])






    # Cooridnates for tiles and squares for tiles

    draw_piece = []
    square_in_pieces = []
    falling_piece = []
    next_piece_holding = []
    second_piece_holding = []
    third_piece_holding = []
    hold_piece_holding = []
    


    


    # Draw pieces
    
    if intro_over == True:
        surface.fill(BACKGROUND)
    
    for y in range(0, B_HEIGHT):
        for x in range(0, B_WIDTH):
            for m in range(0, len(stacked_piece)):
                    if x == stacked_piece[m][0] and y == stacked_piece[m][1]:
                        draw_piece.append(pygame.Rect((x * TILE + L_BORDER), (y * TILE + TOP_BORDER), TILE, TILE))

                        square_in_pieces.append([((x * TILE + L_BORDER), (y * TILE + TOP_BORDER)), ((x * TILE+ L_BORDER), \
                                        (y * TILE + TILE + TOP_BORDER)), ((x * TILE + TILE + L_BORDER), \
                                        (y * TILE + TILE + TOP_BORDER)), ((x * TILE + TILE + L_BORDER), (y * TILE + TOP_BORDER))])

                        number_of_tiles += 1

    for y in range(0, B_HEIGHT):
        for x in range(0, B_WIDTH):                 
            if board[x][y] == 2:

                falling_piece.append(pygame.Rect((x * TILE + L_BORDER), (y * TILE + TOP_BORDER), TILE, TILE))

                square_in_pieces.append([((x * TILE + L_BORDER), (y * TILE + TOP_BORDER)), ((x * TILE+ L_BORDER), \
                                    (y * TILE + TILE + TOP_BORDER)), ((x * TILE + TILE + L_BORDER), \
                                    (y * TILE + TILE + TOP_BORDER)), ((x * TILE + TILE + L_BORDER), (y * TILE + TOP_BORDER))])


    for y in range(0, 4):
        for x in range(0, 4):
            if next_piece_help[x][y] == 2:

                next_piece_holding.append(pygame.Rect((L_BORDER + B_WIDTH * TILE + x * (TILE / 2) + TEN), (y * (TILE / 2) + TOP_BORDER), (TILE / 2), (TILE / 2)))

    for y in range(0, 4):
        for x in range(0, 4):
            if second_piece_help[x][y] == 2:

                second_piece_holding.append(pygame.Rect((L_BORDER + B_WIDTH * TILE + x * (TILE / 2) + TEN), (y * (TILE / 2) + TOP_BORDER + SEVENTY), (TILE / 2), (TILE / 2)))

    for y in range(0, 4):
        for x in range(0, 4):
            if third_piece_help[x][y] == 2:

                third_piece_holding.append(pygame.Rect((L_BORDER + B_WIDTH * TILE + x * (TILE / 2) + TEN), (y * (TILE / 2) + TOP_BORDER + SEVENTY + SEVENTY), (TILE / 2), (TILE / 2)))

    for y in range(0, 4):
        for x in range(0, 4):
            if hold_piece_help[x][y] == 2:

                hold_piece_holding.append(pygame.Rect(TWENTY + (x * TILE / 2), (y * (TILE / 2) + TOP_BORDER), (TILE / 2), (TILE / 2)))









    # Remove line

    for m in range(0, B_HEIGHT):
        if board[0][m] == 1:
            if board[1][m] == 1 and board[2][m] == 1 and board[3][m] == 1 and board[4][m] == 1 and board[4][m] == 1 \
            and board[5][m] == 1 and board[6][m] == 1 and board[7][m] == 1 and board[8][m] == 1 and board[9][m] == 1:

                n = len(stacked_piece) - 1
                
                while n > -1:
                    if stacked_piece[n][1] == m:
                        stacked_piece.pop(n)
                    n -= 1

                for n in range(0, len(stacked_piece)):
                    if stacked_piece[n][1] < m:
                        stacked_piece[n][1] += 1
                        
                goal_number = str(int(goal_number) - 1)

                if goal_number == '-1' or goal_number == '-2' or goal_number == '-3':
                    goal_number = '0'

                goal_no = font.render(goal_number, True, FIREBRICK, DIMMER_GRAY)

                lines_cleared += 1

                # Calculate score

                score = int(score)
                
    if lines_cleared == 1:
        single_cap.play()
        score += int(40 * (int(level) + 1))
        number_times_removed += 1
    elif lines_cleared == 2:
        double_cap.play()
        number_times_removed += 1
        score += int(100 * (int(level) + 1))
    elif lines_cleared == 3:
        triple_cap.play()
        number_times_removed += 1
        score += int(300 * (int(level) + 1))
    elif lines_cleared == 4:
        tetris_cap.play()
        number_times_removed += 1
        score += int(1200 * (int(level) + 1))

    score = str(score)

    lines_cleared = 0

    score_number = font.render(score, True, FIREBRICK, DIMMER_GRAY)






    # Background change and speed increase

    if number_times_removed % 2 == 0 and number_times_removed != 0:
        #change_color = True

        # Speed increase

        #temp_interval -= 2
        #speed_increase_interval += 2


        # Background change


        

        # BLUE TO YELLOW

        if next_color == (255,215,0) and number_times_removed == number_check:

            if number_changed == False:
                #number_check += 2
                number_changed = True
                
                dr = 3
                dg = .225
                db = -6.25
                
            if BACKGROUND != next_color:
                dr, dg, db, BACKGROUND = change_the_background(r, g, b, BACKGROUND, dr, dg, db)


        if BACKGROUND == next_color:                
            next_color = (192,0,0)
            number_check += 2
            
            dr = 0
            dg = 0
            db = 0
            #change_color = False
            number_changed = False
            dr, dg, db, BACKGROUND = change_the_background(r, g, b, BACKGROUND, dr, dg, db)



        # YELLOW TO RED

        if next_color == (192,0,0) and number_times_removed == number_check:

            if number_changed == False:
                #number_check += 2
                number_changed = True
                
                dr = -1.575
                dg = -5.375
                db = 0
                
            if BACKGROUND != next_color:

                dr, dg, db, BACKGROUND = change_the_background(r, g, b, BACKGROUND, dr, dg, db)


        if BACKGROUND == next_color:
            next_color = (135, 206, 250)
            number_check += 2
            
            dr = 0
            dg = 0
            db = 0
            #change_color = False
            number_changed = False
            dr, dg, db, BACKGROUND = change_the_background(r, g, b, BACKGROUND, dr, dg, db)



        # RED TO BLUE

        if next_color == (135, 206, 250) and number_times_removed == number_check:

            if number_changed == False:
                #number_check += 2
                number_changed = True
                
                dr = -1.425
                dg = 5.15
                db = 6.25
                
            if BACKGROUND != next_color:

                dr, dg, db, BACKGROUND = change_the_background(r, g, b, BACKGROUND, dr, dg, db)


        if BACKGROUND == next_color:
            next_color = (255,215,0)
            number_check += 2
            
            dr = 0
            dg = 0
            db = 0
            #change_color = False
            number_changed = False
            dr, dg, db, BACKGROUND = change_the_background(r, g, b, BACKGROUND, dr, dg, db)

    next_piece = font.render('NEXT PIECE', True, FIREBRICK, BACKGROUND)
    hold = font.render('HOLD', True, FIREBRICK, BACKGROUND)
    goal = font.render('GOAL', True, FIREBRICK, BACKGROUND)
    level_number = font.render(level, True, FIREBRICK, BACKGROUND)
    level_text = font.render('LEVEL', True, FIREBRICK, BACKGROUND)





                        


                

    # Print background

    if intro_over == True:
        pygame.draw.polygon(surface, back_color, back_vertices, 0)
        pygame.draw.polygon(surface, score_area_color, score_area_vertices, 0)
        pygame.draw.polygon(surface, hold_area_color, hold_area_vertices, 0)
        pygame.draw.polygon(surface, next_area_color, next_area_vertices, 0)
        pygame.draw.polygon(surface, ha_layer_color, ha_layer_vertices, 0)
        pygame.draw.polygon(surface, b_layer_color, b_layer_vertices, 0)
        pygame.draw.polygon(surface, na_layer_color, na_layer_vertices, 0)
        pygame.draw.polygon(surface, goal_area_color, goal_area_vertices, 0)
        pygame.draw.polygon(surface, ga_layer_color, ga_layer_vertices, 0)
        pygame.draw.polygon(surface, la_layer_color, la_layer_vertices, 0)

    # Print circles in grid

    if intro_over == True:
        for y in range(0, len(circles_in_grid)):
            pygame.draw.circle(surface, DIM_GRAY, circles_in_grid[y], 3, 1)






    # Print number_of_tiles

    COLOR = MEDIUM_ORCHID

    if intro_over == True:
        for x in range(0, number_of_tiles):            
            pygame.draw.rect(surface, COLOR, draw_piece[x])

        for x in range(0, len(falling_piece)):
            if selection == 1 or selection == 2 or selection == 3 or selection == 4:
                pygame.draw.rect(surface, TURQUOISE, falling_piece[x])
            elif selection == 5 or selection == 6 or selection == 7 or selection == 8:
                pygame.draw.rect(surface, BLUE, falling_piece[x])
            elif selection == 9 or selection == 10 or selection == 11 or selection == 12:
                pygame.draw.rect(surface, ORANGE, falling_piece[x])
            elif selection == 13 or selection == 14 or selection == 15 or selection == 16:
                pygame.draw.rect(surface, YELLOW, falling_piece[x])
            elif selection == 17 or selection == 18 or selection == 19 or selection == 20:
                pygame.draw.rect(surface, GREEN, falling_piece[x])
            elif selection == 21 or selection == 22 or selection == 23 or selection == 24:
                pygame.draw.rect(surface, PURPLE, falling_piece[x])
            elif selection == 25 or selection == 26 or selection == 27 or selection == 28:
                pygame.draw.rect(surface, RED, falling_piece[x])
            else:
                pygame.draw.rect(surface, BLUE, falling_piece[x])
            
        for x in range(0, number_of_tiles):
            pygame.draw.lines(surface, BLACK, True, square_in_pieces[x], LINE_WIDTH)








    if intro_over == True:
        # Drawing the next pieces

        P2 = piece_in_holding
        P3 = second_piece
        P4 = third_piece
        P5 = hold_piece

        # NEXT PIECE DRAWING

        if P2 == 1 or P2 == 2 or P2 == 3 or P2 == 4:
            for x in range(0, 4):
                pygame.draw.rect(surface, TURQUOISE, next_piece_holding[x])
        if P2 == 5 or P2 == 6 or P2 == 7 or P2 == 8:
            for x in range(0, 4):
                pygame.draw.rect(surface, BLUE, next_piece_holding[x])
        if P2 == 9 or P2 == 10 or P2 == 11 or P2 == 12:
            for x in range(0, 4):
                pygame.draw.rect(surface, ORANGE, next_piece_holding[x])
        if P2 == 13 or P2 == 14 or P2 == 15 or P2 == 16:
            for x in range(0, 4):
                pygame.draw.rect(surface, YELLOW, next_piece_holding[x])
        if P2 == 17 or P2 == 18 or P2 == 19 or P2 == 20:
            for x in range(0, 4):
                pygame.draw.rect(surface, GREEN, next_piece_holding[x])
        if P2 == 21 or P2 == 22 or P2 == 23 or P2 == 24:
            for x in range(0, 4):
                pygame.draw.rect(surface, PURPLE, next_piece_holding[x])
        if P2 == 25 or P2 == 26 or P2 == 27 or P2 == 28:
            for x in range(0, 4):
                pygame.draw.rect(surface, RED, next_piece_holding[x])

        # SECOND PIECE DRAWING

        if P3 == 1 or P3 == 2 or P3 == 3 or P3 == 4:
            for x in range(0, 4):
                pygame.draw.rect(surface, TURQUOISE, second_piece_holding[x])
        if P3 == 5 or P3 == 6 or P3 == 7 or P3 == 8:
            for x in range(0, 4):
                pygame.draw.rect(surface, BLUE, second_piece_holding[x])
        if P3 == 9 or P3 == 10 or P3 == 11 or P3 == 12:
            for x in range(0, 4):
                pygame.draw.rect(surface, ORANGE, second_piece_holding[x])
        if P3 == 13 or P3 == 14 or P3 == 15 or P3 == 16:
            for x in range(0, 4):
                pygame.draw.rect(surface, YELLOW, second_piece_holding[x])
        if P3 == 17 or P3 == 18 or P3 == 19 or P3 == 20:
            for x in range(0, 4):
                pygame.draw.rect(surface, GREEN, second_piece_holding[x])
        if P3 == 21 or P3 == 22 or P3 == 23 or P3 == 24:
            for x in range(0, 4):
                pygame.draw.rect(surface, PURPLE, second_piece_holding[x])
        if P3 == 25 or P3 == 26 or P3 == 27 or P3 == 28:
            for x in range(0, 4):
                pygame.draw.rect(surface, RED, second_piece_holding[x])

        # THIRD PIECE DRAWING

        if P4 == 1 or P4 == 2 or P4 == 3 or P4 == 4:
            for x in range(0, 4):
                pygame.draw.rect(surface, TURQUOISE, third_piece_holding[x])
        if P4 == 5 or P4 == 6 or P4 == 7 or P4 == 8:
            for x in range(0, 4):
                pygame.draw.rect(surface, BLUE, third_piece_holding[x])
        if P4 == 9 or P4 == 10 or P4 == 11 or P4 == 12:
            for x in range(0, 4):
                pygame.draw.rect(surface, ORANGE, third_piece_holding[x])
        if P4 == 13 or P4 == 14 or P4 == 15 or P4 == 16:
            for x in range(0, 4):
                pygame.draw.rect(surface, YELLOW, third_piece_holding[x])
        if P4 == 17 or P4 == 18 or P4 == 19 or P4 == 20:
            for x in range(0, 4):
                pygame.draw.rect(surface, GREEN, third_piece_holding[x])
        if P4 == 21 or P4 == 22 or P4 == 23 or P4 == 24:
            for x in range(0, 4):
                pygame.draw.rect(surface, PURPLE, third_piece_holding[x])
        if P4 == 25 or P4 == 26 or P4 == 27 or P4 == 28:
            for x in range(0, 4):
                pygame.draw.rect(surface, RED, third_piece_holding[x])

        # HOLD PIECE DRAWING

        if P5 == 1 or P5 == 2 or P5 == 3 or P5 == 4:
            for x in range(0, 4):
                pygame.draw.rect(surface, TURQUOISE, hold_piece_holding[x])
        if P5 == 5 or P5 == 6 or P5 == 7 or P5 == 8:
            for x in range(0, 4):
                pygame.draw.rect(surface, BLUE, hold_piece_holding[x])
        if P5 == 9 or P5 == 10 or P5 == 11 or P5 == 12:
            for x in range(0, 4):
                pygame.draw.rect(surface, ORANGE, hold_piece_holding[x])
        if P5 == 13 or P5 == 14 or P5 == 15 or P5 == 16:
            for x in range(0, 4):
                pygame.draw.rect(surface, YELLOW, hold_piece_holding[x])
        if P5 == 17 or P5 == 18 or P5 == 19 or P5 == 20:
            for x in range(0, 4):
                pygame.draw.rect(surface, GREEN, hold_piece_holding[x])
        if P5 == 21 or P5 == 22 or P5 == 23 or P5 == 24:
            for x in range(0, 4):
                pygame.draw.rect(surface, PURPLE, hold_piece_holding[x])
        if P5 == 25 or P5 == 26 or P5 == 27 or P5 == 28:
            for x in range(0, 4):
                pygame.draw.rect(surface, RED, hold_piece_holding[x])





            

        # Drawing lines around tiles

        for x in range(0, B_HEIGHT * B_WIDTH):
            pygame.draw.lines(surface, DIM_GRAY, True, intro_squares[x], 1)

        pygame.draw.polygon(surface, side_back_color, side_back_vertices, 0)




        

        # Blit the text

        surface.blit(next_piece, next_pieceRect)
        surface.blit(hold, holdRect)
        surface.blit(goal, goalRect)
        surface.blit(goal_no, goal_noRect)
        surface.blit(music_choice, (TEN,HEIGHT - SEVENTY))
        surface.blit(score_number, score_numberRect)
        surface.blit(level_number, level_numberRect)
        surface.blit(level_text, level_textRect)

        for x in range(0, num_of_scores):
            surface.blit(high_score_names_font[x], high_score_names_fontRect[x])
            surface.blit(high_scores_font[x], high_scores_fontRect[x])
        
        if game_over_true == True:
            surface.blit(game_over, game_overRect)

        pygame.draw.polygon(surface, pause_back_color, pause_back_vertices, 0)
        pygame.draw.polygon(surface, pause_layer_color, pause_layer_vertices, 0)
        surface.blit(t, tRect)
        surface.blit(e, eRect)
        surface.blit(t2, t2Rect)
        surface.blit(are, areRect)
        surface.blit(i, iRect)
        surface.blit(s, sRect)
        pygame.draw.polygon(surface, for_sure_color, for_sure_vertices)
        surface.blit(for_sure, for_sureRect)
        surface.blit(data_lost, data_lostRect)
        surface.blit(yes_answer, yes_answerRect)
        surface.blit(no_answer, no_answerRect)
        pygame.draw.polygon(surface, resume_back_color, resume_back_vertices)
        pygame.draw.polygon(surface, quit_back_color, quit_back_vertices)
        surface.blit(resume_play, resume_playRect)
        surface.blit(quit_play, quit_playRect)

    if intro_over == False:
            surface.blit(intro_text, intro_textRect)
            surface.blit(my_name, my_nameRect)
            surface.blit(enter_name, enter_nameRect)
            surface.blit(initial_area, initial_areaRect)
            pygame.draw.rect(surface, WHITE, name_area, 3)
    
    pygame.display.flip()








    # Calculate delay

    endtime = pygame.time.get_ticks()
    totaltime = endtime - starttime
    timeleft = int(FRAME_RATE - totaltime)
    if timeleft > 0:
        pygame.time.delay(timeleft)
