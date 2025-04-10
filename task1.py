
import tkinter as tk
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("tk")
window.geometry("400x30")

entry1 = tk.Entry(window,text="hello", width=15)
entry2 = tk.Entry(window,text="world", width=15)
entry3 = tk.Entry(window,text="hello world", width=30)

lable1 = tk.Label(window, text="X")
lable2 = tk.Label(window, text="=", relief = "solid")

entry1.pack(side="left") 
lable1.pack(side="left")
entry2.pack(side="left")
lable2.pack(side="left")
entry3.pack(side="left")

nF = Frame()
nF.pack()

window.mainloop()


