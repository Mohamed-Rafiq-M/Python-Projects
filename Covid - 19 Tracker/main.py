from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
from covid import Covid

window = Tk()
window.geometry('675x360')
window.title('Covid - 19 Tracker')
window.resizable(False, False)
window['bg'] = '#f5f0e1'

icon = PhotoImage(file = 'covid.png')
window.iconphoto(False, icon)

corona_virus = Covid()
countries = corona_virus.list_countries()

country_option = []
for country_dict in countries:
    country_option.append(country_dict['name'])
country_option.sort()

country_name = StringVar()

country_name.set('Choose a Country')

font_style = ('arial', 16, 'bold')

def get_data():
    if country_name.get() not in country_option:
        msg.showerror('Error', 'Select a Valid Country Name')
    else:
        covid_status = corona_virus.get_status_by_country_name(str(country_name.get()))
        
        lbl_confirmed_count.config(text = str(covid_status['confirmed']))
        lbl_active_count.config(text = str(covid_status['active']))
        lbl_death_count.config(text = str(covid_status['deaths']))
        lbl_recovered_count.config(text = str(covid_status['recovered'])) 

lbl_info = Label(window, text = 'COVID - 19 TRACKER', font = ('arial', 20, 'bold'), bg = '#f5f0e1', padx = 15, pady = 15).pack()

lbl_cntry_name = Label(window, text = 'Country Name', font = ('arial', 16, 'bold'), bg = '#f5f0e1').place(x = 60, y = 80)
drp_cntry_name = ttk.Combobox(window, textvariable = country_name, values = country_option, width = 25, font = font_style).place(x = 280, y = 80)

lbl_confirmed_cases = Label(window, text = 'Confirmed Cases', font = ('arial', 16, 'bold'), bg = '#f5f0e1').place(x = 60, y = 200)
lbl_confirmed_count = Label(window, font = ('arial', 16, 'bold'), bg = '#f5f0e1', fg = '#e71837')
lbl_confirmed_count.place(x = 300, y = 200)

lbl_active_cases = Label(window, text = 'Active Cases', font = ('arial', 16, 'bold'), bg = '#f5f0e1').place(x = 60, y = 235)
lbl_active_count = Label(window, font = ('arial', 16, 'bold'), bg = '#f5f0e1', fg = '#fc9303')
lbl_active_count.place(x = 300, y = 235)

lbl_death_cases = Label(window, text = 'Death', font = ('arial', 16, 'bold'), bg = '#f5f0e1').place(x = 60, y = 270)
lbl_death_count = Label(window, font = ('arial', 16, 'bold'), bg = '#f5f0e1', fg = '#6a6c6d')
lbl_death_count.place(x = 300, y = 270)

lbl_recovered_cases = Label(window, text = 'Recovered', font = ('arial', 16, 'bold'), bg = '#f5f0e1').place(x = 60, y = 305)
lbl_recovered_count = Label(window, font = ('arial', 16, 'bold'), bg = '#f5f0e1', fg = '#49b675')
lbl_recovered_count.place(x = 300, y = 305)

btn_get_data = Button(window, text = 'Get Data', font = ('arial', 14), height = 1, width = 12, bd = 1, command = get_data).place(x = 250, y = 140)

window.mainloop()
