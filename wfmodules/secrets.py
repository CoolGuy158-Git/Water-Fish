"""
Easter Eggs
---
Cool little secret Easter Eggs.
Can serve as experimentation on how far you can push the browser.
It's also pretty fun
"""
import pygame
import time
import urllib.parse
import tkinter as tk
from PIL import Image, ImageTk
import winsound

# Ok why did 1 am me decide to turn this into base64?
rickroll = "audio/rickroll.mp3"
def checkurl(url, currentframe):
    url = urllib.parse.unquote(url).lower()
    url = " ".join(url.split())

    if "/egg rickroll" in url:
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(rickroll)
            pygame.mixer.music.play()
        except Exception as e:
            print(e)
    elif "/egg help i accidentally" in url: # Ya'll seen those memes though, yea if its not clear enough its what inspired this
        helpi = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>helpiegged</title>
        </head>
        <body>
        <h1>Help I Accidentally</h1>
        <hr>
        <ul>
          <li>Made a Browser</li>
          <li>Ate a F-22 Raptor</li>
          <li>Built an Asus TUF Gaming A15</li>
          <li>Proved string theory</li>
          <li>...</li>
        </ul>
        </body>
        </html>
        """
        currentframe.load_html(helpi)
        time.sleep(1) # I spent like 30 mins wondering why helpi won't show...It was because load was covering it, so yea delay is here to make helpi visible.
    elif "/egg bsod" in url: # Only works in Windows sorry~
        winsound.MessageBeep(winsound.MB_ICONHAND)
        bsod = tk.Toplevel()
        bsod.attributes("-fullscreen", True)
        bsod.overrideredirect(True)
        w = bsod.winfo_screenwidth()
        h = bsod.winfo_screenheight()
        img = Image.open("images/bsoa.png") # Img from https://megtaza.com/
        img = img.resize((w, h), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        bg = tk.Label(bsod, image=img)
        bg.place(relwidth=1, relheight=1)
        bg.image = img
        bsod.bind("<Escape>", lambda e: bsod.destroy())
        time.sleep(0.1)

