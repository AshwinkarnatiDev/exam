from tkinter import *
from tkinter import messagebox

root=Tk()

Label(text="name").grid(row=1, column=0,padx=5,pady=5)
Entry(root).grid(row=1, column=1,padx=5,pady=5)
root.mainloop()