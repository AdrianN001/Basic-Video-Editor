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
root.geometry('1280x720')


def videoCutting():
    file1 = filedialog.askopenfilename(initialdir='/', title = 'Choose a file', filetypes=(("MP4 file", "*.mp4"),("all files", "*.*")))
    tkr.Label(master = root,text= file1).pack()


    if file1 != None:
        kezdetLabel = tkr.Label(master = root, text = 'Kezdeti Időpont')
        kezdetLabel.pack()

        kezdet = tkr.Entry(master = root)
        kezdet.pack()
        
        vegLabel = tkr.Label(master = root, text = 'Vegső Időpont')
        vegLabel.pack()
        veg = tkr.Entry(master = root)
        veg.pack()
        
        def videoEdit():

            try:
                clip2 = VideoFileClip(file1).subclip(kezdet.get(),veg.get())

            except:
                clip2 = VideoFileClip(file1).subclip(0,veg.get())
                
            clip2.write_videofile("Final_Video.mp4") 
        submit = tkr.Button(text='Submit', command=videoEdit)
        submit.pack()
    



greeting = tkr.Label(master = root,text= "Welcom To My Video Editor").pack()
chooseingFile = tkr.Button(master = root,text = "Choose a File", command= videoCutting).pack()




root.mainloop()
