from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import canvas
import time

def buildWindow():
    win = Tk()

    width = win.winfo_screenwidth()               
    height = win.winfo_screenheight()               
    win.geometry("%dx%d" % (width*.8, height*.8))

    # Title of the game
    label= Label(win, text= "Penguin Paradise", font=('Times New Roman bold',30))
    label.pack()

    # This is the area where you can interact with the population number
    p1 = PanedWindow(win,background="white")
    p1.pack(side="left",fill="y",expand=False)

    # This is where the user can input a population
    population = Label(p1, text="Number of Penguins:", background="White")
    populationEntry = Entry(p1)
    population.grid(row = 0, column=0, sticky=W,pady=2)
    populationEntry.grid(row=0,column=1, sticky=W,pady=2)
    
    polution = Label(p1, text="Pounds of Polution:", background="White")
    polutionEntry = Entry(p1)
    polution.grid(row = 1, column=0, sticky=W,pady=2)
    polutionEntry.grid(row=1,column=1, sticky=W,pady=2)

    c1 = canvas.MyCanvas(win)
    c1.canvas.pack(fill="both",expand="true")

    c1width = c1.canvas.winfo_width()
    c1height = c1.canvas.winfo_height()
    print(c1width)
    print(c1height)


    landscapeImage = Image.open("landscape.png")
    resized_image3 = landscapeImage.resize((int(landscapeImage.width*5), int(landscapeImage.height*5)), Image.Resampling.LANCZOS)
    landscapeImage = ImageTk.PhotoImage(resized_image3)
    c1.canvas.create_image(-50,175,anchor=NW,image=landscapeImage)
    win.mainloop()


buildWindow()

