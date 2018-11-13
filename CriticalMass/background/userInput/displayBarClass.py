################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: displayBarClass.py
################################################################################



################################################################################
#### Imports
################################################################################

from buttonClass import *
from boxClass import *
import pygame
pygame.init()



################################################################################
#### Class
################################################################################


################################################################################
# Class: BoxBar
# DESCRIPTION:
# This function creates boxes in a bar format for use in UI player stat display
################################################################################

class BoxBar(pygame.sprite.LayeredUpdates):


################################################################################
# FUNCTION: __init__
# DESCRIPTION:
# This function initializes the values for object use
# INPUTS:
#self: The BoxBar Object
#screen: the values of the screen where the button is placed
#barTopRight: the location of the top right point of the rectangle
#boxList: information stored for use in box filler
#bgColor: the background color
#ALGORITHM:
##INITIALIZE the sprite instance
##OPEN the sprites dictionary
##SET activatedElement to None
##DEPRIVATIZE screen and barTopRight
##IF bgColor is equal to None:
##    SET bgColor to GREY8
##ELSE:
##    DEPRIVATIZE bgColor
#ENDIF
##OPEN the boxes dictionary
##SET numberOfBoxes to 0
##SET active to False
##SET visible to True
##SET transitionSpeed to 5
##RUN addBarShell function
##FOR boxInfo IN boxList:
##    IF the length of boxInfo is equal to 0,
##      RUN addBarBox function
##    ELSEIF length of boxInfo is equal to 1,
#       RUN addBarBox function with the first item in boxInfo List
##    ELSEIF length of boxInfo is equal to 2,
#       RUN addBarBox function with the first and second item in boxInfo List
#ENDIF
##    SET self numberOfBoxes to numberOfBoxes PLUS ONE
################################################################################    

    def __init__(self, screen, BarTopRight, boxList, bgColor = None):
        # this line is required to properly create the sprite
        pygame.sprite.LayeredUpdates.__init__(self)
        self.SpritesDict = {}
        self.activatedElement = None

        self.screen = screen
        self.BarTopRight = BarTopRight
        if bgColor == None: self.bgColor = GREY8
        else: self.bgColor = bgColor
        
        self.BoxesDict = {}
        self.numberOfBoxes = 0
        self.active = False
        self.visible = True

        self.addBarShell()
        for boxInfo in boxList:
            if len(boxInfo) == 0: self.addBarBox()
            elif len(boxInfo) == 1: self.addBarBox(boxInfo[0])
            elif len(boxInfo) == 2: self.addBarBox(boxInfo[0], boxInfo[1])
            self.numberOfBoxes += 1


################################################################################
# FUNCTION: addBarShell
# DESCRIPTION:
# This function creates bar shells
# INPUTS:
# self: The BoxBar Object
# ALGORITHM:
##SET barBackground to Barshell class object, with paramaters (0,0) and bgColor
##SET barBackgroundTopLeft to self.barBackground.rect.topleft (this constructor finds the top left of the rect of barBackground)
##ADD barBackground
##SET result of Sprites dictionary "Background" to barBackground
################################################################################

    def addBarShell(self):
        self.barBackground = BarShell([0,0], self.bgColor)
        self.barBackgroundTopLeft = self.barBackground.rect.topleft
        self.add(self.barBackground)
        self.SpritesDict["Background"] = self.barBackground


################################################################################
# FUNCTION: addBarBox
# DESCRIPTION:
# This function creates barboxes
# INPUTS:
# self: The BoxBar Object
# bgColor: the background color
# boxText: the text to be printed onto the box
# ALGORITHM:
##SET numBox to numberOfBoxes
##SET boxRect to contain the 4 values, which in order, decribe the y1 position, y2 position, x1 position, x2 position : (150*numBox PLUS 20*(numBox + 1)), (barBackGroundTopLeft[1] + ((barBackground.barHeight-100)/2)),150,100
##SET box to Box(screen,boxRect,numBox,BoxText, bgColor)
##ADD box
##OPEN sprites dictionary to entry STRING of numBox and SET retrieved to box
##OPEN boxes dictionary to entry STRING of numBox and SET retrieved to box
################################################################################

    def addBarBox(self, boxText = "Box", bgColor = None):
        numBox = self.numberOfBoxes
        boxRect = ((150*numBox) + (20*(numBox + 1)),self.barBackgroundTopLeft[1] + ((self.barBackground.barHeight-100) / 2),150,100)
        box = Box(self.screen, boxRect, numBox, boxText, bgColor)
        self.add(box)
        self.SpritesDict[str(numBox)] = box
        self.BoxesDict[str(numBox)] = box


