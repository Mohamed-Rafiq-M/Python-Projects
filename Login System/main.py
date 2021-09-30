from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox as msg
import re
import pandas as pd

font_style = ('arial', 16, 'bold')
sec_ques_options = ['What city were you born in?', 'What is your oldest sibling middle name?', 'What primary school did you attend?', 'What is your favorite color?', 'What is your favorite movie?']
    
def existing_user():
    global window, user_name, pass_word

    window = Tk()
    window.title('Login')
    window.geometry('900x500')
    window.resizable(False, False)
    window['bg'] = '#FBEAEB'

    user_name = StringVar()
    pass_word = StringVar()
    
    lbl_head = Label(window, text = 'Existing User - Login', font = ('arial', 35, 'bold'), bg = '#FBEAEB', fg = '#2F3C7E', padx = 15, pady = 15).pack()

    lbl_new_account = Label(window, text = 'Are you a new user ? Click ➤', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 100, y = 130)
    btn_new_user = Button(window, text = 'New User', font = ('arial', 10, 'bold'), height = 1, width = 10, bd = 1, command = new_user).place(x = 400, y = 130)

    lbl_username = Label(window, text = 'Username', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 100, y = 200)
    ent_username = Entry(window, textvariable = user_name, font = ('arial', 16, 'bold'), width = 35).place(x = 300, y = 200)

    lbl_password = Label(window, text = 'Password', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 100, y = 240)
    ent_password = Entry(window, textvariable = pass_word, font = ('arial', 16, 'bold'), width = 35, show = '*').place(x = 300, y = 240)

    btn_show = Button(window, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_password).place(x = 730, y = 240)
    btn_forget_password = Button(window, text = 'Forget Password', font = ('arial', 10, 'bold'), height = 1, width = 15, bd = 1, command = forget_password).place(x = 595, y = 280)
    btn_login = Button(window, text = 'Login', font = ('arial', 16, 'bold'), height = 1, width = 10, bd = 1, command = login_user).place(x = 375, y = 350)

def show_password():
    ent_password = Entry(window, textvariable = pass_word, font = ('arial', 16, 'bold'), width = 35).place(x = 300, y = 240)
    btn_hide = Button(window, text = 'Hide', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = hide_password).place(x = 730, y = 240)

def hide_password():
    ent_password = Entry(window, textvariable = pass_word, font = ('arial', 16, 'bold'), width = 35, show = '*').place(x = 300, y = 240)
    btn_show = Button(window, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_password).place(x = 730, y = 240)

def forget_password():
    window.destroy()
    global window_1, user_name

    window_1 = Tk()
    window_1.title('Forget Password')
    window_1.geometry('600x200')
    window_1.resizable(False, False)
    window_1['bg'] = '#FBEAEB'

    user_name = StringVar()
    
    lbl_username = Label(window_1, text = 'Username', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 20, y = 40)
    ent_username = Entry(window_1, textvariable = user_name, font = ('arial', 16, 'bold'), width = 35).place(x = 140, y = 40)

    btn_back = Button(window_1, text = 'Back', font = ('arial', 14, 'bold'), height = 1, width = 10, bd = 1, command = move_backward).place(x = 20, y = 100)
    btn_change_password = Button(window_1, text = 'Change', font = ('arial', 14, 'bold'), height = 1, width = 10, bd = 1, command = change_password).place(x = 440, y = 100)

def move_backward():
    window_1.destroy()
    existing_user()
    

