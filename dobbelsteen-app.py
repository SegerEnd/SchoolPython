from random import randint
import tkinter as tk
window =  tk.Tk()

window.geometry('200x150') 
window.configure(bg='snow')

hint = tk.Label(text="Druk op dobbelen om te dobbelen", bg="snow")
hint2 = tk.Label(text="Aantal dobbelstenen:", bg="snow")
keren = tk.Entry(text="Keren dobbelen", bg='snow')
button = tk.Button(text='Dobbelen')
gegooid = tk.Label(text="", bg="snow")

hint.pack()
hint2.pack()
keren.pack()
button.pack()
gegooid.pack()

def dobbelen(event):
    gegooid["text"] = ""
    kerenD = keren.get()
    if kerenD.isnumeric() == True and kerenD != "0":
        for keer in range(int(kerenD)):
            gegooid["text"] = gegooid["text"]+str(randint(1,6))+", "
    else:
        gegooid["text"] = str(randint(1,6))


button.bind("<Button-1>",dobbelen)

window.mainloop()