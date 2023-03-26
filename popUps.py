import tkinter as tk

def winPopUp():
    top= Toplevel(win)
    top.geometry("750x250")
    top.title("Penguin Paradise")
    Label(top, text= "You won!", font=('Mistral 18 bold')).place(x=150,y=80)

def losePopUp():
    top= tk.Toplevel(win)
    top.geometry("750x250")
    top.title("Penguin Paradise")
    tk.Label(top, text= "You Lost!", font=('Mistral 18 bold')).place(x=150,y=80)