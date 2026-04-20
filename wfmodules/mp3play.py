"""
Music Player
---
WfModule that lets user play music.
Used when user wants to listen to Bg Musics while surfing.
Useful also for experimentation because I want the browser to play the sound if a link containing a mp3 file is opened.
User can also add their own songs to dir audio/songs.

All the music are from https://ncs.io
"""

import tkinter as tk
import pygame
import os

def initPlay(root):
    pygame.mixer.init()
    def play():
        selectsong = listsong.curselection()
        if not selectsong:
            return
        file = listsong.get(selectsong[0])
        pygame.mixer.music.load(f"audio/songs/{file}")
        pygame.mixer.music.play()
    app = tk.Toplevel(root)
    app.geometry("400x300")
    app.title("mp3play")
    app.resizable(False, False)
    app.iconbitmap("images/waterfish.ico")
    listsong = tk.Listbox(app, width=400, height=250, bg='lightblue') # Yippee! I don't have to manually make a scroll wheel thing!
    listsong.pack()
    listsong.propagate(False)
    for file in os.listdir("audio/songs"):
        if file.endswith(".mp3"):
            listsong.insert("end", file)
    listsong.bind("<<ListboxSelect>>", lambda e: play())
def stopsng():
    pygame.mixer.music.stop()