"""
Overview
---
Simple Overview module that gives infos about a page.
Shows wf users the page title, page type(if available), search query, url, and HTML code.
Useful for devs who want to see what their favorite webpage's code looks like.
Can onl be accessed if devopts is turned on.
"""

import requests
import tkinter as tk

def pageOverview(currentframe, urlgoesbrr, root, search):
    pageTitle = currentframe.title

    # This thing just matches a title and see if it fits a pageType category, half the time it doesn't but ehh
    pageType = "Unknown"
    if "dictionary" in pageTitle.lower() or "school" in pageTitle.lower() or "education" in pageTitle.lower():
        pageType = "Education"
    elif "homepage" in pageTitle.lower() or "waterfish" in pageTitle.lower():
        pageType = "Water-Fish"
    elif "how to" in pageTitle.lower() or "diy" in pageTitle.lower() or "do it yourself" in pageTitle.lower():
        pageType = "DIY"
    elif "news" in pageTitle.lower() or "breaking" in pageTitle.lower():
        pageType = "News"
    elif "game" in pageTitle.lower() or "play" in pageTitle.lower():
        pageType = "Gaming"
    elif "shop" in pageTitle.lower() or "buy" in pageTitle.lower() or "store" in pageTitle.lower():
        pageType = "Shopping"
    elif "login" in pageTitle.lower() or "sign in" in pageTitle.lower():
        pageType = "Login"
    elif "wiki" in pageTitle.lower() or "encyclopedia" in pageTitle.lower():
        pageType = "Reference"
    elif "video" in pageTitle.lower() or "watch" in pageTitle.lower():
        pageType = "Video"
    else:
        pass
    searchQuery = search.get().strip().lower() or "None"
    pageUrl = urlgoesbrr or "None"
    try:
        htmlCode = requests.get(urlgoesbrr).text
    except requests.exceptions.MissingSchema:
        htmlCode = "Viewing a file or invalid url"
    def copyHTML():
        overview.clipboard_clear()
        overview.clipboard_append(htmlCode)
    overview = tk.Toplevel(root)
    overview.title(pageTitle)
    overview.geometry("400x500")
    overview.resizable(False, False)
    title = tk.Label(overview, text="Page Title: " + pageTitle, font=("Arial", 20), wraplength=400)
    title.pack(side="top")
    line = tk.Label(overview, text="_____________________________________", font=("Arial", 10)) # LINE
    line.pack(side="top")
    query = tk.Label(overview, text="Search Query: " + searchQuery, font=("Arial", 10), wraplength=380)
    query.pack(side="top")
    url = tk.Label(overview, text="Page Url: " + pageUrl, font=("Arial", 10), wraplength=380)
    url.pack(side="top")
    type = tk.Label(overview, text="Page Type: " + pageType, font=("Arial", 10))
    type.pack(side="top")
    code = tk.Label(overview, text="Page Code: ", font=("Arial", 10))
    code.pack(side="top")

    copyButton = tk.Button(overview, text="Copy HTML", command=copyHTML)
    copyButton.pack(side="top")

    # Ugh why do I have to do all this just for a scroll bar
    canvas = tk.Canvas(overview, bg="gray")
    scrollbar = tk.Scrollbar(canvas, command=canvas.yview)
    scrollFrame = tk.Frame(overview, bg="gray")
    scrollFrame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollFrame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="top", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    html = tk.Label(scrollFrame,text= htmlCode,font=("Arial", 10),wraplength=380,bg="gray",justify="left")
    html.pack(side="top")

    # Since devopts is True just print it ig
    print()
    print("Page Title: " + pageTitle)
    print("Page Type: " + pageType)
    print("Search Query: " + searchQuery)
    print("Page Url: " + pageUrl)
    print()
    print(htmlCode)