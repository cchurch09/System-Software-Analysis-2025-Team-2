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
        self.ballCount = 1
        self.ballColor = (255, 255, 255)
        self.rallyMode = False
        self.singleRally = True
        self.freePlay = False

customGame = Customization()
