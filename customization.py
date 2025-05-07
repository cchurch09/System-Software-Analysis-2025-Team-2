"""
File Name: customization.py
Author: Brenden Melody
Date last updated: 5/2/2025
Purpose: This module facilitates all of the customization options via boolean values
"""


class Customization():
    def __init__(self):
        self.paddleRotation = True
        self.multiBall = False
        self.ballCount = 2
        self.ballColor = (255, 255, 255)
        self.rallyMode = False
        self.singleRally = False
        self.freePlay = False

    def update_mode(self, selection):
        if selection == "1-Player Rally":
            self.singleRally = True
        elif selection == "2-Player Rally":
            self.rallyMode = True
        elif selection == "Standard":
            self.rallyMode = False
            self.singleRally = False


customGame = Customization()
