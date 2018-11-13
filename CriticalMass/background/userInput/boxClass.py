################################################################################
#    CREATOR: Lucas Cowell
#    DATE: 27/12/2017
#    FILE NAME: boxClass.py
################################################################################



################################################################################
#### Imports
################################################################################

from createText import *
import pygame
pygame.init()



################################################################################
#### Class
################################################################################

class Box(pygame.sprite.Sprite):

    def __init__(self, screen, boxRect, boxIndex = None, inactiveBoxText = None, activeBoxText = None, textColor = None, bgColor = None):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()

        self.boxRect = boxRect
        if boxIndex == None: self.boxIndex = 9
        else: self.boxIndex = boxIndex
        if inactiveBoxText == None: self.boxInactiveText = "NO TEXT"
        else: self.boxInactiveText = inactiveBoxText
        if activeBoxText == None: self.boxActiveText = self.boxInactiveText
        else: self.boxActiveText = activeBoxText
        if textColor == None: self.textColor = WHITE
        else: self.textColor = textColor
        if bgColor == None: self.bgColor = BLACK
        else: self.bgColor = bgColor
        

        self.mouseOverBox = False
        self.boxDown = False
        self.boxUp = False
        self.visible = True

        boxDimensions = self.boxRect[2:]
        self.image = pygame.Surface(boxDimensions)
        self.image.fill(BLACK)

        self.inactiveText = createTextSurface(self.boxInactiveText, boxDimensions, 15, self.textColor, GREY7)
        self.activeText = createTextSurface(self.boxActiveText, boxDimensions, 15, self.textColor, GREY8)
        
        self.inactive = pygame.Surface(boxDimensions)
        self.inactive.fill(self.bgColor)
        self.inactiveFg = pygame.Surface((boxDimensions[0] - 10, boxDimensions[1] - 10))
        self.inactiveFg.fill(GREY7)
        self.inactive.blit(self.inactiveText, (5,5))

        self.active = pygame.Surface(boxDimensions)
        self.active.fill(self.bgColor)
        self.activeFg = pygame.Surface((boxDimensions[0] - 10, boxDimensions[1] - 10))
        self.activeFg.fill(GREY8)
        self.active.blit(self.activeText, (5,5))

        self.image.blit(self.inactive, (0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (boxRect[:2])

    def update(self):
        mousePos = pygame.mouse.get_pos()

        if not self.mouseOverBox and self.rect.collidepoint(mousePos):
            self.mouseOverBox = True
            self.image.blit(self.active, (0,0))
        elif self.mouseOverBox and not self.rect.collidepoint(mousePos):
            self.mouseOverBox = False
            self.image.blit(self.inactive, (0,0))

    def move(self, xVect, yVect):
        self.rect = self.rect.move(xVect, yVect)


