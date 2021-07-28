from tkinter import * 
import tkinter.messagebox as msg
import random
import pandas as pd

window = Tk()
window.geometry('450x330')
window.title('Stone Paper Scissor')
window.resizable(False, False)
window['bg'] = '#c6d7eb'

name = StringVar()
points = IntVar()

points_win = 0
player_call = ''
computer_call = ''
player_score = 0
computer_score = 0
result = ''

class stone_paper_scissor:
    def __init__(self, points_win, player_call, computer_call, player_score, computer_score, result):
        self.points_win = points_win
        self.player_call = player_call
        self.computer_call = computer_call
        self.player_score = player_score
        self.computer_score = computer_score
        self.result = result

    def start(self):
        global window_1
        window_1 = Toplevel()
        window_1.geometry('700x250')
        window_1.title('Stone Paper Scissor')
        window_1.resizable(False, False)
        window_1['bg'] = '#c6d7eb'

        lbl_info = Label(window_1, text = 'STONE PAPER SCISSOR', font = ('arial', 20, 'bold'), bg = '#c6d7eb', fg = '#1868ae', padx = 15, pady = 15).pack()

        lbl_name = Label(window_1, text = 'Name', font = ('arial', 16, 'bold'), bg = '#c6d7eb').place(x = 30, y = 70)
        ent_name = Entry(window_1, textvariable = name, font = ('arial', 15), width = 40).place(x = 220, y = 70)

        lbl_points = Label(window_1, text = 'Points to Win', font = ('arial', 16, 'bold'), bg = '#c6d7eb').place(x = 30, y = 110)
        ent_points = Entry(window_1, textvariable = points, font = ('arial', 15), width = 15).place(x = 220, y = 110)

        btn_start = Button(window_1, text = 'Lets Begin', font = ('arial', 12), bd = 1, width = 11, command = self.begin).place(x = 290, y = 200)

    def begin(self):
        try:
            if name.get() == '' or points.get() == 0:
                msg.showinfo('Attention', 'One or more fields is empty !!!')
            else:
                if points.get() >= 10:
                    ent_name = Entry(window_1, textvariable = name, font = ('arial', 15), width = 40, state = DISABLED).place(x = 220, y = 70)
                    ent_points = Entry(window_1, textvariable = points, font = ('arial', 15), width = 15, state = DISABLED).place(x = 220, y = 110)
                    
                    self.points_win = points.get()

                    lbl_result = Label(window_1, text = 'Winner', font = ('arial', 16, 'bold'), bg = '#c6d7eb').place(x = 30, y = 150)
                        
                    window_1.geometry('700x550')

                    lbl_score = Label(window_1, text = (name.get()).capitalize() + "'s Score", font = ('arial', 16, 'bold'), bg = '#c6d7eb').place(x = 200, y = 265)
                    lbl_score = Label(window_1, text = "Computer's Score", font = ('arial', 16, 'bold'), bg = '#c6d7eb').place(x = 200, y = 295)

                    lbl_player = Label(window_1, text = (name.get()).capitalize() + "'s Call", font = ('arial', 16, 'bold'), bg = '#c6d7eb').place(x = 200, y = 345)

                    btn_stone = Button(window_1, text = 'Stone', font = ('arial', 15), bd = 1, height = 2, width = 10, command = self.stone).place(x = 170, y = 450)
                    btn_paper = Button(window_1, text = 'Paper', font = ('arial', 15), bd = 1, height = 2, width = 10, command = self.paper).place(x = 288, y = 450)
                    btn_sciss = Button(window_1, text = 'Scissor', font = ('arial', 15), bd = 1, height = 2, width = 10, command = self.sciss).place(x = 406, y = 450)
                    
                else:
                    msg.showinfo('Attention', 'Points should be minimum 10 !!!')

        except:
            msg.showinfo('Attention', 'Invalid Entry of Data')
     
    def stone(self):
        self.player_call = 'Stone  '
        lbl_stone = Label(window_1, text = self.player_call, font = ('arial', 16, 'bold'), bg = '#c6d7eb', fg = '#e0a96d').place(x = 420, y = 345)
        self.computer_play()
        
    def paper(self):
        self.player_call = 'Paper  '
        lbl_paper = Label(window_1, text = self.player_call, font = ('arial', 16, 'bold'), bg = '#c6d7eb', fg = '#e0a96d').place(x = 420, y = 345)
        self.computer_play()

    def sciss(self):
        self.player_call = 'Scissor'
        lbl_sciss = Label(window_1, text = self.player_call, font = ('arial', 16, 'bold'), bg = '#c6d7eb', fg = '#e0a96d').place(x = 420, y = 345)
        self.computer_play()

    def computer_play(self):
        lbl_computer = Label(window_1, text = "Computer's Call", font = ('arial', 15, 'bold'), bg = '#c6d7eb').place(x = 200, y = 385)
        choice_list = ['Stone  ', 'Paper  ', 'Scissor']
        self.computer_call = random.choice(choice_list)
        lbl_computer = Label(window_1, text = self.computer_call, font = ('arial', 16, 'bold'), bg = '#c6d7eb', fg = '#e0a96d').place(x = 420, y = 385)

        if self.player_call == 'Paper  ' and self.computer_call == 'Stone  ':
            self.player_score += 1
        elif self.player_call == 'Stone  ' and self.computer_call == 'Paper  ':
            self.computer_score += 1
        elif self.player_call == 'Scissor' and self.computer_call == 'Paper  ':
            self.player_score += 1
        elif self.player_call == 'Paper  ' and self.computer_call == 'Scissor':
            self.computer_score += 1
        elif self.player_call == 'Stone  ' and self.computer_call == 'Scissor':
            self.player_score += 1
        elif self.player_call == 'Scissor' and self.computer_call == 'Stone  ':
            self.computer_score += 1

        lbl_score = Label(window_1, text = str(self.player_score), font = ('arial', 15, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 450, y = 265)
        lbl_score = Label(window_1, text = str(self.computer_score), font = ('arial', 15, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 450, y = 295)

        if self.player_score ==  self.points_win or self.computer_score == self.points_win:
            self.game_over()

    def game_over(self):
        window_1.geometry('700x250')
        if self.player_score ==  self.points_win:
            self.result = 'Player'
            msg.showinfo('Match Ended', name.get().upper() + ' won the game\n\n' + name.get().upper() + "'s Score: " + str(self.player_score) + "\nComputer's Score: " + str(self.computer_score))
            lbl_winner = Label(window_1, text = name.get().upper(), font = ('arial', 16, 'bold'), bg = '#c6d7eb', fg = '#228B22').place(x = 220, y = 150) 
        elif self.computer_score == self.points_win:
            self.result = 'Computer'
            msg.showinfo('Match Ended', 'Computer won the game\n\n' + name.get().upper() + "'s Score: " + str(self.player_score) + "\nComputer's Score: " + str(self.computer_score))
            lbl_winner = Label(window_1, text = 'COMPUTER', font = ('arial', 16, 'bold'), bg = '#c6d7eb', fg = '#228B22').place(x = 220, y = 150)

        file = pd.read_csv('stats.csv')
        file.loc[len(file.index)] = [self.points_win, self.player_score, self.computer_score, self.result]
        file.to_csv('stats.csv', index = False)
        
        btn_exit = Button(window_1, text = 'Exit', font = ('arial', 12), bd = 1, width = 11, command = self.exit_game).place(x = 290, y = 200)

    def exit_game(self):
        name.set('')
        points.set(0)
        self.points_win = 0
        self.player_call = ''
        self.computer_call = ''
        self.player_score = 0
        self.computer_score = 0
        self.result = ''

        window_1.destroy()

    def stats_match(self):
        global window_2
        window_2 = Toplevel()
        window_2.title('Stats')
        window_2.geometry('480x370')
        window_2.resizable(False, False)
        window_2['bg'] = '#c6d7eb'

        lbl_info = Label(window_2, text = 'STATS', font = ('arial', 20, 'bold'), bg = '#c6d7eb', fg = '#1868ae', padx = 15, pady = 15).pack()
    
        file = pd.read_csv('stats.csv')

        total_matches = file.shape[0]
        total_points = file['Point'].sum()
        
        lbl_tmtch = Label(window_2, text = 'Total Games Played', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 70)
        lbl_tmtch = Label(window_2, text = total_matches, font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 70)

        if total_matches == 0:
            lbl_pwon = Label(window_2, text = 'Games Won', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 95)
            lbl_pwon = Label(window_2, text = '0', font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 95)

            lbl_pwon_percent = Label(window_2, text = 'Win Percentage', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 120)
            lbl_pwon_percent = Label(window_2, text = '0' + '%', font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 120)

            lbl_cwon = Label(window_2, text = 'Games Loss', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 145)
            lbl_cwon = Label(window_2, text = '0', font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 145)

            lbl_cwon_percent = Label(window_2, text = 'Loss Percentage', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 170)
            lbl_cwon_percent = Label(window_2, text = '0' + '%', font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 170)

            lbl_tot_points = Label(window_2, text = 'Total Points Played', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 195)
            lbl_tot_points = Label(window_2, text = total_points, font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 195)

            lbl_ply_points = Label(window_2, text = 'Total Points Scored by Player', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 220)
            lbl_ply_points = Label(window_2, text = '0', font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 220)

            lbl_com_points = Label(window_2, text = 'Total Points Scored by Computer', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 245)
            lbl_com_points = Label(window_2, text = '0', font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 245)

        else:
            player_win = 0
            for record in file['Result']:
                if record == 'Player':
                    player_win += 1

            player_points = file['Player Score'].sum()
            computer_points = file['Computer Score'].sum()
 
            lbl_pwon = Label(window_2, text = 'Matches Won', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 95)
            lbl_pwon = Label(window_2, text = player_win, font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 95)

            lbl_pwon_percent = Label(window_2, text = 'Win Percentage', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 120)
            lbl_pwon_percent = Label(window_2, text = str('%.2f'%((player_win / total_matches) * 100)) + '%', font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 120)

            lbl_cwon = Label(window_2, text = 'Matches Loss', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 145)
            lbl_cwon = Label(window_2, text = total_matches - player_win, font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 145)

            lbl_cwon_percent = Label(window_2, text = 'Loss Percentage', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 170)
            lbl_cwon_percent = Label(window_2, text = str('%.2f'%(((total_matches - player_win) / total_matches) * 100)) + '%', font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 170)

            lbl_tot_points = Label(window_2, text = 'Total Points Played', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 195)
            lbl_tot_points = Label(window_2, text = total_points, font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 195)
            
            lbl_ply_points = Label(window_2, text = 'Total Points Scored by Player', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 220)
            lbl_ply_points = Label(window_2, text = player_points, font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 220)

            lbl_com_points = Label(window_2, text = 'Total Points Scored by Computer', font = ('arial', 12, 'bold'), bg = '#c6d7eb').place(x = 40, y = 245)
            lbl_com_points = Label(window_2, text = computer_points, font = ('arial', 12, 'bold'), bg = '#c6d7eb', fg = '#7a2048').place(x = 350, y = 245)
      

        btn_reset = Button(window_2,  text = 'Reset Stats',  font = ('arial', 12), width = 12, command = self.reset_stats).place(x = 80, y = 300)
        btn_finish = Button(window_2,  text = 'Close', font = ('arial', 12), width = 12, command = window_2.destroy).place(x = 260, y = 300)

    def reset_stats(self):
        file = pd.read_csv('stats.csv')

        for index, row in file.iterrows():
            file.drop(index, inplace = True)

        file.to_csv('stats.csv', index = False)

        window_2.destroy()
        self.stats_match()

sps = stone_paper_scissor(points_win, player_call, computer_call, player_score, computer_score, result)
    
lbl_info = Label(window, text = 'STONE PAPER SCISSOR', font = ('arial', 20, 'bold'), bg = '#c6d7eb', fg = '#1868ae', padx = 15, pady = 15).pack()

btn_start = Button(window, text = 'Start Game', font = ('arial', 16, 'bold'), bd = 2, height = 2, width = 15, command = sps.start).place(x = 110, y = 75)
btn_stats = Button(window, text = 'Statistics', font = ('arial', 16, 'bold'), bd = 2, height = 2, width = 15, command = sps.stats_match).place(x = 110, y = 155)
btn_exit = Button(window, text = 'QUIT', font = ('arial', 16, 'bold'), bd = 2, height = 2, width = 15, command = window.destroy).place(x = 110, y = 235)

window.mainloop()
