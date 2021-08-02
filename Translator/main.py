from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
from googletrans import Translator, LANGUAGES
import pyperclip

window = Tk()
window.geometry('1350x430')
window.title('Translator')
window.resizable(False, False)
window['bg'] = '#a7beae'

from_language = StringVar()
to_language = StringVar()

from_language.set('Choose Language')
to_language.set('Choose Language')

font_style = ('arial', 15)

language_options = list(LANGUAGES.values())

def translate():
    try:
        if from_language.get() not in language_options:
            msg.showinfo('Attention', 'Choose the Language of the Text')
        elif to_language.get() not in language_options:
            msg.showinfo('Attention', 'Choose the Language to Translate')
        else:
            translator = Translator()
            translated_text = translator.translate(text = ent_trans.get(1.0, END), src = from_language.get(), dest = to_language.get())
            ent_text_trans.delete(1.0, END)
            ent_text_trans.insert(END, translated_text.text)
    except:
        msg.showinfo('Attention', 'Enter the Text to Translate')

def copy_source():
    source_text = ent_trans.get(1.0, END)
    pyperclip.copy(source_text)

def clear_source():
    ent_trans.delete(1.0, END)
    from_language.set('Choose Language')

def copy_dest():
    dest_text = ent_text_trans.get(1.0, END)
    pyperclip.copy(dest_text)

def clear_dest():
    ent_text_trans.delete(1.0, END)
    to_language.set('Choose Language')

def clear_all():
    ent_trans.delete(1.0, END)
    from_language.set('Choose Language')
    ent_text_trans.delete(1.0, END)
    to_language.set('Choose Language')

lbl_info = Label(window, text = 'TRANSLATOR', font = ('arial', 20, 'bold'), bg = '#a7beae', fg = '#4203c9', padx = 15, pady = 15).pack()

lbl_lang = Label(window, text = 'Language', font = ('arial', 16, 'bold'), bg = '#a7beae').place(x = 40, y = 90)
drp_lang = ttk.Combobox(window, textvariable = from_language, values = language_options, width = 25, font = font_style).place(x = 240, y = 90)

lbl_trans = Label(window, text = 'Enter the Text to Translate', font = ('arial', 16, 'bold'), bg = '#a7beae').place(x = 40, y = 130)
ent_trans = Text(window, font = ('arial', 15), wrap = WORD, height = 8, width = 50, padx = 5, pady = 5)
ent_trans.place(x = 40, y = 160)

lbl_lang = Label(window, text = 'Language', font = ('arial', 16, 'bold'), bg = '#a7beae').place(x = 740, y = 90)
drp_lang = ttk.Combobox(window, textvariable = to_language, values = language_options, width = 25, font = font_style).place(x = 940, y = 90)

lbl_text_trans = Label(window, text = 'Translated Text', font = ('arial', 16, 'bold'), bg = '#a7beae').place(x = 740, y = 130)
ent_text_trans = Text(window, font = ('arial', 15), wrap = WORD, height = 8, width = 50, padx = 5, pady = 5)
ent_text_trans.place(x = 740, y = 160)

btn_copy_source = Button(window, text = 'Copy', font = ('arial', 12, 'bold'), bd = 1, height = 1, width = 8, command = copy_source).place(x = 40, y = 365)
btn_clear_source = Button(window, text = 'Clear', font = ('arial', 12, 'bold'), bd = 1, height = 1, width = 8, command = clear_source).place(x = 515, y = 365)

btn_copy_dest = Button(window, text = 'Copy', font = ('arial', 12, 'bold'), bd = 1, height = 1, width = 8, command = copy_dest).place(x = 740, y = 365)
btn_clear_dest = Button(window, text = 'Clear', font = ('arial', 12, 'bold'), bd = 1, height = 1, width = 8, command = clear_dest).place(x = 1215, y = 365)

btn_translate = Button(window, text = 'Translate', font = ('arial', 12, 'bold'), bd = 1, height = 2, width = 10, command = translate).place(x = 620, y = 200)
btn_clear_all = Button(window, text = 'Clear All', font = ('arial', 12, 'bold'), bd = 1, height = 2, width = 10, command = clear_all).place(x = 620, y = 275)

window.mainloop