def change_password():
    if user_name.get() == '':
        msg.showwarning('Warning', 'Enter the Username')
    elif user_name.get() != '':
        email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        if(not(re.search(email, str(user_name.get())))):
            msg.showwarning('Warning', 'Invalid User Name')
        else:
            changing_username = str(user_name.get())

            file = pd.read_csv('user details.csv')

            global row_count
            row_count = 0

            flag = 0
            for index, row in file.iterrows():
                if row['username'] == str(user_name.get()):
                    window_1.destroy()
                    
                    global window_2, question_answer, new_pass_word, confirm_pass_word, existing_answer
                    window_2 = Tk()
                    window_2.title('Forget Password')
                    window_2.geometry('600x400')
                    window_2.resizable(False, False)
                    window_2['bg'] = '#FBEAEB'

                    question_answer = StringVar()
                    new_pass_word = StringVar()
                    confirm_pass_word = StringVar()

                    existing_answer = row['answer']

                    lbl_username = Label(window_2, text = 'Username', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 20, y = 40)
                    txt_username = Text(window_2, font = ('arial', 16, 'bold'), height = 1, width = 45, state = NORMAL)
                    txt_username.delete('1.0', 'end')
                    txt_username.insert(END, changing_username)
                    txt_username.config(state = DISABLED)
                    txt_username.place(x = 20, y = 70)

                    lbl_security_question = Label(window_2, text = row['security_question'], font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 20, y = 110)
                    ent_security_question = Entry(window_2, textvariable = question_answer, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 20, y = 140)

                    lbl_new_password = Label(window_2, text = 'New Password', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 20, y = 180)
                    ent_new_password = Entry(window_2, textvariable = new_pass_word, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 20, y = 210)

                    lbl_confirm_password = Label(window_2, text = 'Confirm Password', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 20, y = 250)
                    ent_confirm_password = Entry(window_2, textvariable = confirm_pass_word, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 20, y = 280)

                    btn_answer_show = Button(window_2, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_answer).place(x = 520, y = 140)
                    btn_password_show = Button(window_2, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_new_password).place(x = 520, y = 210)
                    btn_confirm_pass_show = Button(window_2, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_confirm_password).place(x = 520, y = 280)

                    btn_cancel = Button(window_2, text = 'Cancel', font = ('arial', 14, 'bold'), height = 1, width = 10, bd = 1, command = cancel_process).place(x = 20, y = 330)
                    btn_change_password = Button(window_2, text = 'Change Password', font = ('arial', 14, 'bold'), height = 1, width = 15, bd = 1, command = password_change).place(x = 375, y = 330)

                    flag = 1                    
                    break
                row_count += 1
                
            if flag == 0:
                msg.showerror('Search Failed', 'Username does not exist')
def show_answer():
    ent_security_question = Entry(window_2, textvariable = question_answer, font = ('arial', 16, 'bold'), width = 40).place(x = 20, y = 140)
    btn_answer_hide = Button(window_2, text = 'Hide', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = hide_answer).place(x = 520, y = 140)

def hide_answer():
    ent_security_question = Entry(window_2, textvariable = question_answer, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 20, y = 140)
    btn_answer_show = Button(window_2, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_answer).place(x = 520, y = 140)

def show_new_password():
    ent_new_password = Entry(window_2, textvariable = new_pass_word, font = ('arial', 16, 'bold'), width = 40).place(x = 20, y = 210)
    btn_password_show = Button(window_2, text = 'Hide', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = hide_new_password).place(x = 520, y = 210)
    
def hide_new_password():
    ent_new_password = Entry(window_2, textvariable = new_pass_word, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 20, y = 210)
    btn_password_show = Button(window_2, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_new_password).place(x = 520, y = 210)

def show_confirm_password():
    ent_confirm_password = Entry(window_2, textvariable = confirm_pass_word, font = ('arial', 16, 'bold'), width = 40).place(x = 20, y = 280)
    btn_confirm_pass_show = Button(window_2, text = 'Hide', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = hide_confirm_password).place(x = 520, y = 280)
    
def hide_confirm_password():
    ent_confirm_password = Entry(window_2, textvariable = confirm_pass_word, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 20, y = 280)
    btn_confirm_pass_show = Button(window_2, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_confirm_password).place(x = 520, y = 280)

    
def cancel_process():
    cancel = msg.askquestion('Cancel the Process', 'Are you sure to cancel the process')
    if cancel == 'yes':
        window_2.destroy()
        existing_user()
    
def password_change():
    if question_answer.get() == '':
        msg.showwarning('Warning', 'Security Question is not answered')
    elif new_pass_word.get() == '':
        msg.showwarning('Warning', 'New Password field is empty')
    elif confirm_pass_word.get() == '':
        msg.showwarning('Warning', 'Confirm Password field is empty')
    else:
        if str(question_answer.get()).lower() == existing_answer:
            password = str(new_pass_word.get())
            special_character = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '/', '?']
            
            if (len(password) < 8) or (not any(letter.isdigit() for letter in password)) or (not any(letter.isupper() for letter in password)) or (not any(letter.islower() for letter in password)) or (not any(letter in special_character for letter in password)):
                msg.showwarning('Warning', 'Length of the Password must be atleast 8\nPassword must contain atleast a number\nPassword must contain atleast a uppercase letter\nPassword must contain atleast a lowercase letter\nPassword must contain atleast a special character - !@#$%^&*_/?')
            else:
                if new_pass_word.get() == confirm_pass_word.get():
                    file = pd.read_csv('user details.csv')
                    file.loc[row_count, 'password'] = str(new_pass_word.get())
                    file.to_csv('user details.csv', index = False)

                    msg.showinfo('Successful', 'Successfully Changed the Password')

                    window_2.destroy()

                    existing_user()
                else:
                    msg.showwarning('Warning', 'New Password must match with the Confirm Password')
        else:
            msg.showerror('Error', 'Security Question Answer is incorrect')

