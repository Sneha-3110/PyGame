import pygame
from pygame.locals import*
from sys import exit

pygame.init()

XO='X' #whose turn

winner,draw=None,None

board=[[None]*3,[None]*3,[None]*3]

clk=pygame.time.Clock() #for fps

screen=pygame.display.set_mode((400,400))

pygame.display.set_caption('Tic Tac Toe')

img_x=pygame.image.load('X.png')
img_o=pygame.image.load('O.png')

img_x=pygame.transform.scale(img_x,(80,80))
img_o=pygame.transform.scale(img_o,(80,80))

def draw_board():
    screen.fill((241,192,185))
    #drawing vertical lines
    pygame.draw.line(screen,(235,248,127),(400/3,0),(400/3,400),6)
    pygame.draw.line(screen,(235,248,127),((400/3)*2,0),((400/3)*2,400),6)

    #drawing horizontal line
    pygame.draw.line(screen,(235,248,127),(0,400/3),(400,400/3),6)
    pygame.draw.line(screen,(235,248,127),(0,(400/3)*2),(400,(400/3)*2),6)

def result():
    global draw,winner
    if winner:
        msg= winner+" won!"
    elif draw:
        msg="Game Draw!"
    else:
        return
    font=pygame.font.SysFont('georgia',70)
    txt=font.render(msg,1,(24,154,180))
    txt_rect=txt.get_rect(center=(400//2,400//2))
    screen.blit(txt,txt_rect)
    pygame.display.update()

def winning(): #winning_conditions
    global board,winner,draw

    #rows
    for r in range(0,3):
        if((board[r][0]==board[r][1]==board[r][2]) and board[r][0] is not None):
            winner=board[r][0]
            pygame.draw.line(screen,(250,0,0),(0,(r+1)*400/3-400/6),(400,(r+1)*400/3-400/6),4)
            result()
            return

    #columns
    for c in range(0,3):
        if((board[0][c]==board[1][c]==board[2][c]) and board[0][c] is not None):
            winner=board[0][c]
            pygame.draw.line(screen,(250,0,0),((c+1)*400/3-400/6,0),((c+1)*400/3-400/6,400),4)
            result()
            return

    #2 diagonals
    if ((board[0][0]==board[1][1]==board[2][2]) and board[0][0] is not None):
        winner=board[0][0]
        pygame.draw.line(screen,(250,70,70),(50,50),(350,350),4)
        result()
        return
        
    if ((board[0][2]==board[1][1]==board[2][0]) and board[0][2] is not None):
        winner=board[0][2]
        pygame.draw.line(screen,(250,70,70),(350,50),(50,350),4)
        result()
        return

    # draw
    if all([all(r) for r in board]) and winner==None:
        draw=True
        result()
        return
        
#putting X and O
def chance(r,c):
    # this function is to render the image in the given coordinates 
    # as the blit function does not takes coordinates so we have to convert it into pixel size
    global board,XO
    if r==1:
        y=30
    if r==2: #after 1st vertical line and 30 units
        y=400/3 +30
    if r==3:
        y=400/3 *2 +30

    if c==1:
        x=30
    if c==2: #after 1st vertical line and 30 units
        x=400/3 +30
    if c==3:
        x=400/3 *2 +30
        
    #assigning value
    board[r-1][c-1]=XO

    #putting img and changing chance
    if XO=='X':
        screen.blit(img_x,(x,y))
        XO='O'
    else:
        screen.blit(img_o,(x,y))
        XO='X'
    pygame.display.update()

    # getting coordinates where mouse is clicked
def get_input():
    x,y=pygame.mouse.get_pos()
    # print(x,y)
    #to get col no.
    if x<400/3:
        col=1
    elif x<400/3 *2:
        col=2
    elif x<400:
        col=3
    else:
        col=None

    #to get row no.
    if y<400/3:
        row=1
    elif y<400/3 *2:
        row=2
    elif y<400:
        row=3
    else:
        row=None

    if row and col and board[row-1][col-1] is None:
        # global XO
        chance(row,col) #putting in given block
        winning() #check for winning condition

draw_board()

#game loop
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
        elif event.type==MOUSEBUTTONDOWN:
            get_input()
    pygame.display.update()
    clk.tick(30)
