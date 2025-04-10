import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Hi!")
window.geometry("255x140")

lable1 = tk.Label(window, text="Pochacco!")

dog = PhotoImage(file="dog.png")
lable2 = tk.Label(window, image=dog)

lable3 = tk.Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="#aaffff")

lable1.place(x=140,y=40)
lable2.place(x=70,y=0)
lable3.place(x=0,y=105)

window.mainloop()