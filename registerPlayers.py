import tkinter as tk
from tkinter import colorchooser
"""
from player import player1
from player import player2
"""
from player import players

class registerPlayers(tk.Tk):
    def __init__(self):
        super().__init__()
        print("registerPlayers was called") # diagnostic print statement
        i = 0
        while i < 2:
            print(players[i].name)
            i += 1
        self.title("Register Players")
        # The actual labels, buttons, and entry boxes
        registerMessage = tk.Label(self, text='Please enter player names: ')
        player1Label = tk.Label(self, text='Player 1: ')
        self.player1Entry = tk.Entry(self, textvariable='player1')
        player1Color = tk.Button(self, text='Player 1 Color', command=lambda: self.chooseColor(players[0].color))
        player2Label = tk.Label(self, text='Player 2: ')
        self.player2Entry = tk.Entry(self, textvariable='player2')
        player2Color = tk.Button(self, text='Player 2 Color', command=lambda: self.chooseColor(players[1].color))
        confirmButton = tk.Button(self, text='Confirm', command=lambda: self.confirmPlayers())
        registerMessage.pack()
        player1Label.pack()
        self.player1Entry.pack()
        player1Color.pack()
        player2Label.pack()
        self.player2Entry.pack()
        player2Color.pack()
        confirmButton.pack()

    def chooseColor(self, playerColor):
        color_code = colorchooser.askcolor(title="Pick Player Color")
        print(color_code)
        playerColor = color_code[1]
        print(playerColor)

    def confirmPlayers(self):
        print("confirmPlayers was called")
        if players[0].name != self.player1Entry.get():
            players[0].name = self.player1Entry.get()
            players[0].wins = 0
            players[0].losses = 0
            print(players[0].name, " has ", players[0].wins, " wins and ", players[0].losses, " losses")
        else:
            print(players[0].name, " no changes")
            print(players[0].name, " has ", players[0].wins, " wins and ", players[0].losses, " losses")
        
        if players[1].name != self.player1Entry.get():
            players[1].name = self.player2Entry.get()
            players[1].wins = 0
            players[1].losses = 0
            print(players[1].name, " has ", players[1].wins, " wins and ", players[1].losses, " losses")
        else:
            print(players[1].name, " no changes")
            print(players[1].name, " has ", players[1].wins, " wins and ", players[1].losses, " losses")
        """
        player1.name = self.player1Entry.get()
        player2.name = self.player2Entry.get()
        print(player1.name, player2.name)
        """
        self.destroy()
