"""
Startupper
---
WfModule that serves no real purpose aside from making the browser feel polished.
It first plays a simple startup animation, then plays a startup audio.
"""
import cv2
import pygame
from PIL import ImageTk
from PIL import Image
import tkinter as tk

anime = cv2.VideoCapture('video/startup.mp4')
def animestart(root):
    moniw, monih = root.winfo_screenwidth(), root.winfo_screenheight()
    winw, winh = 600, 600
    x = (moniw // 2) - (winw // 2)
    y = (monih // 2) - (winh // 2) # Get the screen info in order to make the thing spawn in the middle, planned on hardcoding it but nvm.
    startscr = tk.Toplevel(root)
    startscr.geometry(f"{winw}x{winh}+{x}+{y}")
    startscr.overrideredirect(True)
    winborder = tk.Frame(startscr, bg="gray", bd=10)
    winborder.pack(fill="both", expand=True)
    label = tk.Label(winborder)
    label.pack()
    def update():
        ret, frame = anime.read()
        if not ret:
            anime.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = anime.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        label.config(image=img)
        label.image = img
        startscr.after(10, update)
    update()
    return startscr
def endanime(window, root, start, data):
    start(root, data)
    window.destroy()
    pygame.mixer.init()
    pygame.mixer.music.load('audio/startup.mp3') # Sound Effect by https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=14572
    pygame.mixer.music.play()
    root.deiconify()