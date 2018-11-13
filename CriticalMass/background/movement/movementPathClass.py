################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: classMovementFunctions.py
################################################################################



################################################################################
#### Imports
################################################################################

import pygame
pygame.init()



################################################################################
#### Class
################################################################################

class PathPresetLine():
    def __init__(self, screen, color, speed):
        self.screen = screen
        self.color = color
        self.speed = speed
        self.vertex = None
        self.lineData = None
        self.clikaDown = False
        self.drawLine = True
        self.setLocation = False
        

    def update(self):
        if self.setLocation:
            self.saveMove()
        if self.vertex != None: 
            mousePos = pygame.mouse.get_pos()
            mouseButtonStatus = pygame.mouse.get_pressed()[0]
            if ((mousePos[1] - self.vertex[1]) ** 2 + (mousePos[0] - self.vertex[0]) ** 2) <= self.speed ** 2:
                self.lineData = (self.screen, self.color, self.vertex, mousePos, 6)
                self.drawLine = True
                self.circleData = (self.screen, GREY3, mousePos, 12)
                if not self.clikaDown and mouseButtonStatus == 1:
                    self.clikaDown = True
                elif self.clikaDown and mouseButtonStatus == 0:
                    self.clikaDown = False
                    self.setLocation = True
                    self.circleData = (self.screen, WHITE, mousePos, 12)
            else:
                self.circleDate = (self.screen, WHITE, mousePos, 12)
                self.drawLine = False

    def draw(self):
        if self.vertex != None and self.lineData != None:
            if self.drawLine:
                pygame.draw.line(self.lineData[0], self.lineData[1], self.lineData[2], self.lineData[3], self.lineData[4])
            pygame.draw.circle(self.circleData[0], self.circleData[1], self.circleData[2], self.circleData[3])

    def saveMove(self):
        pass


