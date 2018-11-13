################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: shipClass.py
################################################################################



################################################################################
#### Imports
################################################################################

import pygame
pygame.init()


################################################################################
#### Class
################################################################################

class Ship(pygame.sprite.Sprite):

    def __init__(self, shipCords, shipImage, deFactor, maxHealth):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()

        
        self.shipImage = shipImage
        size = self.shipImage.get_rect().size
        self.image = pygame.transform.scale(self.shipImage, (int(size[0] / deFactor), int(size[1] / deFactor)))
        self.rect = self.image.get_rect()
        self.rect.topleft = shipCords
        self.maxHealth = maxHealth
        self.health = self.maxHealth

        self.bgColor = BLACK


        self.mouseOverShip = False
        self.shipActive = False
        self.shipSelected = False

        self.angle = 0 # in degrees

    def update(self):
        mousePos = pygame.mouse.get_pos()
        mouseShipStatus = pygame.mouse.get_pressed()

        if not self.mouseOverShip and self.rect.collidepoint(mousePos): self.mouseOverShip = True
        elif self.mouseOverShip and not self.rect.collidepoint(mousePos): self.mouseOverShip = False

        if self.mouseOverShip:
            if not self.shipActive and mouseShipStatus[0] == 1:
                self.shipActive = True
            elif self.shipActive and mouseShipStatus[0] == 0:
                self.shipActive = False
                self.shipSelected = True

    def rotate(self): pass

    def move(self, xVect, yVect):
        self.xCord += xVect
        self.yCord += yVect
        self.rect.topleft = (int(self.xCord),int(self.yCord))


