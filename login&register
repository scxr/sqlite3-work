"""
Charlie Wilson
10/06/2019
Aim: Create a working login/registration program in the form of a GUI with sqlite3 and tkinter
"""


import tkinter as tk
import sqlite3
from tkinter import messagebox
import sys
import string
not_allowed = ';#-' # Things that will flag an input as an SQL injection if they are in the input
broken = False  # If detected sql injection
#-------------------------------------------------------------------------------
# Main form
class main:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.crtable = tk.Button(self.frame, text = 'Create table', width = 50, command = self.create_table) # Button to create the table
        self.crtable.pack()
        self.frame.pack()

        self.login = tk.Button(self.frame, text = 'Login', width = 50, command = self.new_window_login) # Button to show the login form
        self.login.pack()
        self.frame.pack()
        self.register = tk.Button(self.frame, text = 'Register', width = 50, command = self.new_window_reg) # Button to show the register form
        self.register.pack()
        self.frame.pack()
    def create_table(self): # The create the table function
        conn = sqlite3.connect('user.db') #Connect to the table
        c = conn.cursor()
        c.execute('''CREATE TABLE login (id INTEGER PRIMARY KEY, uname TEXT NOT NULL, pword TEXT NOT NULL);''') # SQL statement to execute
        conn.commit() # Execute the statement
        conn.close() # Close the connection
    def new_window_login(self): # Show the login form function
        self.newWindow = tk.Toplevel(self.master)
        self.app = login(self.newWindow) # Show the login class form (coded below)

    def new_window_reg(self): # Show the register form function
        self.newWindow = tk.Toplevel(self.master)
        self.app = reg(self.newWindow) # Show the register class function (coded below)
#-------------------------------------------------------------------------------
# Login form
class login:
    def __init__(self,master):
        self.attempts=0
        entryText = tk.StringVar() # Varibales for the text the user is going to input
        entryTextPass = tk.StringVar() # Variable for the pass the user is going to input
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame,text ='Login', width = 50, command = self.login) # The Button to login
        self.e1 = tk.Entry(self.master, textvariable=entryText) # Create the text box
        entryText.set("Username")
        self.e2 = tk.Entry(self.master, textvariable = entryTextPass) # Create the text box for pass
        entryTextPass.set("Password")
        self.e1.pack()
        self.e2.pack()
        self.button1.pack()
        self.frame.pack()
    def hello(self):
        print('hello')
    def login(self): # Login function
        attempt = True

        while attempt == True and self.attempts < 4:
            uname = self.e1.get() # Get what the user has put into the text box
            pword = self.e2.get() # Get what the user has put into the text box

            conn = sqlite3.connect('user.db')  # connect to the database
            c = conn.cursor()
            c.execute('''SELECT pword FROM login WHERE uname = ?''',(uname,)) # Select the password for the username entered
            real_pword = c.fetchall() # The expected pass
            conn.commit()
            conn.close()
            try:
                if pword == real_pword[0][0]: # If the password is correct
                    print('Welcome back ' + uname) # allow the user in
                    attempt = False # The user doesn't need to retry logging in
                else:
                    print('Incorrect password')
                    again = input('Would you like to retry? (y)/(n)') # Ask if the user would like to re-input their password
                    if again == 'y':
                        pass
                    else:
                        attempt = False # Break out of the loop
            except IndexError: # If the user isn't found
                print('user not found')
                break
#-------------------------------------------------------------------------------
#Register form
class reg:
    def __init__(self,master):
        entryText = tk.StringVar() # Define the entry as string variable
        entryTextPass = tk.StringVar() # Define the entry pass as string variable
        self.master = master
        self.frame = tk.Frame(self.master)
        self.reg_button = tk.Button(self.frame, text='Register', width = 50, command = self.reg) # Register button
        self.reg_button.pack()
        self.e1 = tk.Entry(self.master, textvariable=entryText) # Text box for Username
        entryText.set("Username")
        self.e2 = tk.Entry(self.master, textvariable = entryTextPass) # Text box for password
        entryTextPass.set("Password")
        self.e1.pack()
        self.e2.pack()
        self.frame.pack()
    def reg(self): # Register form
        self.attempts+=1
        special_chars = string.digits + string.punctuation
        if self.e1.get() in special_chars:
            messagebox.showerror("Invalid","Please do not put special characters or numbers in your username")
            sys.exit()
        def check_if_exists(uname):
            conn=sqlite3.connect("user.db")
            c=conn.cursor()
            c.execute('''SELECT uname FROM login''')
            chck = c.fetchall().split()
            conn.commit()
            conn.close()
            for i in chck:
                if i == uname:
                    messagebox.showerror("invalid","This user is already registered")
                    sys.exit()
                else:
                    next
        broken = False
        uname = self.e1.get() # Get the Username
        pword = self.e2.get() # Get the password
        if len(uname.split()) != 2:
            messagebox.showerror("First & Last name","You need to put both your first and last name in")
            sys.exit()
        if uname.remove(" ")=="": # removes all spaces to see if the user has just spammed spacebars
            messagebox.showerror("Error in username","Enter a username next time please")
            
        if uname.lower() == "admin":
            messagebox.showerror("Invalid","A username admin cannot be submitted")
            
        if len(pword) > 6:
            pass
        else:
            messagebox.showerror("Insecure password","Your password must be at least 6 characters long")
            
        check_if_exists(uname)
        tot = uname + pword
        for i in tot:
            if i in not_allowed:
                messagebox.showerror("Error", "SQL injection detected") # If any character inputted is in the not_allowed variable it will be flagged
                sys.exit() # close the program
            if uname == '' or pword == '': # if the fields are left empty
                print('you failed to enter text into one of the text boxes...... exitting')
                break
        tot = str(self.e1.get()) + str(self.e2.get())
        print(tot)
        for i in tot:
            if i in not_allowed: # Prevents SQL injection
                broken = True
        if broken == False: # If its not a sql injection attempt
            print('not broken')
            conn = sqlite3.connect('user.db') # Connect to the database
            c = conn.cursor()
            params = (uname,pword) # Things to insert
            c.execute('INSERT INTO login VALUES (null,?,?)',params) # SQL statement to Execute
            conn.commit() # Execute the sql statement
            conn.close() # Close the connection
        else:
            messagebox.showerror("Error", "SQL injection detected") # If an sql injection has been detected

if __name__ == '__main__': # Run it
    root = tk.Tk()
    app = main(root)
    root.mainloop() # Run function

"""
Outcome: Working GUI program using sqlite3 and tkinter
Aim: Met
"""
