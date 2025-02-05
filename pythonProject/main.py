#hospital
#final
import mysql.connector
from mysql.connector import Error
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import csv

root = Tk()
root.title("Hospital Management System")
root.configure(width=1500, height=600, bg="cyan")

def Add_Items():
    global id1, pname, age, deptchoosen, value, doc
    my_w = tk.Tk()
    # my_w.geometry("800x850")
    my_w.configure(width=800, height=600, bg="green")
    Label(my_w, text="REGISTRATION", font=("Times", "24", "bold")).grid(row=0, columnspan=7, pady=10)

    Label(my_w, text='PATIENT ID', font=("Times", "14")).grid(row=1, column=0, pady=5)
    id1 = Entry(my_w, width=50)
    id1.grid(row=1, column=1)

    Label(my_w, text='NAME', font=("Times", "14")).grid(row=2, column=0, pady=5)
    pname = Entry(my_w, width=50)
    pname.grid(row=2, column=1)

    Label(my_w, text='AGE', font=("Times", "14")).grid(row=3, column=0, pady=5)
    age = Entry(my_w, width=50)
    age.grid(row=3, column=1)

    Label(my_w, text="Department :", font=("Times New Roman", 14)).grid(column=0, row=5, padx=10, pady=25)

    # Combobox creation
    n = tk.StringVar()
    deptchoosen = ttk.Combobox(my_w, width=27, textvariable=n)

    # Adding combobox drop down list
    deptchoosen['values'] = ('ENT',
                             'Gynecologist',
                             'Pulmonary',
                             'skin',
                             'Physcian',
                             'Emergency',
                             'ICU ',
                             )

    deptchoosen.grid(column=1, row=5)
    deptchoosen.current()
    deptchoosen.bind("<<ComboboxSelected>>", selected)
    # print("doctor",dr)
    Label(my_w, text='doctor', font=("Times", "14")).grid(row=7, column=0, pady=5)
    # Label(my_w, font=("Times", "14"), width=30, height=1 ).grid(row=7, column=1, pady=5)
    doc = Entry(my_w, width=50)
    doc.grid(row=7, column=1)

    # button
    clr = Button(my_w, text="Clear", relief=SOLID, font=("Times", "14", "bold"), command=Clear_Item)
    reg = Button(my_w, text="Register", relief=SOLID, font=("Times", "14", "bold"), command=submit)
    ext = Button(my_w, text="Exit", relief=SOLID, font=("Times", "14", "bold"), command=my_w.destroy)
    fdoc = Button(my_w, text="Find Doctor", relief=SOLID, font=("Times", "14", "bold"), command=find)

    clr.grid(row=10, column=0)
    reg.grid(row=10, column=1)
    ext.grid(row=10, column=2)
    fdoc.grid(row=10, column=3)
    my_w.mainloop()


def selected(event):
    global value
    value = deptchoosen.get()
    print(value)


def find():
    global deptchoosen, EN1, dr
    EN1 = deptchoosen.get()
    print("find", EN1)
    connection = mysql.connector.connect(host='localhost', database='ujjala', user="root", password="vedu1901")
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
    print("You're connected to database: ", record)
    q1 = "SELECT * FROM doctor WHERE department=" + "\"" + deptchoosen.get() + "\";"
    print(q1)
    cursor.execute(q1)
    # fetch result
    record = cursor.fetchall()
    for row in record:
        if row[0] == EN1:
            dr = row[1]
            print("Department = ", row[0])
            print("Name = ", row[1])
            print(dr)


def submit():
    try:
        connection = mysql.connector.connect(host='localhost', database='ujjala', user="root", password="vedu1901")
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
        print("You're connected to database: ", record)
        EN1 = id1.get()
        EN2 = pname.get()
        EN3 = age.get()
        EN4 = doc.get()
        record = (EN1, EN2, EN3, value, EN4)
        q1 = """INSERT INTO patient(id,name,age,department,doctor) values(%s, %s, %s, %s, %s) """
        cursor.execute(q1, record)
        connection.commit()
        # print(record)
        print("Record inserted successfully into the table")
        messagebox.showinfo("ADD ITEM", "ITEM ADDED SUCCESSFULLY....!!!!!")
    except Error as e:
        print("Error while connecting to MySQL", e)


def Delete_Items():
    EN1 = Entry_1.get()

    try:

        connection = mysql.connector.connect(host='localhost', database='book', user="root", password="vedu1901")
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
        print("You're connected to database: ", record)

        sql_delete = "DELETE FROM booklist WHERE name = %s"
        print(sql_delete)
        sql_data = (EN1,)
        cursor.execute(sql_delete, sql_data)

        connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
    messagebox.showinfo("DELETE ITEM", "ITEM DELETED SUCCESSFULLY....!!!!!")


