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
import html
from tkinter import messagebox
import threading
import sys
from wfmodules.Welcome import start # Planning to make a feature where users can create their own wfmodules
import wfmodules.secrets
from wfmodules.command import urlcheck
from wfmodules.checkonline import checkonline
from wfmodules.history import historytrack, obliterate
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
root.minsize(900, 620)
root.title("Water Fish")
root.iconbitmap("images/waterfish.ico")
root.configure(bg="#f4f7fb")
textchoice = ['The buggiest browser ever.', 'Is this even a browser?', '"I will feed you Ai." -Not my browser', 'Why are you using ts?', 'Magnificant browser', 'Slightly better than IE!', 'Fun fact this browser was made by a 13 yo!', 'Is using tkinterweb cheating?'] # Comment on my yt channel what other text I should add!

brand_bg = "#102542"
toolbar_bg = "#f4f7fb"
panel_bg = "#ffffff"
panel_alt = "#dfe7f2"
primary_btn = "#0f6ab4"
primary_hover = "#155d99"
danger_btn = "#b64949"
danger_hover = "#963d3d"
text_main = "#102542"
text_muted = "#5e7188"
tab_idle = "#d7e1ed"
tab_active = "#9ed0ff"
homepage_url = "waterfish://home"
settings_url = "waterfish://settings"
toggle_https_url = "waterfish://toggle-https-only"
allowed_remote_schemes = {"http", "https"}

if "https_only" not in data:
    data["https_only"] = "False"

def style_button(btn, bg, activebg=None, fg="#ffffff", padx=14, pady=8):
    btn.config(
        bg=bg,
        fg=fg,
        activebackground=activebg or bg,
        activeforeground=fg,
        bd=0,
        relief="flat",
        cursor="hand2",
        padx=padx,
        pady=pady,
        font=("Segoe UI", 10, "bold"),
    )

def set_status(text):
    status_var.set(text)

def is_https_only_enabled():
    return data.get("https_only", "False") == "True"

