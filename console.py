import sys
import tkinter as t2
from tkinter import ttk, Frame, messagebox, PanedWindow, BOTH
from PIL import ImageTk,Image
import time


import mysql_op as mysql
import translate as ts
import mess
from importlib import reload
import system_main_function as fun


ts_count = 0
pages = [0,0,0]
class Main:
    text1 = "translate"
    text2 = "User"
    text3 = "Exit"
    text4 = "More"
    text5 = "web search"
    text6 = "Query"
    text7 = "User: "
    text8 = "Back"
    text9 = "Welcome to the Institute system"
    text10 = "Modify account"
    text12 = "Delete account"
    text11 = "Confirm"
    text13 = "Home"
    text15 = "Login without password"
    def __init__(self):
        self.mainframe = t2.Toplevel()
        self.mainframe.title("System")
        self.mainframe.geometry('300x400')

        self.photo2 = Image.open('UI_img/img.jpg')
        self.photo2 = self.photo2.resize((300, 400))
        self.photo2 = ImageTk.PhotoImage(self.photo2)


        self.bd_s = t2.Label(self.mainframe)
        self.bd_s.pack()
        self.bd_s['image'] = self.photo2

        self.mb = t2.Menubutton(self.mainframe, text=self.text4, relief="raised")
        self.mb.place(x=15, y=10)
        #self.mb.pack()

        self.page()
    def page(self,k = 0):
        if k == 1:
            self.bur()
        self.imgs = Image.open(r'UI_img/ui.jpg')
        self.imgs = self.imgs.resize((268, 290))
        self.imgs = ImageTk.PhotoImage(self.imgs)
        pages[1] = 1
        self.inter = t2.Frame(self.mainframe, width=268, height=290)
        self.inter.place(x=15, y=50)
        self.bds = t2.Label(self.inter)
        self.bds.pack()
        self.bds['image'] = self.imgs

        self.l2 = t2.Label(self.inter,text=self.text9)
        self.l2.place(x=25,y=30)


        self.web = t2.Button(self.mainframe, command=lambda:self.web_op(),text=self.text5,width=9,height=1)
        self.web.place(x=75,y=10)

        self.data = t2.Button(self.mainframe, command=lambda:self.data_op(), text=self.text6, width=4, height=1)
        self.data.place(x=150, y=10)


        self.mb = t2.Menubutton(self.mainframe, text=self.text4, relief="raised")
        self.mb.place(x=15, y=10)
        self.option = t2.Menu(self.mb, tearoff=False)
        self.option.add_command(label=self.text1, command=lambda: self.reload())
        self.option.add_command(label=self.text2, command=lambda: self.user())
        self.option.add_separator()
        self.option.add_command(label=self.text3, command=lambda: self.quit2())
        self.mb.config(menu=self.option)


        self.mainframe.mainloop()

    def quit2(self):
        mess.user_console(4)
        self.mainframe.destroy()
        mysql.log_out()
        sys.exit()

    def reload(self):
        global ts_count
        ts.Translator = ts.Translator('zh')
        self.text1 = ts.Translator.translate(self.text1)
        self.text2 = ts.Translator.translate(self.text2)
        self.text3 = ts.Translator.translate(self.text3)
        self.text4 = ts.Translator.translate(self.text4)
        self.text5 = ts.Translator.translate(self.text5)
        self.text6 = ts.Translator.translate(self.text6)
        self.text7 = ts.Translator.translate(self.text7)
        self.text8 = ts.Translator.translate(self.text8)
        self.text9 = ts.Translator.translate(self.text9)
        self.text10 = ts.Translator.translate(self.text10)
        self.text11 = ts.Translator.translate(self.text11)
        self.text12 = ts.Translator.translate(self.text12)
        self.text13 = ts.Translator.translate(self.text13)
        self.text15 = ts.Translator.translate(self.text15)
        ts_count = 1
        self.page(1)

    def des(self):
        for i in self.inter2.winfo_children():
            i.destroy()
        pages[0] = 0
        self.page(1)

    def des2(self):
        for i in self.inter3.winfo_children():
            i.destroy()
        pages[2] = 0
        self.page(1)

    def des3(self):
        if mysql.update_user(str(self.email.get()), str(self.newusername.get()), str(self.newpassword.get())) == 1:
            self.editframe.destroy()
            self.mainframe.deiconify()
    def del_user(self):
        if mess.user_console(5):
            mysql.del_user()
            mess.user_console(7)
            self.mainframe.destroy()
            from main import main
            main()


    def edit_user(self):
        self.mainframe.iconify()
        self.editframe = t2.Toplevel()
        self.editframe.title("Edit user")
        self.editframe.geometry('300x400')

        self.edit_img = Image.open(r'UI_img/edit.jpg')
        self.edit_img = self.edit_img.resize((300, 400))
        self.edit_img = ImageTk.PhotoImage(self.edit_img)

        self.edit_bds = t2.Label(self.editframe)
        self.edit_bds.pack()
        self.edit_bds['image'] = self.edit_img

        self.email = t2.Entry(self.editframe, width=21, cursor='plus')
        self.email.place(x=90,y=70)

        self.newusername = t2.Entry(self.editframe, width=21, cursor='plus')
        self.newusername.place(x=90, y=105)

        self.newpassword = t2.Entry(self.editframe, width=21, cursor='plus',show='*')
        self.newpassword.place(x=90, y=140)

        self.but_back2 = t2.Button(self.editframe, text=self.text8, background="#00008B", command=lambda: [self.editframe.destroy(),self.mainframe.deiconify()], width=6, height=1)
        self.but_back2.place(x=90, y=210)

        self.but_back2 = t2.Button(self.editframe, text=self.text11,background="#98FB98", command=lambda: self.des3(), width=6,height=1)

        self.but_back2.place(x=168, y=210)
        self.editframe.mainloop()

    check = 0
    def setup_user(self):
        if self.check == 0:
            self.check = self.check + 1
            mysql.update_access_code(1,mysql.username_infor)
            self.c.select()
        else:
            self.check = 0
            mysql.update_access_code(0,mysql.username_infor)
            self.c.deselect()
        print(self.check)
    def user(self):
        pages[0] = 1
        self.mainframe.withdraw()
        self.inter.destroy()
        pages[1] = 0
        self.inter2 = t2.Frame(self.mainframe, width=268, height=290,background="#FFFFFF")
        self.inter2.place(x=15, y=50)


        self.user_infor = t2.Label(self.inter2,text=self.text7 + mysql.username_infor)
        self.user_infor.place(x=110,y=80)

        self.img = Image.open(r'UI_img/im.png')
        self.img = self.img.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.img)
        self.user_img = t2.Label(self.inter2,width=50,height=50,image=self.img)
        self.user_img.place(x=110, y=20)

        self.but_back = t2.Button(self.inter2, text=self.text8, command=lambda: self.des(),width=6, height=1)
        self.but_back.place(x=110,y=130)

        self.but_edit = t2.Button(self.inter2, background="pink",text=self.text10, command=lambda: self.edit_user(), width=12, height=1)
        self.but_edit.place(x=30, y=240)

        self.but_del = t2.Button(self.inter2, background="red", text=self.text12, command=lambda: self.del_user(),width=12, height=1)
        self.but_del.place(x=160, y=240)

        self.c = t2.Checkbutton(self.inter2,text=self.text15,command=lambda: self.setup_user(),variable= mysql.access_code_value(),onvalue=1,offvalue=0)
        self.c.place(x=30,y=200)
        if mysql.access_code_value() == 1:
            self.c.select()
        else:
            self.c.deselect()






        self.mainframe.deiconify()

        #print(self.text1)

    def bur(self):
        global ts_count
        self.mainframe.withdraw()

        self.mb.destroy()
        self.option.destroy()
        if ts_count == 1:
            mess.user_console(1)
        self.mainframe.deiconify()

    def data_op(self):
        global ts_count
        self.mainframe.iconify()
        if pages[0] == 1:
            self.inter2.destroy()
        if pages[1] == 1:
            self.inter.destroy()

        pages[2] = 1
        fun.start(ts_count)
        self.mainframe.deiconify()

    def web_op(self):
        pass
