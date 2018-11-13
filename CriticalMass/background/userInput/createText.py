################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: createText.py
################################################################################



################################################################################
#### Imports
################################################################################

import pygame
pygame.init()



################################################################################
#### Function
################################################################################

def createTextSurface(text, surfaceDimensions, fontSize, textColor, bgColor):

    textSurfaceFont = pygame.font.Font("freesansbold.ttf", fontSize)
    numLines = text.count('\n') + 0
    if numLines == 0: textList = [text]
    else: textList = text.split('\n')

    textSurface = pygame.surface.Surface((surfaceDimensions[0] - 10, surfaceDimensions[1] - 10))
    textSurface.fill(bgColor)
    fontBlitYLocation = 5

    for line in textList:
        textSurfaceLine = textSurfaceFont.render(line, True, textColor, bgColor)
        textSurface.blit(textSurfaceLine, (5, fontBlitYLocation))
        fontBlitYLocation += fontSize + 2

    return textSurface