################################################################################
# FUNCTION: update
# DESCRIPTION:
# This function updates the Box
# INPUTS:
# self: the BoxBar object
# ALGORITHM:
##FOR spritename in SpritesDict:
##    UPDATE sprite dictionary with spriteName
##    SET activatedElement to None
##FOR boxName in BoxesDict:
##    IF BoxesDict[boxName].boxUp is True:
##        SET activatedElement to CONTAIN [barIndex, BoxesDict[boxName].boxIndex]
#ENDIF
################################################################################

    def update(self):
        for spriteName in self.SpritesDict: self.SpritesDict[spriteName].update()
        self.activatedElement = None
        for boxName in self.BoxesDict:
            if self.BoxesDict[boxName].boxUp:
                self.activatedElement = [self.barIndex, self.BoxesDict[boxName].boxIndex]

################################################################################
# Class: InteractiveBar
# DESCRIPTION:
# This function creates interactive buttons in a bar format for use in UI 
# player stat display.
################################################################################

class InteractiveBar(pygame.sprite.LayeredUpdates):


################################################################################
# FUNCTION: __init__
# DESCRIPTION:
# This function initializes the values for object use
# INPUTS:
#self: The InteractiveBar Object
#screen: the values of the screen where the button is placed
#barName: Holds name of Bar 
#buttonList: information stored for use in button filler
#bgColor: the background color
#ALGORITHM:
##INITIALIZE the sprite instance
##OPEN the sprites dictionary
##SET activatedElement to None
##DEPRIVATIZE screen and barTopRight
##IF bgColor is equal to None:
##    SET bgColor to GREY8
##ELSE:
##    DEPRIVATIZE bgColor
#ENDIF
##OPEN the button dictionary
##SET numberOfButtons to 0
##SET barOpening to False
##SET barClosing to False
##SET turnOn to False
##SET turnOff to False
##SET active to False
##SET visible to True
##SET transitionSpeed to 5
##RUN addButtonShell function
##FOR buttonInfo IN buttonList:
##    IF the length of buttonInfo is equal to 0,
#       RUN addButtonbutton function
##    ELSEIF length of buttonInfo is equal to 1,
#           RUN addButtonbutton function with the first item in buttonInfo List
##    ELSEIF length of buttonInfo is equal to 2,
#           RUN addButtonbutton function with the first and second item in buttonInfo List
##    ELSEIF length of buttonInfo is equal to 3,
#           RUN addButtonbutton function with the first, second and third items in buttonInfo List
#ENDIF
#ENDFOR
##    SET self numberOfbuttons to numberOfbuttons PLUS ONE
################################################################################

    def __init__(self, screen, buttonList, barIndex, barName = "New bar", bgColor = None):
        # this line is required to properly create the sprite
        pygame.sprite.LayeredUpdates.__init__(self)
        self.SpritesDict = {}
        self.activatedElement = None

        self.screen = screen
        self.barIndex = barIndex
        self.barName = barName
        if bgColor == None: self.bgColor = GREY8
        else: self.bgColor = bgColor
        
        self.ButtonsDict = {}
        self.numberOfButtons = 0
        self.barOpening = False
        self.barClosing = False
        self.turnOn = False
        self.turnOff = False
        self.active = False
        self.visible = True
        self.transitionSpeed = 10

        self.addBarShell()
        for buttonInfo in buttonList:
            if len(buttonInfo) == 0: self.addBarButton()
            elif len(buttonInfo) == 1: self.addBarButton(buttonInfo[0])
            elif len(buttonInfo) == 2: self.addBarButton(buttonInfo[0], buttonInfo[1])
            elif len(buttonInfo) == 3: self.addBarButton(buttonInfo[0], buttonInfo[1], buttonInfo[2])
            self.numberOfButtons += 1


