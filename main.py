from tkinter import *
from tkinter import messagebox
def pr():
    messagebox.showinfo('ответ' ,eval(y.get()))




root = Tk()
root.title('умножение')
root.geometry('300x500')
y = Entry(root , width=25, bg='black' , fg='white').pack()
Button(root , text='вывод' , command=pr).pack()
root.mainloop()

