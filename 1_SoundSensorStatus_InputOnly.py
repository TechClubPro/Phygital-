# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:41:04 2019

@author: Innotechway
"""

import Phygital as phy
import pygame
import time


pygame.init()
width=800
height=400

#Create a Screen with dimensions
screen = pygame.display.set_mode( ( width, height) )

#Set a Title of Screen
pygame.display.set_caption('Smart Box')

#Set a background Image for screen
#Background = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/pathbck.jpg").convert()
Background = pygame.image.load("images/SounBackg.jpg").convert()
#Draw screen from location x=0,y=0
screen.blit(Background,(0,0))

#port=input("Please Enter the COM port")
phy.init('COM3')


quit_flag=False
time.sleep(1)

while True:

    soundData=phy.dRead(2)

    if soundData==0:
        path=pygame.image.load("images/Sound_Detected.png").convert_alpha()
        screen.blit(path,(0,0))
        pygame.display.update()
        time.sleep(3)
    else:

        path=pygame.image.load("images/NoSound_Detected.png").convert_alpha()
        screen.blit(path,(0,0))
        pygame.display.update()


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                phy.close()
                pygame.quit()
                quit_flag=True
                break
            
    if quit_flag==True:
         break
            
print('closing')
