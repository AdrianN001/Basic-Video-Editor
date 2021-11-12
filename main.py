from tkinter import *
from tkinter import filedialog
import tkinter as tkr
import moviepy
from moviepy.editor import *
import os 
from PIL import ImageTk,Image
import time



root = tkr.Tk()

root.title('Video Editor')
root.geometry('500x400')


def calc():
    file1 = filedialog.askopenfilename(initialdir='/', title = 'Choose a file', filetypes=(("MP4 file", "*.mp4"),("all files", "*.*")))
    tkr.Label(master = root,text= file1).pack()


    if file1 != None:
        kezdet = tkr.Entry(master = root)
        kezdet.pack()
        veg = tkr.Entry(master = root)
        veg.pack()
        
        def videoEdit():
            clip2 = VideoFileClip(file1).subclip(kezdet.get(),veg.get())
            clip2.write_videofile("Final_Video.mp4") 
        submit = tkr.Button(text='Submit', command=videoEdit)
        submit.pack()
    



greeting = tkr.Label(master = root,text= "Welcom To My Video Editor").pack()
chooseingFile = tkr.Button(master = root,text = "Choose a File", command= calc).pack()




root.mainloop()
