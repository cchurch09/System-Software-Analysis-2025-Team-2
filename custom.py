import tkinter as tk
import player
from tkinter import messagebox

class customMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customization Menu")
        windowButton = tk.Button(self, "Change window size")
        windowButton.pack()