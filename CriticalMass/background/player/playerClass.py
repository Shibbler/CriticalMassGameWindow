################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: playerClass.py
################################################################################



################################################################################
#### Imports
################################################################################

from displayBarClass import *
from playerFleetClass import *
import pygame
pygame.init()



################################################################################
#### Class
################################################################################

class Player():
    def __init__(self, screen, teamIndex, teamName, teamColor, teamShipDropCordList, shipPictureList):
        # this line is required to properly create the sprite

        self.screen = screen
        self.teamName = teamName
        self.teamIndex = teamIndex
        self.teamColor = teamColor
        self.teamShipDropCordList = teamShipDropCordList

        self.statChanged = False
        self.money = 1000

        self.fleet = PlayerFleet(teamShipDropCordList, shipPictureList, self.teamColor)
        self.pathLine = None

        self.barBoxList = [["Money\nData","You have:\n" + str(self.money) + " Sj"], ["Who am I","I am " + self.teamName], ["How many \nships do I have?", str(self.fleet.numShips)]]
        self.statBar = self.setStatBar([0,1],self.barBoxList)

    def setStatBar(self, BarTopRight, BarBoxes):
        return BoxBar(self.screen, BarTopRight, BarBoxes, self.teamColor)

    def updateStatBar(self):
        self.barBoxList = [["Money\nData","You have:\n" + str(self.money) + " Sj"], ["Who am I","I am " + self.teamName], ["How many \nships do I have?", str(self.fleet.numShips)]]
        self.statBar = self.setStatBar([0,1],self.barBoxList)

    def update(self):
        self.statBar.update()
        self.fleet.update()
        if self.pathLine != None:
            self.pathLine.update()
            if self.pathLine.setLocation: self.pathLine = None
        
    def draw(self):
        self.statBar.draw(self.screen)
        if self.pathLine != None: self.pathLine.draw()

