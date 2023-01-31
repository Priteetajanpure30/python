from tkinter import *
window = Tk()
window.title("calculator")
window.geometry('350x200')

lbl1 = Label(window, text="Enter 1st no.")
lbl2 = Label(window, text="Enter 2st no.")
lbl3 = Label(window, text="result")
lbl1.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
lbl3.grid(column=0, row=2)

txt1 = Entry(window,width=10)
txt2 = Entry(window,width=10)
txt3 = Entry(window,width=10)
txt1.grid(column=1,row=0)
txt2.grid(column=1,row=1)
txt3.grid(column=1,row=2)


def sub():
    txt3.delete(0, 10)
    a = int(txt1.get())
    b = int(txt2.get())
    txt3.insert(0, (a - b))


btn = Button(window, text="sub", command=sub)
btn.grid(column=2, row=0)


window.mainloop()
