import sys
import tkinter as tk
from tkinter.constants import (HORIZONTAL, VERTICAL, RIGHT, LEFT, X, Y, BOTH, BOTTOM, YES)
from tkinter import ttk, Frame, messagebox, PanedWindow, BOTH
from PIL import ImageTk,Image
import time as t
import data_mysql_op as mysql
import translate as ts
import mess



class fun:
    pages = [0,0,0]
    text14 = "Query result"
    text16 = "Department name"
    text17 = "Specialties"
    text18 = "Universal search"
    text19 = "Including personnel"
    text20 = "form of study"
    text21 = "Submit"
    text22 = "Enter your name"
    text23 = "Modify data"
    text24 = "The updated profession"
    text25 = "Modify student major"
    text26 = "Add data"
    text27 = "Enter a new major"
    text28 = "Enter your department"
    text29 = "Enter phone number"
    text30 = "Delete majors information"
    options = 0
    optionss = 0
    optionsss = 0
    count = 0
    def text(self,count):
        if count == 1:
            self.change()
    def init(self,count = 0):
        self.dataframe = tk.Toplevel()
        self.dataframe.title("Data query")
        self.dataframe.geometry('1000x600')

        self.image = Image.open(r'UI_img/data_bd.jpg')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)

        self.backgroud = tk.Label(self.dataframe)
        self.backgroud.pack()
        self.backgroud['image'] = self.image

        self.board = Image.open(r"UI_img/board.png")
        self.board = self.board.resize((870,310))
        self.board = ImageTk.PhotoImage(self.board)

        self.framex = tk.Frame(self.dataframe, relief='sunken',bd=5,width=870, height=310)
        self.framex.place(x=60, y=250)
        self.backboard = tk.Label(self.framex)
        self.backboard.pack()
        self.backboard['image'] = self.board


        self.sb = tk.Scrollbar(self.framex,orient=HORIZONTAL)
        self.sb.pack(side=BOTTOM,fill=X)

        self.textframe = tk.Text(self.framex,width=106,height=16,undo=True,autoseparators=False)
        self.textframe.place(x=10,y=10)

        self.textframe.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.textframe.xview)



        self.operationframe1 = tk.Frame(self.dataframe,relief='solid',bd=5,width=500,height=120,background="#FFFFFF")
        self.operationframe1.place(x=60,y=120)
        self.pages[0] = 1
        #self.but = tk.Button(self.dataframe,text=self.text18,state='active', relief='sunken',width=17, height=2)
        #self.but.place(x=60,y=60)


        self.list = tk.Listbox(self.operationframe1,selectmode='multiple',cursor='cross',height=4)
        self.list.place(x=15,y=30)


        self.listarr = list()
        self.listarr = mysql.get_department()
        for i in self.listarr:
            self.list.insert("end",i)

        self.var = tk.StringVar()
        self.specialties = ttk.Combobox(self.operationframe1,textvariable=self.var,width=10,state='readonly')
        self.splis = list()
        self.splis = mysql.get_specialties()
        self.specialties['values'] = self.splis
        self.specialties.place(x=160,y=30)

        self.option1 = tk.Checkbutton(self.operationframe1,text=self.text19,command=lambda: self.display_person(),onvalue=1,offvalue=0)
        self.option1.place(x=250,y=6)
        self.operationframe2 = tk.Frame(self.dataframe, relief='solid', bd=5, width=347, height=120,background="#FFFFFF")
        self.operationframe2.place(x=600, y=120)

        self.submit = tk.Button(self.operationframe1,text=self.text21,command=lambda : self.result(),width=6)
        self.submit.place(x=400,y=6)

        self.option2 = tk.Checkbutton(self.operationframe1, text=self.text23, command=lambda: self.display_update(),
                                      onvalue=1, offvalue=0)
        self.option2.place(x=250, y=50)

        self.option3 = tk.Checkbutton(self.operationframe1, text=self.text26, command=lambda: self.display_add(),
                                      onvalue=1, offvalue=0)
        self.option3.place(x=250, y=80)


        self.text(count)
        self.Lab = tk.Label(self.framex,text=self.text14,width=10)
        self.Lab.place(x=384,y=270)

        self.title1 = tk.Label(self.operationframe1, text=self.text16, width=17)
        self.title1.place(x=15, y=6)

        self.title2 = tk.Label(self.operationframe1, text=self.text17, width=10)
        self.title2.place(x=160, y=6)




        self.dataframe.mainloop()
    def change(self):
        self.text14 = ts.Translator.translate(self.text14)
        self.text16 = ts.Translator.translate(self.text16)
        self.text17 = ts.Translator.translate(self.text17)
        self.text19 = ts.Translator.translate(self.text19)
        self.text20 = ts.Translator.translate(self.text20)
        self.text21 = ts.Translator.translate(self.text21)
        self.text22 = ts.Translator.translate(self.text22)
        self.text23 = ts.Translator.translate(self.text23)
        self.text24 = ts.Translator.translate(self.text24)
        self.text25 = ts.Translator.translate(self.text25)
        self.text26 = ts.Translator.translate(self.text26)
        self.text27 = ts.Translator.translate(self.text27)
        self.text28 = ts.Translator.translate(self.text28)
        self.text29 = ts.Translator.translate(self.text29)
        self.text30 = ts.Translator.translate(self.text30)
        self.dataframe.withdraw()
        self.dataframe.deiconify()

    def display_person(self):
        if self.options == 0:
            self.options = 1
            if self.optionss == 1:
                self.option2.deselect()
                self.optionss = 0
                for i in self.operationframe2.winfo_children():
                    i.destroy()
            self.title3 = tk.Label(self.operationframe2, text=self.text20, width=10)
            self.title3.place(x=10, y=6)
            self.var2 = tk.StringVar()
            self.study = ttk.Combobox(self.operationframe2,textvariable=self.var2,width=10,state='readonly')
            self.studylis = list()
            self.studylis = mysql.get_form_study()

            self.title4 = tk.Label(self.operationframe2,text=self.text22,width=18)
            self.title4.place(x=110,y=6)
            self.person_name = tk.Entry(self.operationframe2,width=20)
            self.person_name.place(x=110,y=30)

            self.study['values'] = self.studylis
            self.study.place(x=10,y=30)

        else:
            self.options = 0
            if self.study:
                for i in self.operationframe2.winfo_children():
                    i.destroy()

    def display_add(self):
        if self.optionsss == 0:
            self.operationframe2.place_forget()
            self.specialties.place_forget()
            self.optionsss = 1
            self.operationframe3 = tk.Frame(self.dataframe, relief='solid', bd=5, width=880, height=40,
                                            background="#FFFFFF")
            self.operationframe3.place(x=60, y=65)
            self.title5 = tk.Label(self.operationframe3, text=self.text27, width=18)
            self.title5.place(x=10, y=6)
            self.title6 = tk.Label(self.operationframe3, text=self.text28, width=18)
            self.title6.place(x=280, y=6)
            self.title7 = tk.Label(self.operationframe3, text=self.text29, width=18)
            self.title7.place(x=560, y=6)
            self.add_f = tk.Entry(self.operationframe3, width=20)
            self.add_f.place(x=420, y=6)
            self.add_p = tk.Entry(self.operationframe3, width=20)
            self.add_p.place(x=700, y=6)
            self.add_name = tk.Entry(self.operationframe3, width=20)
            self.add_name.place(x=150,y=6)
            self.list.config(selectmode='single')
        else:
            self.list.config(selectmode='multiple')
            self.optionsss = 0
            for i in self.operationframe3.winfo_children():
                i.destroy()
            self.operationframe3.destroy()
            self.operationframe2.place(x=600, y=120)
            self.specialties.place(x=160,y=30)

    def display_update(self):
        if self.optionss == 0:
            self.optionss = 1

            if self.options == 1:
                self.option1.deselect()
                self.options = 0
                for i in self.operationframe2.winfo_children():
                    i.destroy()
            self.option3_1 = tk.Checkbutton(self.operationframe2, text=self.text30,command=lambda :self.review(),onvalue=1, offvalue=0)
            self.option3_1.place(x=10, y=80)

            self.list.config(selectmode='single')
            self.title4 = tk.Label(self.operationframe2, text=self.text25, width=18)
            self.title4.place(x=10, y=6)

            self.person_name_up = tk.Entry(self.operationframe2, width=20)
            self.person_name_up.place(x=10, y=30)
        else:
            self.optionss = 0
            self.list.config(selectmode='multiple')
            for i in self.operationframe2.winfo_children():
                i.destroy()

    def review(self):
        if self.count == 0:
            self.count = 1
            self.title4.place_forget()
            self.specialties.place_forget()
            self.person_name_up.place_forget()
            self.title0 = tk.Label(self.operationframe2, text=self.text30, width=20)
            self.title0.place(x=10, y=6)
            self.person_m_up = tk.Entry(self.operationframe2, width=20)
            self.person_m_up.place(x=10, y=30)
        else:
            self.count = 0
            self.title4.place(x=10, y=6)
            self.person_name_up.place(x=10, y=30)
            self.title0.destroy()
            self.person_m_up.destroy()
            self.specialties.place(x=160, y=30)
    def result(self):

        self.textframe.delete(1.0,"end")
        search_department_number = list()

        for i in self.list.curselection():
                search_department_number.append(i)

        var_specialties = self.var.get()
        if self.optionsss == 1:
            add_name = self.add_name.get()
            add_fac = self.add_f.get()
            add_phone = self.add_p.get()
            re_add = mysql.add_data(search_department_number,add_name,add_fac,add_phone)
            self.textframe.insert('insert', re_add)
        try:
            if self.options == 0:
                if self.optionss == 1:
                    if self.count == 1:
                        del_m = self.person_m_up.get()
                        mysql.del_data(str(del_m))
                        self.textframe.insert('insert', "Delete professional success")
                        self.dataframe.withdraw()
                        self.dataframe.deiconify()
                    else:
                        update_name = self.person_name_up.get()
                        update_re = mysql.operation_update(search_department_number,str(var_specialties),str(update_name))
                        self.textframe.insert('insert', update_re)
                        self.dataframe.withdraw()
                        self.dataframe.deiconify()
                else:
                    re = mysql.print_fun1(search_department_number,str(var_specialties))
                    self.textframe.insert('insert', re)
                    self.dataframe.withdraw()
                    self.dataframe.deiconify()
            elif self.options == 1:
                search_name = self.person_name.get()
                var_form_of_study = self.var2.get()
                re2 = mysql.print_fun2(search_department_number, str(var_specialties),search_name,var_form_of_study)
                self.textframe.insert('insert', re2)
                self.dataframe.withdraw()
                self.dataframe.deiconify()
            else:
                mess.user_data(2)
        except:
            print("heelo")

def start(count):
    main = fun()
    main.init(count)


