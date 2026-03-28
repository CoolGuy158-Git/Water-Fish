import tkinter as tk
from tkinterweb import HtmlFrame # Planning to make my own renderer but for know imma stick with tkinterweb
import urllib.parse
import requests
import random
from tkinter import messagebox
import subprocess
import platform
import threading

data = {}

with open('settings.txt', 'r') as file:
    for line in file:
        if '=' in line:
            name, value = line.strip().split('=')
            data[name.strip()] = value.strip()


root = tk.Tk()
root.geometry("1000x700")
root.title("Water Fish")
root.iconbitmap("waterfish.ico")
textchoice = ['The buggiest browser ever.', 'Is this even a browser?', 'I will feed you Ai. -Not my browser', 'Why are you using ts?', 'Magnificant browser', 'Slightly better than IE!', 'Fun fact this browser was made by a 13 yo!', 'Is using tkinterweb cheating?'] # Comment on my yt channel what other text I should add!
def homepage():
    text = random.choice(textchoice)
    return f"""
<!DOCTYPE html>
<html>
  <head>
    <title>WaterFish</title>
  </head>
  <body bgcolor="lightblue">
  <center>
    <h1><a href=info.html>WaterFish</a></h1>
    <hr>
    <img src=waterfish.png width=300 height=300>
    <hr>
    <br>
    <table border="1" cellpadding="5">
    <tr>
    <td><a href="https://text.npr.org/" target="_blank">NPR</a></td>
    <td><a href="https://lite.cnn.com/" target="_blank">CNN</a></td>
    <td><a href="https://www.bbc.co.uk/news/10628494" target="_blank">BBC</a></td>
    <td><a href="https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/" target="_blank">FDIC</a></td>
    <td><a href="https://www.linfo.org/" target="_blank">Linfo.org</a></td>
    </tr>
    <tr>
    <td><a href="https://www.dictionary.com/e/word-of-the-day/" target="_blank">Dictionary.com</a></td>
    <td><a href="https://www.cplusplus.com/doc/tutorial/" target="_blank">C++ Tutorial</a></td>
    <td><a href="https://www.gnu.org/manual/manual.html" target="_blank">GNU Manuals</a></td>
    <td><a href="https://www.ietf.org/rfc/" target="_blank">RFC Editor</a></td>
    <td><a href="https://www.w3.org/TR/html52/" target="_blank">W3C HTML5.2</a></td>
    </tr>
  </table>
  <br>
  <hr>
  <h3>{text}</h3>
  <hr>
  </center>
  </body>
</html>"""

tabs = []
current = None
currentframe = None
tabbtnn = []
max = 20
def switch(index):
    global current, currentframe

    for t in tabs:
        t.pack_forget()

    tabs[index].pack(fill="both", expand=True)

    current = index
    currentframe = tabs[index]
    curtab.config(text=f"Current Tab: {current + 1}")
def newtab(url=None):
    global currentframe

    if len(tabs) >= max:
        messagebox.showinfo(title="Max tabs", message="Im to lazy to add a scroll thing") # Don't worry im planning to add it
        return

    frame = HtmlFrame(root)
    tabs.append(frame)

    index = len(tabs) - 1
    addtab(index)

    currentframe = frame

    if url:
        frame.load_website(url)
    else:
        frame.load_html(homepage())

    switch(index)
def addtab(index):
    btn = tk.Button(tabbar,text=f"Tab {index + 1}",command=lambda i=index: switch(i)
    )
    btn.pack(side="left")
    tabbtnn.append(btn)
def remtab(index):
    global current

    if len(tabs) <= 1:
        return
    tabs[index].destroy()
    tabbtnn[index].destroy()

    tabs.pop(index)
    tabbtnn.pop(index)

    for i, btn in enumerate(tabbtnn):
        btn.config(text=f"Tab {i + 1}",
                   command=lambda x=i: switch(x))

    current = max(0, index - 1)
    switch(current)

