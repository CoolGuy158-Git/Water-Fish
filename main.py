import tkinter as tk
from tkinterweb import HtmlFrame
import urllib.parse

visits = {}

root = tk.Tk()
root.geometry("1000x700")
root.title("Water Fish")
root.iconbitmap("waterfish.ico")
colorthing = tk.Frame(root, width=1000, height=200, bg="gray")
colorthing.pack(fill='x')
searchtab = tk.Frame(colorthing, width=1000, height=100, bg="gray")
searchtab.pack(pady=20)

gohome = tk.Button(searchtab, text="Home")
gohome.pack(side='left', padx=(0,5))

search = tk.Entry(searchtab, width=80)
search.pack(side='left')

searchbutton = tk.Button(searchtab, width=10, text="Search")
searchbutton.pack(side='left')

homepage = """
<!DOCTYPE html>
<html>
  <head>
    <title>WaterFish</title>
  </head>
  <body bgcolor="lightblue">
  <center>
    <h1><a href=info.html>WaterFish</a></h1>
    <hr>
    <img src=waterfish.png width=200 height=200>
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
    <h3>WaterFish is a lightweight very barebones web browser made in python</h3>
    <h3>Unfortunately it only minimally or doesn't even support css/js which means most modern pages won't open</h3>
    <h3>This project is not anything serious I was just playing around with the idea of making a browser after firefox got into that controversy</h3>
    <h3>Oh btw the search engine used is in <a href="https://wiby.me/">here</a></h3>
  </center>
  </body>
</html>"""

webframe = HtmlFrame(root)
webframe.pack(fill='both', expand=True)
webframe.load_html(homepage)
def searchfor():
    query = urllib.parse.quote(search.get())
    url = f"https://wiby.me/?q={query}"
    webframe.load_website(url)

def gohomefunc():
    webframe.load_html(homepage)
    search.delete(0, tk.END)

searchbutton.config(command=searchfor)
gohome.config(command=gohomefunc)
root.mainloop()