def login_user():
    if user_name.get() == '':
        msg.showwarning('Warning', 'Username is Required')
    elif pass_word.get() == '':
        msg.showwarning('Warning', 'Password is Required')
    elif user_name.get() != '' and pass_word.get() != '':
        email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        if(not(re.search(email, str(user_name.get())))):
            msg.showwarning('Warning', 'Invalid User Name')
        else:
            file = pd.read_csv('user details.csv')

            flag = 0
            for index, row in file.iterrows():
                if row['username'] == str(user_name.get()) and row['password'] == str(pass_word.get()):
                    flag = 1
                    break

            if flag == 0:
                msg.showerror('Login Failed', 'Invalid Login Credentials')
                pass_word.set('')
            else:                
                window.destroy()

                global window_1
                window_1 = Tk()
                window_1.title('Logged In')
                window_1.geometry('600x200')
                window_1.resizable(False, False)
                window_1['bg'] = '#FBEAEB'

                lbl_info = Label(window_1, text = 'Successful Login', font = ('arial', 28, 'bold'), bg = '#FBEAEB', fg = '#2F3C7E', padx = 15, pady = 15).pack()

                btn_logout = Button(window_1, text = 'Sign Out', font = ('arial', 16, 'bold'), width = 10, height = 1, bd = 1, command = sign_out).place (x = 230, y = 75)

def sign_out():
    log_off = msg.askquestion('Log Out', 'Do you want to sign out')
    if log_off == 'yes':
        window_1.destroy()
        existing_user()

def new_user():
    window.destroy()

    global window_1, reg_user_name, security_question, sec_ques_answer, reg_pass_word, reg_confirm_pass_word
    
    window_1 = Tk()
    window_1.title('New User Registration')
    window_1.geometry('630x540')
    window_1.resizable(False, False)
    window_1['bg'] = '#FBEAEB'

    reg_user_name = StringVar()
    security_question = StringVar()
    sec_ques_answer = StringVar()
    reg_pass_word = StringVar()
    reg_confirm_pass_word = StringVar()

    lbl_info = Label(window_1, text = 'New User Registration', font = ('arial', 30, 'bold'), bg = '#FBEAEB', fg = '#2F3C7E', padx = 15, pady = 15).pack()

    lbl_user_name = Label(window_1, text = 'Username', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 40, y = 80)
    ent_user_name = Entry(window_1, textvariable = reg_user_name, font = ('arial', 16, 'bold'), width = 45).place(x = 40, y = 110)

    lbl_security_question = Label(window_1, text = 'Security Question', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 40, y = 150)
    drp_security_question = Combobox(window_1, textvariable = security_question, values = sec_ques_options, width = 44, font = font_style).place(x = 40, y = 180)
    
    lbl_question_answer = Label(window_1, text = 'Security Question Answer', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 40, y = 220)
    ent_question_answer = Entry(window_1, textvariable = sec_ques_answer, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 40, y = 250)

    lbl_password = Label(window_1, text = 'Password', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 40, y = 290)
    ent_password = Entry(window_1, textvariable = reg_pass_word, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 40, y = 320)

    lbl_reg_confirm_password = Label(window_1, text = 'Confirm Password', font = ('arial', 16, 'bold'), bg = '#FBEAEB', fg = '#CC313D').place(x = 40, y = 360)
    ent_reg_confirm_password = Entry(window_1, textvariable = reg_confirm_pass_word, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 40, y = 390)

    btn_answer_show = Button(window_1, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_question_answer).place(x = 530, y = 250)
    btn_password_show = Button(window_1, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_reg_password).place(x = 530, y = 320)
    btn_confirm_pass_show = Button(window_1, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_reg_confirm_password).place(x = 530, y = 390)

    btn_back = Button(window_1, text = 'Back', font = ('arial', 14, 'bold'), height = 1, width = 8, bd = 1, command = move_backward).place(x = 40, y = 470)
    btn_register = Button(window_1, text = 'Register', font = ('arial', 14, 'bold'), height = 1, width = 8, bd = 1, command = register_user).place(x = 470, y = 470) 

