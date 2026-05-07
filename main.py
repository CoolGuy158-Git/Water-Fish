"""
Water-Fish
----
A simple but privacy focused web browser
Meant as an alternative to other browsers
Project currently on Beta
Contribute by trying out the program, writing code for it, and writing issues regarding bugs and such
Under General Public License Version 3
"""
import tkinter as tk
from tkinterweb import HtmlFrame # Planning to make my own renderer but for know imma stick with tkinterweb
import urllib.parse
import random
from tkinter import messagebox
import threading
import sys
from wfmodules.Welcome import start # Planning to make a feature where users can create their own wfmodules
import wfmodules.secrets
from wfmodules.command import urlcheck
from wfmodules.checkonline import checkonline
from wfmodules.history import historytrack, obliterate
from wfmodules.startup import animestart, endanime
from wfmodules.stars import openbook
from wfmodules.reload import reloadmain, reload
from wfmodules.logger import log
from wfmodules.dragndrop import dragndrop
from wfmodules.mp3play import initPlay, stopsng
from wfmodules.overview import pageOverview
import tkinterdnd2 as tkd # Used this for root so that drag and drop can be used, the other tk widgets are still usable though.
from wfmodules.runcustmod import runCust
from wfmodules.offgame import error_internet
from WaterSearch.client import clientSTART
data = {}
try:
    with open('system/settings.txt', 'r') as file: # Yes it's a txt, why? idk
        for line in file:
            if '=' in line:
                name, value = line.strip().split('=')
                data[name.strip()] = value.strip()

except FileNotFoundError:
    messagebox.showerror('Fatal Error', 'Settings file not found')
    sys.exit()
except Exception as e:
    messagebox.showerror('Error', e)
    sys.exit()

root = tkd.Tk()
if data['startup'] == 'True':
    root.withdraw()
    startscr = animestart(root)
    root.after(2500, lambda: endanime(startscr, root, start, data))
else:
    start(root, data)
root.geometry("1000x700")
root.title("Water Fish")
root.iconbitmap("images/waterfish.ico")
textchoice = ['The buggiest browser ever.', 'Is this even a browser?', '"I will feed you Ai." -Not my browser', 'Why are you using ts?', 'Magnificant browser', 'Slightly better than IE!', 'Fun fact this browser was made by a 13 yo!', 'Is using tkinterweb cheating?'] # Comment on my yt channel what other text I should add!
def homepage():
    favorites = []
    with open("system/favorites.txt", "r") as f: # Yup NO MORE HARD CODING!!!
        for line in f:
            link, name = line.strip().split(", ")
            favorites.append((link, name))
    text = random.choice(textchoice) # Wait this actually worked?
    rows = ""
    colsrow = 5
    for i in range(0, len(favorites), colsrow):
        chunk = favorites[i:i + colsrow]
        row = "".join(f'<td><a href="{link}" target="_blank">{name}</a></td>'for link, name in chunk)
        rows += f"<tr>{row}</tr>"
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
        <title>Homepage</title>
      </head>
      <body bgcolor="lightblue">
      <center>
        <h1><a href="info.html">WaterFish</a></h1>
        <hr>
        <img src="images/waterfish.png" width="300" height="300">
        <hr><br>
        <table border="1" cellpadding="5">
        {rows}
        </table>
        <br><hr>
        <h3>{text}</h3>
        <hr>
      </center>
      </body>
    </html>
    """
tabs = []
current = None
currentframe = None
tabbtnn = []
maxtabs = 12
urlgoesbrr = ""

def switch(index): # This function handles tab switching as well as highlighting current tab so that users actually know where they are
    search.delete(0, tk.END)
    global current, currentframe
    for t in tabs:
        t.pack_forget()
    tabs[index].pack(fill="both", expand=True)
    current = index
    currentframe = tabs[index]
    for i, tabbtn in enumerate(tabbtnn):
        if i == current:
            tabbtn.config(bg=data['hightabcol']) # High cholesterol
        else:
            tabbtn.config(bg="SystemButtonFace")
def newtab(url=None):
    global currentframe

    if len(tabs) >= maxtabs:
        messagebox.showinfo(title="Max tabs", message="Im to lazy to add a scroll thing") # Don't worry im planning to add it
        return
    frame = HtmlFrame(root)
    frame.enable_link_clicks = True
    if data["devopts"] == "True":
        frame.config(messages_enabled=True)
    else:
        pass


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
    btn = tk.Button(tabbar,text=f"Tab {index + 1}",command=lambda i=index: switch(i))
    btn.pack(side="left")
    tabbtnn.append(btn)
def remtab(index): # removes your ex- i mean unused tabs
    global current

    if len(tabs) <= 1:
        return
    tabs[index].destroy()
    tabbtnn[index].destroy()

    tabs.pop(index)
    tabbtnn.pop(index)

    for i, btn in enumerate(tabbtnn):
        btn.config(text=f"Tab {i + 1}",command=lambda x=i: switch(x))

    current = max(0, min(index, len(tabs) - 1))
    switch(current)

def updatetab(): # Updates tab title
    tabtitle = currentframe.title
    global current
    if current is None or currentframe is None:
        return
    try:
        if tabtitle:
            tabbtnn[current].config(text=tabtitle)
            root.title(tabtitle)
    except:
        pass
    root.after(100, updatetab)
def back():
    global urlgoesbrr
    with open("system/history.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    cur = urlgoesbrr
    for i in range(1, len(lines)):
        for i in range(len(lines)):
            if lines[i] == cur:
                if i == 0:
                    return
                urlgoesbrr = lines[i - 1]
                currentframe.load_website(lines[i - 1])
                return
def forward():
    global urlgoesbrr
    with open("system/history.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    cur = urlgoesbrr
    for i in range(len(lines)):
        if lines[i] == cur:
            if i == len(lines) - 1:
                return
            urlgoesbrr = lines[i + 1]
            currentframe.load_website(lines[i + 1])
            return

menubar = tk.Frame(root, width=1000, height=70,bg='darkgray')
menubar.pack(fill="x")

colorthing = tk.Frame(root, width=1000, height=130, bg=data['color'])
colorthing.pack(fill='x')
colorthing.pack_propagate(False)

openstar = tk.Button(menubar, text="Open Star")
openstar.pack(side="left")

refresh = tk.Button(menubar, text="Refresh Root", command=lambda: reloadmain(root))
refresh.pack(side="left")

reloadpg = tk.Button(menubar, text="Reload", command=lambda: reload(currentframe))
reloadpg.pack(side="left")

startsng = tk.Button(menubar, text="Start Sng", command=lambda: initPlay(root))
startsng.pack(side="left")

endsong = tk.Button(menubar, text="End Sng", command=lambda: stopsng())
endsong.pack(side="left")

searchtab = tk.Frame(colorthing, width=1000, height=100, bg=data['color'])
searchtab.pack(pady=20)

backbtn = tk.Button(searchtab, text="Back", command=back)
backbtn.pack(side="left", pady=20)

forwardbtn = tk.Button(searchtab, text="Forward", command=forward)
forwardbtn.pack(side="right")

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
  </html>
  """
