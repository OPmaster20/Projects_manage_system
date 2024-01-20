import pymysql

import mess
import mess as m
import random as r
import time as t
import re
import prettytable as pp

conn = pymysql.connect(host="localhost",port=3306,
                       user="root",password="root",
                       database="institute_db",charset="utf8mb4")

cur = conn.cursor()
list_de = ['all','Economy_institute','Information_institute','Language_institute']
connect = list()
def get_department():
    search = "select distinct title from department;"
    cur.execute(search)

    arr = list()
    arr.append("All")
    for i in cur.fetchall():
        for j in i:
            arr.append(j)

    return arr
def get_specialties():
    search = "select distinct specialties from department;"
    cur.execute(search)

    arr = list()
    arr.append("All")
    for i in cur.fetchall():
        for j in i:
            arr.append(j)

    return arr

def get_form_study():
    search = "select distinct form_study from specialty_s;"
    cur.execute(search)
    arr = list()
    arr.append("All ")
    for i in cur.fetchall():
        for j in i:
            arr.append(j)

    return arr
def print_fun1_department(var_list = list()):
    global connect
    search = ("select title,specialties,faculty,phone_number,semester from department,discipline where "
              "department.title = discipline.title_d")
    tb = pp.PrettyTable()
    lists = list()
    clean()
    connect = var_list
    tb.field_names = ['Name', 'Specialties', 'Faculty', 'Phone','Semester']
    str1 = list(get_values())
    if int(var_list[0]) == 0:
        search = search + ';'
        cur.execute(search)
        for i in cur.fetchall():
            lists.append(list(i))
        for j in range(len(lists)):
            tb.add_row(lists[j])
        return tb
    else:

        search = search + " and "
        p = 0
        for i in range(len(var_list)):
            search = search + "`title` = \'" + str1[p] + "\'"
            if (i+1) < (len(var_list)):
                search = search + " or "
                p += 1
        search = search + ";"
        print(search)
        cur.execute(search)
        for i in cur.fetchall():
            lists.append(list(i))

        for j in range(len(lists)):
            tb.add_row(lists[j])
        return tb
def print_fun1_majoy(var_string):
    tb = pp.PrettyTable()
    lists = list()
    tb.field_names = ['Specialties','Hours','Report']
    if var_string == 'All':
        search = "select specialties,hours,reporting from department,discipline where department.title = discipline.title_d;"
        cur.execute(search)
        for i in cur.fetchall():
            lists.append(list(i))
        for j in range(len(lists)):
            tb.add_row(lists[j])
        return tb
    search_random = "select specialties,hours,reporting from department,discipline where department.title = discipline.title_d and specialties = "
    search_random = search_random + "\'" + var_string + '\';'
    cur.execute(search_random)
    for i in cur.fetchall():
        lists.append(list(i))
    for j in range(len(lists)):
        tb.add_row(lists[j])
    return tb

