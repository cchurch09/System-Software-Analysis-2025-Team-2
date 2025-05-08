"""
Project Name: Group2Project.py
Author: Brenden Melody, Darcy Ralstin, Cailli Church
Date last updated: 13 April 2025
Description: Program is designed to play a version of Pong that allows players
            to choose their names and colors.
"""

import tkinter as tk
import PongExample2
import registerPlayers
import customMenu
import player
import pygame as pg
from tkinter import messagebox
from game import game1

"""
This module actually initializes the main menu with the 3 main buttons to start the game
change the name of the players, and to close the game.
"""
def main():
    mainMenu = tk.Tk()
    mainMenu.title("Pong")
    mainMenu.geometry("500x500")
    welcomeMessage = tk.Label(mainMenu, text="Welcome to Pong!")
    multiButton = tk.Button(mainMenu, text="Play Pygame Game", command=lambda: game1.main())
    tkinterButton = tk.Button(mainMenu, text="Play tkinter game")
    registryButton = tk.Button(mainMenu, text="Register Players", command=lambda: registerPlayers.registerPlayers())
    customButton = tk.Button(mainMenu, text ="Customization Menu", command=lambda: customMenu.customMenu())
    exitButton = tk.Button(mainMenu, text="Exit", command=mainMenu.quit)

    welcomeMessage.pack()
    multiButton.pack()
    tkinterButton.pack()
    registryButton.pack()
    customButton.pack()
    exitButton.pack()
    mainMenu.mainloop()
    


if __name__ == '__main__':
    main()