"""
File Name: customization.py
Author: Team 2
Date last updated: 5/2/2025
Purpose: This module initializes the players and all of their values in game, also allows all of their values to be modified
"""

import pygame as pg

class Player():
    def __init__(self, name, color):
        # initializing initial calues
        self.name = name
        self.color = color
        self.wins = 0
        self.losses = 0
        self.rally = 0

    def newName(self, name):
        self.name = name

    def newColor(self, color):
        self.color = color

players = []
for i in range(2):
    j = str(i + 1)
    players.append(Player("Player " + j, (255, 255, 255)))
    print(players[i].name)


"""
player1 = Player("Player 1", pg.color.Color(255, 255, 255))
player2 = Player("Player 2", pg.color.Color(255, 255, 255))
"""
