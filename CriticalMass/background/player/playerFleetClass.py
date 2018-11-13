################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: playerFleetClass.py
################################################################################



################################################################################
#### Imports
################################################################################

from mainCreation import *
import pygame
pygame.init()



################################################################################
#### Class
################################################################################

class PlayerFleet(pygame.sprite.LayeredUpdates):
    def __init__(self, shipPictureList, ShipDropCordList, color):
        pygame.sprite.LayeredUpdates.__init__(self)
        self.SpritesDict = {}
        self.ShipsDict = {}
        self.shipList = []
        self.pathLine = None
        self.numShips = 0

        self.shipPictureList = shipPictureList
        self.ShipDropCordList = ShipDropCordList
        self.color = color
        self.selectedShip = None

    def buyShip(self, shipID):
        self.numShips += 1
        if shipID == 0: newShip = createScout(self.ShipDropCordList[shipID], self.shipPictureList[shipID])
        if shipID == 1: newShip = createCruiser(self.ShipDropCordList[shipID], self.shipPictureList[shipID])
        if shipID == 2: newShip = createDestroyer(self.ShipDropCordList[shipID], self.shipPictureList[shipID])
        self.add(newShip)
        self.SpritesDict[str(self.numShips)] = newShip
        self.ShipsDict[str(self.numShips)] = newShip
        self.shipList.append(newShip)

    def update(self):
        self.selectedShip = None
        for shipName in self.ShipsDict:
            self.ShipsDict[shipName].update()
            if self.ShipsDict[shipName].shipSelected:
                self.selectedShip = self.ShipsDict[shipName]


