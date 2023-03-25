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
    p1.pack(fill=BOTH, expand=2)

    left = Label(p1, text="Left Panel", background="yellow")
    p1.add(left)
    p1.pack(padx=(width/5), pady=(height/5))

    p2 = PanedWindow(p1)
    p2.pack(fill=BOTH, expand=2)
    p1.add(p2)

    c1 = Canvas(p1, bg="blue")
    c1.pack(fill=BOTH)
    p1.add(c1)

    win.mainloop()


buildWindow()

