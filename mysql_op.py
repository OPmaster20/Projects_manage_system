import pymysql

import mess
import mess as m
import random as r
import time as t
import re

k = True
c = 0
access_code = 2000  #2000 are normal

username_infor = ''
password_infor = ''

conn = pymysql.connect(host="localhost",port=3306,
                       user="root",password="root",
                       database="institute_db",charset="utf8mb4")

cur = conn.cursor()
def verify_database(username,password):
    if setup_in_user(str(username.get())) == 1:
        global username_infor, password_infor
        username_infor = str(username.get())
        password_infor = get_password()
        return 1
    if len(str(username.get())) == 0 and len(str(password.get())) == 0:
        m.halt(200)
        return 0
    elif len(str(password.get())) == 0:
        m.halt(101)
        return 0
    elif len(str(username.get())) == 0:
        m.halt(100)
        return 0
    else:
        if user_data_fun(str(username.get()),str(password.get())) == 1:
            return 1
        else:
            return 0
    #print(f"> {str(username.get())} , {str(password.get())}")

def get_password():
    search = "select user_password from user where user_name = \'" + username_infor + "\';"
    cur.execute(search)
    for i in cur.fetchall():
        return i[0]
def access_code_value():
    return_value = "select access_code from access_infor where user_index_a = (select user_index from user where user_name = \'" + username_infor + "\');"
    print(return_value)
    cur.execute(return_value)
    for i in cur.fetchall():
        print(i[0])
        if i[0] == "2000":
            return 0
        else:
            return 1
def setup_in_user(username):
    search = "select user_index from user where user_name = \'" + str(username) + "\';"
    cur.execute(search)
    index = 0
    access_p = 0
    for i in cur.fetchall():
        index = int(i[0])

    if index == 0:
        m.halt(301)
        return 0
    else:
        check = "select access_code from access_infor where user_index_a = \'" + str(index) + "\';"
        cur.execute(check)
        for i in cur.fetchall():
            access_p = int(i[0])

        if access_p == 2000:
            return 0
        else:
            return 1


def update_access_code(n,username):
    search = "select user_index from user where user_name = \'" + str(username) + "\';"
    cur.execute(search)
    index = 0
    for i in cur.fetchall():
        index = int(i[0])
    if n == 1:
        update1 = "update `access_infor` set `access_code` = \'2001\' where `user_index_a` = \'" + str(index) + "\';"
        cur.execute(update1)
        conn.commit()
        mess.user_console(8)
    else:
        update2 = "update `access_infor` set `access_code` = \'2000\' where `user_index_a` = \'" + str(index) + "\';"
        cur.execute(update2)
        conn.commit()
        mess.user_console(9)



def user_data_fun(username,password):
    global username_infor,password_infor
    search = "select user_name,user_password from user;"
    k = 0
    cur.execute(search)
    for i in cur.fetchall():
        if i[0] == username and i[1] == password:
            m.user_res(5)
            k = 1
            access(username,password)
            username_infor = username
            password_infor = password
            return 1

    if k == 0:
        m.halt(350)
        return 0
def user_data_fun_register(username,password,email,number):
    global username_infor, password_infor
    index = r.randrange(2, 100)
    insert = ("insert into `user`(`user_index`,`user_name`,`user_password`,`user_email`,`user_number`) values(" +
              '\'' + str(index) + '\'' + "," + '\'' + str(username) + '\'' +  ',' + '\'' + str(password) + '\'' +  ',' + '\'' + str(email) + '\'' +  ',' + '\'' + str(number) + '\'' + ');')
    cur.execute(insert)
    conn.commit()
    m.user_res(4)
    access(username,password)
    username_infor = username
    password_infor = password
    return 1

def access(username,password):
    search = "select user_index from user where user_name = \'" + str(username) + "\' and " + "user_password = \'" + str(password) + "\';"
    cur.execute(search)
    for i in cur.fetchall():
        index = i[0]

    time = t.gmtime()
    if is_there(index) == 0:
        add_user = "insert into `access_infor` (`user_index_a`,`access_time`,`access_code`,`log_out_time`) values (\'" + str(index) + '\',' + '\'' + str(t.strftime("%Y-%m-%d %H:%M:%S",time)) + '\',\'' + str(access_code) + '\',\'During\');'
        cur.execute(add_user)
        conn.commit()
    else:
        update_user = "update `access_infor` set `access_time` = " + '\'' + str(t.strftime("%Y-%m-%d %H:%M:%S",time)) + '\' ' + 'where user_index_a = ' + '\'' + str(index) + '\';'
        print(update_user)
        cur.execute(update_user)
        conn.commit()
def is_there(index):
    verify = "select user_index_a from access_infor where user_index_a = \'" + str(index) + '\';'
    cur.execute(verify)
    if len(cur.fetchall()) == 0:
        return 0
    return 1

def log_out():
    search = "select user_index from user where user_name = \'" + username_infor + "\' and " + "user_password = \'" + password_infor + "\';"
    cur.execute(search)
    for i in cur.fetchall():
        n = i[0]
    time = t.gmtime()
    update = "update `access_infor` set `log_out_time` = \'" + str(t.strftime("%Y-%m-%d %H:%M:%S",time)) + "\' where user_index_a = \'" + str(n) + "\';"
    cur.execute(update)
    conn.commit()
def del_user():
    search = "delete * from user where user_name = \'" + username_infor + "\' and " + "user_password = \'" + password_infor + "\';"
    cur.execute(search)
    conn.commit()
    m.user_console(6)

def update_user(email,username,password):
    verify_eamil = "select count(*) from user where user_email = \'" + str(email) + '\';'
    cur.execute(verify_eamil)
    print(email)
    k = 0
    for i in cur.fetchall():
        if int(i[0]) == 0:
            print(int(i[0]))
            m.user_console(2)
            return 0
        else:
            k += 1
    if not re.search("^[0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z]$",str(password)):
        m.user_res(1)
        return 0

    search_same = "select * from user where user_name = \'" + str(username) + "\';"
    cur.execute(search_same)
    for i in cur.fetchall():
        if int(i[0]) != 0:
            m.user_res(6)
            return 0

    if k == 1:
        update = "update `user` set `user_name` = \'" + str(username) + '\',`user_password` = \'' + str(password) + '\' where user_email = \'' + str(email) + '\';'
        print(update)
        cur.execute(update)
        conn.commit()
        m.user_console(3)
        return 1
def success():
    print("success!!")