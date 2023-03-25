from tkinter import *
from tkinter import ttk

def buildWindow():
    win = Tk()
    frame = Frame(win)
    win.geometry("650x250")

    width = win.winfo_screenwidth()               
    height = win.winfo_screenheight()               
    win.geometry("%dx%d" % (width, height))
    
    frame.pack()

    label= Label(win, text= "Penguin Paradise", font=('Times New Roman bold',20))
    label.pack(padx=10, pady=10)

    p1 = PanedWindow()
    p1.pack(fill=BOTH, expand=TRUE)

    left = Label(p1, text="Left Panel", background="yellow")
    p1.add(left)
    numberEntry = Entry(text = "This is an entry")
    
    p1.add(numberEntry)
    
    p2 = PanedWindow(p1)
    p2.pack(fill=BOTH, expand=2)
    p1.add(p2)

    c1 = Canvas(p1, bg="blue")
    
    p1.pack()
    
    c1.pack(fill=BOTH)
    p1.add(c1)

    win.mainloop()


buildWindow()