def save_setting(name, value):
    data[name] = value
    settings = {}
    try:
        with open("system/settings.txt", "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    key, current_value = line.strip().split("=", 1)
                    settings[key.strip()] = current_value.strip()
    except FileNotFoundError:
        pass
    settings[name] = value
    with open("system/settings.txt", "w", encoding="utf-8") as f:
        for key, current_value in settings.items():
            f.write(f"{key} = {current_value}\n")

def homepage():
    favorites = []
    with open("system/favorites.txt", "r") as f: # Yup NO MORE HARD CODING!!!
        for line in f:
            link, name = line.strip().split(", ")
            favorites.append((link, name))
    text = random.choice(textchoice) # Wait this actually worked?
    cards = "".join(
        f"""
        <a class="card" href="{html.escape(link, quote=True)}" target="_blank">
          <span class="card-title">{html.escape(name)}</span>
          <span class="card-url">{html.escape(link)}</span>
        </a>
        """
        for link, name in favorites
    )
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
        <title>Homepage</title>
        <style>
          body {{
            margin: 0;
            font-family: Segoe UI, Arial, sans-serif;
            background: linear-gradient(160deg, #eff6ff 0%, #d8e8f9 100%);
            color: #102542;
          }}
          .wrap {{
            max-width: 960px;
            margin: 0 auto;
            padding: 30px 24px 40px;
            text-align: center;
          }}
          .hero {{
            background: rgba(255, 255, 255, 0.88);
            border: 1px solid #c9d8e8;
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 18px 40px rgba(16, 37, 66, 0.12);
          }}
          h1 {{
            margin: 0;
            font-size: 40px;
            letter-spacing: 1px;
          }}
          h1 a {{
            color: #102542;
            text-decoration: none;
          }}
          p {{
            color: #4d627d;
          }}
          img {{
            margin: 16px 0 6px;
          }}
          .badge {{
            display: inline-block;
            background: #102542;
            color: #ffffff;
            padding: 8px 14px;
            border-radius: 999px;
            font-size: 13px;
            margin-top: 10px;
          }}
          .grid {{
            margin-top: 24px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 14px;
          }}
          .card {{
            display: block;
            text-align: left;
            background: #ffffff;
            border: 1px solid #c9d8e8;
            border-radius: 18px;
            padding: 16px;
            text-decoration: none;
            box-shadow: 0 10px 24px rgba(16, 37, 66, 0.08);
          }}
          .card-title {{
            display: block;
            color: #102542;
            font-weight: 700;
            margin-bottom: 6px;
          }}
          .card-url {{
            color: #4d627d;
            font-size: 12px;
            word-break: break-word;
          }}
          .footer {{
            margin-top: 18px;
            color: #4d627d;
            font-size: 15px;
          }}
        </style>
      </head>
      <body>
        <div class="wrap">
          <div class="hero">
            <h1><a href="info.html">WaterFish</a></h1>
            <p>One web, one world, one flow.</p>
            <img src="images/waterfish.png" width="220" height="220">
            <div class="badge">Lightweight experiment browser</div>
            <p><a href="{settings_url}">Open settings</a></p>
            <div class="grid">
              {cards}
            </div>
            <p class="footer">{html.escape(text)}</p>
          </div>
        </div>
      </body>
    </html>
    """
tabs = []
current = None
currentframe = None
tabbtnn = []
tabhistory = []
tabhistorypos = []
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
            tabbtn.config(bg=tab_active, fg=text_main) # High cholesterol
        else:
            tabbtn.config(bg=tab_idle, fg=text_main)
    set_status(f"Viewing tab {index + 1}")
    update_nav_buttons()

def update_nav_buttons():
    if current is None or current >= len(tabhistory):
        backbtn.config(state="disabled")
        forwardbtn.config(state="disabled")
        return
    pos = tabhistorypos[current]
    history = tabhistory[current]
    backbtn.config(state="normal" if pos > 0 else "disabled")
    forwardbtn.config(state="normal" if pos < len(history) - 1 else "disabled")

def record_navigation(index, url):
    if index is None or index >= len(tabhistory):
        return
    if not url or url == "None":
        return
    history = tabhistory[index]
    pos = tabhistorypos[index]
    if pos >= 0 and history[pos] == url:
        update_nav_buttons()
        return
    if pos < len(history) - 1:
        del history[pos + 1:]
    history.append(url)
    tabhistorypos[index] = len(history) - 1
    update_nav_buttons()

def load_internal_page(content, page_url):
    global urlgoesbrr
    if current is None or currentframe is None:
        return
    currentframe.load_html(content)
    urlgoesbrr = page_url
    record_navigation(current, page_url)
    update_nav_buttons()

def settings_page():
    https_state = "ON" if is_https_only_enabled() else "OFF"
    https_button = "Disable HTTPS only" if is_https_only_enabled() else "Enable HTTPS only"
    https_summary = (
        "Only HTTPS pages are allowed. Plain HTTP addresses will be upgraded when possible."
        if is_https_only_enabled()
        else "HTTP and HTTPS pages are both allowed."
    )
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
        <title>Settings</title>
        <style>
          body {{
            margin: 0;
            font-family: Segoe UI, Arial, sans-serif;
            background: linear-gradient(160deg, #eef5ff 0%, #d6e6f7 100%);
            color: #102542;
          }}
          .wrap {{
            max-width: 860px;
            margin: 0 auto;
            padding: 34px 24px 48px;
          }}
          .card {{
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid #c9d8e8;
            border-radius: 24px;
            padding: 28px;
            box-shadow: 0 18px 40px rgba(16, 37, 66, 0.12);
          }}
          .label {{
            display: inline-block;
            padding: 8px 12px;
            border-radius: 999px;
            background: #102542;
            color: #ffffff;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.6px;
            text-transform: uppercase;
          }}
          h1 {{
            margin: 14px 0 8px;
            font-size: 36px;
          }}
          p {{
            color: #4d627d;
            line-height: 1.6;
          }}
          .setting {{
            margin-top: 24px;
            border: 1px solid #d6e1ec;
            border-radius: 20px;
            padding: 20px;
            background: #f7fbff;
          }}
          .state {{
            display: inline-block;
            margin-top: 10px;
            padding: 8px 12px;
            border-radius: 999px;
            background: {"#102542" if is_https_only_enabled() else "#b64949"};
            color: #ffffff;
            font-weight: 700;
            font-size: 13px;
          }}
          .action {{
            display: inline-block;
            margin-top: 16px;
            padding: 12px 16px;
            border-radius: 12px;
            background: #0f6ab4;
            color: #ffffff;
            text-decoration: none;
            font-weight: 700;
          }}
          .secondary {{
            display: inline-block;
            margin-top: 16px;
            margin-left: 10px;
            color: #0f6ab4;
            text-decoration: none;
            font-weight: 700;
          }}
        </style>
      </head>
      <body>
        <div class="wrap">
          <div class="card">
            <span class="label">WaterFish Settings</span>
            <h1>Settings</h1>
            <p>Control how WaterFish handles browsing and safety features.</p>
            <div class="setting">
              <h2>Allow HTTPS only</h2>
              <p>{https_summary}</p>
              <span class="state">Current state: {https_state}</span>
              <br>
              <a class="action" href="{toggle_https_url}">{https_button}</a>
              <a class="secondary" href="{homepage_url}">Back to homepage</a>
            </div>
          </div>
        </div>
      </body>
    </html>
    """

def open_settings_page():
    load_internal_page(settings_page(), settings_url)
    set_status("Settings")

def handle_internal_navigation(url):
    normalized = url.strip().lower()
    if normalized == homepage_url:
        load_internal_page(homepage(), homepage_url)
        set_status("Homepage")
        return True
    if normalized == settings_url:
        open_settings_page()
        return True
    if normalized == toggle_https_url:
        next_value = "False" if is_https_only_enabled() else "True"
        save_setting("https_only", next_value)
        open_settings_page()
        return True
    return False

def handle_frame_link_click(url):
    if handle_internal_navigation(url):
        return
    load(url)

def newtab(url=None):
    global currentframe

    if len(tabs) >= maxtabs:
        messagebox.showinfo(title="Max tabs", message="Im to lazy to add a scroll thing") # Don't worry im planning to add it
        return
    frame = HtmlFrame(root, on_link_click=handle_frame_link_click)
    frame.enable_link_clicks = True
    if data["devopts"] == "True":
        frame.config(messages_enabled=True)
    else:
        pass


    tabs.append(frame)
    tabhistory.append([])
    tabhistorypos.append(-1)

    index = len(tabs) - 1
    addtab(index)

    currentframe = frame

    if url:
        frame.load_website(url)
    else:
        frame.load_html(homepage())
        tabhistory[index].append(homepage_url)
        tabhistorypos[index] = 0

    switch(index)
def addtab(index):
    btn = tk.Button(tabbar,text=f"Tab {index + 1}",command=lambda i=index: switch(i)
    )
    btn.pack(side="left", padx=(0, 8), pady=6)
    style_button(btn, tab_idle, tab_idle, fg=text_main, padx=12, pady=6)
    tabbtnn.append(btn)
def remtab(index): # removes your ex- i mean unused tabs
    global current

    if len(tabs) <= 1:
        return
    tabs[index].destroy()
    tabbtnn[index].destroy()

    tabs.pop(index)
    tabbtnn.pop(index)
    tabhistory.pop(index)
    tabhistorypos.pop(index)

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
            set_status(tabtitle)
    except:
        pass
    root.after(100, updatetab)
def back():
    global urlgoesbrr
    if current is None:
        return
    if tabhistorypos[current] <= 0:
        update_nav_buttons()
        return
    tabhistorypos[current] -= 1
    target = tabhistory[current][tabhistorypos[current]]
    urlgoesbrr = target
    if target == homepage_url:
        currentframe.load_html(homepage())
    elif target == settings_url:
        currentframe.load_html(settings_page())
    else:
        currentframe.load_website(target)
    set_status(f"Back to {target}")
    update_nav_buttons()

def forward():
    global urlgoesbrr
    if current is None:
        return
    if tabhistorypos[current] >= len(tabhistory[current]) - 1:
        update_nav_buttons()
        return
    tabhistorypos[current] += 1
    target = tabhistory[current][tabhistorypos[current]]
    urlgoesbrr = target
    if target == homepage_url:
        currentframe.load_html(homepage())
    elif target == settings_url:
        currentframe.load_html(settings_page())
    else:
        currentframe.load_website(target)
    set_status(f"Forward to {target}")
    update_nav_buttons()
colorthing = tk.Frame(root, bg=toolbar_bg, padx=18, pady=16)
colorthing.pack(fill='x')

brandbar = tk.Frame(colorthing, bg=brand_bg, padx=18, pady=14)
brandbar.pack(fill="x")
brand = tk.Label(
    brandbar,
    text="WaterFish",
    bg=brand_bg,
    fg="#ffffff",
    font=("Segoe UI", 18, "bold"),
)
brand.pack(side="left")
tagline = tk.Label(
    brandbar,
    text="small browser, cleaner surface",
    bg=brand_bg,
    fg="#c4d7eb",
    font=("Segoe UI", 10),
)
tagline.pack(side="left", padx=(12, 0))
status_var = tk.StringVar(value="Ready")
statuspill = tk.Label(
    brandbar,
    textvariable=status_var,
    bg="#1b3557",
    fg="#eef6ff",
    font=("Segoe UI", 10, "bold"),
    padx=12,
    pady=6,
)
statuspill.pack(side="right")

searchtab = tk.Frame(colorthing, bg=toolbar_bg, pady=14)
searchtab.pack(fill="x")

backbtn = tk.Button(searchtab, text="Back", command=back)
backbtn.pack(side="left", padx=(0, 8))
style_button(backbtn, primary_btn, primary_hover, fg="#ffffff")

forwardbtn = tk.Button(searchtab, text="Forward", command=forward)
forwardbtn.pack(side="left", padx=(0, 8))
style_button(forwardbtn, primary_btn, primary_hover, fg="#ffffff")

gohome = tk.Button(searchtab, text="Home")
gohome.pack(side='left', padx=(0, 12))
style_button(gohome, "#24476b", "#1d3854")

settingsbtn = tk.Button(searchtab, text="Settings", command=open_settings_page)
settingsbtn.pack(side='left', padx=(0, 12))
style_button(settingsbtn, "#2e5b87", "#274d72")

addresswrap = tk.Frame(searchtab, bg=panel_bg, bd=1, relief="solid")
addresswrap.pack(side='left', fill="x", expand=True)

search = tk.Entry(
    addresswrap,
    width=80,
    bd=0,
    relief="flat",
    font=("Segoe UI", 11),
    bg=panel_bg,
    fg=text_main,
    insertbackground=text_main,
)
search.pack(fill="x", padx=12, pady=10)

searchbutton = tk.Button(searchtab, width=10, text="Search")
searchbutton.pack(side='left', padx=(12, 0))
style_button(searchbutton, primary_btn, primary_hover)

tabbar = tk.Frame(colorthing, bg=toolbar_bg)
tabbar.pack(fill="x")

addbtn = tk.Button(tabbar, text="New Tab", command=newtab)
addbtn.pack(side="right", padx=(8, 0), pady=6)
style_button(addbtn, primary_btn, primary_hover, padx=12, pady=6)

rembtn = tk.Button(tabbar, text="Close Tab", command=lambda: remtab(current if current is not None else 0))
rembtn.pack(side="right", pady=6)
style_button(rembtn, danger_btn, danger_hover, padx=12, pady=6)

# TODO make an offline game!!!
# Although we have to find out how to make a game that's html only...unless someone helps me make a renderer which can be expanded upon to support css and js (wink)
def build_error_page(title, subtitle, attempted_url="", details="", suggestions=None):
    clean_url = html.escape(attempted_url or "Unknown")
    clean_details = html.escape(details or "No extra details were provided.")
    suggestion_items = "".join(
        f"<li>{html.escape(item)}</li>" for item in (suggestions or [])
    )
    return f"""
<!DOCTYPE html>
<html>
  <head>
  <title>{html.escape(title)}</title>
  <style>
    body {{
      margin: 0;
      background: linear-gradient(180deg, #f7fbff 0%, #dfeaf5 100%);
      font-family: Segoe UI, Arial, sans-serif;
      color: #102542;
    }}
    .shell {{
      max-width: 760px;
      margin: 54px auto;
      padding: 0 18px;
    }}
    .card {{
      background: #ffffff;
      border: 1px solid #c9d8e8;
      border-radius: 24px;
      padding: 30px;
      box-shadow: 0 20px 40px rgba(16, 37, 66, 0.12);
    }}
    .eyebrow {{
      display: inline-block;
      background: #102542;
      color: #ffffff;
      border-radius: 999px;
      padding: 7px 12px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.6px;
      text-transform: uppercase;
    }}
    h1 {{
      margin: 14px 0 10px;
      font-size: 34px;
    }}
    p {{
      color: #4d627d;
      line-height: 1.6;
    }}
    .panel {{
      margin-top: 18px;
      background: #f4f7fb;
      border: 1px solid #d6e1ec;
      border-radius: 18px;
      padding: 16px 18px;
    }}
    .label {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: #5e7188;
      margin-bottom: 8px;
      font-weight: 700;
    }}
    code {{
      display: block;
      white-space: pre-wrap;
      word-break: break-word;
      color: #102542;
      font-family: Consolas, monospace;
      font-size: 13px;
    }}
    ul {{
      margin: 10px 0 0;
      padding-left: 18px;
      color: #4d627d;
      line-height: 1.6;
    }}
    .footer {{
      margin-top: 18px;
      font-size: 14px;
    }}
    a {{
      color: #0f6ab4;
    }}
  </style>
  </head>
  <body>
    <div class="shell">
      <div class="card">
        <span class="eyebrow">WaterFish Error</span>
        <h1>{html.escape(title)}</h1>
        <p>{html.escape(subtitle)}</p>
        <div class="panel">
          <div class="label">Attempted Address</div>
          <code>{clean_url}</code>
        </div>
        <div class="panel">
          <div class="label">Details</div>
          <code>{clean_details}</code>
        </div>
        <div class="panel">
          <div class="label">What You Can Try</div>
          <ul>{suggestion_items}</ul>
        </div>
        <p class="footer">If the issue keeps happening, file an issue on the <a href='https://github.com/CoolGuy158-Git/Water-Fish'>official github repo</a>. Your feedback truly matters.</p>
      </div>
    </div>
  </body>
  </html>
  """

def error_internet_page(url):
    return build_error_page(
        "No Connection",
        "WaterFish could not confirm that the internet or the target page is reachable right now.",
        attempted_url=url,
        details="Connectivity checks failed for both common sites and the requested address.",
        suggestions=[
            "Check that your Wi-Fi or Ethernet connection is working.",
            "Try opening a simpler website or searching again in a few seconds.",
            "Use the Home button to return to the local start page.",
        ],
    )

def error_generic_page(url, error):
    return build_error_page(
        "Page Failed To Load",
        "Something went wrong while WaterFish was trying to open the page.",
        attempted_url=url,
        details=error or "Unknown failure.",
        suggestions=[
            "Double-check the address for typos.",
            "Try the page again, or go back to the homepage.",
            "Remember that WaterFish has limited CSS and JavaScript support on modern sites.",
        ],
    )

def security_block_page(url, title, details, suggestions=None):
    return build_error_page(
        title,
        "WaterFish blocked this navigation to keep the browsing session safer.",
        attempted_url=url,
        details=details,
        suggestions=suggestions or [
            "Go back to the homepage or settings page.",
            "Use an HTTPS address if the site supports it.",
            "Check the address for unsupported or unsafe URL schemes.",
        ],
    )

def apply_navigation_policy(url):
    parsed = urllib.parse.urlsplit(url)
    scheme = parsed.scheme.lower()

    if scheme not in allowed_remote_schemes:
        return None, security_block_page(
            url,
            "Blocked Address",
            f"The '{scheme or 'unknown'}' URL scheme is not allowed in WaterFish right now.",
            [
                "Use a normal web address with https:// or http://.",
                "Open internal pages only through WaterFish buttons or waterfish:// links.",
                "Return to the homepage if you are unsure what to do next.",
            ],
        ), "Blocked unsafe scheme"

    if is_https_only_enabled() and scheme != "https":
        return None, security_block_page(
            url,
            "HTTPS Only Mode",
            "This page was blocked because HTTPS-only mode is enabled and the address is not using HTTPS.",
            [
                "Try the same address with https:// instead of http://.",
                "Disable HTTPS-only mode in Settings if you intentionally want to allow plain HTTP.",
                "Return to the homepage and continue browsing from there.",
            ],
        ), "Blocked insecure HTTP page"

    return url, None, None

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
      <style>
        body {{
          margin: 0;
          background: linear-gradient(160deg, #eff6ff 0%, #d8e8f9 100%);
          font-family: Segoe UI, Arial, sans-serif;
          color: #102542;
        }}
        .card {{
          max-width: 640px;
          margin: 84px auto;
          background: rgba(255, 255, 255, 0.9);
          border: 1px solid #c9d8e8;
          border-radius: 24px;
          padding: 28px;
          text-align: center;
          box-shadow: 0 20px 40px rgba(16, 37, 66, 0.12);
        }}
        .pulse {{
          display: inline-block;
          width: 14px;
          height: 14px;
          border-radius: 50%;
          background: #0f6ab4;
          margin-bottom: 10px;
        }}
        p {{
          color: #4d627d;
        }}
      </style>
      </head>
      <body>
      <div class="card">
        <div class="pulse"></div>
        <h1>{loadtext}</h1>
        <p>WaterFish is working on it.</p>
      </div>
      </body>
      </html>
    """

def loadnoworelse(url): # hehe now I can throw error at your face
    try:
        global loadcount
        global urlgoesbrr
        url = url.strip()
        if handle_internal_navigation(url):
            return
        wfmodules.secrets.checkurl(url, currentframe)
        urlcheck(url, root, colorthing, searchtab, tabbar, currentframe, homepage)
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
            wfmodules.secrets.checkurl(url, currentframe)
            urlcheck(url, root, colorthing, searchtab, tabbar, currentframe, homepage)
        allowed_url, blocked_page, blocked_status = apply_navigation_policy(url)
        if not allowed_url:
            loadcount = 999
            set_status(blocked_status)
            currentframe.load_html(blocked_page)
            return
        url = allowed_url
        resetLoader()
        updloadtext()
        set_status(f"Opening {url}")
        ok = checkonline(url, data)
        if not ok: # I'm not ok --broken heart emoji-
            loadcount = 999
            set_status("Offline")
            currentframe.load_html(error_internet_page(url))
            return

        loadcount = 999
        set_status(f"Loaded {url}")
        currentframe.load_website(url)
    except Exception as e:
        set_status("Page failed to load")
        currentframe.load_html(error_generic_page(url, str(e)))
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
        load_internal_page(homepage(), homepage_url)
        set_status("Homepage")
    search.delete(0, tk.END)
searchbutton.config(command=searchfor)
gohome.config(command=gohomefunc)
def updateurl():
    global urlgoesbrr
    if currentframe:
        try:
            latest_url = currentframe.current_url
            if latest_url and latest_url.startswith("waterfish://") and latest_url != urlgoesbrr:
                urlgoesbrr = latest_url
                handle_internal_navigation(latest_url)
                root.after(100, updateurl)
                return
            if latest_url and latest_url != homepage_url and latest_url != urlgoesbrr:
                urlgoesbrr = latest_url
                record_navigation(current, latest_url)
        except:
            pass
    root.after(100, updateurl)
newtab()
updatetab()
updateurl()
historytrack(root, lambda: urlgoesbrr, data)
root.protocol("WM_DELETE_WINDOW", lambda: (obliterate(), root.destroy())) # Clear history.txt once user exits root
root.mainloop()
