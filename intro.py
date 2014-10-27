"""
Author: rossbot

intro sequence for 2038
"""

import pygame, sys, time, random
# import constants from pygame
from pygame.locals import *

# set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

def intro_sequence(windowSurface=pygame.display.set_mode((1024, 760), 0, 32), mainClock=pygame.time.Clock(), currentObjects=[]):
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
                
        
        windowSurface.fill(BLACK)
        drawText(windowSurface, introString[:curIndex],
                 GREEN, introRect, introFont, True, BLACK)
        pygame.display.update()
        mainClock.tick(15)
        curIndex += 1

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

if __name__ == '__main__':
    print "this is the intro sequence"

    # initialize pygame
    pygame.init()
    pygame.display.set_caption('intro')
    intro_sequence()