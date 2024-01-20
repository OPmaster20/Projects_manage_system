from tkinter import ttk, Frame,messagebox
import tkinter as t

def halt(code):
    if code == 100:
        t.messagebox.showinfo(title='Error',message='You username is NULL !')
    elif code == 101:
        t.messagebox.showinfo(title='Error', message='You password is NULL !')
    elif code == 200:
        t.messagebox.showinfo(title='Error', message='You username and password is NULL !')
    elif code == 301:
        t.messagebox.showinfo(title='Warn', message='You username is not existed !')
    elif code == 302:
        t.messagebox.showinfo(title='Warn', message='You password is not existed !')
    elif code == 350:
        t.messagebox.showinfo(title='Warn', message='You information is not existed !')
    elif code == 400:
        t.messagebox.showinfo(title='Warn', message='LOG IN SUCCESS!')
    elif code == 450:
        t.messagebox.showinfo(title='Warn', message='Database connect error!')
    elif code == 500:
        t.messagebox.showinfo(title='Warn', message='No data can operate!')


def user_res(code):
    if code == 1:
        t.messagebox.showinfo(title='Error', message='The password is invalid!')
    elif code == 2:
        t.messagebox.showinfo(title='Error', message='You email is invalid !')
    elif code == 3:
        t.messagebox.showinfo(title='Error', message='You phone number is invalid !')
    elif code == 4:
        t.messagebox.showinfo(title='warn', message='Register success! ')
    elif code == 5:
        t.messagebox.showinfo(title='warn', message='Log in success! ')
    elif code == 6:
        t.messagebox.showinfo(title='Error', message='User name has been registered, please re-enter!')


def user_console(code):
    if code == 1:
        t.messagebox.showinfo(title='warn', message='The language has changed')
    elif code == 2:
        t.messagebox.showinfo(title='warn', message='The mailbox does not exist')
    elif code == 3:
        t.messagebox.showinfo(title='warn', message='The user name and password are successfully changed')
    elif code == 4:
        t.messagebox.showinfo(title='warn', message='Exit successfully')
    elif code == 5:
        n = t.messagebox.askquestion(title='warn', message='Are you sure you want to delete your account?')
        if n == 'yes':
            return 1
    elif code == 6:
        t.messagebox.showinfo(title='warn', message='Delete successfully')
    elif code == 7:
        t.messagebox.showinfo(title='warn', message='Please login again')
    elif code == 8:
        t.messagebox.showinfo(title='warn', message='Next time you can log in without a password if you check it')
    elif code == 9:
        t.messagebox.showinfo(title='warn', message='Next time you need a password to log in if you unchecked it')

def user_data(code):
    if code == 1:
        t.messagebox.showinfo(title='warn', message='The database is modified successfully')
    elif code == 2:
        t.messagebox.showinfo(title='warn', message='No information is selected')
    elif code == 3:
        t.messagebox.showinfo(title='warn', message='Data update success')
    elif code == 4:
        t.messagebox.showinfo(title='warn', message='Delete professional success')
