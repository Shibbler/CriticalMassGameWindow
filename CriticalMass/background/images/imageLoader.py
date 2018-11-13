################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: imageLoader.py
################################################################################



################################################################################
#### Imports
################################################################################

from os import path
img_dir = "C:\\Users\\cbary\\Desktop\\Education\\Grade 12\\Semester 1\\3 ComSci\\Lucas_C_Caleb_B_Summative_ICS4U\\background\\images"

import __builtin__
import pygame
pygame.init()



################################################################################
#### Function
################################################################################

def openImage(fileName):
    pic = pygame.image.load(path.join(img_dir, fileName)).convert()
    pic.set_colorkey((255,242,0), pygame.RLEACCEL)
    return pic

def loadAllImages():
    __builtin__.backgroundSpace = openImage("backgroundSpace.jpg")
    __builtin__.scout_red = openImage("ScoutRed.png")
    __builtin__.cruiser_red = openImage("CruiserRed.png")
    __builtin__.destroyer_red = openImage("DestroyerRed.png")
    __builtin__.scout_blue = openImage("ScoutBlue.png")
    __builtin__.cruiser_blue = openImage("CruiserBlue.png")
    __builtin__.destroyer_blue = openImage("DestroyerBlue.png")



