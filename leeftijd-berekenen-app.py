import tkinter as tk
from tkinter import Button, font
window =  tk.Tk()

# importing date class from datetime module
from datetime import date
  
# creating the date object of today's date
todays_date = date.today()

window.geometry('200x100')  
window.configure(bg='yellow')

label = tk.Label(text="Voer uw geboortejaar in.", font='Century 12', fg='blue', bg='yellow')
entry = tk.Entry(font='Century 12', bg='pink', fg='green')
button = tk.Button(text='Verzenden')
jaartalAnsw = tk.Label(text="")

label.pack()
entry.pack()
button.pack()
jaartalAnsw.pack()

def jaarberekenen(event):
    jaartal = entry.get()
    if jaartal.isnumeric() == True:
        jaartalAnsw["text"] = ("Je bent of wordt dit jaar "+str(todays_date.year - int(jaartal))+" jaar oud.")
    else:
        jaartalAnsw["text"] = "Voer een geldig jaartal in!"


button.bind("<Button-1>",jaarberekenen)

window.mainloop()