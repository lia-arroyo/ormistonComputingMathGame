# Ormiston Computing Interface Class
# 24/06/2020
# Lia

from tkinter import *
from user import *
from tkinter import messagebox

# Interface class
class Interface:

    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.restart = False

        # Setting minimum sizes for window 
        self.parent_window.minsize(450, 250)
        self.parent_window.columnconfigure(1, minsize=150)
        self.parent_window.columnconfigure(2, minsize=150)
        self.parent_window.columnconfigure(3, minsize=150)

    def start(self):
        self.parent = Frame(self.parent_window)
        self.parent_window.configure(background="#00ffff") #changing bg to blue
        self.parent.grid()

        # Minimum row size
        self.parent_window.rowconfigure(2, minsize=50)
        self.parent_window.rowconfigure(3, minsize=50)
        self.parent_window.rowconfigure(4, minsize=50)

        # Welcome text
        Label(self.parent_window, text="Ormiston Computing", bg="#00ffff", font=("Helvetica", 14, 'bold'), pady = 20).grid(row=1, column=1, columnspan = 3)

        
        # Name and year
        Label(self.parent_window, text="Name:", bg="#00ffff", padx=25, font=("Helvetica", 12, 'bold')).grid(row=2, column=1, sticky=E)
        self.name = Entry(self.parent_window, width=30)
        self.name.grid(row=2, column=2, columnspan=2)

        Label(self.parent_window, text="Year:", bg="#00ffff", padx=25, font=("Helvetica", 12, 'bold')).grid(row=3, column=1, sticky=E)
        self.year = Entry(self.parent_window, width=30)
        self.year.grid(row=3, column=2, columnspan=2)
        
        # Buttons - Quit and Next
        quit_btn = Button(self.parent_window, text="Quit", bg="#ff0000", width=10, font=("Helvetica", 10, 'bold'), command=self.quit)
        quit_btn.grid(row=4, column=1, columnspan=2)

        next_btn = Button(self.parent_window, text="Next", bg="#abab0a", width=10, font=("Helvetica", 10, 'bold'), command=self.error)
        next_btn.grid(row=4, column=2, columnspan=2)

    def error(self):

        # Getting students data before destroying widgets
        self.name = self.name.get().title()
        self.year = self.year.get().title()

        # Sending data to user class (creating an instance)
        self.student = Students(self.name, self.year) 
        
        if self.year not in ["6","7","8"]:
            messagebox.showerror("ERROR", "For year level, please enter a whole number from 6 to 8. This program is intended for Year 6 to 8 only.")
            Interface.start(self)

        elif self.name == "":
            messagebox.showerror("ERROR", "Please enter your name.")
            Interface.start(self)

        else:
            Interface.home(self)

    def home(self):
        
        # destroying widgets from previous frame
        for widget in self.parent_window.winfo_children() :
            widget.destroy()
        
        # Welcome text
        Label(self.parent_window, text="Ormiston Computing", bg="#00ffff", font=("Helvetica", 14, 'bold'), pady = 20).grid(row=1, column=1, columnspan = 3)

        # Buttons
        start_btn = Button(self.parent_window, text="Start", bg="#ffff00", font=("Helvetica", 14, 'bold'), width=8, command=self.option)
        start_btn.grid(row=2, column=2, rowspan=2)

        quit_btn = Button(self.parent_window, text="Quit", bg="#ff0000", font=("Helvetica", 12, 'bold'), width=6, command=self.quit)
        quit_btn.grid(row=3, column=2, rowspan=2)

        # Footer text
        help_link = Button(self.parent_window, text="Help?", padx = 25, bg="#00ffff", fg="#0000ff", borderwidth=0, font=("Helvetica", 8, 'underline'), command=self.help)
        help_link.grid(row=5, column=1, sticky=W)
        
        Label(self.parent_window, text="Creator : Thong & Lia", bg="#00ffff", font=("Helvetica", 8), pady = 20).grid(row=5, column=3)


    def help(self):
        # destroying widgets from previous frame
        for widget in self.parent_window.winfo_children() :
            widget.destroy()

        # Header "instructions" text
        Label(self.parent_window, text="Instructions:", padx=25, pady=25, bg="#00ffff", borderwidth=0, font=("Helvetica", 14, 'bold')).grid(row=1, column=1)
        home_btn = Button(self.parent_window, text="Home", bg="#abab0a", font=("Helvetica", 10, 'bold'), width=9, command=self.home)
        home_btn.grid(row=1, column=3)

        Label(self.parent_window, bg="#00ffff", width = 25, text='''Simply type your answer to the question in the text box below the question then click Submit. \n
        The program will then show you if you are correct or not. Click next to answer the next question. Example Below:''', font=("Helvetica", 14, 'bold')).grid(row=2, column=1, columnspan=3)

        
        
    def option(self):
        # destroying widgets from previous frame
        for widget in self.parent_window.winfo_children() :
            widget.destroy()
            
        # Minimum row size
        self.parent_window.rowconfigure(2, minsize=10)
        self.parent_window.rowconfigure(3, minsize=60)
        self.parent_window.rowconfigure(4, minsize=60)

        # Welcome, [student] text
        Label(self.parent_window, text="Welcome, {}".format(self.name), bg="#00ffff", font=("Helvetica", 14, 'bold'), pady = 20).grid(row=1, column=1, columnspan = 3)

        # Question
        Label(self.parent_window, text="Which topic would you like to practice?", bg="#00ffff", font=("Helvetica", 12, 'bold')).grid(row=2, column=1, columnspan = 3)
        
        # Buttons
        addition_btn = Button(self.parent_window, text="Addition [+]", bg="#ffff00", font=("Helvetica", 10, 'bold'), pady = 8, padx = 35, width=8)
        addition_btn.grid(row=3, column=2)
        
        multiplication_btn = Button(self.parent_window, text="Multiplication [x]", bg="#ffff00", font=("Helvetica", 10, 'bold'), pady = 8, padx = 35, width=8)
        multiplication_btn.grid(row=4, column=2)
        
    def quit(self):
        self.parent_window.destroy()

