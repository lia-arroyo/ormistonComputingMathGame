# Ormiston Computing User Class
# 24/07/2020
# Lia

import random
import computing_interface

class Students:

    def __init__(self, name, year, option, level):
        self.name = name
        self.year = year
        self.option = option
        self.level = level
        self.points = 0 # starts off with zero points

        self.ranges()

    def ranges(self): # customisable ranges for each level and option

        # for multiplication
        if self.level == "Easy" and self.option == "Multiplication": # Easy tests students from 1 to 10
            self.start = 1
            self.end = 10

        elif self.level == "Medium" and self.option == "Multiplication": # Medium tests students from 5 to 15
            self.start = 5
            self.end = 15

        elif self.level == "Hard" and self.option == "Multiplication": # Hard tests students from 15 to 20
            self.start = 15
            self.end = 20

        # for addition

        elif self.level == "Easy" and self.option == "Addition": # Easy tests 1 to 20
            self.start = 1
            self.end = 20

        elif self.level == "Medium" and self.option == "Addition": # Medium tests 10 to 20
            self.start = 10
            self.end = 20

        else: # Hard + Addition tests 20 to 50
            self.start = 20
            self.end = 50

        self.questions()
            
    def questions(self):

        num1 = random.randint(self.start, self.end)
        num2 = random.randint(self.start, self.end)

        if self.option == "Addition":
            correct_answer = num1 + num2
            display = "{} + {} = {}".format(num1,num2,correct_answer)

        else: # multiplication
            correct_answer = num2 * num2
            display = "{} x {} = {}".format(num1, num2, correct_answer)
        
        computing_interface.Interface.questions_frame(num1, num2, correct_answer)