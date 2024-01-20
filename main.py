import sys
import tkinter as t
from tkinter import ttk, Frame,messagebox
from PIL import ImageTk,Image
import time

import mysql_op
import mysql_op as mysql
import console as s
import register_user as r




#img = Image.open("UI_img/label.png")
#imgs = img.resize((20,20))
#imgs = ImageTk.PhotoImage(imgs)


class user:
    def __init__(self, name, password):
        self.window = t.Tk()
        self.window.title("Institute system")
        self.window.geometry('300x400')
        self.photo = Image.open(r'UI_img/user.jpg')
        self.photo = self.photo.resize((300, 400))
        self.photo = ImageTk.PhotoImage(self.photo)
        self.bd = t.Label()
        self.bd.pack()
        self.bd['image'] = self.photo

        if mysql_op.k:
            self.icon = t.PhotoImage(file='UI_img/label.png')
            mysql_op.k = False
            self.window.iconphoto(True, self.icon)


        self.username = name
        self.passwords = password

        self.user_interface()
    def user_interface(self):



        self.text2 = t.Label(self.window, text='Log entry',background='blue', width=18, height=1)
        self.text2.place(x=90, y=100)

        self.L1 = t.Label(text='U')
        self.L1.place(x=75,y=145)

        self.L2 = t.Label(text='P')
        self.L2.place(x=75, y=170)

        self.username_entry = t.Entry(self.window, width=21, cursor='plus')
        self.username_entry.place(x=90, y=145)

        self.password_entry = t.Entry(self.window, show='*',width=21, cursor='plus')
        self.password_entry.place(x=90,y=170)

        self.log_button = t.Button(self.window ,text='Log in', command=lambda: self.entry(mysql.verify_database(self.username_entry,self.password_entry)), width=6, height=1)
        self.log_button.place(x=90, y=210)

        self.log_button = t.Button(self.window, text='Register',command=lambda: self.init_register(), width=6, height=1)
        self.log_button.place(x=168, y=210)

        self.window.mainloop()

    def recover(self):
        self.window.update()
        self.window.after(100)
        self.window.deiconify()

    def user_get(self):
        pass
        #print(str(self.get()))

    def entry(self,k):
        if k == 1:
            self.window.withdraw()
            self.vis_window(1)

    def init_register(self):
        self.window.withdraw()
        self.user = r.user_register(" ", " ", " ", " ")
        self.user.register_interface()
        self.window.deiconify()

    def vis_window(self,k):
        if k == 1:
            s.Main()


def main(k = 0):
    if mysql_op.k:
        t = user(" ", 0)
    else:
        t2 = user(" ", 0)
        t2.recover()


if __name__ == '__main__':
    main()



