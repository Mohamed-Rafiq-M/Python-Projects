from tkinter import *
import random

window = Tk()
window.title('Dice Roller')
window.geometry('400x360')
window.resizable(False, False)
window['bg'] = '#f5f0e1'

icon = PhotoImage(file = 'Dice.png')
window.iconphoto(False, icon)

def roll_dice():
    dice_list = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

    dice_dict = {'\u2680' : 1, '\u2681' : 2, '\u2682' : 3, '\u2683' : 4, '\u2684' : 5, '\u2685' : 6}
    
    dice_1_unicode = random.choice(dice_list)
    dice_2_unicode = random.choice(dice_list)

    if dice_1_unicode in dice_dict.keys():
        dice_1_num = dice_dict[dice_1_unicode]
        
    if dice_2_unicode in dice_dict.keys():
        dice_2_num = dice_dict[dice_2_unicode]

    lbl_dice_1.config(text = dice_1_unicode)
    lbl_dice_2.config(text = dice_2_unicode)

    lbl_dice_1_num.config(text = dice_1_num)
    lbl_dice_2_num.config(text = dice_2_num)

    lbl_rolled_sum.config(text = dice_1_num + dice_2_num)

lbl_rolled = Label(window, text = 'You Rolled:', font = ('arial', 20, 'bold'), bg = '#f5f0e1').place(x = 60, y = 25)

lbl_rolled_sum = Label(window, font = ('arial', 20, 'bold'), bg = '#f5f0e1')
lbl_rolled_sum.place(x = 260, y = 25)

lbl_dice_1 = Label(window, font = ('arial', 160, 'bold'), bg = '#f5f0e1', fg = '#000000')
lbl_dice_1.place(x = 20, y = 100)

lbl_dice_2 = Label(window, font = ('arial', 160, 'bold'), bg = '#f5f0e1', fg = '#000000')
lbl_dice_2.place(x = 200, y = 100)

lbl_dice_1_num = Label(window, font = ('arial', 20, 'bold'), bg = '#f5f0e1')
lbl_dice_1_num.place(x = 90, y = 300)

lbl_dice_2_num = Label(window, font = ('arial', 20, 'bold'), bg = '#f5f0e1')
lbl_dice_2_num.place(x = 270, y = 300)

btn_roll_dice = Button(window, text = 'Roll Dice', font = ('arial', 16, 'bold'), height = 1, width = 10, bd = 1, command = roll_dice).place(x = 125, y = 80)

window.mainloop()