def customize(): # Originally I wanted a tkinter top level to appear so you can edit the settings, but I was too lazy so enjoy editing settings via notepad hehe
    if platform.system() == "Windows":
        proc = subprocess.Popen(["notepad.exe", "settings.txt"])
    elif platform.system() == "Darwin":
        proc = subprocess.Popen(["open", "settings.txt"])
    else:
        proc = subprocess.Popen(["xdg-open", "settings.txt"])
    checkditor(proc)


def checkditor(proc):
    if proc.poll() is None:
        root.after(500, lambda: checkditor(proc))
    else:
        refreshsettings()


def refreshsettings():
    global data
    try:
        newdata = {}
        with open('settings.txt', 'r') as file:
            for line in file:
                if '=' in line:
                    name, value = line.strip().split('=')
                    newdata[name.strip()] = value.strip()

        data = newdata

        colorthing.config(bg=data['color'])
        searchtab.config(bg=data['color'])
        curtab.config(bg=data['color'])
        tabbar.config(bg=data['tabcol'])

    except Exception as e:
        print(e)

def imalwaysright(event): # idc what you say this is the best func name
    customize()

colorthing = tk.Frame(root, width=1000, height=100, bg=data['color'])
colorthing.pack(fill='x')
colorthing.pack_propagate(False)
colorthing.bind("<Button-3>", imalwaysright)

searchtab = tk.Frame(colorthing, width=1000, height=100, bg=data['color'])
searchtab.pack(pady=20)

curtabvar = tk.StringVar()
curtabvar.set("0")

curtab = tk.Label(searchtab, text="Current Tab: 0", bg=data['color'])
curtab.pack(side='left', padx=(0,5))

gohome = tk.Button(searchtab, text="Home")
gohome.pack(side='left')

search = tk.Entry(searchtab, width=80)
search.pack(side='left')

searchbutton = tk.Button(searchtab, width=10, text="Search")
searchbutton.pack(side='left')

tabbar = tk.Frame(colorthing, bg=data['tabcol'])
tabbar.pack(fill="x")

addbtn = tk.Button(tabbar, text="+", command=newtab)
addbtn.pack(side="right")

rembtn = tk.Button(tabbar, text="-", command=lambda: remtab(current if current is not None else 0))
rembtn.pack(side="right")

# TODO make an offline game!!!
error_internet = f"""
<!DOCTYPE html>
<html>
  <head>
  <title>Error</title>
  </head>
  <body>
  <h1>Error Loading Page</h1>
  <hr>
  <p>Please check your internet connection</p>
  <p>If error persists, file an issue on the <a href='https://github.com/CoolGuy158-Git/Water-Fish'>official github repo</a></p>
  <p>your feedback truly matters</p>
  </body>
  """
error_generic = """
<!DOCTYPE html>
<html>
  <head>
  <title>Error</title>
  </head>
  <body>
  <h1>Error Loading Page</h1>
  <hr>
  <p>Unknown failure</p>
  <p>If error persists, file an issue on the <a href='https://github.com/CoolGuy158-Git/Water-Fish'>official github repo</a></p>
  <p>your feedback truly matters</p>
  </body>
  """
def checkonline(url):
    try:
        requests.head(url, timeout=3) # Slows down the browser a bit but ehh better safe than sorry ig
        return True
    except:
        return False
def loadnoworelse(url): # hehe now I can throw errors at your face
    try:
        if not url.startswith("http"):
            url = "https://wiby.me/?q=" + urllib.parse.quote(url)

        if not checkonline(url):
            currentframe.load_html(error_internet)
            return

        currentframe.load_website(url)

    except Exception as e:
        currentframe.load_html(error_generic)
        print(e)

def load(url):
    threading.Thread(target=loadnoworelse, args=(url,), daemon=True).start()

def searchfor():
    if not search.get().strip():
        messagebox.showwarning(title="Error", message="Entry empty") # Windows messagebox jumpscare
        return
    query = urllib.parse.quote(search.get())
    url = f"https://wiby.me/?q={query}"
    load(url)

search.bind('<Return>', lambda event: searchfor())

def gohomefunc(): # Yea go home vro
    if currentframe:
        currentframe.load_html(homepage())
    search.delete(0, tk.END)

searchbutton.config(command=searchfor)
gohome.config(command=gohomefunc)
newtab()
root.mainloop()

