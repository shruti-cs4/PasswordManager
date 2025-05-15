import tkinter as tk
from tkinter import messagebox


def add():
    username = entryName.get()
    password = entryPassword.get()
    if username and password:
        f = open("passwords.txt", 'a')
        f.write(f"{username} {password}\n")
        messagebox.showinfo("Success", "Password added !!")
        f.close()
    else:
        messagebox.showerror("Error", "Please enter both the fields")

def get():
    username = entryName.get()
    passwords = {}
    try:
        f = open("passwords.txt", 'r')
        data = f.readlines()
        for k in data:
            i = k.split()
            if len(i) == 2:
                passwords[i[0]] = i[1]
    except EOFError:
        print("ERROR !!")
    finally:
        f.close()
    if passwords:
        for i in passwords:
            if i == username:
                mess = f"Password for {username} is {passwords[i]}\n"
                break
        else:
            mess = "No Such Username Exists !!"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "EMPTY LIST!!")

def getlist():
    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            data = f.readlines()
            for k in data:
                i = k.split()
                if len(i) == 2:
                    passwords[i[0]] = i[1]
    except EOFError:
        print("No passwords found!!")
    if passwords:
        mess = "List of passwords:\n"
        for name, password in passwords.items():
            mess += f"Password for {name} is {password}\n"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "Empty List !!")

def delete():
    username = entryName.get()
    temp_passwords = []
    try:
        with open("passwords.txt", 'r') as f: 
            data = f.readlines()
            for k in data:
                i = k.split()
                if len(i) == 2 and i[0] != username:
                    temp_passwords.append(f"{i[0]} {i[1]}")
        with open("passwords.txt", 'w') as f:
                for i in temp_passwords:
                    f.write(i+"\n")
        if any(username == k.split()[0] for k in data if len(k.split()) == 2):
            messagebox.showinfo("Success", f"User {username} deleted successfully!")
        else: 
            messagebox.showinfo("Info", f"No user named {username} was found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting user {username}: {e}")


app = tk.Tk()
app.resizable(0,0)
app.geometry("600x300")
app.configure(bg='#aed6f1')
app.title("Password Management System")

center_frame = tk.Frame(app) 
center_frame.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

entry = tk.Label(app, bg='#aed6f1', fg='#FFFFFF', text='Welcome to Password Management System!', font=('Footlight MT Light',16,'bold'))
entry.place(x=10, y=30, width=600, height=40)

labelName = tk.Label(center_frame, text="USERNAME:")
labelName.grid(row=0, column=0, padx=15, pady=15)
entryName = tk.Entry(center_frame)
entryName.grid(row=0, column=1, padx=15, pady=15)

labelPassword = tk.Label(center_frame, text="PASSWORD:")
labelPassword.grid(row=1, column=0, padx=10, pady=5)
entryPassword = tk.Entry(center_frame)
entryPassword.grid(row=1, column=1, padx=10, pady=5)

buttonAdd = tk.Button(center_frame, text="Add", command=add)
buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

buttonGet = tk.Button(center_frame, text="Get", command=get)
buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")
buttonList = tk.Button(center_frame, text="List", command=getlist)
buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")

buttonDelete = tk.Button(center_frame, text="Delete", command=delete)
buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")
    
app.mainloop()