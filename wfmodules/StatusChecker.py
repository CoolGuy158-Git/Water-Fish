"""
Status checker
---
Checks the status of any sites.
Returns Up or Down,
if Down shows why (e.g. 404).
Useful is user wants to know if a site's down or their connection is just slow.
"""
import requests
import tkinter as tk

user = {"User-Agent": "Mozilla/5.0"}
status = {
    # Success
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    # Client Errors
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    408: "Request Timeout",
    # Server Errors
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    # The rest are pretty rare and are mostly just errors anyway.
}
def CheckWebsiteStatus(root):
    app = tk.Toplevel(root)
    app.title("Status Checker")
    app.resizable(False, False)
    app.geometry("190x100")
    search = (tk.Entry(app))
    search.pack(side="left")
    btnofdoom = tk.Button(app, text="check", command=lambda:check())
    btnofdoom.pack(side="left")
    UpDown = tk.Label(app, text="Results will appear here.", wraplength=200)
    UpDown.place(y=55)

    def check():
        site = search.get().strip()
        if not site.startswith("http"):
            site = "https://" + site
        try:
            response = requests.get(site, timeout=10, headers=user)
            code = response.status_code
            UporDown = f"{site} : {code} ,  {status.get(code, 'DOWN')}"
        except (requests.exceptions.ConnectionError,requests.exceptions.Timeout):
            UporDown= site + " :" , "You're offline"
        UpDown.config(text=UporDown)