loadstates = ["Checking connection", "Searching", "Loading Page"]
loadindex = 0
loadtext = loadstates[0]
loadcount = 0

def resetLoader():
    global loadindex, loadcount
    loadindex = 0
    loadcount = 0

def updloadtext():
    global loadindex, loadtext, loadcount
    if loadcount >= 3:
        return
    loadtext = loadstates[loadindex]
    loadindex = (loadindex + 1) % len(loadstates)
    loadcount += 1
    if currentframe:
        currentframe.load_html(loading())
    root.after(500, updloadtext)
def loading():
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
      <title>{loadtext}</title>
      </head>
      <body>
      <hr>
      <h1>{loadtext}</h1>
      <hr>
      </body>
      </html>
    """
def loadnoworelse(url): # hehe now I can throw error at your face
    try:
        global loadcount
        global urlgoesbrr
        url = url.strip()
        wfmodules.secrets.checkurl(url, currentframe)
        urlcheck(url, root, colorthing, searchtab, tabbar, currentframe, homepage, data)
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
            wfmodules.secrets.checkurl(url, currentframe)
            urlcheck(url, root, colorthing, searchtab, tabbar, currentframe, homepage, data)
        if url.startswith(("http://")):
            if messagebox.askokcancel("Warning", "Http sites may be unsafe, continue with caution."):
                currentframe.load_website(url)
            else:
                currentframe.load_html(homepage())
                return
        resetLoader()
        updloadtext()
        ok = checkonline(url, data)
        if not ok: # I'm not ok --broken heart emoji-
            loadcount = 999
            currentframe.load_html(error_internet())
            return

        loadcount = 999
        currentframe.load_website(url)
    except Exception as e:
        currentframe.load_html(error_generic)
        log(e, logtype='error')

def load(url):
    threading.Thread(target=loadnoworelse, args=(url,), daemon=True).start()

def searchfor(urlthing=None):
    raw = urlthing or search.get().strip()

    if not raw:
        messagebox.showwarning(title="Error", message="Entry empty")
        return

    if raw.startswith(("http://", "https://")):
        load(raw)

    elif "." in raw:
        load("https://" + raw)

    else:
        query = urllib.parse.quote(raw)
        if data["wfsearch"] != "True":
            url = f"https://wiby.me/?q={query}" # Originally I wanted to use Duckduckgo but since this browser is dumb, it needed the og web so yea we lab wiby
            load(url)
        if data["wfsearch"] == "True":
            threading.Thread(target=lambda: clientSTART(query, currentframe, data), daemon=True).start()

openstar.config(command=lambda: openbook(root, searchfor, urlgoesbrr))
search.bind('<Return>', lambda event: searchfor())

def gohomefunc(): # Yea go home vro
    if currentframe:
        currentframe.load_html(homepage())
    search.delete(0, tk.END)
searchbutton.config(command=searchfor)
gohome.config(command=gohomefunc)
def updateurl():
    global urlgoesbrr
    if currentframe:
        try:
            urlgoesbrr = currentframe.current_url
        except:
            pass
    root.after(100, updateurl)
def closingwarn():
    urlname = currentframe.title
    if urlname != "Homepage":
        if messagebox.askokcancel("Unsaved Work", "You may have some unsaved work, are you sure you want to quit?"):
            root.destroy()
    else:
        root.destroy()

newtab()
updatetab()
updateurl()
dragndrop(root, lambda: currentframe)
historytrack(root, lambda: urlgoesbrr, data)
root.protocol("WM_DELETE_WINDOW", lambda: (obliterate(), closingwarn())) # Clear history.txt once user exits root
if data["custmodBETA"] == "True":
    root.after(3000, lambda: runCust(data, root, currentframe, menubar))
if data["devopts"] == "True":
    root.bind("<Button-2>", lambda event: pageOverview(currentframe, urlgoesbrr, root, search))
root.mainloop()


