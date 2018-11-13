################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: main.py
################################################################################



################################################################################
#### Imports
################################################################################

from importFile import addNewDirectories
listOfDirectories = ["animation", "creation","images","movement",\
                     "player","unit","userInput"]
addNewDirectories(listOfDirectories)

from mainAnimation import *

################################################################################
#### Function
################################################################################

def run():
    createMainWindow()



