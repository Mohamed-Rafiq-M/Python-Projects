from tkinter import *
import tkinter.messagebox as msg
import pyshorteners
import re
import pyperclip

window = Tk()
window.geometry('780x260')
window.title('URL Shortener')
window['bg'] = '#ecc19c'
window.resizable(False, False)

url_link = StringVar()
url_link_short = StringVar()

def shorten_url():
    if url_link.get() == '':
        msg.showinfo('Info', 'Enter the link to shorten')
    else:
        try:
            link = url_link.get()
            regex = ('((http|https)://)(www.)?' + '[a-zA-Z0-9@:%._\\+~#?&//=]' + '{2,256}\\.[a-z]' + '{2,6}\\b([-a-zA-Z0-9@:%' + '._\\+~#?&//=]*)')     
            regex_compile = re.compile(regex)
        
            if re.search(regex_compile, link):
                shortener = pyshorteners.Shortener()
                shortend_link = shortener.tinyurl.short(link)

                url_link_short.set(shortend_link)

                ent_shortend = Entry(window, textvariable = url_link_short, font = ('arial', 13),state = DISABLED, width = 55).place(x = 220, y = 120)

            else:
                msg.showinfo('Info', 'Enter a valid link')

        except:
            msg.showinfo('Info', 'Check the link entered')
            
def clear():
    url_link.set('')
    url_link_short.set('')

def copy():
    copy_link = url_link_short.get()
    pyperclip.copy(copy_link)
    
lbl_info = Label(window, text = 'URL SHORTENER', font = ('arial', 20, 'bold'), bg = '#ecc19c', fg = '#7a2048', padx = 20, pady = 20).pack()

lbl_url = Label(window, text = 'Enter the URL', font = ('arial', 14, 'bold'), bg = '#ecc19c', fg = '#201e20').place(x = 30, y = 80)
ent_url = Entry(window, textvariable = url_link, font = ('arial', 13), width = 55).place(x = 220, y = 80)

lbl_shortend = Label(window, text = 'Shortened URL', font = ('arial', 14, 'bold'), bg = '#ecc19c', fg = '#201e20').place(x = 30, y = 120)
ent_shortend = Entry(window, textvariable = url_link_short, font = ('arial', 13), state = DISABLED, width = 55).place(x = 220, y = 120)


btn_generate = Button(window, text = 'Shorten Link', font = ('arial', 12, 'bold'), bd = 1, width = 12, command = shorten_url).place(x = 80, y = 200)
btn_generate = Button(window, text = 'Copy Link', font = ('arial', 12, 'bold'), bd = 1, width = 12, command = copy).place(x = 240, y = 200)
btn_clear = Button(window, text = 'Clear', font = ('arial', 12, 'bold'), bd = 1, width = 12, command = clear).place(x = 400, y = 200)
btn_quit = Button(window, text = 'Quit', font = ('arial', 12, 'bold'), bd = 1, width = 12, command = window.destroy).place(x = 560, y = 200)

window.mainloop()
