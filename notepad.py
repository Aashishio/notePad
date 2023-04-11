from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

root = Tk()

root.title("Copyright Notepad")
root.geometry("700x700")

imgOpen = ImageTk.PhotoImage(Image.open("open.png"))
imgExit = ImageTk.PhotoImage(Image.open("exit.jpg"))
imgSave = ImageTk.PhotoImage(Image.open("save.png"))






img_OpenBtn = Button(root, image=imgOpen, text="Open")
img_OpenBtn.place(relx=0.05, rely=0.03, anchor=CENETER)

img_ExitBtn = Button(root, image=imgExit, text="Exit")
img_ExitBtn.place(relx=0.11, rely=0.03, anchor=CENETER)

img_SaveBtn = Button(root, image=imgSave, text="Save")
img_SaveBtn.place(relx=0.17, rely=0.03, anchor=CENETER)


root.mainloop()