################################################################################
# FUNCTION: addBarShell
# DESCRIPTION:
# This function creates bar shells
# INPUTS:
# self: The InteractiveBar Object
# ALGORITHM:
##SET barBackground to Barshell class object, with paramaters (0,0) and bgColor
##SET barBackgroundTopLeft to self.barBackground.rect.topleft (this constructor finds the top left of the rect of barBackground)
##ADD barBackground
##SET result of Sprites dictionary "Background" to barBackground
##SET buttonWidth to 75
##SET buttonRect to CONTAIN (((buttonWidth + 25) * barIndex), (self.barBackgroundTopLeft[1]-75), buttonWidth, 75)
##SET barActiveButton to Button class object CONTAINING values (screen, buttonRect, 'a', ('\n'+ barName))
##ADD barActiveButton
##SET result of Sprites dictionary "ActiveButt" to barActiveButton
##SET result of Buttons Dictionary 'a' to barActiveButton
################################################################################

    def addBarShell(self):
        self.barBackground = BarShell([0,screenRange])
        self.barBackgroundTopLeft = self.barBackground.rect.topleft
        self.add(self.barBackground)
        self.SpritesDict["Background"] = self.barBackground
        buttonWidth = 75
        buttonRect = (0 + ((buttonWidth + 25) * self.barIndex), self.barBackgroundTopLeft[1]-75,buttonWidth,75)
        self.barActiveButton = Button(self.screen, buttonRect, 'a', '\n' + self.barName)
        self.add(self.barActiveButton)
        self.SpritesDict["ActiveButt"] = self.barActiveButton
        self.ButtonsDict['a'] = self.barActiveButton


################################################################################
# FUNCTION: addBarBox
# DESCRIPTION:
# This function creates barboxes
# INPUTS:
# self: The InteractiveBar Object
# bgColor: the background color
# buttonText: the text to be printed onto the button
# ALGORITHM:
##SET numButt to numberOfBoxes
##SET buttonRect to contain the 4 values: (150*numButt PLUS 20*(numButt + 1)), (barBackGroundTopLeft[1] + ((barBackground.barHeight-100)/2)),150,100
##SET button to Button(screen,boxRect,numButt,BoxText, bgColor)
##ADD button
##OPEN sprites dictionary to entry STRING of numButt and SET retrieved to button
##OPEN buttons dictionary to entry STRING of numButt and SET retrieved to button
################################################################################

    def addBarButton(self, buttonText = "Button", bgColor = None):
        numButt = self.numberOfButtons
        buttonRect = ((150*numButt) + (20*(numButt + 1)),self.barBackgroundTopLeft[1] + ((self.barBackground.barHeight-100) / 2),150,100)
        button = Button(self.screen, buttonRect, numButt, buttonText, 20, bgColor)
        self.add(button)
        self.SpritesDict[str(numButt)] = button
        self.ButtonsDict[str(numButt)] = button


################################################################################
# FUNCTION: update
# DESCRIPTION:
# This function updates the Bar
# INPUTS:
# self: the InteractiveBar object
# ALGORITHM:
##FOR spritename in SpritesDict:
##    UPDATE sprite dictionary with spriteName
##    SET activatedElement to None
##FOR boxName in BoxesDict:
##    IF BoxesDict[boxName].boxUp is True:
##        SET activatedElement to CONTAIN [barIndex, BoxesDict[boxName].boxIndex]
##IF barOpening, RUN openBar()
##ELIF barClosing, RUN closeBar()
##ELIF turnOn, RUN emergeBar()
##ELIF turnOff, RUN vanishBar()
##ELIF barActiveButton.buttonUp AND visible:
##    IF active:
##        SET barClosing to True
##    ELSE:
##        SET barOpening to True
#           ENDIF
#ENDIF
################################################################################

    def update(self):
        for spriteName in self.SpritesDict: self.SpritesDict[spriteName].update()
        self.activatedElement = None
        for buttonName in self.ButtonsDict:
            if self.ButtonsDict[buttonName].buttonUp:
                self.activatedElement = [self.barIndex, self.ButtonsDict[buttonName].buttonIndex]
        if self.barOpening: self.openBar()
        elif self.barClosing: self.closeBar()
        elif self.turnOn: self.emergeBar()
        elif self.turnOff: self.vanishBar()
        elif self.barActiveButton.buttonUp and self.visible:
            if self.active: self.barClosing = True
            else: self.barOpening = True


################################################################################
# FUNCTION: openBar
# DESCRIPTION:
# This function opens the Bar
# INPUTS:
# self: the InteractiveBar object
# ALGORITHM:
##IF barBackground.rect.y IS GREATER THAN (screenRange - barBackground.barHeight):
##    MOVE AT -transitionSpeed
##ELSE:
##    SET barOpening to False
##    SET active to True
#ENDIF
################################################################################    

    def openBar(self):
        if self.barBackground.rect.y > screenRange - self.barBackground.barHeight:
            self.move(-self.transitionSpeed)
        else:
            self.barOpening = False
            self.active = True


