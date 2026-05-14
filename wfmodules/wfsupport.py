"""
WfSupport
---
Checks if a page is supported by water-fish.

How does it check?
Well it has three category

- Supported (Contains little to no CSS, and no JS)
- Can load (Site might load but may look a bit weird, these are for sites with large CSS usage)
- Unsupported (Sites may not load, these are for sites that contain js.)

It works by getting the file of a site using requests, it then checks if any file that ends with .js exists then classifies it unsupported.
Then it checks CSS and if a css file is found classifies as can load.
Then checks HTML to find if there's any <script> tag, if so unsupported.
Then checks HTML again to find if any <style> (inline not counted) tag, if so counts how many lines it takes up.

It's pretty simple, and isn't perfect, but it usually works well.
"""
import tkinter as tk
from tkinterweb import HtmlFrame
import requests
from bs4 import BeautifulSoup
import html

def check(url):
    """
    Hierarchy/order
    ---
    check if supported first
    check if it can load then overwrite
    check if unsupported then overwrite
    """
    dahtml = requests.get(url).text
    soup = BeautifulSoup(dahtml, "lxml")
    styletext = ""
    WfSupportVar = "supported" # Just do supported first, then overwrite if other conditions are meet.
    reason = "doesn't use css, or js."
    if "google-analytics" in dahtml or "gtag" in dahtml or "analytics" in dahtml or "cloudflareinsights" in dahtml: # Overwrite reason
        WfSupportVar = "supported"
        reason = "Js usage is only in analytics"

    elif "<style" in dahtml: # Do can load first
        styles = soup.find_all("style")
        for style in styles:
            styletext += style.get_text() + "\n"
        if 30 < len(styletext):
            WfSupportVar = "can load"
            reason = "uses more than 30 lines of css"
        else:
            WfSupportVar = "supported"
            reason = "Only a little css is used, js is not used."
    elif "<link" in dahtml:
        WfSupportVar = "can load"
        reason = "most likely uses css"

    elif "<script" in dahtml: # Then unsupported, cuz unsupported is more concerning than can load lol.
        WfSupportVar = "unsupported"
        reason = "uses javascript"
    return "Support: " + WfSupportVar + "\nReason: " + reason + "\n" + "If you want to check it yourself here's the HTML: " + "\n" + "\n" + html.escape(dahtml)


def checkGUI(root):
    def getURL():
        try:
            url = entry.get()
            outputHTML = f"""
            <html>
            <body bgcolor="lightblue">
            <h1>Results</h1>
            <hr>
            <pre><code class="language-html">
            {check(url)}
            </code></pre>
            </body>
            </html>
            """
            output.load_html(outputHTML)
        except Exception as e:
            outputHTML = f"""
            <html>
            <body bgcolor="red">
            <h1>ERROR</h1>
            <hr>
            <p>{e}</p>
            </body>
            </html>
            """
            output.load_html(outputHTML)
    app = tk.Toplevel(root)
    app.title("WfSupport")
    app.geometry("400x300")
    entrycanva = tk.Canvas(app, bg='gray')
    entrycanva.pack(fill='x')
    entry = tk.Entry(entrycanva, bg='lightgray')
    entry.pack(side='left', fill='x', expand=True)
    enter = tk.Button(entrycanva, text="Check", command=getURL, bg='lightgray')
    enter.pack(side='left')

    output = HtmlFrame(app)
    output.pack(fill='both', expand=True)
    outputHTML = """
    <html>
    <body bgcolor="lightblue">
    <hr>
    <h1>Output is shown here</h1>
    <hr>
    </body>
    </html>
    """
    output.load_html(outputHTML)
