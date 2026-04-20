"""
Stars modules
---
Allows user to bookmark specific url and access them via /cmds stars.
Useful when you want to save a url for future purposes.
"""
import tkinter as tk
def addbook(urlgoesbrr):
    bookfile = open("system/bookfile.txt", "a")
    bookfile.write(urlgoesbrr + "\n")
    bookfile.close()
def removebook(urlgoesbrr):
    with open("system/bookfile.txt", "r") as file:
        content = file.read()
    content = content.replace(urlgoesbrr + "\n", "")
    with open("system/bookfile.txt", "w") as file:
        file.write(content)
def openbook(root, searchfor, urlgoesbrr):
    """
    Opens new toplevel that lets you
    add stars, remove stars, and load stars.
    Unfortunately I wasn't able to make it so that it updates and shows newly added or removed stars.
    Why?
    I have to be honest,
    I'm too lazy, and too dumb.
    Also why's this one added to menu bar meanwhile customize and fav are not?
    3 words,
    Bad design choice.
    Don't worry may still add someday,
    take note 'MAY'.
    """
    with open("system/bookfile.txt", "r") as file:
        content = file.read()

    app = tk.Toplevel(root)
    app.iconbitmap("images/waterfish.ico")
    app.title("Stars")
    app.geometry("400x200")
    app.resizable(False, False)
    staropt = tk.Frame(app,bg='blue')
    staropt.pack(fill="x")
    addstar = tk.Button(staropt, text="Add Star", command=lambda u=urlgoesbrr: addbook(u))
    addstar.pack(side="left")
    remstar = tk.Button(staropt, text="Remove Star", command=lambda u=urlgoesbrr: removebook(u))
    remstar.pack(side="left")
    canvas = tk.Canvas(app, bg="#1a0033", highlightthickness=0)
    scrollbar = tk.Scrollbar(app, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    frame = tk.Frame(canvas, bg="#1a0033")
    canvas.create_window((0, 0), window=frame, anchor="nw", width=380)
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    label = tk.Label(frame, text="Stars", font=('Arial', 30), bg="#1a0033", fg="#FFD700")
    label.pack()
    info = tk.Label(frame, text="Close and reopen to refresh bookmarks.", bg='#1a0033', fg='white') # Sorry dawg
    info.pack()

    buttons = []

    for item in content.splitlines():
        if item.strip():
            btn = tk.Button(frame,text=item,bg='#FFD700',fg='#1a0033',command=lambda x=item: searchfor(x))
            btn.pack(pady=5)
            buttons.append(btn)