################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: alertBlock.py
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

class AlertNotice(pygame.sprite.Sprite):

    def __init__(self, alertText, textColor = None, bgColor = None):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()

        self.text = alertText
        if textColor == None: self.textColor = WHITE
        else: self.textColor = textColor
        if bgColor == None: self.bgColor = BLACK
        else: self.bgColor = bgColor


        self.rect = pygame.rect.Rect(screenDomain/4,screenRange/4,screenDomain/2,screenRange/2)

        self.image = pygame.Surface((screenDomain/2,screenRange/2))
        self.image.fill(BLACK)
        self.message = pygame.Surface((screenDomain/2 - 20, screenRange/2 - 20))
        self.setText("")
        

    def update(self):
        if self.framesLeft > 0:
            self.framesLeft = self.framesLeft - 1
            return True
        else: return False

    def setText(self, alertText):
        self.text = "Warning:\n" + alertText
        self.framesLeft = 60
        self.message.fill(GREY2)
        self.texSurface = createTextSurface(self.text, [350,80], 25, BLACK, GREY2)
        self.message.blit(self.texSurface, (screenDomain/4 - 175,screenRange/4 - 40))
        self.image.blit(self.message, (10,10))

    def move(self, xVect, yVect):
        self.rect = self.rect.move(xVect, yVect)



