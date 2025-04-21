import tkinter as tk
from tkinter import colorchooser
from player import player1
from player import player2

class registerPlayers(tk.Tk):
    def __init__(self):
        super().__init__()
        print("registerPlayers was called") # diagnostic print statement
        print(player1.name)
        print(player2.name)
        self.title("Register Players")
        # The actual labels, buttons, and entry boxes
        registerMessage = tk.Label(self, text='Please enter player names: ')
        player1Label = tk.Label(self, text='Player 1: ')
        self.player1Entry = tk.Entry(self, textvariable='player1')
        player1Color = tk.Button(self, text='Player 1 Color', command=lambda: self.chooseColor(player1.color))
        player2Label = tk.Label(self, text='Player 2: ')
        self.player2Entry = tk.Entry(self, textvariable='player2')
        player2Color = tk.Button(self, text='Player 2 Color', command=lambda: self.chooseColor(player2.color))
        confirmButton = tk.Button(self, text='Confirm', command=lambda: self.confirmPlayers())
        registerMessage.pack()
        player1Label.pack()
        self.player1Entry.pack()
        player1Color.pack()
        player2Label.pack()
        self.player2Entry.pack()
        confirmButton.pack()

    def chooseColor(self, playerColor):
        color_code = colorchooser.askcolor(title="Pick Player Color")
        print(color_code)
        playerColor = color_code
        print(playerColor)


    def confirmPlayers(self):
        print("confirmPlayers was called")
        player1.name = self.player1Entry.get()
        player2.name = self.player2Entry.get()
        print(player1.name, player2.name)
        self.destroy()
