import tkinter as tk
import sqlite3
from tkinter import messagebox
import sys
not_allowed = ';#-'
broken = False
class main:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.crtable = tk.Button(self.frame, text = 'Create table', width = 50, command = self.create_table)
        self.crtable.pack()
        self.frame.pack()
        self.login = tk.Button(self.frame, text = 'Login', width = 50, command = self.new_window_login)
        self.login.pack()
        self.frame.pack()
        self.register = tk.Button(self.frame, text = 'Register', width = 50, command = self.new_window_reg)
        self.register.pack()
        self.frame.pack()
    def create_table(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE login (id INTEGER PRIMARY KEY, uname TEXT NOT NULL, pword TEXT NOT NULL);''')
        conn.commit()
        conn.close()
    def new_window_login(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = login(self.newWindow)
    
    def new_window_reg(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = reg(self.newWindow)

class login:
    def __init__(self,master):
        entryText = tk.StringVar()
        entryTextPass = tk.StringVar()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame,text ='Login', width = 50, command = self.login)
        self.e1 = tk.Entry(self.master, textvariable=entryText)
        entryText.set("Username")
        self.e2 = tk.Entry(self.master, textvariable = entryTextPass)
        entryTextPass.set("Password")
        self.e1.pack()
        self.e2.pack()
        self.button1.pack()
        self.frame.pack()
    def hello(self):
        print('hello')
    def login(self):
        attempt = True
        while attempt == True:
            uname = self.e1.get()
            pword = self.e2.get()
            tot = uname + pword
            for i in tot:
                if i in not_allowed:
                    messagebox.showerror("Error", "SQL injection detected")
                    sys.exit()
            if uname == '' or pword == '':
                print('you failed to enter text into one of the text boxes...... exitting')
                break
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute('''SELECT pword FROM login WHERE uname = ?''',(uname,))
            real_pword = c.fetchall()
            conn.commit()
            conn.close()
            try:
                if pword == real_pword[0][0]:
                    print('Welcome back ' + uname)
                    attempt = False
                else:
                    print('Incorrect password')
                    again = input('Would you like to retry? (y)/(n)')
                    if again == 'y':
                        pass
                    else:
                        attempt = False
            except IndexError:
                print('user not found')
                break
class reg:
    def __init__(self,master):
        entryText = tk.StringVar()
        entryTextPass = tk.StringVar()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.reg_button = tk.Button(self.frame, text='Register', width = 50, command = self.reg)
        self.reg_button.pack()
        self.e1 = tk.Entry(self.master, textvariable=entryText)
        entryText.set("Username")
        self.e2 = tk.Entry(self.master, textvariable = entryTextPass)
        entryTextPass.set("Password")
        self.e1.pack()
        self.e2.pack()
        self.frame.pack()
    def reg(self):
        broken = False
        uname = self.e1.get()
        pword = self.e2.get()
        tot = str(self.e1.get()) + str(self.e2.get())
        print(tot)
        for i in tot:
            if i in not_allowed:
                broken = True
        if broken == False:
            print('not broken')
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            params = (uname,pword)
            c.execute('INSERT INTO login VALUES (null,?,?)',params)
            conn.commit()
            conn.close()
        else:
            messagebox.showerror("Error", "SQL injection detected")

if __name__ == '__main__':
    root = tk.Tk()
    app = main(root)
    root.mainloop
