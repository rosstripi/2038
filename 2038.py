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

# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2
 
    # get the height of the font
    fontHeight = font.size("Tg")[1]
 
    while text:
        i = 1
 
        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # see if current character is a newline
        #if text[0] == "\n":
        #    i = rect.width
            
        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
 
        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1
 
        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)
 
        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
 
        # remove the text we just blitted
        text = text[i:]
 
    return text


def leave_game():
    print "Exiting game..."
    pygame.quit()
    sys.exit()

def getButtonAtPixel(x, y, items):
    for recta, item in items:
        if x in range(recta.left, recta.right + 1) and y in range(recta.top, recta.bottom + 1):
            return recta
    return None
            
def fade_out(objects=currentObjects):
    alpha = 255
    alpha_vel = -1

    # fade alpha out while waiting    
    while alpha > 0:        
        # get key input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                #leave_game()
            
        # draw
        alpha += alpha_vel

        windowSurface.fill(BLACK)
        for recta, item in objects:
            item.set_alpha(alpha)
            windowSurface.blit(item, recta)
        pygame.display.flip()
        pygame.time.delay(5)

def fade_in(objects=currentObjects):
    alpha = 0
    alpha_vel = 1

    # fade alpha in while waiting    
    while alpha < 255:        
        # get key input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                #leave_game()
            
        # draw
        alpha += alpha_vel

        windowSurface.fill(BLACK)
        for recta, item in objects:
            item.set_alpha(alpha)
            windowSurface.blit(item, recta)
        pygame.display.flip()
        pygame.time.delay(10)

def main_menu_loop():
    mousex, mousey = 0, 0
    # create main menu
    # set up main menu background
    background = pygame.Rect(windowSurface.get_rect().left - 450,
                             windowSurface.get_rect().top,
                             760, 1024)

    lowerCityImage = pygame.image.load('assets/art/mainmenu.jpg').convert()
    lowerCityScaledImage = pygame.transform.scale(lowerCityImage, (1024, 1024))
    currentObjects.append((background, lowerCityImage))

    # set up the title and menu
    titleFont = pygame.font.SysFont(None, 30)
    title = titleFont.render('2038', True, BLACK)
    titleRect = title.get_rect()
    titleRect.centerx = windowSurface.get_rect().centerx + 114
    titleRect.top = windowSurface.get_rect().top
    currentObjects.append((titleRect, title))

    menuFont = pygame.font.SysFont(None, 26)
    newgame = menuFont.render('new game', True, BLACK)
    newgameRect = newgame.get_rect()
    newgameRect.centerx = windowSurface.get_rect().centerx
    newgameRect.top = windowSurface.get_rect().top + 15

    loadgame = menuFont.render('load game', True, BLACK)
    loadgameRect = loadgame.get_rect()
    loadgameRect.centerx = windowSurface.get_rect().centerx
    loadgameRect.top = windowSurface.get_rect().top + 37

    menubuttons = [(newgameRect, newgame), (loadgameRect, loadgame)]
    for item in menubuttons:
        currentObjects.append(item)
    
    # blit main menu elements
    for recta, item in currentObjects:
        windowSurface.blit(item, recta)
    # draw the window onto the screen
    pygame.display.update()

    # setup main game clock
    #mainClock = pygame.time.Clock()

    mainClock.tick(1)
    # update window
    pygame.display.update()

    startmenubool = True
    while startmenubool:
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                print "from start menu loop"
                leave_game()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        buttonrect = getButtonAtPixel(mousex, mousey, menubuttons)
        if buttonrect != None and mouseClicked:
            if buttonrect == newgameRect:
                fade_out()
                del currentObjects[:]
                startmenubool = False
                #load_computer_lab()
                intro_sequence()
