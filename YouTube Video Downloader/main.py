from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import tkinter.filedialog as fld
import pafy
import os

window = Tk()
window.title('YouTube Video Downloader')
window.geometry('830x290')
window.resizable(False, False)
window['bg'] = '#fff1e1'

yt_video_link = StringVar()
download_path = StringVar()
download_format = StringVar()

download_format_options = ['Audio', 'Video']

download_format.set('Choose Format')

font_style = ('arial', 15)

def browse_path():
    download_directory = fld.askdirectory(initialdir = 'YOUR DIRECTORY PATH')
    download_path.set(download_directory)

def download_video():
    try:
        if yt_video_link.get() == '' or download_path.get() == '' or (download_format.get() not in download_format_options):
            msg.showinfo('Attention', 'Fill all the Fields')
        else:
            window.geometry('830x590')

            link = yt_video_link.get()
            yt_video = pafy.new(link)

            lbl_author = Text(window, font = ('arial', 15), height = 1, width = 45, bg = '#fff1e1')
            lbl_author.insert(END, yt_video.author)
            lbl_author.configure(state = DISABLED)
            lbl_author.place(x = 295, y = 310)

            lbl_title = Text(window, font = ('arial', 15), height = 3, width = 45, bg = '#fff1e1')
            lbl_title.insert(END, str(yt_video.title))
            lbl_title.configure(state = DISABLED)
            lbl_title.place(x = 295, y = 350)

            lbl_duration = Text(window, font = ('arial', 15), height = 1, width = 45, bg = '#fff1e1')
            lbl_duration.insert(END, str(yt_video.length) + " seconds")
            lbl_duration.configure(state = DISABLED)
            lbl_duration.place(x = 295, y = 435)

            lbl_views = Text(window, font = ('arial', 15), height = 1, width = 45, bg = '#fff1e1')
            lbl_views.insert(END, str(yt_video.viewcount) + " views")
            lbl_views.configure(state = DISABLED)
            lbl_views.place(x = 295, y = 475)

            path = str(download_path.get())
            os.chdir(path)
            
            choice = download_format.get()
            if choice == 'Audio':
                specified_format = yt_video.getbestaudio()
            else:
                specified_format = yt_video.getbest()

            specified_format.download()

            lbl_completed = Label(window, text = 'Download Completed', font = ('arial', 18, 'bold'), bg= '#fff1e1', fg = '#013220').place(x = 250, y = 520)
    except:
        msg.showinfo('Attention', 'Invalid Link')

def reset():
    window.geometry('830x290')
    
    yt_video_link.set('')
    download_path.set('')
    download_format.set('Choose Format')
    
lbl_info = Label(window, text = 'YOUTUBE VIDEO DOWNLOADER', font = ('arial', 20, 'bold'), bg= '#fff1e1',  padx = 10, pady = 10).pack()

lbl_link = Label(window, text = 'Enter the Video Link', font = ('arial', 16, 'bold'), bg= '#fff1e1').place(x = 30, y = 80)
ent_link = Entry(window, textvariable = yt_video_link, font = font_style, width = 35).place(x = 295, y = 80)

lbl_path = Label(window, text = 'Enter the Path to Save', font = ('arial', 16, 'bold'), bg= '#fff1e1').place(x = 30, y = 120)
ent_path = Entry(window, textvariable = download_path, font = font_style, width = 35).place(x = 295, y = 120)

lbl_down = Label(window, text = 'Download Format', font = ('arial', 16, 'bold'), bg= '#fff1e1').place(x = 30, y = 160)
drp_down = ttk.Combobox(window, textvariable = download_format, values = download_format_options, font = font_style, width = 20).place(x = 295, y = 160)

lbl_ch_name = Label(window, text = 'Channel Name', font = ('arial', 16, 'bold'), bg= '#fff1e1').place(x = 50, y = 310)
lbl_vd_tit = Label(window, text = 'Vidoe Title', font = ('arial', 16, 'bold'), bg= '#fff1e1').place(x = 50, y = 375)
lbl_vd_len = Label(window, text = 'Video Duration', font = ('arial', 16, 'bold'), bg= '#fff1e1').place(x = 50, y = 435)
lbl_vd_view = Label(window, text = 'Video Views', font = ('arial', 16, 'bold'), bg= '#fff1e1').place(x = 50, y = 475)

btn_path = Button(window, text = 'Browse', font = ('arial', 10), bd = 1, width = 10, command = browse_path).place(x = 695, y = 120)

btn_clear = Button(window, text = 'Clear', font = ('arial', 12), bd = 1, height = 1, width = 13, command = reset).place(x = 70, y = 220)
btn_download = Button(window, text = 'Download', font = ('arial', 12), bd = 1, height = 1, width = 13, command = download_video).place(x = 620, y = 220)

window.mainloop()
