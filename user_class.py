# Ormiston Computing User Class
# 24/07/2020
# Lia

import random

class Students:

    def __init__(self, name, year, option, level):
        self.name = name
        self.year = year
        self.option = option
        self.level = level

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

        # initialising variables 
        self.points = 0 # starts off with zero points
        self.question_num = 1 # starts with question 1

        # Sending points and question number only
        send_qinfo = [self.points, self.question_num]
        return send_qinfo
   
    def questions(self):

        num1 = random.randint(self.start, self.end)
        num2 = random.randint(self.start, self.end)

        if self.option == "Addition":
            self.correct_answer = num1 + num2

        else: # multiplication
            self.correct_answer = num1 * num2

        send_question = [num1, num2, self.correct_answer] 
        return  send_question


    def check_answers(self, answer):

        if answer == self.correct_answer:
            correct = 1 # 1 means it is correct
            self.points +=1

        else:
            correct = 0 # 0 means it is incorrect

        self.question_num += 1
        send_result = [correct, self.points, self.question_num]

        return send_result

    def write_file(self):
        file = open("students_report.txt", 'a')
        file.write("\n-------------------------------------")
        file.write("\nName: {} \nYear Level: {} \nTopic: {}\nLevel: {}\nPoints: {}\n".format(self.name, self.year, self.option, self.level, self.points)) 
        file.write("\n-------------------------------------")

        file.close()

        