def print_fun1(var_list = list(),var_string = ''):
    #print(var_list,var_string)
    global connect
    tb = pp.PrettyTable()
    lists = list()
    if var_string == '':
        tb = print_fun1_department(var_list)
        return tb
    if len(var_list) == 0:
        tb = print_fun1_majoy(var_string)
        return tb
    if int(var_list[0]) == 0 and var_string == 'All':
        clean()
        tb.field_names = ["Name","Specialties","Faculty","Phone","Semester","Hours","Report","Total credits"]
        search_number = "select structure from department inner join discipline on department.title = discipline.title_d order by hours DESC;"
        cur.execute(search_number)
        Credit = list()
        num = 0
        for x in cur.fetchall():
            for y in range(len(list(x))):
                for k in x[y]:
                    if k != ',':
                        print(k)
                        num = num + int(k)
            Credit.append(num)
            num = 0
        search1 = "select title,specialties,faculty,phone_number,semester,hours,reporting from department inner join discipline on department.title = discipline.title_d order by hours DESC;"
        cur.execute(search1)
        for i in cur.fetchall():
            lists.append(list(i))

        vart = 0
        for z in range(len(lists)):
            lists[z].append(Credit[vart])
            vart += 1
        print(lists)
        for j in range(len(lists)):
            tb.add_row(lists[j])
        print(Credit)
        return tb

    elif int(var_list[0]) == 0 and var_string != 'All':
        clean()
        tb.field_names = ["Name", "Specialties", "Faculty", "Phone", "Semester", "Hours", "Name_d",
                          "Report"]
        search6 = "select * from department inner join discipline on department.title = discipline.title_d where specialties = \'" + var_string + "\';"
        cur.execute(search6)
        for i in cur.fetchall():
            lists.append(list(i))
        for j in range(len(lists)):
            tb.add_row(lists[j])
        return tb

    elif var_string == 'All' and int(var_list[0]) != 0 and len(var_list) >= 1:
        clean()
        tb.field_names = ["Name", "Specialties", "Faculty", "Phone", "Name_d", "Semester", "Hours", "Structure",
                          "Report"]

        searchx = "select * from department inner join discipline on department.title = discipline.title_d where "
        connect = var_list
        str1 = list(get_values())
        p = 0
        for i in range(len(var_list)):
            searchx = searchx + "title = \'" + str1[p] + "\'"

            if (i+1) < (len(var_list)):
                searchx = searchx + " or "
                p += 1

        searchx = searchx + ";"
        print(searchx)
        cur.execute(searchx)
        for i in cur.fetchall():
            lists.append(list(i))
        for j in range(len(lists)):
            tb.add_row(lists[j])
        return tb

    elif len(var_list) == 1:
        clean()
        connect = var_list
        str1 = get_values()

        tb.field_names = ["Name", "Specialties", "Faculty", "Phone", "Name_d", "Semester", "Hours", "Structure",
                          "Report"]
        if var_string == 'All' and len(var_list) >= 1:
            search2 = "select * from department inner join discipline on department.title = discipline.title_d where" + " title = \'" + str1 + "\';"
        elif var_string != 'All' and len(var_list) >= 1:
            search2 = "select * from department inner join discipline on department.title = discipline.title_d where specialties = \'" + var_string + "\' or "
            p = 0
            for i in range(len(var_list)):
                search2 = search2 + "title = \'" + str1[p] + "\'"

                if (i + 1) < (len(var_list)):
                    search2 = search2 + " and "
                    p += 1
            search2 = search2 + ";"
            print(search2)
        cur.execute(search2)
        for i in cur.fetchall():
            lists.append(list(i))
        for j in range(len(lists)):
            tb.add_row(lists[j])
        return tb

    elif len(var_list) > 1 and int(var_list[0]) != 0 and var_string == '':
        clean()
        connect = var_list
        str1 = list(get_values())
        if len(str) == 2:
            tb.field_names = ["Name", "Specialties", "Faculty", "Phone", "Name_d", "Semester", "Hours", "Structure",
                          "Report"]
            search4 = "select * from department inner join discipline on department.title = discipline.title_d where" + " title = \'" + str1[0] + "\' or title = \'" + str1[1] + "\' and specialties = \'" + var_string + "\';"
            cur.execute(search4)
            for i in cur.fetchall():
                lists.append(list(i))
            for j in range(len(lists)):
                tb.add_row(lists[j])
            return tb
        else:
            tb.field_names = ["Name", "Specialties", "Faculty", "Phone", "Name_d", "Semester", "Hours", "Structure",
                              "Report"]
            search5 = "select * from department inner join discipline on department.title = discipline.title_d where" + " title = \'" + str1[0] + "\' or title = \'" + str1[1] + "\' or title = \'" + str1[2] + "\' and specialties = \'" + var_string + "\';"
            cur.execute(search5)
            for i in cur.fetchall():
                lists.append(list(i))
            for j in range(len(lists)):
                tb.add_row(lists[j])
            return tb
    else:
        return "None"

def get_values(n = 0):
    global list_de,connect
    if len(connect) == 0:
        for i in range(len(list_de)):
            if i == n:
                return list_de[n]
    else:
        result = []
        x = 0
        for j in range(len(list_de)):
            print(j)
            if j == int(connect[x]):
                print(connect[x],j)
                if (x+1) < len(connect):
                    x += 1
                result.append(list_de[j])
        print(result)
        return result

