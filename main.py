from tkinter import *
from tkinter import filedialog
import tkinter as tkr
import moviepy
from moviepy.editor import *
import os 
from PIL import ImageTk,Image
import time
from moviepy.editor import VideoFileClip, concatenate_videoclips



root = tkr.Tk()

root.title('Video Editor')
root.geometry('1280x720')


def videoCutting():  # Video Cutting Button's function
    
    videoCuttingRoot = tkr.Tk()
    videoCuttingRoot.title('Video Editor')
    videoCuttingRoot.geometry('1280x720')


    file1 = filedialog.askopenfilename(initialdir='/', title = 'Choose a file', filetypes=(("MP4 file", "*.mp4"),("all files", "*.*")))
    tkr.Label(master = videoCuttingRoot,text= file1).pack() # It'll print out the location of the file 


    if file1 != None:  # Things with the files are starts here
        kezdetLabel = tkr.Label(master = videoCuttingRoot, text = 'Kezdeti Időpont') # Input 1
        kezdetLabel.pack()

        kezdet = tkr.Entry(master = videoCuttingRoot)
        kezdet.pack()
        
        vegLabel = tkr.Label(master = videoCuttingRoot, text = 'Vegső Időpont') # Input2
        vegLabel.pack()

        veg = tkr.Entry(master = videoCuttingRoot)
        veg.pack()
        
        #Video cutting with the datas of the inputs
        def videoEdit():

            try:
                clip2 = VideoFileClip(file1).subclip(kezdet.get(),veg.get())

            except:
                clip2 = VideoFileClip(file1).subclip(0,veg.get())

            clip2.write_videofile("Final_Video.mp4") 
        submit = tkr.Button(master = videoCuttingRoot, text='Submit', command=videoEdit)
        submit.pack()
    videoCuttingRoot.mainloop()


def videoRotating():
    videoRotatingRoot = tkr.Tk()
    videoRotatingRoot.title('Video Rotating')
    videoRotatingRoot.geometry('1280x720')

    file1 = filedialog.askopenfilename(initialdir='/', title = 'Choose a file', filetypes=(("MP4 file", "*.mp4"),("all files", "*.*")))
    tkr.Label(master = videoRotatingRoot,text= file1).pack()
    
    tkr.Label(master = videoRotatingRoot, text = 'Jelenlegi fok:').pack()
    degreeLabel = tkr.Label(master = videoRotatingRoot, text = '0')
    degreeLabel.pack()


    if file1 != None: # Actual Rotating
        validDegrees = [0,90,180,-90]
        x = [0]
        def rotateingRight():
            if x[0] < 3: 
                x[0] += 1
            elif x[0] >= 3: 
                x[0] = 0
            global rotateingValue
            rotateingValue = validDegrees[x[0]]
            degreeLabel.config(text=f"{rotateingValue}")
            
            
        def rotateingLeft():
            if x[0] > -3: 
                x[0] -= 1
            elif x[0] <= -3: 
                x[0] = 0
            global rotateingValue
            rotateingValue = validDegrees[x[0]]
            degreeLabel.config(text=f"{rotateingValue}")
            
        def rendering(): # Rendering
            
            clipRotate = VideoFileClip(file1).rotate(rotateingValue)

            clipRotate.write_videofile("Rotated_Clip.mp4") 

        rotateRight = tkr.Button(master = videoRotatingRoot, text = "Rotateing Right",command=rotateingRight).pack() # Buttons
        rotateLeft = tkr.Button(master = videoRotatingRoot, text = "Rotateing Left",command=rotateingLeft).pack()
        submit = tkr.Button(master = videoRotatingRoot, text = 'Done', command= rendering).pack()
    videoRotatingRoot.mainloop()


def videoMerging():
    #global videoMergingRoot
    #videoMergingRoot = tkr.Tk()
    #videoMergingRoot.title('Video Merger')
    #videoMergingRoot.geometry('1280x720')

    files = filedialog.askopenfilenames(initialdir='/', title = 'Choose a file', filetypes=(("MP4 file", "*.mp4"),("all files", "*.*")))
    #tkr.Label(master = videoMergingRoot,text= files).pack()

    if files != None:
        clips = [] # Here it creates a lot of clips from the files 
        for x in files:
            clip = VideoFileClip(x)
            clips.append(clip)
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile('Merged_Video.mp4')


   # videoMergingRoot = tkr.Tk()



#   MAIN MENU
greeting = tkr.Label(master = root,text= "Welcom To My Video Editor").pack()
videoEditingButton = tkr.Button(master = root,text = "Video Editing", command= videoCutting).pack()
videoRotatingButton = tkr.Button(master = root,text = "Video Rotating", command= videoRotating).pack()
videoRotatingButton = tkr.Button(master = root,text = "Video Merging", command= videoMerging).pack()





root.mainloop()