def output():
    global name, e1, e2, e3, e4, e5
    my_w1 = tk.Tk()
    my_w1.configure(width=800, height=600, bg="green")
    Label(my_w1, text="text1", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)

    Label(my_w1, text='Name', font=("Times", "14")).grid(row=1, column=0, pady=5)
    name = Entry(my_w1, width=50)
    name.grid(row=1, column=1)

    Label(my_w1, text='a1', font=("Times", "14")).grid(row=2, column=0, pady=5)
    e1 = Entry(my_w1, width=50)
    e1.grid(row=2, column=1)

    Label(my_w1, text='a2', font=("Times", "14")).grid(row=3, column=0, pady=5)
    e2 = Entry(my_w1, width=50)
    e2.grid(row=3, column=1)

    Label(my_w1, text='a3', font=("Times", "14")).grid(row=4, column=0, pady=5)
    e3 = Entry(my_w1, width=50)
    e3.grid(row=4, column=1)

    my_w1.mainloop()


def opendata():
    my_w2 = tk.Tk()
    # my_w.geometry("800x850")
    my_w2.configure(width=800, height=600, bg="green")
    Label(my_w2, text="REGISTRATION", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)

    # button

    reg = Button(my_w2, text="Register", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),
                 command=Add_Items)
    reg1 = Button(my_w2, text="Registered", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=list1)
    ext = Button(my_w2, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),
                 command=my_w2.destroy)

    reg.grid(row=1, column=0, pady=20)
    reg1.grid(row=1, column=1, pady=20)
    ext.grid(row=1, column=2, pady=20)

    my_w2.mainloop()


def login():
    global un, pwd
    my = tk.Tk()
    my.configure(width=700, height=600, bg="green")
    l1 = Label(my, text="Enter user Id ", fg="black", bg="green", font=("Times new roman", 30, 'bold'))
    l1.grid(row=1, column=0)
    un = Entry(my, width=50, bd=10, fg="blue", font=("Times new roman", 15, 'bold'))
    un.grid(row=1, column=1)
    id1 = un.get()

    l2 = Label(my, text="Enter password ", fg="black", bd=10, bg="green", font=("Times new roman", 30, 'bold'))
    l2.grid(row=2, column=0)
    pwd = Entry(my, width=50, bd=10, fg="blue", font=("Times new roman", 15, 'bold'))
    pwd.grid(row=2, column=1, padx=10, pady=10)
    pass1 = pwd.get()

    if (id1 == "vedu" and pass1 == "vedu1901"):
        Add_Items()

    btn = Button(my, text="open", padx=20, pady=10, bd=10, command=opendata)
    btn.grid(row=4, column=0, padx=10, pady=10)
    # ext = Button(my, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=my.destroy)
    # ext.grid(row=4, column=1, pady=20)
    my.mainloop()


def list1():
    my_w = tk.Tk()
    my_w.geometry("400x250")

    connection = mysql.connector.connect(host='localhost', database='ujjala', user="root", password="vedu1901")
    my_conn = connection.cursor()
    my_conn.execute("SELECT * FROM patient limit 0,100")
    myresult = my_conn.fetchall()
    i = 0
    for student in myresult:
        for j in range(len(student)):
            print(j, student[j])
            e = Entry(my_w, width=10, fg='blue')
            e.grid(row=i, column=j)
            # e.insert(END, student[j])
            e.insert(0, student[j])
        i = i + 1
    bottom = Button(my_w, text="Close", command=my_w.destroy)
    bottom.grid(row=10, column=4, padx=10, pady=10)

    my_w.mainloop()


def Exit():
    Exit = messagebox.askyesno("Exit the System", "Do you want to Exit(y/n)?")
    if Exit > 0:
        root.destroy()
        return


l = Label(root, text="HOSPITAL MANAGEMENT SYSTEM", fg="black", bg="green", font=("Times new roman", 30, 'bold'))
l.grid(row=2, columnspan=8)
btn_2 = Button(root, text="Login", bd=10, bg="#49D810", fg="black", width=20, font=("Times new roman", 20),
               command=login)
btn_2.grid(row=8, column=0, padx=10, pady=10)

image = Image.open('hos.jpg')
pic1 = ImageTk.PhotoImage(image)
labell = Label(root, image=pic1)
labell.grid(row=6, column=3)


def Clear_Item():
    print('hello')


root.mainloop()

import os

current_working_directory = os.getcwd()

# print output to the console
print('it is:', current_working_directory)