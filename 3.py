from tkinter import *
from tkinter import filedialog
import tkinter as tkr
import moviepy
from moviepy.editor import *
import os 
from tkinter import *
from PIL import ImageTk,Image


root = tkr.Tk()

root.title('Video Editor')
root.geometry('500x400')


greeting = tkr.Label(master = root,text= "Welcom To My Video Editor").pack()

def openingAFile():
    root.filenames = filedialog.askopenfilenames(initialdir='/', title = 'Choose a file', filetypes=(("MP4 files", "*.mp4"),("all files", "*.*")))
    image = ImageTk.PhotoImage(Image.open(root.filenames[0]))
    imageLabel = tkr.Laber(image = image).pack()

chooseingFile = tkr.Button(master = root,text = "Choose a File", command= openingAFile).pack()




root.mainloop()