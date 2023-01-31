from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Login form")
window.geometry('350x200')

lbl1 = Label(window, text="Enter Username")
lbl2 = Label(window, text="Enter Password")
lbl1.grid(column=0, row=0)
lbl2.grid(column=0, row=1)

txt1 = Entry(window, width=10)
txt2 = Entry(window, width=10)
txt1.grid(column=1,row=0)
txt2.grid(column=1,row=1)

def Login():
    user = txt1.get()
    pass1 = txt2.get()
    if(user==pass1):
        messagebox.showinfo('Message title', 'Login successfully')
    else:
        messagebox.showinfo('Message title', 'Login Fail')

btn = Button(window, text="Login", command=Login)
btn.grid(column=2, row=0)


window.mainloop()
