################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: createShip.py
################################################################################



################################################################################
#### Imports
################################################################################

from shipClass import *

import pygame
pygame.init()

################################################################################
#### Function
################################################################################

def createScout(location, shipImage):
    Scout = Ship(location, shipImage, 2, 250)
    return Scout

def createCruiser(location, shipImage):
    Cruiser = Ship(location, shipImage, 1.5, 650)
    return Cruiser

def createDestroyer(location, shipImage):
    Destroyer = Ship(location, shipImage, 1, 1000)
    return Destroyer
