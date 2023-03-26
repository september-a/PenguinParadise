from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

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

    c1 = Canvas(win, bg="blue")
    c1.pack(fill="both",expand="true")

    penguinImage = Image.open("penguin.png")
    resized_image= penguinImage.resize((int(penguinImage.width/10),int(penguinImage.height/10)), Image.Resampling.LANCZOS)
    img= ImageTk.PhotoImage(resized_image)
    for i in range(10):
        for j in range(10):
            c1.create_image(150 * j,100*i,anchor=NW,image=img)

    win.mainloop()


buildWindow()

