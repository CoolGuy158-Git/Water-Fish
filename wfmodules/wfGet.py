"""
Water-Fish get
---
WfModule that lets user install things from the web to their desktops.
Wf first verifies whether the file is safe or not.
( If executable warns user )

It is useful if users wants to get files online as currently wf just crashes when a download link is clicked.
"""

from urllib.parse import urlparse
import requests
from tkinter import filedialog, messagebox
import os



def checkLink(currentframe, url, data):
    """
    This function checks if the link is binary or nah.
    It does it by defining 2 extensions types.
    Normal (text)
    Binary (binary obviously)
    Then it calls the download func for either just download or download binary.
    """
    if data["devopts"] == "True":
        print("wfget sees: ", url)
    path = urlparse(url).path.lower()
    if path.endswith("/"):
        path = path[:-1]

    filename = path.split("/")[-1]
    if "." not in filename:
        if data["devopts"] == "True":
            print(f" {url} isn't a download link.")
        return
    fileExtensions = [
    ".html",
    ".htm",
    ".css",
    ".js",
    ".json",
    ".xml",
    ".txt",
    ".csv",
    ".md",
    ".py",
    ".java",
    ".cpp",
    ".c",
    ".cs",
    ".php",
    ".go",
    ".ts",
    ".rs",
    ".bat",
    ".cmd",
    ".sh",
    ".log"
    ]
    BinaryFileExtensions = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".svg",
    ".bmp",
    ".ico",
    ".mp4",
    ".webm",
    ".mov",
    ".avi",
    ".mkv",
    ".mp3",
    ".wav",
    ".ogg",
    ".flac",
    ".aac",
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".zip",
    ".rar",
    ".7z",
    ".tar",
    ".gz",
    ".exe",
    ".msi",
    ".com",
    ".scr",
    ".bin",
    ".run",
    ".appimage",
    ".dmg",
    ".pkg",
    ".img",
    ".iso",
    ".rom",
    ".bak"
    ]


    if any(url.endswith(ext) for ext in fileExtensions):
        if data["devopts"] == "True":
            print(f" {url} is a download link.")
        fileName = urlparse(url).path.split("/")[-1]
        rrr = requests.get(url, stream=True)
        size = rrr.headers.get("Content-Length")
        text = rrr.text # Normal files get their text downloaded temporarily (If user hasn't picked yes or no) so that if header Content-Length doesn't exist size can still be shown! Not true for binaries though.
        if size is None:
            size = len(text.encode("utf-8"))
        confirmation = messagebox.askyesno("Download?", f"Do you want to download {fileName} ({size} bytes)?")
        if confirmation:
            Download(fileName, currentframe, text)
        else:
            currentframe.load_html(
                f"""
                    <html>
                    <head>
                    <title>Abort</title>
                    </head>
                    <body bgcolor="lightblue">
                    <hr>
                    <h1>Aborted download {fileName}</h1>
                    <hr>
                    <p>You can now return to homepage</p>
                    </body>
                    </html>
                    """
            )
        return
    if any(url.endswith(ext) for ext in BinaryFileExtensions):
        if data["devopts"] == "True":
            print(f" {url} isn a download link.")
        fileName = urlparse(url).path.split("/")[-1]
        rrr = requests.get(url, stream=True)
        size = rrr.headers.get("Content-Length")
        confirmation = messagebox.askyesno("Download?", f"Do you want to download {fileName} ({size} bytes)?")
        if confirmation:
            # Extra user confirmation cuz its an executable
            MoreConfirmation = messagebox.askyesno("Are you sure?", "The file is in binary therefore it may be an executable, please confirm it is from a trusted source.")
            if MoreConfirmation:
                DownloadExecutable(fileName, rrr, currentframe)
            else:
                currentframe.load_html(
                    f"""
                        <html>
                        <head>
                        <title>Abort</title>
                        </head>
                        <body bgcolor="lightblue">
                        <hr>
                        <h1>Aborted download {fileName}</h1>
                        <hr>
                        <p>You can now return to homepage</p>
                        </body>
                        </html>
                        """
                )
        return
    if data["devopts"] == "True":
        print(f" {url} isn't a download link.")
    return

def Download(fileName,currentframe, text):
        folderToSave = filedialog.askdirectory()

        PATHWAYTOTARTARUS = os.path.join(folderToSave, fileName) # GD REFERENCEEEEE
        with open(PATHWAYTOTARTARUS, "w", encoding="utf-8") as f:
            f.write(text)
        currentframe.load_html(
            f"""
                <html>
                <head>
                <title>Success</title>
                </head>
                <body bgcolor="lightblue">
                <hr>
                <h1>Successfully downloaded {fileName}</h1>
                <hr>
                <p>You can now return to homepage</p>
                </body>
                </html>
                """
        )

def DownloadExecutable(fileName, rrr, currentframe):
    folderToSave = filedialog.askdirectory()
    PATHWAYTOTARTARUS = os.path.join(folderToSave, fileName)
    with open(PATHWAYTOTARTARUS, "wb") as f:
        f.write(rrr.content)
    currentframe.load_html(
        f"""
        <html>
        <head>
        <title>Success</title>
        </head>
        <body bgcolor="lightblue">
        <hr>
        <h1>Successfully downloaded {fileName}</h1>
        <hr>
        <p>You can now return to homepage</p>
        </body>
        </html>
        """
    )

