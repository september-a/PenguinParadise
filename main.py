from tkinter import NW, W, Tk,PanedWindow,Label,Entry
from tkinter import ttk
from PIL import Image,ImageTk
import canvas
import random

def build_Window():
    poundsOfTrash = 0
    numPenguins = 3
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
    population = Label(p1, text="Number of Penguins:", background="white",foreground="black")
    population_Display = Label(p1,text=f"{numPenguins}")
    population.grid(row = 0, column=0, sticky=W,pady=2)
    population_Display.grid(row=0,column=1, sticky=W,pady=2)
    
    polution = Label(p1, text="Pounds of Polution:", background="white",foreground="black")
    polution_Display = Label(p1,text=f"{poundsOfTrash}")
    polution.grid(row = 1, column=0, sticky=W,pady=2)
    polution_Display.grid(row=1,column=1, sticky=W,pady=2)

    c1 = canvas.MyCanvas(win)
    c1.canvas.pack(fill="both",expand="true")

    landscapeImage = Image.open("landscape.png")
    resized_image3 = landscapeImage.resize((int(landscapeImage.width*5), int(landscapeImage.height*5)), Image.ANTIALIAS)
    landscapeImage = ImageTk.PhotoImage(resized_image3)
    c1.canvas.create_image(-50,175,anchor=NW,image=landscapeImage)

    penguin_list = []
    birthRate = 5
    deathRate = 7
    numiterations = 0

    
    # Have three initial penguins added to the screen (a 4th is added in the update function)
    for i in range(3):
        penguin_list.append(c1.drawPenguin(random.randint(0,750),random.randint(250,600)))
    # Update function for tkinter window
    def update():
        nonlocal penguin_list
        nonlocal birthRate
        nonlocal deathRate
        nonlocal numiterations
        nonlocal numPenguins
        nonlocal poundsOfTrash
        if(numiterations % birthRate == 0):
            penguin_list.append(c1.drawPenguin(random.randint(0,750),random.randint(200,600)))
            numPenguins += 1
        if(numiterations % deathRate == 0):
            numPenguins -= 1
            c1.canvas.delete(penguin_list[0])
            del penguin_list[0]
        if(numiterations % 2 == 0 ):
            poundsOfTrash = c1.drawTrash(random.randint(0,750),random.randint(200,600))
        population_Display["text"]=f"{numPenguins}"
        polution_Display["text" ]= f"{poundsOfTrash}"
        numiterations += 1
        win.after(1000,update)
    update()
    win.mainloop()


build_Window()

