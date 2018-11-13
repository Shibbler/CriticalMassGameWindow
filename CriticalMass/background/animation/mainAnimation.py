################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: mainAnimation.py
################################################################################



################################################################################
#### Imports
################################################################################

import __builtin__
from gameDisplay import *




################################################################################
#### Function
################################################################################

def createMainWindow():
    __builtin__.optionsFolder = 'default'
    __builtin__.screenDomain = 1200
    __builtin__.screenRange = 700
    __builtin__.FPS = 50
    __builtin__.BLACK   = (0,0,0)
    __builtin__.GREY9   = (0,0,0)
    __builtin__.GREY8   = (32,32,32)
    __builtin__.GREY7   = (64,64,64)
    __builtin__.GREY6   = (96,96,96)
    __builtin__.GREY5   = (128,128,128)
    __builtin__.GREY4   = (160,160,160)
    __builtin__.GREY3   = (192,192,192)
    __builtin__.GREY2   = (224,224,224)
    __builtin__.GREY1   = (255,255,255)
    __builtin__.YELLOW  = (255,255,0)
    __builtin__.WHITE   = (255,255,255)
    __builtin__.PINK    = (255,105,180)
    __builtin__.PURPLE  = (104,34,139)
    __builtin__.VIOLET  = (138,43,226)
    __builtin__.ORANGE  = (255,140,0)
    __builtin__.DRKBLUE = (16,78,139)
    __builtin__.RED     = (255,0,0)
    GameMap = mainDisplayWindow()
    GameMap.animateGameDisplay()


