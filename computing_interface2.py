# Ormiston Computing Interface Class Redo
# 27/07/2020
# Lia

from tkinter import *
from user import *

class Interface:

    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.restart = False

        # Setting minimum sizes for window
        self.parent_window.minsize(450, 250)
        self.parent_window.columnconfigure(1, minsize=150)
        self.parent_window.columnconfigure(2, minsize=150)
        self.parent_window.columnconfigure(3, minsize=150)

        # Changing default background to blue
        self.parent_window.configure(background="#00ffff")
        
    def start(self):
        self.start_frame = Frame(self.parent_window)
        self.start_frame.grid()

         # Minimum row size
        self.parent_window.rowconfigure(2, minsize=50)
        self.parent_window.rowconfigure(3, minsize=50)
        self.parent_window.rowconfigure(4, minsize=50)

        # Welcome text
        Label(self.start_frame, text="Ormiston Computing", bg="#00ffff", font=("Helvetica", 14, 'bold'), pady = 20).grid(row=1, column=1, columnspan = 3)

        # Name and year
        Label(self.start_frame, text="Name:", bg="#00ffff", font=("Helvetica", 12, 'bold')).grid(row=2, column=1)
        self.name = Entry(self.start_frame, width=30)
        self.name.grid(row=2, column=2, columnspan=2)

        Label(self.start_frame, text="Year:", bg="#00ffff", font=("Helvetica", 12, 'bold')).grid(row=3, column=1)
        self.year = Entry(self.start_frame, width=30)
        self.year.grid(row=3, column=2, columnspan=2)

        
