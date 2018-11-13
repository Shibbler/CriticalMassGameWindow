################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: gameDisplay.py
################################################################################



################################################################################
#### Imports
################################################################################

from playerClass import *
from imageLoader import *

from mainCreation import *
from mainMovement import *
from mainUserInput import *

import __builtin__

import pygame
pygame.init()
event = pygame.event




################################################################################
#### Class
################################################################################

class mainDisplayWindow():

    def __init__(self):
        pygame.init()

        self.animateSurface = True
        self.count = 0
        self.time = pygame.time.Clock()

        self.screen = pygame.display.set_mode((screenDomain, screenRange))
        pygame.display.set_caption = 'THE BATTLE FEILD... except it\'s not a feild it\'s an ocean... THE BATTLE OCEAN!!!'

        loadAllImages()

        self.background = pygame.sprite.LayeredUpdates()
        self.backgroundImage = Background(self.screen)
        self.background.add(self.backgroundImage)
        self.background.draw(self.screen)

        self.alertScreen = AlertNotice("")
        self.alert = False

        self.shipsInMotion = False
        self.attackSetActive = False
        self.moveSetActive = False

        self.playerList = []
        imageList = [scout_red, cruiser_red, destroyer_red]
        dropCordList = [[100,200],[150,200],[250,200]]
        self.Player1 = Player(self.screen, 0, "RICK", RED, imageList, dropCordList)
        self.playerList.append(self.Player1)
        imageList = [scout_blue, cruiser_blue, destroyer_blue]
        dropCordList = [[screenDomain - 75,screenRange - 300],[screenDomain - 150,screenRange - 300],[screenDomain - 275,screenRange - 300]]
        self.Player2 = Player(self.screen, 1, "MORTY", DRKBLUE, imageList, dropCordList)
        self.playerList.append(self.Player2)
        self.currentPlayer = self.playerList[0]

        self.interactiveBarsList = []
        self.interactiveBarsGroup = pygame.sprite.LayeredUpdates()
        self.AllSprites = pygame.sprite.LayeredUpdates()

        mainBarButtons = (["\nCOMPLETE\nTURN"],["\nCrew\n(VOID)"],["\nStore\n(VOID)"],["\nSettings\n(VOID)"])
        self.mainBar = InteractiveBar(self.screen, mainBarButtons, 0, "Main")
        self.interactiveBarsList.append(self.mainBar)
        self.interactiveBarsGroup.add(self.mainBar)
        self.AllSprites.add(self.mainBar)

        shopBarButtons = (["\nScout\n75 Sj"],["\nCruiser\n150 Sj"],["\nDestroyer\n250 Sj"])
        self.shopBar = InteractiveBar(self.screen, shopBarButtons, 1, "Shop")
        self.interactiveBarsList.append(self.shopBar)
        self.interactiveBarsGroup.add(self.shopBar)
        self.AllSprites.add(self.shopBar)

        moveBarButtons = (["\nRest"],["\nSlow\nSpeed"],["\nNormal\nSpeed"],["\nFast\nSpeed"])
        self.moveBar = InteractiveBar(self.screen, moveBarButtons, 2, "Move")
        self.interactiveBarsList.append(self.moveBar)
        self.interactiveBarsGroup.add(self.moveBar)
        self.AllSprites.add(self.moveBar)

        combatBarButtons = (["\nBurst\nLaser\n(VOID)"],["\nPhoton\nTorpedos\n(VOID)"],["\nHeavy\nMissile\n(VOID)"])
        self.combatBar = InteractiveBar(self.screen, combatBarButtons, 3, "Combat")
        self.interactiveBarsList.append(self.combatBar)
        self.interactiveBarsGroup.add(self.combatBar)
        self.AllSprites.add(self.combatBar)

        self.cursorGroup = pygame.sprite.LayeredUpdates()
        self.cursor = Cursor(self.playerList)
        self.cursorGroup.add(self.cursor)
        self.AllSprites.add(self.cursorGroup)

    def animateGameDisplay(self):
        self.roundNum = 1

        self.events()

        while self.animateSurface:
            self.time.tick(FPS)
            self.update()

            if self.moveSetActive: self.setMove()
            elif self.attackSetActive: pass
            else: self.checkButtons()

            self.draw()
            self.events()

    def events(self):
        for e in event.get():
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_ESCAPE:
                    self.quit()
                    self.animateSurface = False
                    return None

    def update(self):
        if not self.alert:
            self.currentPlayer.update()
            if self.shipsInMotion:
                print "Round",str(self.roundNum),"Complete"
                self.roundNum += 1
                self.shipsInMotion = False
            self.mainBar.update()
            self.shopBar.update()
            self.moveBar.update()
            self.combatBar.update()
            self.cursorGroup.update()
        else: self.alert = self.alertScreen.update()

    def setMove(self):
        for ship in self.currentPlayer.fleet.shipList:
            if ship.shipSelected:
                self.currentPlayer.pathLine.vertex = ship.rect.center
                ship.shipSelected = False
                self.moveSetActive = False


    def checkButtons(self):
        for spriteGroup in self.interactiveBarsList:
            if spriteGroup.activatedElement != None:
                elementBar = spriteGroup.activatedElement[0]
                elementButt = spriteGroup.activatedElement[1]
                if not self.alert:
                    if elementBar == 0:
                        if elementButt == 'a': self.switchSeperateBars(spriteGroup, elementBar)
                        elif elementButt == 0: self.endTurn()
                    if elementBar == 1:
                        if elementButt == 'a': self.switchSeperateBars(spriteGroup, elementBar)
                        else: self.purchaseShip(elementButt)
                    if elementBar == 2:
                        if elementButt == 'a': self.switchSeperateBars(spriteGroup, elementBar)
                        else: self.startMoveSet(elementButt)
                    if elementBar == 3:
                        if elementButt == 'a': self.switchSeperateBars(spriteGroup, elementBar)
                        else: self.startAttackSet(elementButt )
                else: spriteGroup.activatedElement = None

    def draw(self):
        if not self.alert:
            self.background.draw(self.screen)
            self.currentPlayer.draw()
            for player in self.playerList: player.fleet.draw(self.screen)
            if self.mainBar.visible: self.mainBar.draw(self.screen)
            if self.shopBar.visible: self.shopBar.draw(self.screen)
            if self.moveBar.visible: self.moveBar.draw(self.screen)
            if self.combatBar.visible: self.combatBar.draw(self.screen)
            self.cursorGroup.draw(self.screen)
        else: self.screen.blit(self.alertScreen.image, self.alertScreen.rect.topleft)

        pygame.display.flip()                                                  #

    def switchSeperateBars(self, spriteGroup, elementBar):
        sepereateBars = self.interactiveBarsList[:]
        pressedBar = sepereateBars.pop(elementBar)
        if spriteGroup.barOpening:
            for bar in sepereateBars:
                if bar.visible: bar.turnOff = True
            self.activeBar = pressedBar
        elif spriteGroup.barClosing:
            for bar in sepereateBars:
                bar.turnOn = True
                bar.visible = True
            self.activeBar = None

    def purchaseShip(self, unitID):
        if unitID == 0:
            if self.currentPlayer.money >= 75:
                self.currentPlayer.money -= 75
                self.currentPlayer.fleet.buyShip(0)
                self.currentPlayer.updateStatBar()
            else:
                self.alert = True
                self.alertScreen.setText("You cant afford this ship")
        if unitID == 1:
            if self.currentPlayer.money >= 150:
                self.currentPlayer.money -= 150
                self.currentPlayer.fleet.buyShip(1)
                self.currentPlayer.updateStatBar()
            else:
                self.alert = True
                self.alertScreen.setText("You cant afford this ship")
        if unitID == 2:
            if self.currentPlayer.money >= 250:
                self.currentPlayer.money -= 250
                self.currentPlayer.fleet.buyShip(2)
                self.currentPlayer.updateStatBar()
            else:
                self.alert = True
                self.alertScreen.setText("You cant afford this ship")

    def startMoveSet(self, moveID):
        if len(self.currentPlayer.fleet.shipList) == 0:
            self.alert = True
            self.alertScreen.setText("There are no ships to move!")
        else:
            self.currentPlayer.pathLine = PathPresetLine(self.screen, self.currentPlayer.teamColor, (moveID * 100) + 100)
            self.moveSetActive = True


    def startAttackSet(self, attackID):
        pass

    def endTurn(self):
        nextPlayerIdx = self.playerList.index(self.currentPlayer) + 1
        if nextPlayerIdx == len(self.playerList):
            nextPlayerIdx = 0
            self.shipsInMotion = True
        self.currentPlayer = self.playerList[nextPlayerIdx]
        self.cursor.setPlayer(self.currentPlayer)

    def quit(self):
        pygame.quit()

class Background(pygame.sprite.Sprite):
    def __init__(self, screen, bgColor = None):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        if bgColor == None: self.bgColor = WHITE
        else: self.bgColor = bgColor

        self.image = backgroundSpace
        self.rect = pygame.rect.Rect(0,-300,screenDomain,screenRange)



