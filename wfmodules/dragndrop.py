"""
Drag N Drop
---
WfModule that lets you drag and drop HTML files to the window.
Useful if user wants to create a webpage and view it via Water-Fish.
"""
from tkinterdnd2 import DND_FILES # My first time using this it's pretty cool ngl
from tkinter import messagebox
from wfmodules.mdrenderer import rendermd

def dragndrop(root, currentframe):
    def getpath(event):
        file = event.data.strip("{}")
        if file.lower().endswith(".md"):
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            rendermd(currentframe(), content, file)
            return
        elif not file.lower().endswith((".html", "htm")):
            messagebox.showerror("Error", "Unsupported file type")
            return
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        currentframe().load_html(content)
    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", getpath)