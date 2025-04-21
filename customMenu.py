import tkinter as tk
import player
from tkinter import messagebox

class customMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customization Menu")
        rotatePaddlesOn = tk.Button(self, text="Turn on rotating paddles")
        rotatePaddlesOff = tk.Button(self, text="Turn off rotating paddles")
        rotatePaddlesOn.pack()
        rotatePaddlesOff.pack()