def show_question_answer():
    ent_question_answer = Entry(window_1, textvariable = sec_ques_answer, font = ('arial', 16, 'bold'), width = 40).place(x = 40, y = 250)
    btn_answer_hdie = Button(window_1, text = 'Hide', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = hide_question_answer).place(x = 530, y = 250)

def hide_question_answer():
    ent_question_answer = Entry(window_1, textvariable = sec_ques_answer, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 40, y = 250)
    btn_answer_hdie = Button(window_1, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_question_answer).place(x = 530, y = 250)

def show_reg_password():
    ent_password = Entry(window_1, textvariable = reg_pass_word, font = ('arial', 16, 'bold'), width = 40).place(x = 40, y = 320)
    btn_password_show = Button(window_1, text = 'Hide', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = hide_reg_password).place(x = 530, y = 320)
    
def hide_reg_password():
    ent_password = Entry(window_1, textvariable = reg_pass_word, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 40, y = 320)
    btn_password_show = Button(window_1, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_reg_password).place(x = 530, y = 320)

def show_reg_confirm_password():
    ent_reg_confirm_password = Entry(window_1, textvariable = reg_confirm_pass_word, font = ('arial', 16, 'bold'), width = 40).place(x = 40, y = 390)
    btn_confirm_pass_show = Button(window_1, text = 'Hide', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = hide_reg_confirm_password).place(x = 530, y = 390)
    
def hide_reg_confirm_password():
    ent_reg_confirm_password = Entry(window_1, textvariable = reg_confirm_pass_word, font = ('arial', 16, 'bold'), width = 40, show = '*').place(x = 40, y = 390)
    btn_confirm_pass_show = Button(window_1, text = 'Show', font = ('arial', 10, 'bold'), height = 1, width = 5, bd = 1, command = show_reg_confirm_password).place(x = 530, y = 390)

def register_user():
    if reg_user_name.get() == '':
        msg.showwarning('Warning', 'Username cannot be empty')
    elif security_question.get() not in sec_ques_options:
        msg.showwarning('Warning', 'Invalid Security Question')
    elif sec_ques_answer.get() == '':
        msg.showwarning('Warning', 'Provide an answer for the security question')
    elif reg_pass_word.get() == '':
        msg.showwarning('Warning', 'Provide a Password')
    elif reg_confirm_pass_word.get() == '':
        msg.showwarning('Warning', 'Provide a Password')
    else:
        email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
        if(not(re.search(email, str(reg_user_name.get())))):
            msg.showwarning('Warning', 'Invalid User Name.\nProvide a Valid Email Address')
        else:
            file = pd.read_csv('user details.csv')

            flag = 0
            for index, row in file.iterrows():
                if row['username'] == str(reg_user_name.get()):
                    flag = 1
                    break
            if flag == 1:
                msg.showerror('Error', 'Email Id is already registered.')
                reg_user_name.set('')
                security_question.set('')
                sec_ques_answer.set('')
                reg_pass_word.set('')
                reg_confirm_pass_word.set('')
            else:
                password = str(reg_pass_word.get())
                special_character = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '/', '?']
                if (len(password) < 8) or (not any(letter.isdigit() for letter in password)) or (not any(letter.isupper() for letter in password)) or (not any(letter.islower() for letter in password)) or (not any(letter in special_character for letter in password)):
                    msg.showwarning('Warning', 'Length of the Password must be atleast 8\nPassword must contain atleast a number\nPassword must contain atleast a uppercase letter\nPassword must contain atleast a lowercase letter\nPassword must contain atleast a special character - !@#$%^&*_/?')
                else:
                    if reg_pass_word.get() == reg_confirm_pass_word.get():
                        file = pd.read_csv('user details.csv')
                        file.loc[len(file.index)] = [str(reg_user_name.get()), str(reg_pass_word.get()), str(security_question.get()), str(sec_ques_answer.get()).lower()]
                        file.to_csv('user details.csv', index = False)

                        msg.showinfo('Success', 'Account Created Successfully')

                        window_1.destroy()

                        existing_user()
                    else:
                        msg.showwarning('Warning', 'Confirm password must match with the password entered')
        
existing_user()