def clean():
    global connect
    if len(connect) != 0:
        connect.clear()


def print_fun2_single_1(var):
    tb_person = pp.PrettyTable()
    list_person = list()
    search = "select specialty,name,form_study from specialty_s where name = \'" + var + "\';"
    cur.execute(search)
    tb_person.field_names = ['Specialty','Name','Form_study']
    for i in cur.fetchall():
        list_person.append(list(i))
    for j in range(len(list_person)):
        tb_person.add_row(list_person[j])
    return tb_person

def print_fun2_single_2(var_s = ''):
    tb_study = pp.PrettyTable()
    list_study = list()
    if (var_s == 'All ') is True:
        tb_study.field_names = ['Form_study']
        query_all_s = "select distinct form_study from specialty_s;"
        print(query_all_s)
        cur.execute(query_all_s)
        for i in cur.fetchall():
            print(i)
            list_study.append(list(i))
        tb_study.add_rows(list_study)
        return tb_study
    else:
        tb_study.field_names = ['Specialty', 'Name', 'Form_study']
        search = "select specialty,name,form_study from specialty_s where form_study = \'" + var_s + "\';"
        cur.execute(search)
        for i in cur.fetchall():
            list_study.append(list(i))
        for j in range(len(list_study)):
            tb_study.add_row(list_study[j])
        return tb_study

def print_fun2_variety_1(var_study,var_name,var_list,var_string):
    tb1 = pp.PrettyTable()
    list1 = list()
    search1 = ("select title,specialty,name,form_study,faculty " +
               "from department,specialty_s where department.specialties = specialty_s.specialty and name = \'" + var_name + "\'")
    if var_string == '' and len(var_list) == 0 and var_name != '' and var_study != '':
        if var_study != 'All ':
            search1 = search1 + " and form_study = \'" + var_study + "\'"
        search1 = search1 + ";"
        print(search1)
        cur.execute(search1)
        tb1.field_names = ['Title', 'Specialty', 'Name','Form_study','Faculty']
        for i in cur.fetchall():
            list1.append(list(i))
        for j in range(len(list1)):
            tb1.add_row(list1[j])
        return tb1
    elif var_string != '' and len(var_list) == 0 and var_name != '' and var_study != '':
        search2 = ("select specialty,name,form_study,faculty from department,specialty_s "
                   "where department.specialties = specialty_s.specialty "
                   "where form_study = \'" + var_study + "\' and name = \'" + var_name + "\' "
                                                                                         "and specialty = \'" + var_string + "\';")
        cur.execute(search2)
        tb1.field_names = ['Specialty', 'Name', 'Form_study', 'faculty']
        for i in cur.fetchall():
            list1.append(list(i))
        for j in range(len(list1)):
            tb1.add_row(list1[j])
        return tb1
    else:
        return "None"
    search3 = ""
    search4 = ""
    search5 = ""
    search6 = ""

def print_fun2(var_list = list(),var_string = '',var_name = '',var_study = ''):
    tb = pp.PrettyTable()
    lists = list()
    print(var_list,var_string,var_name,var_study)
    search = "select * from department,discipline,specialty_s where department.title = discipline.title_d and department.specialties = specialty_s.specialty"
    if len(var_list) == 0 and var_name != '' and var_study == '' and var_string == '':
        tb = print_fun2_single_1(var_name)
        return tb
    elif len(var_list) == 0 and var_name == '' and var_study != '' and var_string == '':
        tb = print_fun2_single_2(var_study)
        return tb

    if len(var_list) >= 1 and var_name != '' and var_study == '' and var_string == '' and int(var_list[0]) == 0:
        clean()

        tb.field_names = ['title', 'specialties', 'faculty', 'phone_number', 'title_d', 'semester', 'hours', 'structure', 'reporting', 'key', 'specialty', 'name', 'form_study']
        print(tb.field_names)
        search = search + " and name = \'" + str(var_name) + "\';"
        print(search)
        cur.execute(search)
        for i in cur.fetchall():
            lists.append(list(i))
        for j in range(len(lists)):
            print(lists[j])
            tb.add_row(lists[j])

        return tb
    elif (len(var_list) > 0 and var_string != '')  or (var_name == '' and var_study == ''):
        tb = print_fun1(var_list,var_string)
        return tb
    elif len(var_list) > 0 or var_string != ''  or var_name != '' or var_study != '':
        tb = print_fun2_variety_1(var_study,var_name,var_list,var_string)
        return tb
    else:
        return "None"

