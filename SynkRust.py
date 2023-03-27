from systemVariables import systemVariables
from keyProcessor import *

from os import listdir, startfile
from os.path import basename, dirname, realpath
from re import match
from sys import exit, argv
from time import sleep
from tkinter import Tk, filedialog

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *





class mainApplication(QMainWindow):
    
    def __init__(self):
        ...
    
    
    
    
    
    def createCommonVariables(self):
        ...
    
    
    
    
    
    def createMainUserInterface(self):
        ...





def startUp():
    
    application = QApplication(argv)
    applicationInitializer = mainApplication()
    applicationInitializer.show()
    exit(application.exec())
        
        
        


if __name__ == '__main__':
    
    try:
        startUp()
    
    except Exception as errorCode:
        print(f"An error has occured!\n{errorCode}")
        sleep(5)
        exit()