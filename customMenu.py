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
        gameModes = ["Standard", "2-Player Rally", "1-Player Rally"]
        self.selected_mode = tk.StringVar(value=gameModes[0])
        modeNum = tk.OptionMenu(self, self.selected_mode, *gameModes)
        modeNum.pack()

        
        # Paddle rotation buttons
        rotatePaddlesOn = tk.Button(self, text="Turn On Rotating Paddles")
        rotatePaddlesOff = tk.Button(self, text="Turn Off Rotating Paddles")
        rotatePaddlesOn.pack()
        rotatePaddlesOff.pack()
        
        # Ball color customization
        ballColor = tk.Button(self, text="Choose Ball Color", command=lambda: self.ballColor(ball2.Ball.color))
        ballColor.pack()
        
        # Dropdown menu for  of balls
        tk.Label(self, text="How many balls would you like to display?").pack(pady=10)
        options = ["1", "2", "3"]
        self.selected_option = tk.StringVar(value=options[0])
        ballNum = tk.OptionMenu(self, self.selected_option, *options)
        ballNum.pack()
        
        # Confirm button to set ball count in game
        confirm_button = tk.Button(self, text="OK")
        confirm_button.pack()


    def ballColor(self, ballColor):
        color_code = colorchooser.askcolor(title="Pick Ball Color")
        ballColor = color_code[1]
        print(color_code)
        print(ballColor)
        
if __name__ == '__main__':
    app = customMenu()
    app.mainloop()