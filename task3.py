import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.resizable(False,False)

lable1 = tk.Label(window, text="Pochacco!")

dog = PhotoImage(file="dog.png")
lable2 = tk.Label(window, image=dog)

lable3 = tk.Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="#aaffff")

lable4 = tk.Label(window,text="            ")

lable5 = tk.Label(window,text="            ")



lable1.grid(row=1,column=3)
lable2.grid(row=1,column=2)
lable3.grid(row=2,column=1,columnspan=4)
lable4.grid(row=1,column=1)
lable5.grid(row=1,column=4)

window.mainloop()