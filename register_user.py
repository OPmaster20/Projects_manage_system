import sys
import tkinter as t1
from PIL import ImageTk,Image
import re
import mysql_op as op
import mess as mm
import console as c
vis = 0
class user_register:
    def __init__(self, name, password,email,number):
        self.username = name
        self.passwords = password
        self.emails = email
        self.numbers = number
    def register_interface(self):
        global vis
        self.frame = t1.Toplevel()
        self.frame.title("📚User register")
        self.frame.geometry('300x400')
        self.photo1 = Image.open(r'UI_img/register.jpg')
        self.photo1 = self.photo1.resize((300,400))
        self.photo1 = ImageTk.PhotoImage(self.photo1)
        self.b = t1.Label(self.frame)
        #self.b.place(x=0,y=0)
        self.b.pack()
        self.b['image'] = self.photo1

        self.L = t1.Label(self.frame,text='Register page', width=18, height=1,background='pink')
        self.L.place(x=90,y=40)

        self.Lu = t1.Label(self.frame, text='U', background='pink')
        self.Lu.place(x=75, y=70)

        self.reg_username_entry = t1.Entry(self.frame, width=21, cursor='plus')
        self.reg_username_entry.place(x=90, y=70)

        self.Lp = t1.Label(self.frame, text='P', background='pink')
        self.Lp.place(x=75, y=105)

        self.reg_password_entry = t1.Entry(self.frame, width=21, cursor='plus')
        self.reg_password_entry.place(x=90, y=105)

        self.Le = t1.Label(self.frame, text='E', background='pink')
        self.Le.place(x=75, y=140)

        self.reg_email_entry = t1.Entry(self.frame, width=21, cursor='plus')
        self.reg_email_entry.place(x=90, y=140)

        self.Ln= t1.Label(self.frame, text='N', background='pink')
        self.Ln.place(x=75, y=170)

        self.reg_number_entry = t1.Entry(self.frame, width=21, cursor='plus')
        self.reg_number_entry.place(x=90, y=170)

        self.exit_button = t1.Button(self.frame, text='Log in',background='green', command=lambda: self.dest(self.reg_username_entry, self.reg_password_entry,
                                                                                                             self.reg_email_entry,self.reg_number_entry), width=6, height=1)
        self.exit_button.place(x=90, y=210)

        self.exit_button = t1.Button(self.frame, text='Exit', background='blue',command=lambda: self.quit(), width=6, height=1)
        self.exit_button.place(x=168, y=210)

        self.frame.mainloop()
    def dest(self,username,password,email,number):
        if re.search('^.*$',str(username.get())):
            if re.search("^[0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z]$",str(password.get())):
                if re.search("^.+.*@[A-Za-z][A-Za-z]\\..*$",str(email.get())):
                    if len(str(number.get())) == 9:
                        self.__init__(str(username.get()),str(password.get()),str(email.get()),str(number.get()))
                        if op.user_data_fun_register(str(username.get()),str(password.get()),str(email.get()),str(number.get())) == 1:
                            self.frame.withdraw()
                            c.Main()
                    else:
                        mm.user_res(3)
                else:
                    mm.user_res(2)
            else:
                mm.user_res(1)
        else:
            print("invalid")

        #self.frame.destroy()

    def quit(self):
        sys.exit()



