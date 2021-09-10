from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
import random
import pandas as pd

window = Tk()
window.title('Cricket')
window.geometry('400x400')
window.resizable(False, False)
window['bg'] = '#ddc3a5'

player_name = StringVar()
toss_call = IntVar()

font_style = ('arial', 15)
values = {"1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6}

player_call = 0
computer_call = 0
innings_num = 0
runs_scored = 0
first_batting_score = 0
second_batting_score = 0
match_winner = 0
first_batting = ''
second_batting = ''
match_result = ''

class cricket:
    def __init__(self, player_call, computer_call, innings_num, runs_scored, first_batting_score, second_batting_score, match_winner, first_batting, second_batting, match_result):
        self.player_call = player_call
        self.computer_call = computer_call
        self.innings_num = innings_num
        self.runs_scored = runs_scored
        self.first_batting_score = first_batting_score
        self.second_batting_score = second_batting_score
        self.match_winner = match_winner
        self.first_batting = first_batting
        self.second_batting = second_batting
        self.match_result = match_result
        
    def start(self):
        global window_1
        window_1 = Toplevel()
        window_1.title('Match Starts')
        window_1.geometry('700x320')
        window_1['bg'] = '#ddc3a5'

        lbl_info = Label(window_1, text = 'CRICKET', font = ('arial', 20, 'bold'), bg = '#ddc3a5', padx = 15, pady = 15).pack()
    
        lbl_name = Label(window_1, text = 'Name', font = ('arial', 16, 'bold'), bg = '#ddc3a5').place(x = 30, y = 70)
        ent_name = Entry(window_1, textvariable = player_name, font = ('arial', 15), width = 40).place(x = 220, y = 70)

        lbl_toss = Label(window_1, text = 'Points to Win', font = ('arial', 16, 'bold'), bg = '#ddc3a5').place(x = 30, y = 120)
        position = 220
        for (text, value) in values.items():
            rad_toss = Radiobutton(window_1, text = text, variable = toss_call, value = value, indicator = 0, font = ('arial', 16, 'bold'), bg = '#ddc3a5', padx = 12, pady = 5).place(x = position, y = 110)
            position += 45

        btn_start = Button(window_1, text = 'Call', font = ('arial', 12), bd = 1, width = 11, command = self.toss).place(x = 290, y = 200)

    def toss(self):
        if player_name.get() == '':
            messagebox.showinfo('Info', 'Name field is empty')
        elif toss_call.get() not in [1, 2, 3, 4, 5, 6]:
            messagebox.showinfo('Info', 'Select a number to call')
        else:
            window_1.destroy()
            
            global window_2
            window_2 = Toplevel()
            window_2.title('Toss')
            window_2.geometry('420x280')
            window_2.resizable(False, False)
            window_2['bg'] = '#ddc3a5'

            lbl_toss = Label(window_2, text = 'Toss Result', font = ('arial', 15, 'bold'), bg = '#ddc3a5', padx = 15, pady = 15).pack()
            
            lbl_player_call = Label(window_2, text = (str(player_name.get())).capitalize() + "'s Call", font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 40, y = 80)
            lbl_player_call = Label(window_2, text = toss_call.get(), font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 320, y = 80)

            lbl_computer_call = Label(window_2, text = "Computer's Call", font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 40, y = 120)

            while True:
                computers_call = random.randint(1,6)
                if computers_call != toss_call.get():
                    break
            lbl_computer_call = Label(window_2, text = computers_call, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 320, y = 120)

            self.player_call = toss_call.get()
            self.computer_call = computers_call

            if self.player_call > self.computer_call:
                lbl_player_win = Label(window_2, text = str(player_name.get()).capitalize() + ' won the Toss', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 40, y = 180)        

                btn_bat = Button(window_2, text = 'BAT', font = ('arial', 12), bd = 1, width = 11, command = self.first_bat).place(x = 60, y = 215)
                btn_bowl = Button(window_2, text = 'FIELD', font = ('arial', 12), bd = 1, width = 11, command = self.first_field).place(x = 210, y = 215)
            else:
                lbl_computer_win = Label(window_2, text = 'Computer won the Toss', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 40, y = 180)
                choice = ['Bat', 'Field']
                computer_choice = choice[(random.randint(0, 1))]
                lbl_computer_win = Label(window_2, text = 'Computer chose to ' + computer_choice + ' first', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 40, y = 210)

                window_2.geometry('420x310')
                
                if computer_choice == 'Bat':
                    btn_bowl = Button(window_2, text = 'FIELD', font = ('arial', 12), bd = 1, width = 11, command = self.first_field).place(x = 140, y = 250)
                else:
                    btn_bat = Button(window_2, text = 'BAT', font = ('arial', 12), bd = 1, width = 11, command = self.first_bat).place(x = 140, y = 250)

    def first_bat(self):
        window_2.destroy()
    
        global window_3
        window_3 = Toplevel()
        window_3.title('Batting')
        window_3.geometry('375x320')
        window_3.resizable(False, False)
        window_3['bg'] = '#ddc3a5'

        lbl_info = Label(window_3, text = str(player_name.get()).capitalize() + ' Batting ', font = ('arial', 15, 'bold'), bg = '#ddc3a5', padx = 15, pady = 15).pack()

        lbl_runs = Label(window_3, text = 'Runs Scored', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 70, y = 50)
        lbl_bat = Label(window_3, text = str(player_name.get()).capitalize() + "'s Play", font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 90)

        self.innings_num = 1
        
        self.button()

    def first_field(self):
        window_2.destroy()
    
        global window_3
        window_3 = Toplevel()
        window_3.title('Bowling')
        window_3.geometry('375x320')
        window_3['bg'] = '#ddc3a5'

        lbl_info = Label(window_3, text = str(player_name.get()).capitalize() + ' Bowling ', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 120, y = 10)

        lbl_runs = Label(window_3, text = 'Runs Scored', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 70, y = 50)
        lbl_bat = Label(window_3, text = str(player_name.get()).capitalize() + "'s Play", font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 90)

        self.innings_num = 2
    
        self.button()

    def second_bat(self):
        window_4.destroy()

        global window_3
        window_3 = Toplevel()
        window_3.title('Batting')
        window_3.geometry('375x320')
        window_3.resizable(False, False)
        window_3['bg'] = '#ddc3a5'

        lbl_info = Label(window_3, text = str(player_name.get()).capitalize() + ' Batting ', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 120, y = 10)

        lbl_targ = Label(window_3, text = 'Target', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 70, y = 50)
        lbl_targ = Label(window_3, text = self.first_batting_score + 1, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 220, y = 50)
        lbl_runs = Label(window_3, text = 'Runs Scored', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 70, y = 90)
        lbl_bat = Label(window_3, text = str(player_name.get()).capitalize() + "'s Play", font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 130)

        self.innings_num = 3
        
        self.button()
  
    def second_field(self):
        window_4.destroy()

        global window_3
        window_3 = Toplevel()
        window_3.title('Bowling')
        window_3.geometry('375x320')
        window_3['bg'] = '#ddc3a5'

        lbl_info = Label(window_3, text = str(player_name.get()).capitalize() + ' Bowling ', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 120, y = 10)

        lbl_targ = Label(window_3, text = 'Target', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 70, y = 50)
        lbl_targ = Label(window_3, text = self.first_batting_score + 1, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 220, y = 50)
        lbl_runs = Label(window_3, text = 'Runs Scored', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 70, y = 90)
        lbl_bat = Label(window_3, text = str(player_name.get()).capitalize() + "'s Play", font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 130)

        self.innings_num = 4

        self.button()
                    
    def button(self):
        btn_1 = Button(window_3, text = '1', font = ('arial', 15, 'bold'), bd = 1, width = 4, command = self.one).place(x = 30, y = 240)
        btn_2 = Button(window_3, text = '2', font = ('arial', 15, 'bold'), bd = 1, width = 4, command = self.two).place(x = 80, y = 240)
        btn_3 = Button(window_3, text = '3', font = ('arial', 15, 'bold'), bd = 1, width = 4, command = self.three).place(x = 130, y = 240)
        btn_4 = Button(window_3, text = '4', font = ('arial', 15, 'bold'), bd = 1, width = 4, command = self.four).place(x = 180, y = 240)
        btn_5 = Button(window_3, text = '5', font = ('arial', 15, 'bold'), bd = 1, width = 4, command = self.five).place(x = 230, y = 240)
        btn_6 = Button(window_3, text = '6', font = ('arial', 15, 'bold'), bd = 1, width = 4, command = self.six).place(x = 280, y = 240)

    def one(self):
        if self.innings_num == 1:
            lbl_one = Label(window_3, text = '1', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bowl(1)
        elif self.innings_num == 2:
            lbl_one = Label(window_3, text = '1', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bat(1)
        elif self.innings_num == 3:
            lbl_one = Label(window_3, text = '1', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bowl(1)
        elif self.innings_num == 4:
            lbl_one = Label(window_3, text = '1', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bat(1)
    
    def two(self):
        if self.innings_num == 1:
            lbl_two = Label(window_3, text = '2', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bowl(2)
        elif self.innings_num == 2:
            lbl_two = Label(window_3, text = '2', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bat(2)
        elif self.innings_num == 3:
            lbl_two = Label(window_3, text = '2', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bowl(2)
        elif self.innings_num == 4:
            lbl_two = Label(window_3, text = '2', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bat(2)
      
    def three(self):
        if self.innings_num == 1:
            lbl_three = Label(window_3, text = '3', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bowl(3)
        elif self.innings_num == 2:
            lbl_three = Label(window_3, text = '3', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bat(3)
        elif self.innings_num == 3:
            lbl_three = Label(window_3, text = '3', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bowl(3)
        elif self.innings_num == 4:
            lbl_three = Label(window_3, text = '3', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bat(3)
     
    def four(self):
        if self.innings_num == 1:
            lbl_four = Label(window_3, text = '4', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bowl(4)
        elif self.innings_num == 2:
            lbl_four = Label(window_3, text = '4', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bat(4)
        elif self.innings_num == 3:
            lbl_four = Label(window_3, text = '4', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bowl(4)
        elif self.innings_num == 4:
            lbl_four = Label(window_3, text = '4', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bat(4)
   
    def five(self):
        if self.innings_num == 1:
            lbl_five = Label(window_3, text = '5', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bowl(5)
        elif self.innings_num == 2:
            lbl_five = Label(window_3, text = '5', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bat(5)
        elif self.innings_num == 3:
            lbl_five = Label(window_3, text = '5', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bowl(5)
        elif self.innings_num == 4:
            lb1_five = Label(window_3, text = '5', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bat(5)
   
    def six(self):
        if self.innings_num == 1:
            lbl_six = Label(window_3, text = '6', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bowl(6)
        elif self.innings_num == 2:
            lbl_six = Label(window_3, text = '6', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 90)
            self.first_computer_bat(6)
        elif self.innings_num == 3:
            lbl_six = Label(window_3, text = '6', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bowl(6)
        elif self.innings_num == 4:
            lbl_six = Label(window_3, text = '6', font = ('arial', 15, 'bold'), bd = 3, bg = '#ddc3a5').place(x = 250, y = 130)
            self.second_computer_bat(6)

    def first_computer_bat(self, run):
        lbl_bat = Label(window_3, text = "Computer's Play", font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 20, y = 130)
        cmp_bat = random.randint(1, 6)
        lbl_cbat = Label(window_3, text = cmp_bat, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 250, y = 130)

        if run != cmp_bat:
            self.runs_scored = self.runs_scored + cmp_bat
            lbl_runs = Label(window_3, text = self.runs_scored, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 220, y = 50)
        elif run == cmp_bat:
            window_3.destroy()
            messagebox.showinfo('OUT','Dismissal : COMPUTER IS OUT\n' + 'Computer Call \t' + str(cmp_bat) + '\nYour Call \t\t' +  str(run))

            self.first_batting_score = self.runs_scored
            self.runs_scored = 0
      
            global window_4
            window_4 = Toplevel()
            window_4.title('Summary')
            window_4.geometry('280x260')
            window_4.resizable(False, False)
            window_4['bg'] = '#ddc3a5'

            lbl_info = Label(window_4, text = 'SUMMARY', font = ('arial', 15, 'bold'), bg = '#ddc3a5', padx = 15, pady = 15).pack()

            lbl_name = Label(window_4, text = 'Computer finished batting', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 70)

            lbl_runs = Label(window_4, text = 'Runs Scored ', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 100)
            lbl_runs = Label(window_4, text = self.first_batting_score, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 180, y = 100)

            lbl_targ = Label(window_4, text = 'Target', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 130)
            lbl_targ = Label(window_4, text = self.first_batting_score + 1, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 180, y = 130)
      
            btn_chase = Button(window_4, text = 'Chase', font = ('arial', 12), bd = 1, width = 11, command = self.second_bat).place(x = 80, y = 190)

    def first_computer_bowl(self, run):
        lbl_bowl = Label(window_3, text = "Computer's Play", font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 130)
        cmp_bowl = random.randint(1,6)
        lbl_cbwl = Label(window_3, text = cmp_bowl, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 250, y = 130)
        if run != cmp_bowl:
            self.runs_scored = self.runs_scored + run
            lbl_runs = Label(window_3, text = self.runs_scored, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 220, y = 50)
        elif run == cmp_bowl:
            window_3.destroy()
            messagebox.showinfo('OUT','Dismissal : YOU ARE OUT\n' + 'Your Call \t\t' + str(run) + '\nComputer Call \t' +  str(cmp_bowl))

            self.first_batting_score = self.runs_scored
            self.runs_scored = 0
      
            global window_4
            window_4 = Toplevel()
            window_4.title('Summary')
            window_4.geometry('280x260')
            window_4.resizable(False, False)
            window_4['bg'] = '#ddc3a5'

            lbl_info = Label(window_4, text = 'SUMMARY', font = ('arial', 15, 'bold'), bg = '#ddc3a5', padx = 15, pady = 15).pack()

            lbl_name = Label(window_4, text = str(player_name.get()).capitalize() + ' finished batting', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 70)

            lbl_runs = Label(window_4, text = 'Runs Scored ', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 100)
            lbl_runs = Label(window_4, text = self.first_batting_score, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 180, y = 100)
            
            lbl_targ = Label(window_4, text = 'Target', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 130)
            lbl_targ = Label(window_4, text = self.first_batting_score + 1, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 180, y = 130)
      
            btn_defend = Button(window_4, text = 'Defend', font = ('arial', 12), bd = 1, width = 11, command = self.second_field).place(x = 80, y = 190)

    def second_computer_bat(self, run):
        lbl_bat = Label(window_3, text = "Computer's Play", font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 170)
        cmp_bat = random.randint(1, 6)
        lbl_cbat = Label(window_3, text = cmp_bat, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 250, y = 170)
        self.player = 2
        if run != cmp_bat:
            self.runs_scored = self.runs_scored + cmp_bat
            if self.runs_scored <= self.first_batting_score:
                lbl_runs = Label(window_3, text = self.runs_scored, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 220, y = 90)
            else:
                self.second_batting_score = self.runs_scored
                self.match_winner = 2
                self.winner()
        elif run == cmp_bat:
            messagebox.showinfo('OUT','Dismissal : COMPUTER IS OUT\n' + 'Computer Call \t' + str(cmp_bat) + '\nYour Call \t\t' +  str(run))
            self.second_batting_score = self.runs_scored
            if self.runs_scored < self.first_batting_score:
                self.match_winner = 1
            elif self.runs_scored == self.bat_first_score:
                self.match_winner = 0
            self.winner()

    def second_computer_bowl(self, run):
        lbl_bowl = Label(window_3, text = "Computer's Play", font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 170)
        cmp_bowl = random.randint(1, 6)
        lbl_cbwl = Label(window_3, text = cmp_bowl, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 250, y = 170)
        self.player = 1
        if run != cmp_bowl:
            self.runs_scored = self.runs_scored + run
            if self.runs_scored <= self.first_batting_score:
                lbl_runs = Label(window_3, text = self.runs_scored, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 220, y = 90)
            else:
                self.second_batting_score = self.runs_scored
                self.match_winner = 1
                self.winner()
        elif run == cmp_bowl:
            messagebox.showinfo('OUT','Dismissal : YOUR ARE OUT\n' + 'Your Call \t\t' + str(run) + '\nComputer Call \t' +  str(cmp_bowl))
            self.second_batting_score = self.runs_scored       
            if self.runs_scored < self.first_batting_score:
                self.match_winner = 2
            elif self.runs_scored == self.first_batting_score:
                self.match_winner = 0
            self.winner()
                
    def winner(self):
        window_3.destroy()

        global window_5    
        window_5 = Toplevel()
        window_5.title('Summary')
        window_5.geometry('400x300')
        window_5['bg'] = '#ddc3a5'

        lbl_info = Label(window_5, text = 'SUMMARY', font = ('arial', 15, 'bold'), bg = '#ddc3a5', padx = 15, pady = 15).pack()

        if self.player == 1:
            lbl_name = Label(window_5, text = 'Computer Batting First', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 50)
            lbl_runs = Label(window_5, text = 'Runs Scored ', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 80)
            lbl_runs = Label(window_5, text = self.first_batting_score, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 220, y = 80)
            lbl_name = Label(window_5, text = str(player_name.get()).capitalize() + ' Batting Second', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 110)
            lbl_runs = Label(window_5, text = 'Runs Scored ', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 140)
            lbl_runs = Label(window_5, text = self.second_batting_score, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 220, y = 140)

            self.first_batting = 'computer'
            self.second_batting = 'player'
        else:
            lbl_name = Label(window_5, text = str(player_name.get()).capitalize() + ' Batting First', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 50)
            lbl_runs = Label(window_5, text = 'Runs Scored ', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 80)
            lbl_runs = Label(window_5, text = self.first_batting_score, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 220, y = 80)
            lbl_name = Label(window_5, text = 'Computer Batting Second', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 110)
            lbl_runs = Label(window_5, text = 'Runs Scored ', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 140)
            lbl_runs = Label(window_5, text = self.second_batting_score, font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 220, y = 140)

            self.first_batting = 'player'
            self.second_batting = 'computer'
      
        if self.match_winner == 0:
            lbl_res = Label(window_5, text = 'It is a DRAW match', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 190)
            self.match_result = 'draw'   
        elif self.match_winner == 1:
            lbl_res = Label(window_5, text = str(player_name.get()).capitalize() + ' won the match', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 190)
            self.match_result = 'player'
        elif self.match_winner == 2:
            lbl_res = Label(window_5, text = 'Computer won the match', font = ('arial', 15, 'bold'), bg = '#ddc3a5').place(x = 20, y = 190)
            self.match_result = 'computer'

        file = pd.read_csv('stats.csv')
        file.loc[len(file.index)] = [self.first_batting, str(self.first_batting_score), self.second_batting, str(self.second_batting_score), self.match_result]
        file.to_csv('stats.csv', index = False)
        
        player_name.set('')
        toss_call.set('')
        self.player_call = 0
        self.computer_call = 0
        self.innings_num = 0
        self.runs_scored = 0
        self.first_batting_score = 0
        self.second_batting_score = 0
        self.match_winner = 0
        self.first_batting = ''
        self.second_batting = ''
        self.match_result = ''

        btn_finish = Button(window_5, text = 'Finish', height = 1, width = 10, font = ('arial', 12), bd = 1, command = window_5.destroy).place(x = 120, y = 240)

    def statistics(self):
        global window_6
        window_6 = Toplevel()
        window_6.title('Stats')
        window_6.geometry('440x350')
        window.resizable(False, False)
        window_6['bg'] = '#ddc3a5'

        lbl_info = Label(window_6, text = 'STATS', font = ('arial', 20, 'bold'), bg = '#ddc3a5', padx = 15, pady = 15).pack()
    
        file = pd.read_csv('stats.csv')

        total_matches = file.shape[0]

        lbl_tmtch = Label(window_6, text = 'Total Matches Played', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 50)
        lbl_tmtch = Label(window_6, text = total_matches, font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 50)

        if total_matches == 0:
            lbl_pwon = Label(window_6, text = 'Matches Won', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 80)
            lbl_pwon = Label(window_6, text = '0', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 80)

            lbl_pwon = Label(window_6, text = 'Win Percentage', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 110)
            lbl_pwon = Label(window_6, text = '0.00' + '%', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 110)

            lbl_cwon = Label(window_6, text = 'Matches Loss', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 140)
            lbl_cwon = Label(window_6, text = '0.00', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 140)

            lbl_pwon = Label(window_6, text = 'Loss Percentage', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 170)
            lbl_pwon = Label(window_6, text = '0.00' + '%', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 170)

            lbl_draw = Label(window_6, text = 'Matches Drawn', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 200)
            lbl_draw = Label(window_6, text = '0.00', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 200)

            lbl_draw = Label(window_6, text = 'Draw Percentage', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 230)
            lbl_draw = Label(window_6, text = '0.00' + '%', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 230)
        else:
            count_play = 0
            count_draw = 0

            for ele in file['win']:
                if ele == 'player':
                    count_play = count_play + 1
                elif ele == 'draw':
                    count_draw = count_draw + 1
      
            lbl_pwon = Label(window_6, text = 'Matches Won', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 80)
            lbl_pwon = Label(window_6, text = count_play, font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 80)

            lbl_pwon = Label(window_6, text = 'Win Percentage', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 110)
            lbl_pwon = Label(window_6, text = str('%.2f'%((count_play / total_matches) * 100)) + '%', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 110)

            lbl_cwon = Label(window_6, text = 'Matches Loss', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 140)
            lbl_cwon = Label(window_6, text = total_matches - count_play - count_draw, font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 140)

            lbl_pwon = Label(window_6, text = 'Loss Percentage', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 170)
            lbl_pwon = Label(window_6, text = str('%.2f'%(((total_matches - count_play - count_draw) / total_matches) * 100)) + '%', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 170)

            lbl_draw = Label(window_6, text = 'Matches Drawn', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 200)
            lbl_draw = Label(window_6, text = count_draw, font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 200)

            lbl_draw = Label(window_6, text = 'Draw Percentage', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 40, y = 230)
            lbl_draw = Label(window_6, text = str('%.2f'%((count_draw/ total_matches) * 100)) + '%', font = ('arial', 12, 'bold'), bg = '#ddc3a5').place(x = 350, y = 230)

        btn_stats = Button(window_6,  text = 'Reset', height = 1, width = 10, font = ('arial', 12), bd = 1, command = self.reset_stats).place(x = 50, y = 280)
        btn_close = Button(window_6,  text = 'Close', height = 1, width = 10, font = ('arial', 12), bd = 1, command = window_6.destroy).place(x = 260, y = 280)

    def reset_stats(self):
        file = pd.read_csv('stats.csv')

        for index, row in file.iterrows():
            file.drop(index, inplace = True)

        file.to_csv('stats.csv', index = False)

        window_6.destroy()
        self.statistics()

cric = cricket(player_call, computer_call, innings_num, runs_scored, first_batting_score, second_batting_score, match_winner, first_batting, second_batting, match_result)

lbl_info = Label(window, text = 'CRICKET', font = ('arial', 20, 'bold'), bg = '#ddc3a5', padx = 15, pady = 15).pack()

btn_start = Button(window, text = 'Start', height = 2, width = 15, font = ('arial', 15, 'bold'), bd = 3, command = cric.start).place(x = 100, y = 90)
btn_stats = Button(window, text = 'Stats', height = 2, width = 15, font = ('arial', 15, 'bold'), bd = 3, command = cric.statistics).place(x = 100, y = 190)
btn_exit = Button(window, text = 'Quit', height = 2, width = 15, font = ('arial', 15, 'bold'), bd = 3, command = window.destroy).place(x = 100, y = 290)                
                
window.mainloop()
