# Ormiston Computing Interface Class
# 24/06/2020
# Lia

from tkinter import *
from tkinter import messagebox
from user_class import Students

# Interface class
class Interface:

    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.restart = False
        self.error_tested = False

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

        next_btn = Button(self.parent_window, text="Next", bg="#abab0a", width=10, font=("Helvetica", 10, 'bold'), command=self.error1)
        next_btn.grid(row=4, column=2, columnspan=2)

    def error1(self):

        try:
            # Getting students data before destroying widgets
            self.name = self.name.get().title()
            self.year = int(self.year.get())
            
        except ValueError:

            testyear = self.year.get() # doesn't save year level as integer, allows to test for no input
            
            if self.name == "" and testyear == "": # if both are not entered/empty
                messagebox.showerror("ERROR", "Please enter your name and your year level.")
                self.start()

            elif self.name != "" and testyear == "": # if only the year level is empty
                messagebox.showerror("ERROR", "Please enter your year level.")
                self.start()

            elif self.name == "": # if name is empty and year level is invalid
                messagebox.showerror("ERROR", "Please enter your name, and enter a whole number from 6 to 8 for year level.")
                self.start()

            else: # if year level is not an integer
                messagebox.showerror("ERROR", "Please enter a whole number from 6 to 8 for year level.")
                self.start()
                
        else:                

            if self.year not in range(6,9) and self.name != "": # if name is expected but year level is outside boundary
                messagebox.showerror("ERROR", "This program is intended for Year 6 to 8 only. Please enter a whole number from 6 to 8.")
                self.start()

            elif self.name == "" and self.year in range(6,9): # if no name is entered but year level is expected
                messagebox.showerror("ERROR", "Please enter your name.")
                self.start()

            elif self.name == "" and self.year not in range(6,9): # if no name is entered and year level is outside boundary
                messagebox.showerror("ERROR", "Please enter your name and year level. This program is intended for Year 6 to 8 only.")
                self.start()

            else:
                self.home()

    def home(self):

        # Minimum row size
        self.parent_window.rowconfigure(2, minsize=50)
        self.parent_window.rowconfigure(3, minsize=50)
        self.parent_window.rowconfigure(4, minsize=50)
        self.parent_window.rowconfigure(6, minsize=0)
        
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
        self.levels()

    def multiplication(self):

        self.option_chosen = "Multiplication"
        # Moving to next frame
        self.levels()
        
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

        medium_btn = Button(self.parent_window, text="Medium", bg="#ffff00", font=("Helvetica", 12, 'bold'), pady = 6, width=10, command=self.medium)
        medium_btn.grid(row=4, column=2)

        hard_btn = Button(self.parent_window, text="Hard", bg="#ffff00", font=("Helvetica", 12, 'bold'), pady = 6, width=10, command=self.hard)
        hard_btn.grid(row=5, column=2)

    # LEVEL OPTIONS   
    def easy(self):
        self.level_chosen = "Easy"
        self.transfer()

    def medium(self):
        self.level_chosen = "Medium"
        self.transfer()

    def hard(self):
        self.level_chosen = "Hard"
        self.transfer()

    # END OF LEVEL OPTIONS

    def transfer(self):
        # sending data to user class (creating an instance)
        self.student = Students(self.name, self.year, self.option_chosen, self.level_chosen)
        self.qinfo = self.student.ranges()

        self.points = self.qinfo[0] # starts w zero
        self.question_num = self.qinfo[1] # starts at 1 
        
        self.questions_frame()

    def questions_frame(self): # displaying question and results page
        # destroying widgets from previous frame
        for widget in self.parent_window.winfo_children():
            widget.destroy()

        self.parent_window.configure(background="#00ffff")
        
        if self.error_tested == False:

            generated_questions = self.student.questions()

            self.num1 = generated_questions[0]
            self.num2 = generated_questions[1]
            self.correct_answer = generated_questions[2]

        else:
            self.error_tested = False # turning it back to false for the next question

        if self.question_num < 11: # 10 questions)

            # Header
            Label(self.parent_window, text="LEVEL: {}".format(self.level_chosen), bg="#00ffff", font=("Helvetica", 12, 'bold'), pady=10, padx=10).grid(row=1, column=1,sticky= "W")
            Label(self.parent_window, text="POINTS: {}".format(self.points), bg="#00ffff", font=("Helvetica", 12, 'bold'), padx=10).grid(row=2, column=1,sticky= "W")

            home_btn = Button(self.parent_window, text="Home", bg="#abab0a", font=("Helvetica", 10, 'bold'), width=9, command=self.home)
            home_btn.grid(row=1, column=3, rowspan=2, columnspan=2, sticky="E", padx=10)

            Label(self.parent_window, text="Question {}".format(self.question_num), bg="#00ffff", font=("Helvetica", 14, 'bold'), pady=10, padx=10).grid(row=3, column=1, columnspan=3)
            
            # Question

            if self.option_chosen == "Addition":
                Label(self.parent_window, text="{} + {}".format(self.num1, self.num2), bg="#00ffff", font=("Helvetica", 18, 'bold'), pady=2).grid(row=4, column=2)

            else:
                Label(self.parent_window, text="{} x {}".format(self.num1, self.num2), bg="#00ffff", font=("Helvetica", 18, 'bold'), pady=2).grid(row=4, column=2)

            # Answer
            self.answer = Entry(self.parent_window, width=7, justify="center", font=("Helvetica", 18, 'bold'))
            self.answer.grid(row=5, column=2, ipady = 5)

            # Submit button
            submit_btn = Button(self.parent_window, text="Submit", bg="#ffff00", width=11, font=("Helvetica", 10, 'bold'), pady=5, command=self.error2)
            submit_btn.grid(row=6, column=2, pady=30)

        else:
            self.final_results()

    def error2(self):

        try:
            self.answer = int(self.answer.get())

        except ValueError:
            messagebox.showerror("ERROR", "Please enter a valid whole number.")
            self.error_tested = True
            self.questions_frame()

        else:
            self.result_frame()
        
    def result_frame(self):

        # Calling check_answers function from user class
        results = self.student.check_answers(self.answer)

        self.correct = results[0]
        self.points = results[1]
        self.question_num = results[2]

        # destroying widgets from previous frame
        for widget in self.parent_window.winfo_children():
            widget.destroy()

        # Changing bg and text to say if it is correct or not
        if self.correct == 1:
            bg_colour = "#66ff66" #changing bg to green
            Label(self.parent_window, text="Correct!", font=("Helvetica", 16, 'bold'), bg=bg_colour).grid(row=2, column=2)

        else:
            bg_colour ="#ff6666" #changing bg to red
            Label(self.parent_window, text="Incorrect!", font=("Helvetica", 16, 'bold'), bg=bg_colour).grid(row=2, column=2)

        # Styling frame
        self.parent_window.configure(background=bg_colour)
        self.parent_window.rowconfigure(1, minsize=60)
        self.parent_window.rowconfigure(5, minsize=0)
        
        # Answer
        if self.option_chosen == "Addition":
            Label(self.parent_window, text="{} + {} = {}".format(self.num1, self.num2, self.correct_answer), bg=bg_colour, font=("Helvetica", 20, 'bold')).grid(row=3, column=2)

        else:
            Label(self.parent_window, text="{} x {} = {}".format(self.num1, self.num2, self.correct_answer), bg=bg_colour, font=("Helvetica", 20, 'bold')).grid(row=3, column=2)

        # Displaying the points
        Label(self.parent_window, text="POINTS: {}".format(self.points), bg=bg_colour, font=("Helvetica", 16, 'bold')).grid(row=4, column=2)

        nextq_btn = Button(self.parent_window, text="Next", bg="#ffff00", width=11, font=("Helvetica", 10, 'bold'), pady=5, command=self.questions_frame)
        nextq_btn.grid(row=5, column=2, pady=10)
        
    def final_results(self):

        # Header
        quit_btn = Button(self.parent_window, text="Quit", bg="#ff0000", width=9, font=("Helvetica", 10, 'bold'), command=self.quit)
        quit_btn.grid(row=1, column=1, sticky="W", padx=10)

        home_btn = Button(self.parent_window, text="Home", bg="#abab0a", font=("Helvetica", 10, 'bold'), width=10, command=self.home)
        home_btn.grid(row=1, column=3, sticky="E", padx=10)

        # Congrats or Game Over
        if self.points > 6: # for points 7 and over
            Label(self.parent_window, text="Congratulations!!", bg = "#00ffff", font=("Helvetica", 14, 'bold')).grid(row=2, column=2)
            next_btn = Button(self.parent_window, text="Next", bg="#abab0a", font=("Helvetica", 10, 'bold'), width=10, command=self.levels)
            next_btn.grid(row=5, column=2)
        
        else:
            Label(self.parent_window, text="Game Over", bg = "#00ffff", font=("Helvetica", 14, 'bold')).grid(row=2, column=2)
            restart_btn = Button(self.parent_window, text="Restart", bg="#abab0a", font=("Helvetica", 10, 'bold'), width=10, command=self.transfer)
            restart_btn.grid(row=5, column=2)
            
        Label(self.parent_window, text="Total Questions: 10\nCorrect: {}".format(self.points), bg="#ffff00", font=("Helvetica", 12, 'bold'), borderwidth=1, relief="solid", width=30, pady=15, padx=15, justify="left", anchor="w").grid(row=3, rowspan=2, column=1, columnspan=3)

    def quit(self):
        self.parent_window.destroy()