def operation_update(var_list = list(),var_string = '',var_name = ''):
    global connect
    clean()
    connect = var_list
    re_tb = pp.PrettyTable()
    list_re = list()
    str1 = list(get_values())
    if len(var_list) == 0 or var_string == '' or var_name == '' or var_string == 'All':
        return "Your input information is incomplete, please enter your name, change the major and the corresponding college of the major"

    know1 = "select * from specialty_s where name = \'" + var_name + "\';"
    cur.execute(know1)
    if len(cur.fetchall()) == 0:
            return "The entered name does not exist"

    know2 = "select * from department where specialties = \'" + var_string + "\' and title = \'" + str1[0] + "\';"
    cur.execute(know2)
    if len(cur.fetchall()) == 0:
            return "Major and college do not match, please re-enter"


    update = "update `specialty_s` set `specialty` = \'" + var_string + "\' where `name` = \'" + var_name + "\';"
    cur.execute(update)
    conn.commit()
    mess.user_data(1)
    re = "select specialty,name,form_study from specialty_s where name = \'" + var_name + "\';"
    cur.execute(re)
    re_tb.field_names = ['Specialty','Name','Form_study']
    for i in cur.fetchall():
        list_re.append(list(i))
    for j in range(len(list_re)):
        print(list_re[j])
        re_tb.add_row(list_re[j])
    return re_tb


def add_data(var_list = list(),var_new = '',var_f = '',var_p = ''):
    global connect
    clean()
    connect = var_list
    add_tb = pp.PrettyTable()
    list_add = list()
    str1 = list(get_values())
    if len(var_list) == 0 or int(var_list[0]) == 0 or var_new == '' or var_p == '' or var_f == '':
        return "Your information is incomplete or errors, please re-enter it"

    if not re.search("^[+].{0,10}$",var_p):
        return "The phone format is incorrect"

    add = "insert into `department`(title,specialties,faculty,phone_number) values (\'" + str1[0] + "\',\'" + var_new + "\',\'" + var_f + "\',\'" + var_p + "\');"
    print(add)
    cur.execute(add)
    conn.commit()
    mess.user_data(3)
    show = "select * from department where specialties = \'" + var_new + "\';"
    cur.execute(show)
    add_tb.field_names = ['title','specialties','faculty','phone_number']
    for i in cur.fetchall():
        list_add.append(list(i))
    for j in range(len(list_add)):
        print(list_add[j])
        add_tb.add_row(list_add[j])
    return add_tb

def del_data(var_string = ''):
    if var_string == '':
        return "No information!"
    search = "select * from department where specialties = \'" + var_string + "\';"
    cur.execute(search)
    if len(cur.fetchall()) == 0:
        return "Information does not exist"
    del_infor = "delete from department where specialties = \'" + var_string + "\';"
    cur.execute(del_infor)
    conn.commit()
    connect_del = "update `specialty_s` set `specialty` = 'None' where specialty = \'" + var_string + "\';"
    cur.execute(connect_del)
    conn.commit()
    mess.user_data(4)


'''
        search_field1 = "show columns from department;"
        cur.execute(search_field1)
        for n in cur.fetchall():
            print(n[0])
            tb.field_names.append(str(n[0]))

        search_field2 = "show columns from discipline;"
        cur.execute(search_field2)
        for n in cur.fetchall():
            tb.field_names.append(str(n[0]))

        search_field3 = "show columns from specialty_s;"
        cur.execute(search_field3)
        for n in cur.fetchall():
            tb.field_names.append(str(n[0]))
'''