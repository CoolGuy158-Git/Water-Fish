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
import requests
from PIL import Image, ImageTk
import winsound
import random
from bs4 import BeautifulSoup
from wfmodules.wfsusdetector import check
from tkinter import messagebox
from wfmodules.wfsafemode import safemode
# Ok why did 1 am me decide to turn this into base64?
rickroll = "audio/rickroll.mp3"
def checkurl(url, currentframe, data, homepage):
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
    elif "/egg bsod" in url:
        """
        Unfortunately yes this only works in windows.
        No it doesn't show a real bsod if you go to images/bsoa.png
        You'll see that first off its a smiley :) face not a sad face :(
        Secondly the text specifically says PC is fine.
        So yea.
        """
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
        sixseven = [6000, 7000]
        bsod.after(random.choice(sixseven), bsod.destroy)
        time.sleep(0.1)
    elif "/egg imfeelinglucky" in url: # Works pretty well, though sometimes a 404 appears cuz the page may have blocked us, but hey that means YOU'RE UNLUCKY!
        try:
            words = ("cats", "dogs", "computers", "website", "wiki", "internet", "security", "developer", "space",
                     "stars", "moon", "sun", "planet", "galaxy", "astronomy", "telescope", "ocean", "fish", "whale",
                     "shark", "coral", "river", "lake", "rain", "forest", "tree", "flower", "mushroom", "bird",
                     "insect", "butterfly", "frog", "history", "ancient", "medieval", "castle", "empire", "rome",
                     "greece", "egypt", "science", "biology", "chemistry", "physics", "math", "geometry", "algebra",
                     "calculus", "music", "piano", "guitar", "jazz", "classical", "vinyl", "radio", "audio", "art",
                     "painting", "drawing", "photography", "design", "typography", "ascii", "pixel", "retro", "vintage",
                     "old", "archive", "museum", "library", "book", "novel", "coffee", "tea", "bread", "cheese",
                     "recipe", "kitchen", "garden", "farm", "travel", "map", "train", "ship", "airplane", "mountain",
                     "island", "village", "philosophy", "poetry", "dream", "memory", "language", "dictionary",
                     "folklore", "myth", "robot", "linux", "terminal", "network", "programming", "privacy", "freedom",
                     "adventure")
            querytheuniverse = random.choice(words)
            if data["devopts"] == "True":
                print(f"\nSelected word: {querytheuniverse}")
            html = """
            <!DOCTYPE html>
            <html>
            <head>
            <title>Picking</title>
            </head>
            <body bgcolor="lightblue">
            <hr>
            <h1>Picking a random website</h1>
            <hr>
            </body>
            </html>"""
            currentframe.load_html(html)
            urllll = f"https://wiby.me/?q={querytheuniverse}"
            response = requests.get(urllll)
            soup = BeautifulSoup(response.text, "html.parser")
            links = []
            for a in soup.find_all("a", href=True):
                if a["href"].startswith("https"):
                    links.append(a["href"])
            link = random.choice(links)
            if data["devopts"] == "True":
                print(f"Selected link: {link}\n")
            html = """
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <title>Safety</title>
                    </head>
                    <body bgcolor="lightblue">
                    <hr>
                    <h1>Running safety check</h1>
                    <hr>
                    </body>
                    </html>"""
            currentframe.load_html(html)
            safety = check(link, data)
            if safety.startswith("F"):
                if not messagebox.askokcancel("WARNING", f"This site is {safety} by Water-Fish! It could be a joke site, it could be a really bad one, who knows? Be safe out there...\n\n press cancel to return to homepage."):
                    currentframe.load_html(homepage())
                    return
            if data["safemode"] == "True":
                safemode(link, currentframe)
            currentframe.load_url(link)
            return True
        except Exception as e:
            html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                <title>Failure</title>
                </head>
                <body bgcolor="lightblue">
                <hr>
                <h1>Oops! Looks like luck's not on your side today!</h1>
                <hr>
                <p>{e}</p>
                <p>If error persists, file an issue on the <a href='https://github.com/CoolGuy158-Git/Water-Fish'>official github repo</a></p>
                </body>
                </html>"""
            currentframe.load_html(html)

