import tkinter
import sqlite3
from tkinter import messagebox

db = sqlite3.connect('login.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')

def login():
  db = sqlite3.connect('login.sqlite')
  db.execute("INSERT INTO login(username, password) VALUES('admin', 'admin')")
  cursor = db.cursor()
  cursor.execute("SELECT * FROM login WHERE username = ? AND password = ?", (userinput.get(), pass_input.get()))
  
  row = cursor.fetchone()
  if row:
    messagebox.showinfo('info', 'sucess')
  else:
    messagebox.showinfo('info', 'fail')
  cursor.connection.commit()
  db.close()

main_window = tkinter.Tk()
main_window.title('Login')
main_window.geometry('400x300')
padd = 20
main_window['padx'] = padd
user_input = tkinter.StringVar()
pass_input = tkinter.StringVar()
info_label = tkinter.Label(main_window, text = 'Login App')
info_label.grid(row = 0, column = 0, pady = 20)

info_user = tkinter.Label(main_window, text = 'Username')
info_user.grid(row = 1, column = 0)
userinput = tkinter.Entry(main_window, text = user_input)
userinput.grid(row = 1, column = 0)

info_pass = tkinter.Label(main_window, text = 'password')
info_pass.grid(row = 2, column = 0, pady = 20)
passinput = tkinter.Entry(main_window, text = pass_input, show = '*')
passinput.grid(row = 2, column = 0)

login_btn = tkinter.Button(main_window, text = 'Login', command = login)
login_btn.grid(row = 3, column = 0)

main_window.mainloop()