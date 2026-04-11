"""
Command Palette
---
Lets you type certain commands in the search bar.
Used for opening customize.
Opening Favorites.
And more in the future!
Very close to secrets except that it doesn't troll you.
"""

import urllib.parse
import subprocess
import platform
from wfmodules.Remora import initRemora
def urlcheck(url, root, colorthing, searchtab, tabbar, currentframe, homepage, data):
    url = urllib.parse.unquote(url).lower()
    url = " ".join(url.split())

    if "/cmds customize" in url:
        def refreshsettings():  # This function triggers whenever the user exits the notepad, thus updating all the settings, well all except for hightabcol you have to open a new tab for that because well tabbtn is a local variable
            global data
            try:
                colorthing.config(bg=data['color'])
                searchtab.config(bg=data['color'])
                tabbar.config(bg=data['tabcol'])

            except Exception as e:
                print(e)
        def checkditor(proc):
            if proc.poll() is None:
                root.after(500, lambda: checkditor(proc))
            else:
                refreshsettings()
        def customize():  # Originally I wanted a tkinter top level to appear so you can edit the settings, but I was too lazy so enjoy editing settings via notepad hehe
            if platform.system() == "Windows":
                proc = subprocess.Popen(["notepad.exe", "system/settings.txt"])
            elif platform.system() == "Darwin":
                proc = subprocess.Popen(["open", "system/settings.txt"])
            else:
                proc = subprocess.Popen(["xdg-open", "settings.txt"])
            checkditor(proc)
        customize()
    if "/cmds fav" in url:
        def refreshsettings():
            try:
                currentframe.load_html(homepage())
            except Exception as e:
                print(e)
        def checkditor(proc):
            if proc.poll() is None:
                root.after(500, lambda: checkditor(proc))
            else:
                refreshsettings()
        def customize():
            if platform.system() == "Windows":
                proc = subprocess.Popen(["notepad.exe", "system/favorites.txt"])
            elif platform.system() == "Darwin":
                proc = subprocess.Popen(["open", "system/favorites.txt"])
            else:
                proc = subprocess.Popen(["xdg-open", "favorites.txt"])
            checkditor(proc)
        customize()
    if "/cmds remora" in url:
        initRemora(root, data)

