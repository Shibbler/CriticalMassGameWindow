################################################################################
#    CREATOR: Caleb Barynin
#    DATE: 27/12/2017
#    FILE NAME: importFile.py
################################################################################



################################################################################
#### Imports
################################################################################

# Import the search directory list
from sys import path



################################################################################
#### Function
################################################################################

def addNewDirectories(listOfDirectories, baseDirectory=path[0]+'\\background\\'):
    for idx in range(len(listOfDirectories)):
        newFilePath = baseDirectory + listOfDirectories[idx]
        path.insert(idx + 2, newFilePath)
