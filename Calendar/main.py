from tkinter import *
import tkinter.messagebox as msg
from datetime import date
import calendar

window = Tk()
window.title('Calendar')
window.geometry('607x740')
window.resizable(False, False)
window['bg'] = '#ecc19c'

current_year = IntVar()

font_style = ('arial', 16, 'bold')

todays_date = date.today()
current_year.set(todays_date.year)

def next_year():
    current_set_year = current_year.get() + 1
    current_year.set(current_set_year)
    view_calendar()

def previous_year():
    current_set_year = current_year.get() - 1
    current_year.set(current_set_year)
    view_calendar()

def view_calendar():
    try:
        txt_calendar.configure(state = NORMAL)
        calendar_year = int(current_year.get())
        calendar_view = calendar.calendar(calendar_year)
        txt_calendar.delete(1.0, 'end')
        txt_calendar.insert(0.0, calendar_view)
        txt_calendar.configure(state = DISABLED)
    except:
        msg.showerror('Attention', 'Invalid Year')
        current_year.set(todays_date.year)
        view_calendar()

lbl_info = Label(window, text = 'CALENDAR',  font = ('arial', 20, 'bold'), bg = '#ecc19c', padx = 15, pady = 15).pack()
ent_path = Entry(window, textvariable = current_year, font = font_style, width = 10, bd = 2, justify = 'center').place(x = 100, y = 70)

txt_calendar = Text(window, width = 72, height = 37, relief = 'raised', bg = '#f5f0e1', padx = 15, pady = 15)
txt_calendar.place(x = 0, y = 120)

btn_previous = Button(window, text = '<', width = 5, font = ('arial', 12), bd = 1, command = previous_year).place(x = 30, y = 70)
btn_next = Button(window, text = '>', width = 5, font = ('arial', 12), bd = 1, command = next_year).place(x = 240, y = 70)

btn_get_date = Button(window, text = 'View Calendar', width = 12, font = ('arial', 11,), bd = 1, command = view_calendar).place(x = 460, y = 70)

view_calendar()

window.mainloop()
