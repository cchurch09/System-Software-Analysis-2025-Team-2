import pygame as pg

class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def newName(self, name):
        self.name = name

    def newColor(self, color):
        self.color = color

player1 = Player("Player 1", pg.color.Color(255, 255, 255))
player2 = Player("Player 2", pg.color.Color(255, 255, 255))
