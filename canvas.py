import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import random

def _imagePrep(text):
        image = Image.open(text)
        resized_image = image.resize((int(image.width/10),int(image.height/10)), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

class MyCanvas(tk.Tk):
    def __init__(self,root):
        MyCanvas.penguinImage = _imagePrep("penguin.png")
        MyCanvas.trashbagImage = _imagePrep("trashbag.png")
        self.canvas = tk.Canvas(root,background="lightblue")
        root.bind('<Configure>', self.resize)
    
    def resize(self,event):
        self.height = event.width
        self.width = event.height

    def drawPenguin(self):
        self.canvas.create_image(random.randint(5, 100),random.randint(5,100),anchor=NW,image=MyCanvas.penguinImage)

    def drawTrash(self):
         self.canvas.create_image(0,0,anchor=NW,image=MyCanvas.trashbagImage)
         
    def deleteTrash(self):
        pass
    def deadPenguin(self):
        pass
