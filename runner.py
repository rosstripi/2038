"""
Author: rossbot

Description: a point-and-click post-cyberpunk story/game

"""

# import necessary files for system calls and pygame libraries
import pygame, sys, time, random
# import constants from pygame
from pygame.locals import *


# initialize pygame
pygame.init()

# create some default variables
FPSCLOCK = pygame.time.Clock()

WINDOWWIDTH = 1024
WINDOWHEIGHT = 760
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

# current objects to be displayed on screen
currentObjects = []

mousex = 0
mousey = 0
pygame.display.set_caption('2038')
mainClock = pygame.time.Clock()

# set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
