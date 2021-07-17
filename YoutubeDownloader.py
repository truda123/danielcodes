import tkinter as tk
from tkinter import messagebox,filedialog
from pytube import YouTube
import os
window = tk.Tk()
window.title("YoutubeDownloader")

v = tk.IntVar(window)

tk.Radiobutton(window, text="Video", variable=v, value=1).grid(column=0, row=3)
tk.Radiobutton(window, text="Audio", variable=v, value=2).grid(column=0, row=5)


lbl = tk.Label(window, text="Video URL here",font=("Comic Sans MS", 20))
lbl.grid(column=0, row=0)

txt = tk.Entry(window,width=30)
txt.grid(column=0, row=1)

def play():
 os.system('py videoPlayer.py')

def clicked():
 
  sel = v.get()
  url =  txt.get()
  youtube = YouTube(url)
  print(youtube.streams)
  name = youtube.title
  if sel == 1 :
   filepath = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("MP4 files","*.mp4"),("All Files","*.*")))
   filedir = os.path.dirname(filepath)
   fname = os.path.basename(filepath)
   video = youtube.streams.first().download(output_path=filedir, filename = fname)
  elif sel == 2:
   filepath = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("MP3 files","*.mp3"),("All Files","*.*")))
   filedir = os.path.dirname(filepath)
   fname = os.path.basename(filepath)
   newname = fname + '.mp3'
   video=youtube.streams.filter(only_audio=True).first().download(output_path=filedir, filename = 'temp')
   os.chdir(filedir)
   os.rename('temp.mp4',newname)
  else:
   messagebox.showinfo("YoutubeDownloader","Please choose an option") 

btn = tk.Button(window, text="Download",command=clicked)
btn.grid(column=1, row=1)

btn2 = tk.Button(window, text="Play",command=play)
btn2.grid(column=2,row=1)

window.geometry('350x200')
window.mainloop()
