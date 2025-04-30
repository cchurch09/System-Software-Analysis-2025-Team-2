import tkinter as tk
import player
import ball
from tkinter import messagebox
from tkinter import colorchooser

class customMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customization Menu")
        rotatePaddlesOn = tk.Button(self, text="Turn on rotating paddles")
        rotatePaddlesOff = tk.Button(self, text="Turn off rotating paddles")
        ballColor = tk.button(self, text="Choose Ball Color", command=lambda: self.ballColor(ball.ball1.color))
        rotatePaddlesOn.pack()
        rotatePaddlesOff.pack()
        ballColor.pack()


    def ballColor(self, ballColor):
        color_code = colorchooser.askcolor(title="Pick Ball Color")
        ballColor = color_code[1]
        print(color_code)
        print(ballColor)
