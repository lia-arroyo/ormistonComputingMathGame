# Ormiston Computing Interface Class
# 24/06/2020
# Lia

from tkinter import *
from tkinter import messagebox
import user_class

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

        # instructions + example

        Label(self.parent_window, bg="#00ffff", justify="left", padx=25, text="Simply type your answer to the question in the text box below the question then click Submit. \nThe program will then show you if you are correct or not. Click next to answer the next question. \nExample Below:", wraplength=400, font=("Helvetica", 12, 'bold')).grid(row=2, column=1, columnspan=3, sticky="W")
        Label(self.parent_window, bg="#00ffff", text="2 + 4 = ?", font=("Helvetica", 14, 'bold')).grid(row=3, column=1, columnspan=3)
        Label(self.parent_window, bg="#00ffff", text="Answer here:", font=("Helvetica", 11, 'bold'), pady=25).grid(row=4, column=1, sticky="e")
        Label(self.parent_window, bg="white", text="6", font=("Helvetica", 11, 'bold'), padx=45, bd=1, relief="solid", pady=4).grid(row=4, column=2)        
        
        
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
        addition_btn = Button(self.parent_window, text="Addition [+]", bg="#ffff00", font=("Helvetica", 10, 'bold'), pady = 8, padx = 35, width=8, command=self.addition)
        addition_btn.grid(row=3, column=2)
        
        multiplication_btn = Button(self.parent_window, text="Multiplication [x]", bg="#ffff00", font=("Helvetica", 10, 'bold'), pady = 8, padx = 35, width=8, command=self.multiplication)
        multiplication_btn.grid(row=4, column=2)

    # OPTION FUNCTIONS
    def addition(self):
    
        self.option_chosen = "Addition"
        # Moving to next frame
        Interface.levels(self)

    def multiplication(self):

        self.option_chosen = "Multiplication"
        # Moving to next frame
        Interface.levels(self)
        
    # END OF OPTION FUNCTIONS
    
    def levels(self):

        # destroying widgets from previous frame
        for widget in self.parent_window.winfo_children() :
            widget.destroy()
        
        self.parent_window.rowconfigure(3, minsize=60)
        self.parent_window.rowconfigure(4, minsize=60)
        self.parent_window.rowconfigure(5, minsize=60)
        self.parent_window.rowconfigure(6, minsize=40)
        
        # Chosen option/topic header
        Label(self.parent_window, text="{}".format(self.option_chosen), bg="#00ffff", font=("Helvetica", 14, 'bold'), pady=20).grid(row=1,column=1, columnspan=3)
        Label(self.parent_window, text="Choose a Level".format(self.option_chosen), bg="#00ffff", font=("Helvetica", 12, 'bold'), pady=5).grid(row=2,column=1, columnspan=3)

        # Buttons for each level
        easy_btn = Button(self.parent_window, text="Easy", bg="#ffff00", font=("Helvetica", 12, 'bold'), pady = 6, width=10, command=self.easy)
        easy_btn.grid(row=3, column=2)

        medium_btn = Button(self.parent_window, text="Medium", bg="#ffff00", font=("Helvetica", 12, 'bold'), pady = 6, width=10)
        medium_btn.grid(row=4, column=2)

        hard_btn = Button(self.parent_window, text="Hard", bg="#ffff00", font=("Helvetica", 12, 'bold'), pady = 6, width=10)
        hard_btn.grid(row=5, column=2)

    # LEVEL OPTIONS   
    def easy(self):
        self.level_chosen = "Easy"
        Interface.transfer(self)

    def medium(self):
        self.level_chosen = "Medium"
        Interface.transfer(self)

    def hard(self):
        self.level_chosen = "Hard"
        Interface.transfer(self)

    # END OF LEVEL OPTIONS

    def transfer(self):
        # sending data to user class (creating an instance)
        self.student = Students(self.name, self.year, self.option_chosen, self.level_chosen)
        self.student.questions()
        
    def questions_frame(self, num1, num2, correct_answer):
        # destroying widgets from previous frame
        for widget in self.parent_window.winfo_children():
            widget.destroy()
        
        Label(self.parent_window, text="{} + {} = {}".format(self.num1, self.num2, self.correct_answer)).grid(row=1, column=1)

    def quit(self):
        self.parent_window.destroy()

