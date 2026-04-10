"""
History Module
---
Keeps track oh history (All the url's you've been in on the browser)
Helps with navigation and stuff.
History automatically gets deleted after user exits main.
"""

import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlast = "" # last url like how urlast in her heart

def historytrack(root, urlgoesbrr, data):
    global urlast
    curl = urlgoesbrr() # Current url
    if curl and curl != "None" and curl != urlast:
        urlast = curl
        if data['devopts'] == 'True':
            print("saving: ", curl, " to history")
        path = os.path.join(basedir, "system", "history.txt")
        with open(path, "a", encoding="utf-8") as f:
            f.write(curl + "\n")

    root.after(500, lambda: historytrack(root, urlgoesbrr, data))

def obliterate(): # Planning to make it so that if user clicks ctrl + del + h it deletes history.
    try:
        path = os.path.join(basedir, "system", "history.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write("")
    except:
        pass
