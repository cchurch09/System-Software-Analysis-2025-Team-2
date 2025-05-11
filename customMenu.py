"""
File Name: customMenu.py
Author: Team 2
Date last updated: 5/10/2025
Purpose: This module uses the customization module with a tkinter GUI to allow players to customize
their game experience
"""

import tkinter as tk
import player
import ball2
from tkinter import messagebox
from tkinter import colorchooser
from customization import customGame

class customMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customization Menu")

        # Game Mode Selection
        tk.Label(self, text="Please Choose Game Mode").pack(pady=10)
        gameModes = ["Standard", "2-Player Rally", "1-Player Rally", "2-Player Free Play"]
        self.selected_mode = tk.StringVar(value=gameModes[0])
        modeChoice = tk.OptionMenu(self, self.selected_mode, *gameModes, command=self.update_game_mode)
        modeChoice.pack()

        
        # Paddle rotation buttons
        self.paddle_rotation_enabled = False # setting paddle rotation to false as baseline
        self.paddle_rotation_button = tk.Button(self, text="Enable Rotating Paddles", command=self.toggle_paddle_rotation)
        self.paddle_rotation_button.pack()
        """
        rotatePaddlesOn = tk.Button(self, text="Turn On Rotating Paddles", command=lambda: customGame.paddleRotation(True))
        rotatePaddlesOff = tk.Button(self, text="Turn Off Rotating Paddles", command=lambda: customGame.paddleRotation(False))
        rotatePaddlesOn.pack()
        rotatePaddlesOff.pack()
        """
        
        # Ball color customization
        ballColor = tk.Button(self, text="Choose Ball Color", command=self.ballColor)
        ballColor.pack()
        
        # Dropdown menu for  of balls
        tk.Label(self, text="How many balls would you like to display?").pack(pady=10)
        options = ["1", "2", "3"]
        self.selected_option = tk.StringVar(value=options[0])
        ballNum = tk.OptionMenu(self, self.selected_option, *options, command=self.update_ball_count)
        ballNum.pack()
        
        # Confirm button to set ball count in game
        confirm_button = tk.Button(self, text="OK", command=lambda: self.confirm_settings())
        confirm_button.pack()

    def enable_paddleRotation(self):
        self.paddleRotation = True

    def disable_paddleRotation(self):
        self.paddleRotation = False

    # This segment allows there to only be one button to manage the paddle rotation
    def toggle_paddle_rotation(self):
        self.paddle_rotation_enabled = not self.paddle_rotation_enabled
        customGame.paddleRotation = self.paddle_rotation_enabled
        if self.paddle_rotation_enabled:
            self.paddle_rotation_button.config(text="Disable Rotating Paddles")
        else:
            self.paddle_rotation_button.config(text="Enable Rotating Paddles")

    # this allows this menu to change the ball's color
    def ballColor(self):
        color_code = colorchooser.askcolor(title="Pick Ball Color")
        if color_code[1]:
            customGame.ballColor = color_code[1]
            print(f"Selected ball color: {customGame.ballColor}")

    # changes the numer of balls allowed to be used in the game
    def update_ball_count(self, value):
        customGame.ballCount = int(value)

    # tells the game which game mode is active
    def update_game_mode(self, selection):
        customGame.update_mode(selection)

    def confirm_settings(self):
        # Print statements to confirm game settings
        print("Game Settings:")
        print(f"Paddle Rotation: {customGame.paddleRotation}")
        print(f"Ball Count: {customGame.ballCount}")
        print(f"Ball Color: {customGame.ballColor}")
        print(f"Game Mode: {self.selected_mode.get()}")
        self.destroy()
        
if __name__ == '__main__':
    app = customMenu()
    app.mainloop()