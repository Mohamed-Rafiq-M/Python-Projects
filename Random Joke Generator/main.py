from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import pyjokes

window = Tk()
window.title('Random Joke Generator')
window.geometry('620x390')
window.resizable(False, False)
window['bg'] = '#1e3d59'

language = StringVar()
category = StringVar()

language_options = ['en - English', 'de - German', 'es - Spanish', 'it - Italian', 'gl - Galician', 'eu - Basque']
category_options = ['neutral - Neutral Geeky Jokes', 'twister - Tongue Twister', 'all - All Types of Joke']

language.set('Choose Language')
category.set('Choose Category')

font_style = ('arial', 14)

def generate():
    language_chosen = language.get()
    category_chosen = category.get()
    
    if language_chosen not in language_options or category_chosen not in category_options:
        msg.showinfo('Info', 'Choose the correct language and category from the drop down')
    else:
        try:
            if language_chosen == 'en - English':
                lang_chosen = 'en'
            elif language_chosen == 'de - German':
                lang_chosen = 'de'
            elif language_chosen == 'es - Spanish':
                lang_chosen = 'es'
            elif language_chosen == 'it - Italian':
                lang_chosen = 'it'
            elif language_chosen == 'gl - Galician':
                lang_chosen = 'gl'
            else:
                lang_chosen = 'eu'

            if category_chosen == 'neutral - Neutral Geeky Jokes':
                catg_chosen = 'neutral'
            elif category_chosen == 'twister - Tongue Twister':
                catg_chosen = 'twister'
            if category_chosen == 'all - All Types of Joke':
                catg_chosen = 'all'

            joke = pyjokes.get_joke(language = lang_chosen, category = catg_chosen)

            lbl_joke = Text(window, font = ('arial', 15), height = 5, width = 49, bg = '#f5f0e1')
            lbl_joke.insert(END, joke)
            lbl_joke.place(x = 40, y = 170)
        
        except:
            msg.showinfo('Info', 'Category not found in the choosed language')

lbl_info = Label(window, text = 'RANDOM JOKE GENERATOR', font = ('arial', 20, 'bold'), padx = 10, pady = 10, bg = '#1e3d59', fg = '#f5f0e1').pack()

lbl_lan = Label(window, text = 'Select the Language', font = ('arial', 16, 'bold'), bg = '#1e3d59', fg = '#e5e5dc').place(x = 40, y = 80)
drp_lan = ttk.Combobox(window, textvariable = language, values = language_options, width = 25, font = font_style).place(x = 280, y = 80)

lbl_cat = Label(window, text = 'Select the Category', font = ('arial', 16, 'bold'), bg = '#1e3d59', fg = '#e5e5dc').place(x = 40, y = 120)
drp_cat = ttk.Combobox(window, textvariable = category, values = category_options, width = 25, font = font_style).place(x = 280, y = 120)

btn_test = Button(window, text = 'Generate', font = ('arial', 12, 'bold'), bd = 1, height = 2, width = 10, command = generate).place(x = 100, y = 310)
btn_exit = Button(window, text = 'Quit', font = ('arial', 12, 'bold'), bd = 1, height = 2, width = 10, command = window.destroy).place(x = 410, y = 310)

window.mainloop()
