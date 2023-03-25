from tkinter import *
from tkinter import ttk

def buildWindow():
    win = Tk()
    win.geometry("650x250")

    width = win.winfo_screenwidth()               
    height = win.winfo_screenheight()               
    win.geometry("%dx%d" % (width, height))

    label= Label(win, text= "Penguin Paradise", font=('Times New Roman bold',20))
    label.pack(padx=10, pady=10)

    p1 = PanedWindow()
    p1.pack(fill=BOTH, expand=1)

    left = Label(p1, text="Left Panel", )
    p1.add(left)

    p2 = PanedWindow(p1, orient=VERTICAL)
    p1.add(p2)

    c1 = Canvas(p2, bg= "blue")
    p2.add(c1)



    win.mainloop()


buildWindow()

