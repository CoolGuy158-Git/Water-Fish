"""
Html Editor
---
A simple text editor where you can create html files to be shown directly in water-fish.
You can also save the html file and load it.

Just a small addition to the environment, also made this cuz I was bored like everything on the browser.
"""
import tkinter as tk
import tkinter.filedialog as filedialog

def Editor(root, currentframe):
    live = False
    def run():
        currentframe.load_html(codeEntry.get("1.0", "end"))
    def save():
        filename = filedialog.asksaveasfile(mode="w", defaultextension=".html")
        if filename: # I'm not sure if you need to do this but ehh my IDE said so
            filename = filename.name
            with open(filename, mode="w") as file:
                file.write(codeEntry.get("1.0", "end"))
    def openFile():
        filename = filedialog.askopenfilename(initialdir="/", title="Open File")
        if filename:
            with open(filename, mode="r") as file:
                code = file.read()
                codeEntry.delete("1.0", "end")
                codeEntry.insert("end", code)
    def toggleLive():
        nonlocal live

        live = not live

        if live:
            codeEntry.bind("<KeyRelease>", lambda event: currentframe.load_html(codeEntry.get("1.0", "end")))
        else:
            codeEntry.unbind("<KeyRelease>")
    app = tk.Toplevel(root, bg="gray", relief="sunken", borderwidth=8)
    app.title("Water-Editor")
    app.geometry("800x600")
    app.resizable(False, False)
    codeEntry = tk.Text(app, bg="#1d1d26", fg="lightgreen", font=("Arial", 12), relief="raised", borderwidth=8, height=30)
    codeEntry.pack(side="top", fill="x", expand=True)

    menuBar = tk.Canvas(app, bg="#30353c", height="100")
    menuBar.pack(side="bottom", fill="x", expand=True)

    runButton = tk.Button(menuBar, text="Run", command=lambda: run(), bg="#427a47", relief="raised")
    runButton.pack(side="left")

    saveButton = tk.Button(menuBar, text="Save", command=lambda: save(), bg="#c2c4ca", relief="raised")
    saveButton.pack(side="left")

    openButton = tk.Button(menuBar, text="Open", command=lambda: openFile(), bg="#c2c4ca", relief="raised")
    openButton.pack(side="left")

    livePreviewButton = tk.Button(menuBar, text="Live", command=lambda: toggleLive(), bg="#c2c4ca", relief="raised")
    livePreviewButton.pack(side="left")