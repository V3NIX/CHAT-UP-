import sqlite3
from tkinter import *
from tkinter import messagebox
import time
import subprocess


# Connect to the database
conn = sqlite3.connect("user.db")
cursor = conn.cursor()

# Create the users table
cursor.execute("CREATE TABLE IF NOT EXISTS reg (username TEXT, password TEXT)")

# Function to check login credentials
def check_credentials():
    username = entry_1.get()
    password = entry_3.get()
    cursor.execute("SELECT * FROM reg WHERE name=? AND password=?", (username, password))
    if cursor.fetchone() is not None:
        messagebox.showinfo("Welcome!", "Welcome!")
        time.sleep(2)
        root.destroy()
        subprocess.call(['python', 'client.py'])
    else:
        # Login failed
        messagebox.showerror("Error", "Invalid username or password")

# Tkinter GUI
root = Tk()
root.geometry('500x500')
bg = PhotoImage(file='source/bg.png')
root.title("LogIn Form")
root.iconbitmap("source/icone.ico")

label2 = Label(root, image=bg)
label2.place(x=0, y=0)

label_0 = Label(root, text="Login Form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)

label_3 = Label(root, text="Password", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
entry_3 = Entry(root)
entry_3.config(show="*")
entry_3.place(x=240, y=230)


Button(root, text='login', width=20, bg='green', fg='white', command=check_credentials).place(x=180, y=380)
root.mainloop()
