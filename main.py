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
import requests
import random
from tkinter import messagebox
import subprocess
import platform
import threading
import os
import sys
from wfmodules.Welcome import start # Planning to make a feature where users can create their own wfmodules

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

root = tk.Tk()
start(root, data)
root.geometry("1000x700")
root.title("Water Fish")
root.iconbitmap("images/waterfish.ico")
textchoice = ['The buggiest browser ever.', 'Is this even a browser?', '"I will feed you Ai." -Not my browser', 'Why are you using ts?', 'Magnificant browser', 'Slightly better than IE!', 'Fun fact this browser was made by a 13 yo!', 'Is using tkinterweb cheating?'] # Comment on my yt channel what other text I should add!
def homepage():
    text = random.choice(textchoice) # Wait this actually worked?
    return f"""
<!DOCTYPE html>
<html>
  <head>
    <title>Homepage</title>
  </head>
  <body bgcolor="lightblue">
  <center>
    <h1><a href=info.html>WaterFish</a></h1>
    <hr>
    <img src=images/waterfish.png width=300 height=300>
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
# I may need to add something that lets the user pick their own fav websites to add here
tabs = []
current = None
currentframe = None
tabbtnn = []
maxtabs = 20

def switch(index): # This function handles tab switching as well as highlighting current tab
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
    btn = tk.Button(tabbar,text=f"Tab {index + 1}",command=lambda i=index: switch(i)
    )
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

def customize(): # Originally I wanted a tkinter top level to appear so you can edit the settings, but I was too lazy so enjoy editing settings via notepad hehe
    if platform.system() == "Windows":
        proc = subprocess.Popen(["notepad.exe", "system/settings.txt"])
    elif platform.system() == "Darwin":
        proc = subprocess.Popen(["open", "system/settings.txt"])
    else:
        proc = subprocess.Popen(["xdg-open", "settings.txt"])
    checkditor(proc)


def checkditor(proc):
    if proc.poll() is None:
        root.after(500, lambda: checkditor(proc))
    else:
        refreshsettings()


def refreshsettings(): # This function triggers whenever the user exits the notepad, thus updating all the settings, well all except for hightabcol you have to open a new tab for that because well tabbtn is a local variable
    global data
    try:
        newdata = {}
        with open('system/settings.txt', 'r') as file:
            for line in file:
                if '=' in line:
                    name, value = line.strip().split('=')
                    newdata[name.strip()] = value.strip()

        if newdata.get("devopts") == data.get("devopts"):
            pass
        else:
            useropt = messagebox.showinfo(title="Settings", message=f"Restart browser to see changes made in DevOpts")
            if useropt == "ok":
                python = sys.executable
                os.execl(python, python, *sys.argv)
        data = newdata
        colorthing.config(bg=data['color'])
        searchtab.config(bg=data['color'])
        tabbar.config(bg=data['tabcol'])

    except Exception as e:
        print(e)

def imalwaysright(event): # idc what you say this is the best func name, ok but really though this activates customize
    customize()

colorthing = tk.Frame(root, width=1000, height=100, bg=data['color'])
colorthing.pack(fill='x')
colorthing.pack_propagate(False)
colorthing.bind("<Button-3>", imalwaysright)
searchtab = tk.Frame(colorthing, width=1000, height=100, bg=data['color'])
searchtab.pack(pady=20)

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
# Although we have to find out how to make a game that's html only...unless someone helps me make a renderer which can be expanded upon to support css and js (wink)
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
  </html>
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

def checkonline(url):
    try:
        requests.get(url, timeout=3)
        return True
    except:
        return False
def loadnoworelse(url): # hehe now I can throw error at your face
    try:
        global loadcount
        url = url.strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        resetLoader()
        updloadtext()
        ok = checkonline(url)
        if not ok:
            currentframe.load_html(error_internet)
            return

        loadcount = 999
        currentframe.load_website(url)
    except Exception as e:
        currentframe.load_html(error_generic)
        print(e)

def load(url):
    threading.Thread(target=loadnoworelse, args=(url,), daemon=True).start()
def searchfor():
    raw = search.get().strip()

    if not raw:
        messagebox.showwarning(title="Error", message="Entry empty")
        return

    if raw.startswith(("http://", "https://")):
        load(raw)

    elif "." in raw:
        load("https://" + raw)

    else:
        query = urllib.parse.quote(raw)
        url = f"https://wiby.me/?q={query}" # Originally I wanted to use Duckduckgo but since this browser is dumb, it needed the og web so yea we lab wiby
        load(url)

search.bind('<Return>', lambda event: searchfor())

def gohomefunc(): # Yea go home vro
    if currentframe:
        currentframe.load_html(homepage())
    search.delete(0, tk.END)
searchbutton.config(command=searchfor)
gohome.config(command=gohomefunc)
newtab()
updatetab()
root.mainloop()
