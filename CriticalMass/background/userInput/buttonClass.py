################################################################################
#    CREATOR: Lucas Cowell
#    DATE: 27/12/2017
#    FILE NAME: buttonClass.py
################################################################################



################################################################################
#### Imports
################################################################################

from createText import *
import pygame
pygame.init()



################################################################################
#### Class
################################################################################

################################################################################
# Class: BoxBar
# DESCRIPTION:
# This is a class for an interactive sprite button, with parameters for text and
# return values for when its been pressed.
################################################################################

class Button(pygame.sprite.Sprite):


################################################################################
##FUNCTION: __init__
##DESCRIPTION:
##This function initializes the fields for use in button creation.
##INPUTS:
##self: The Button Object
##screen: the values of the screen where the button is placed
##buttonRect: the rectangle the button will be attached to
##buttonIndex: used to check status of button
##buttonText: The text to be displayed on the button
##bgColor: the background color
##ALGORITHM:
##INITIALIZE Sprite with parameter of self
##INITIALIZE font for sprite
##SET buttonFont to freesansbold, size of 15
##DEPRIVATIZE buttonRect and buttonIndex
##IF buttonIndex is equal to None,
##   SET buttonIndex to 9
##ELSE DEPRIVATIZE buttonIndex
##IF buttonText is equal to None,
##   SET buttonText to 'Button'
##ELSE DEPRIVATIZE buttonText
##IF bgColor is equal to None,
##   SET bgColor to BLACK
##ELSE DEPRIVATIZE bgColor
#ENDIF
##SET mouseOverButton, buttonDown, and buttonUp to False
##SET visible to True
##SET buttonDimensions to a buttonRect of size 2
##SET image to the surface of a size given by buttonDimensions
##FILL the image with color: BLACK
##Now to define the states of the buttons: inactive, activeUp and activeDown
##SET inactive to surface of size given by buttonDimensions
##FILL inactive surface with bgColor
##SET inactiveFg to surface with buttonDimensions 0-10, 1-10
##FILL inactiveFg with color GREY3
##ATTACH inactiveFg to the inactive button surface
##SET activeUp to surface of size given by buttonDimensions
##FILL activeUp surface with bgColor
##SET activeUp to surface with buttonDimensions 0-10, 1-10
##FILL activeUp with color GREY4
##ATTACH activeUpFg to the activeUp button surface
##SET activeDown to surface of size given by buttonDimensions
##FILL activeDown surface with bgColor
##SET activeDownFg to surface with buttonDimensions 0-10, 1-10
##FILL activeDownFg with color GREY5
##ATTACH activeDownFg to the activeDown button surface
##ATTACH image to inactive button state
##CREATE rect using get_rect() function with image values
##SET topleft of rect to equal buttonrect with given paramater 2
################################################################################

    def __init__(self, screen, buttonRect, buttonIndex = None, buttonText = None, fontSize = None, textColor = None, bgColor = None):

        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()

        #Assign all values dummy values if none are given by method calling this method
        self.buttonRect = buttonRect
        if buttonIndex == None: self.buttonIndex = 9
        else: self.buttonIndex = buttonIndex
        if buttonText == None: self.buttonText = "Button"
        else: self.buttonText = buttonText
        if fontSize == None: self.fontSize = 15
        else: self.fontSize = fontSize
        if textColor == None: self.textColor = GREY8
        else: self.textColor = textColor
        if bgColor == None: self.bgColor = BLACK
        else: self.bgColor = bgColor

        #set booleans to be overriden by mouse
        self.mouseOverButton = False
        self.buttonDown = False
        self.buttonUp = False
        self.visible = True

        #Set image button will be placed on
        buttonDimensions = self.buttonRect[2:]
        self.image = pygame.Surface(buttonDimensions)
        self.image.fill(BLACK)

        #define inactive Surface
        self.inactive = pygame.Surface(buttonDimensions)
        self.inactive.fill(self.bgColor)
        self.inactiveFg = pygame.Surface((5,5))
        self.inactiveFg.fill(GREY3)
        self.inactive.blit(self.inactiveFg, (5,5))
        self.inactiveText = createTextSurface(self.buttonText, buttonDimensions, self.fontSize, self.textColor, GREY3)
        self.inactive.blit(self.inactiveText, (5,5))

        #define activeUp Surface
        self.activeUp = pygame.Surface(buttonDimensions)
        self.activeUp.fill(self.bgColor)
        self.activeUpFg = pygame.Surface((5,5))
        self.activeUpFg.fill(GREY4)
        self.activeUp.blit(self.activeUpFg, (5,5))
        self.activeUpText = createTextSurface(self.buttonText, buttonDimensions, self.fontSize, self.textColor, GREY4)
        self.activeUp.blit(self.activeUpText, (5,5))

        #define activeDown Surface
        self.activeDown = pygame.Surface(buttonDimensions)
        self.activeDown.fill(self.bgColor)
        self.activeDownFg = pygame.Surface((5,5))
        self.activeDownFg.fill(GREY5)
        self.activeDown.blit(self.activeDownFg, (5,5))
        self.activeDownText = createTextSurface(self.buttonText, buttonDimensions, self.fontSize, self.textColor, GREY5)
        self.activeDown.blit(self.activeDownText, (5,5))

        #Finalize Sprite specifications
        self.image.blit(self.inactive, (0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (buttonRect[:2])


################################################################################
##FUNCTION: update
##DESCRIPTION:
##This function tells the button how to behave when pressed or hovered over
##INPUTS:
##self: the Button object
##ALGORITHM:
##GET mouse position from function get_pos()
##GET mouse status from function get_pressed()
##IF mouseOverButton is False and the variable collidepoint, which tells whether the mouse is over the button is True,
##    SET mouseOverButton to True
##    ATTACH image to activeUp, on co-ordinates (0,0)
##ELSEIF mouseOverButton is False and the variable collidepoint, which tells whether the mouse is over the button is False,
##    SET mouseOverButton to False
##    ATTACH image to inactive, on co-ordinates (0,0)
##ENDIF
##SET buttonUp to False
##IF mouseOverButton is True:
##    IF NOT buttonDown and mouseButtonStatus is equal to 1:
##        SET buttonDown to True
##        ATTACH image to activeDown, on co-ordinates (0,0)
##    ELIF buttonDown and mouseButton is equal to 0:
##        SET buttonDown to False
##        SET buttonUp to True
##        ATTACH image to activeUp, on co-ordinates (0,0)
##    ENDIF
##ENDIF
################################################################################

    def update(self):
        mousePos = pygame.mouse.get_pos()
        mouseButtonStatus = pygame.mouse.get_pressed()

        #Update variables that represent mouse over button to whether False or True, depending on whether or not the mouse is over the button
        if not self.mouseOverButton and self.rect.collidepoint(mousePos):
            self.mouseOverButton = True
            self.image.blit(self.activeUp, (0,0))
        elif self.mouseOverButton and not self.rect.collidepoint(mousePos):
            self.mouseOverButton = False
            self.image.blit(self.inactive, (0,0))

        #Update variuables that represent whether or not the mouse has been pushed, to False or True.
        self.buttonUp = False
        if self.mouseOverButton:
            if not self.buttonDown and mouseButtonStatus[0] == 1:
                self.buttonDown = True
                self.image.blit(self.activeDown, (0,0))
            elif self.buttonDown and mouseButtonStatus[0] == 0:
                self.buttonDown = False
                self.buttonUp = True
                self.image.blit(self.activeUp, (0,0))

    def move(self, xVect, yVect):
        self.rect = self.rect.move(xVect, yVect)







################################################################################
#### Program
################################################################################

# First line