################################################################################
# FUNCTION: closeBar
# DESCRIPTION:
# This function closes the Bar
# INPUTS:
# self: the InteractiveBar object
# ALGORITHM:
##IF barBackground.rect.y IS GREATER THAN screenRange
##    MOVE AT transitionSpeed
##ELSE:
##    SET barOpening to False
##    SET active to False
#ENDIF
################################################################################

    def closeBar(self):
        if self.barBackground.rect.y < screenRange:
            self.move(self.transitionSpeed)
        else:
            self.barClosing = False
            self.active = False


################################################################################
# FUNCTION: emergeBar
# DESCRIPTION:
# This function shows the Bar
# INPUTS:
# self: the InteractiveBar object
# ALGORITHM:
##IF barBackground.rect.y IS GREATER THAN screenRange
##    MOVE AT -transitionSpeed
##ELSE:
##    SET turnOn to False
#ENDIF
################################################################################

    def emergeBar(self):
        if self.barBackground.rect.y > screenRange:
            self.move(-self.transitionSpeed)
        else: 
            self.turnOn = False


################################################################################
# FUNCTION: vanishBar
# DESCRIPTION:
# This function makes the Bar dissappear
# INPUTS:
# self: the InteractiveBar object
# ALGORITHM:
##IF barBackground.rect.y IS LESSER THAN (screenRange PLUS 75)
##    MOVE AT -transitionSpeed
##ELSE:
##    SET turnOff to False
##    SET visible to False
#ENDIF
################################################################################

    def vanishBar(self):
        if self.barBackground.rect.y < screenRange + 75:
            self.move(self.transitionSpeed)
        else:
            self.turnOff = False
            self.visible = False


################################################################################
# FUNCTION: move
# DESCRIPTION:
# This function moves the Bar object
# INPUTS:
# self: the InteractiveBar object
# speed: an int value that tells the bar how quickly to move
# ALGORITHM:
##FOR spritename IN SpritesDict:
##    SpritesDict[spriteName].move(0,speed)
#ENDFOR
################################################################################    

    def move(self, speed):
        for spriteName in self.SpritesDict:
            self.SpritesDict[spriteName].move(0, speed)


################################################################################
# Class: BarShell
# DESCRIPTION:
# This function creates interactive boxes and bars for use in UI
################################################################################

class BarShell(pygame.sprite.Sprite):
    

################################################################################
# FUNCTION: __init__
# DESCRIPTION:
# This function initializes the values for Bar use
# INPUTS:
# self: The BarShell Object
# topRight: the x,y value of where the topRight of a rect lies
# bgColor: the background color
# ALGORITHM:
##INITIALIZE sprites
##IF bgColor is equal to None:
##    SET bgColor to GREY8
##ELSE:
##    DEPRIVATIZE bgColor
#ENDIF
##SET barHeight to 150
##SET image to pygame.Surface(screenDomain, self.barHeight)
##FILL image with color: BLACK
##SET fgImage to pygame.Surface(screenDomain - 20, self.barHeight - 20)
##FILL fgImage with color: bgColor
##ATTACH image to fgImage, (10,10)
##SET rect to pygame.rect.Rect(topRight[0], topRight[1], screenDomain, self.barHeight)
################################################################################

    def __init__(self, topRight, bgColor = None):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)

        if bgColor == None: self.bgColor = GREY8
        else: self.bgColor = bgColor
        self.barHeight = 150
        
        self.image = pygame.Surface((screenDomain, self.barHeight))
        self.image.fill(BLACK)
        self.fgImage = pygame.Surface((screenDomain - 14, self.barHeight - 14))
        self.fgImage.fill(self.bgColor)
        self.image.blit(self.fgImage,(7,7))
        self.rect = pygame.rect.Rect(topRight[0], topRight[1], screenDomain, self.barHeight)


################################################################################
# FUNCTION: setLocation
# DESCRIPTION:
# This function sets location of the Bar
# INPUTS:
# self: the BarShell Object
# The xCord and yCord of a location
# OUTPUTS:
# self: the BarShell Object
# ALGORITHM:
##SET rect.center to (xCord,yCord)
##RETURN self.
################################################################################

    def setLocation(self, (xCord, yCord)):
        self.rect.center = (xCord, yCord)
        return self


################################################################################
# FUNCTION: move
# DESCRIPTION:
# This function moves the Bar
# INPUTS:
# self: the BarShell Object
# The xVect and yVect of movement
# ALGORITHM:
##SET rect to (xVect,yVect)
##RETURN self.
################################################################################

    def move(self, xVect, yVect):
        self.rect = self.rect.move(xVect, yVect)


