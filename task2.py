import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.resizable(False,False)

lable1 = tk.Label(window, text="Search by Name", relief = "groove")

entry1 = tk.Entry(window,text="Bonjour", width=15)

lable2 = tk.Label(window, text="Client Database")

lable3 = tk.Label(window, text="Name")

lable4 = tk.Label(window, text="Type")

lable5 = tk.Label(window, text="Breed")

lable6 = tk.Label(window, text="Owner")

lable7 = tk.Label(window, text="Birthdate")

dog = PhotoImage(file="dog.png")
lable8 = tk.Label(window, image=dog)

entry2 = tk.Entry(window,text="A", width=10)

entry3 = tk.Entry(window,text="B", width=10)

entry4 = tk.Entry(window,text="C", width=10)

entry5 = tk.Entry(window,text="D", width=10)

entry6 = tk.Entry(window,text="E", width=10)

button1 = tk.Button(window,text="<Previous", relief="groove")

button2 = tk.Button(window,text="Save Entry", height=2, relief="raised")

button3 = tk.Button(window,text="Next>", relief="groove")


lable8.grid(row=2,column=1)
lable1.grid(row=1,column=4)
entry1.grid(row=1,column=5)
lable2.grid(row=2,column=3)
lable3.grid(row=3,column=1)
lable4.grid(row=3,column=2)
lable5.grid(row=3,column=3)
lable6.grid(row=3,column=4)
lable7.grid(row=3,column=5)
entry2.grid(row=4,column=5)
entry3.grid(row=4,column=1)
entry4.grid(row=4,column=2)
entry5.grid(row=4,column=3)
entry6.grid(row=4,column=4)
button1.grid(row=5,column=1)
button2.grid(row=5,column=3)
button3.grid(row=5,column=5)

window.mainloop()