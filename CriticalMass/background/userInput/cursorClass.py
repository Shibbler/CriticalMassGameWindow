################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: cursorClass.py
################################################################################



################################################################################
#### Imports
################################################################################

import pygame
pygame.init()



################################################################################
#### Class
################################################################################

class Cursor(pygame.sprite.Sprite):

    def __init__(self, playerList):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        pygame.mouse.set_visible(0)


        self.playerList = playerList
        self.currentPlayer = self.playerList[0]

        # create a plain rectangle for the sprite image
        self.image = pygame.Surface((40,40))
        self.image.fill(BLACK)
        self.pointer = pygame.Surface((10,10))
        self.pointer.fill(WHITE)
        self.fgImage = pygame.Surface((28, 28))
        self.setPlayer(self.currentPlayer)

        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def setPlayer(self, currentPlayer):
        self.currentPlayer = currentPlayer
        self.fgImage.fill(self.currentPlayer.teamColor)
        self.image.blit(self.pointer, (3,3))
        self.image.blit(self.fgImage, (6,6))



