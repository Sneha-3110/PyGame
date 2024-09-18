import pygame
from pygame.locals import*
pygame.init()
from sys import exit

import time
import random

screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Snake Game")

bg=pygame.image.load('grass.jpg').convert()

snake_pos=[80,30] #initial position of snake
snake_speed=10

clk=pygame.time.Clock() #to set fps

snake_body=[[80,30],[70,30]]

food_pos=[random.randrange(1,(600//10))*10, random.randrange(1,(500//10))*10]

food=True #to know in change of food position

score=0

def display_score():
    font=pygame.font.SysFont('georgia',50)
    Font=font.render('Score: '+str(score),True,'white')
    rect=Font.get_rect()
    screen.blit(Font,rect) #display text on screen

def game_over():
    font=pygame.font.SysFont('georgia',50)
    Font=font.render('GAME OVER Score: '+str(score),True,'red')
    rect=Font.get_rect()
    rect.midtop=(600//2,500//4)
    screen.blit(Font,rect)
    pygame.display.flip()
    time.sleep(2) #pause program for 2sec then auto quit
    exit() #auto exit after game over 
    
# HANDLING MOVEMENTS
dir='RIGHT' #initial direction of movement
next_dir=dir

while True:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_UP:
                next_dir='UP'
            if event.key==K_DOWN:
                next_dir='DOWN'
            if event.key==K_LEFT:
                next_dir='LEFT'
            if event.key==K_RIGHT:
                next_dir='RIGHT'
    #updating dir with next_dir
    if next_dir=='UP' and dir!='DOWN': #while moving down we can next move only in x-axis 
        dir='UP'
    if next_dir=='DOWN' and dir!='UP':
        dir='DOWN'
    if next_dir=='LEFT' and dir!='RIGHT':
        dir='LEFT'
    if next_dir=='RIGHT' and dir!='LEFT':
        dir='RIGHT'
    
    #moving snake
    if dir=='UP':
        snake_pos[1]-=10
    if dir=='DOWN':
        snake_pos[1]+=10
    if dir=='RIGHT':
        snake_pos[0]+=10
    if dir=='LEFT':
        snake_pos[0]-=10
    
    snake_body.insert(0,list(snake_pos))

    if snake_pos[0]==food_pos[0] and snake_pos[1]==food_pos[1]:
        score+=10
        food=False
    else:
        snake_body.pop()
    if not food:
        food_pos=[random.randrange(1,(600//10))*10, random.randrange(1,(500//10))*10]
    food=True
    screen.fill('black')
    # screen.blit(bg,(0,0))

    for pos in snake_body: #drawing snake
        pygame.draw.rect(screen,'green',(pos[0],pos[1],10,10))
    pygame.draw.circle(screen,'red',(food_pos[0],food_pos[1]),5)

    #game over conditions
    if snake_pos[0]<0 or snake_pos[0]>600-10: #left or right wall
        game_over()
    if snake_pos[1]<0 or snake_pos[1]>500-10: #up or down wall
        game_over()
    for b in snake_body[1:]: #eats own body
        if snake_pos[0]==b[0] and snake_pos[1]==b[1]:
            game_over()
    
    display_score() #displays score all time

    pygame.display.update()
    clk.tick(snake_speed)
    
        
    


            




