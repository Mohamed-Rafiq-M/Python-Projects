from tkinter import *
from time import strftime

window = Tk()
window.title('Digital Clock')
window.geometry('660x200')
window.resizable(False, False)
window['bg'] = '#f3ca20 '

def show_time():
    lbl_time.config(text = strftime('%I:%M:%S %p'))
    lbl_time.after(1000, show_time)

lbl_date = Label(window, text = strftime('%d %B %Y, %A'), font = ('arial', 24, 'bold'), bg = '#f3ca20', padx = 10, pady = 15)
lbl_date.pack()

lbl_time = Label(window, font = ('arial', 70, 'bold'), bg = '#f3ca20')
lbl_time.pack()
    
show_time()

window.mainloop()
