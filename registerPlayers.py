import tkinter as tk
import tkinter.colorchooser
from tkinter.colorchooser import askcolor

class registerPlayers(tk.Tk, player1, player2):
    def __init__(self):
        super().__init__()
        print("registerPlayers was called") # diagnostic print statement
        self.title("Register Players")
        # The actual labels, buttons, and entry boxes
        registerMessage = tk.Label(self, text='Please enter player names: ')
        player1Label = tk.Label(self, text='Player 1: ')
        self.player1Entry = tk.Entry(self, textvariable='player1')
        player2Label = tk.Label(self, text='Player 2: ')
        self.player2Entry = tk.Entry(self, textvariable='player2')
        confirmButton = tk.Button(self, text='Confirm', command=lambda: self.confirmPlayers())
        registerMessage.pack()
        player1Label.pack()
        self.player1Entry.pack()
        player2Label.pack()
        self.player2Entry.pack()
        confirmButton.pack()

    def confirmPlayers(self):
        print("confirmPlayers was called")
        """
        global player1
        global player2
        player1 = self.player1Entry.get()
        player2 = self.player2Entry.get()
        print(player1, player2)
        self.destroy()
        """
