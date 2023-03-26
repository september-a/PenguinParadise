import tkinter as tk
from PIL import Image,ImageTk
import random

def _image_prep(text):
        image = Image.open(text)
        resized_image = image.resize((int(image.width/10),int(image.height/10)), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

class MyCanvas(tk.Tk):
    def __init__(self,root):
        MyCanvas.redPenguin = _image_prep("redPenguin.png")
        MyCanvas.penguinImage = _image_prep("penguin.png")
        MyCanvas.trashbagImage = _image_prep("trashbag.png")
        self.canvas = tk.Canvas(root,background="lightblue")
        root.bind('<Configure>', self.resize)
    
    def resize(self,event):
        self.height = event.width
        self.width = event.height

    def drawPenguin(self,x,y):
        penguin = ""
        if(random.randint(1,2)==1):
            penguin = MyCanvas.redPenguin
        else:
            penguin = MyCanvas.penguinImage
        return self.canvas.create_image(x,y,anchor=tk.NW,image=penguin)

    def drawTrash(self,x,y):
        return self.canvas.create_image(x,y,anchor=tk.NW,image=MyCanvas.trashbagImage)
         
    # def deleteTrash(self):
    #     pass
    # def deadPenguin(self):
    #     pass