##########################################################
# METHODS FOR LOADING LOCATIONS                          #
##########################################################
def intro_sequence():
    introString ="""It is the year 2038. Contrary to predictions by Moore's Law that computing power would ultimately cap by 2020, the performance of computing machines has continued to grow steadily with no ceiling in sight. 

Concurrent to the continuing advancement of computers, humankind has begun to experience a rapid, albeit self-regulated, evolution. Neural implants, readily available prosthetic body parts, finally realized stem cell treatments. 

These changes have given rise to questions about the state of man:

What is an individual? His physical parts? Or his self-concept? 
Are we playing God? 
Does it even matter?
"""

    introFont = pygame.font.SysFont("courier", 18)
    introRect = pygame.Rect(windowSurface.get_rect().left + 10,
                            windowSurface.get_rect().top + 10, 
                            windowSurface.get_width() - 200,
                            windowSurface.get_height() - 20)
                            
    curIndex = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print "from intro sequence"
                leave_game()
            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN: #skip intro sequence
                windowSurface.fill(BLACK)
                pygame.display.update()
                del currentObjects[:]
                load_computer_lab()
                return
                
        """
        introText = introFont.render(introString[:curIndex], True,
                                     GREEN, BLACK)
        introRect = introText.get_rect()
        introRect.top = windowSurface.get_rect().top + 10
        introRect.left = windowSurface.get_rect().left + 10
        introRect.width = windowSurface.get_rect().width - 20
        introRect.height = windowSurface.get_rect().height - 20
        #currentObjects.append((introRect, introText))
        windowSurface.blit(introText, introRect)
        """
        windowSurface.fill(BLACK)
        drawText(windowSurface, introString[:curIndex],
                 GREEN, introRect, introFont, True, BLACK)
        pygame.display.update()
        mainClock.tick(15)
        curIndex += 1


def load_computer_lab():
    print "loading lab area"
    del currentObjects[:]
    # set up main menu background
    background = pygame.Rect(windowSurface.get_rect().left - 250,
                             windowSurface.get_rect().top - 150,
                             760, 1024)

    computerLabImage = pygame.image.load('assets/art/computerlab.jpg').convert()
    currentObjects.append((background, computerLabImage))
    fade_in()
    computer_screen_maximize()

def computer_screen_maximize(objects=currentObjects):
    print "maximizing screen"
    screenmaxwidth = int(1024 * .8)
    screenmaxheight = int(760 * .8)
    screencurrwidth = 0
    screencurrheight = 0
    screenRect = pygame.Rect(windowSurface.get_rect().centerx, windowSurface.get_rect().centery, screencurrwidth, screencurrheight)
    screenImage = pygame.image.load('assets/art/screen.jpg').convert()
    screenScaledImage = pygame.transform.scale(screenImage, (screencurrwidth, screencurrheight))

    while (screencurrwidth, screencurrheight) <= (screenmaxwidth, screenmaxheight):
        # get key input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                #leave_game()
        screencurrwidth, screencurrheight = int(screencurrwidth + (screenmaxwidth * .01)), int(screencurrheight + (screenmaxheight * .01))
        for recta, item in objects:
            windowSurface.blit(item, recta)
        #screenRect = pygame.Rect(windowSurface.get_rect().centerx, windowSurface.get_rect().centery, screencurrwidth, screencurrheight)
        screenRect.width, screenRect.height = screencurrwidth, screencurrheight
        screenRect.centerx = windowSurface.get_rect().centerx
        screenRect.bottom = int(760 * .9)
        #screenImage = pygame.image.load('assets/art/screen.jpg').convert()
        screenScaledImage = pygame.transform.scale(screenImage, (screencurrwidth, screencurrheight))
        windowSurface.blit(screenScaledImage, screenRect)
        pygame.display.flip()
        #pygame.time.delay(10)
    objects.append((screenRect, screenScaledImage)) #adds screen to objects
    
##########################################################
# MAIN GAME OPERATIONS                                   #
#   run main_menu_loop()                                 #
##########################################################

main_menu_loop()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print "from runner loop"
            leave_game()
