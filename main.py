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
root.iconbitmap('Git es Repok\Video Editor\icon.ico')
root.configure(background='#292727')

def videoCutting():  # Video Cutting Button's function
    
    videoCuttingRoot = tkr.Tk()
    videoCuttingRoot.title('Video Editor')
    videoCuttingRoot.geometry('1280x720')
    videoCuttingRoot.iconbitmap('Git es Repok\Video Editor\icon.ico')
    videoCuttingRoot.configure(background='#292727')

    file1 = filedialog.askopenfilename(initialdir='/', title = 'Choose a file', filetypes=(("MP4 file", "*.mp4"),("all files", "*.*")))
    tkr.Label(master = videoCuttingRoot,text= file1).pack() # It'll print out the location of the file 


    if file1 != None:  # Things with the files are starts here
        kezdetLabel = tkr.Label(master = videoCuttingRoot, text = 'Kezdeti Időpont',background='#292727', border=0,font =('Consolas',19)) # Input 1
        kezdetLabel.pack(padx=20, pady=30)

        kezdet = tkr.Entry(master = videoCuttingRoot,background='#545151', border=0,font =('Consolas',19))
        kezdet.pack(padx=20, pady=30)
        
        vegLabel = tkr.Label(master = videoCuttingRoot, text = 'Vegső Időpont',background='#292727', border=0,font =('Consolas',19)) # Input2
        vegLabel.pack(padx=20, pady=30)

        veg = tkr.Entry(master = videoCuttingRoot,background='#545151', border=0,font =('Consolas',19))
        veg.pack(padx=20, pady=30)
        
        #Video cutting with the datas of the inputs
        def videoEdit():

            try:
                clip2 = VideoFileClip(file1).subclip(kezdet.get(),veg.get())

            except:
                clip2 = VideoFileClip(file1).subclip(0,veg.get())

            clip2.write_videofile("Final_Video.mp4") 
        submit = tkr.Button(master = videoCuttingRoot, text='Submit', command=videoEdit,background='#545151', border=0,font =('Consolas',19))
        submit.pack(padx=20, pady=30)
    videoCuttingRoot.mainloop()


def videoRotating():
    videoRotatingRoot = tkr.Tk()
    videoRotatingRoot.title('Video Rotating')
    videoRotatingRoot.geometry('1280x720')
    videoRotatingRoot.iconbitmap('Git es Repok\Video Editor\icon.ico')
    videoRotatingRoot.configure(background='#292727')

    file1 = filedialog.askopenfilename(initialdir='/', title = 'Choose a file', filetypes=(("MP4 file", "*.mp4"),("all files", "*.*")))
    tkr.Label(master = videoRotatingRoot,text= file1).pack(padx=20, pady=30)
    
    tkr.Label(master = videoRotatingRoot, text = 'Jelenlegi fok:',background='#292727', border=0,font =('Consolas',19)).pack(padx=20, pady=30)
    degreeLabel = tkr.Label(master = videoRotatingRoot, text = '0',background='#545151', border=0,font =('Consolas',19))
    degreeLabel.pack(padx=20, pady=30)


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

        rotateRight = tkr.Button(master = videoRotatingRoot, text = "Rotateing Right",command=rotateingRight,background='#545151', border=0,font =('Consolas',19)).pack(padx=20, pady=30) # Buttons
        rotateLeft = tkr.Button(master = videoRotatingRoot, text = "Rotateing Left",command=rotateingLeft,background='#545151', border=0,font =('Consolas',19)).pack(padx=20, pady=30)
        submit = tkr.Button(master = videoRotatingRoot, text = 'Done', command= rendering,background='#545151', border=0,font =('Consolas',19)).pack(padx=20, pady=30)
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
greeting = tkr.Label(master = root,text= "Welcome To My Video Editor",background='#545151', border=0,font =('Arial',25)).pack(padx=20, pady=30)



videoEditingButton = tkr.Button(master = root,text = "Video Editing", command= videoCutting,background='#545151', border=0,font =('Consolas',19)).pack(padx=20, pady=30)



videoRotatingButton = tkr.Button(master = root,text = "Video Rotating", command= videoRotating,background='#545151', border=0,font =('Consolas',19)).pack(padx=20, pady=30)



videoRotatingButton = tkr.Button(master = root,text = "Video Merging", command= videoMerging,background='#545151', border=0,font =('Consolas',19)).pack(padx=20, pady=30)





root.mainloop()
