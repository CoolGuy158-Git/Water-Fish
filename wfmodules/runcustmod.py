"""
Runner for custom modules
---
A wfmodule that lets users run custom modules.
Has safety checks etc.
Custom-modules are stored as .wfmd files.

Expected syntax:
    name: insert-name
    consent: "
    this one is multiline basically the terms and agreement
    "
    license: insert-license
    repository: insert-repository (GitHub, GitLab, code-berg etc.)
    code: "
    # e.g.
    # This will make the browser open the example domain
    url = "https://example.com"
    # the simple interpreter shall only do line to line execution no multiline.
    "
    All the '"' are supposed to be three but if I do that here in the multiline comment it breaks python.

Users are expected to read the source code, as such the browser will not run any non .wfmd files
Read more in custmod.md
"""

import os
import tkinter as tk

with open("system/acceptedcust.txt") as r:
    accepted = r.read().splitlines()

def runCust(data, root, currentframe, menubar): # Yay! Turtle Case!!!
    def getFile(data):
        """
        This function grabs all the files from custmod dir
        """
        file = [
            f for f in os.listdir("custmod")
            if os.path.isfile(os.path.join("custmod", f)) and f not in accepted
        ]
        if data['devopts'] == 'True':
            print(file)
        return file

    def parseFile():
        """
        Parses the file so that it gets the name, consent, license, repository, and code
        """
        for file in getFile(data):
            path = os.path.join("custmod", file)
            name = None
            multiline = None
            consent = []
            code = []
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("name:"):
                        name = line.split(":", 1)[1].strip()
                    elif line.startswith("consent:"):
                        multiline = "consent"
                        continue
                    elif line.startswith("license:"):
                        license = line.split(":", 1)[1].strip()
                    elif line.startswith("repository:"):
                        repository = line.split(":", 1)[1].strip()
                    # Code and consent are both multiline
                    # Lowkey ts took me long to code
                    elif line.startswith("code:"):
                        multiline = "code"
                        continue
                    if multiline == "consent":
                        if line.strip() == '"':
                            multiline = None
                        else:
                            consent.append(line)
                    elif multiline == "code":
                        if line.strip() == '"':
                            multiline = None
                        else:
                            code.append(line)

                if data['devopts'] == 'True' and name:
                    print("name:", name)
                if data['devopts'] == 'True' and consent:
                    print("consent:", consent)
                if data['devopts'] == 'True' and license:
                    print("license:", license)
                if data['devopts'] == 'True' and repository:
                    print("repository:", repository)
                if data['devopts'] == 'True' and code:
                    print("code:", code)
                return name, consent, license, repository, code
    def consentShow(root, file):
        """
        Shows a popup contaning info about the module.
        It makes sure the user has power over deciding which modules runs on his browser.
        """
        # License pops up twice idk why
        name, consent, license, repository, code = parseFile()
        consent = "".join(consent).strip("{}")
        up = tk.Toplevel(root)
        up.title(name)
        up.resizable(False, False)
        up.geometry("400x350")
        consentl = tk.Label(up, text=consent)
        consentl.pack()
        wfmessage = tk.Label(up, text="Before clicking accept make sure to read the source code\nAfter clickng accept make sure to resfresh root")
        wfmessage.pack()
        licensel = tk.Label(up, text=license)
        licensel.pack()
        repositoryl = tk.Label(up, text=repository)
        repositoryl.pack()
        def agree():
            up.destroy()
            f = open("system/acceptedcust.txt", "a")
            f.write(file + "\n")
            f.close()
            run(currentframe, menubar)
        agreebtn = tk.Button(up, text="I agree", bg='green', fg='white', command=agree)
        agreebtn.pack()
        disagreebtn = tk.Button(up, text="I disagree", bg='red', fg='white', command=lambda: up.destroy()) # TODO: make a function that places any modules which the user didn't accept to a seperate dir
        disagreebtn.pack()

    def run(currentframe, menubar):
        """
        This part reads the code and actually runs it as the name would suggest,
        in fact why am I making these comments the names already tell everything,
        but ehh.
        """
        buttons = {}
        for file in os.listdir("custmod"):
            if file in accepted:
                path = os.path.join("custmod", file)
                with open(path) as f:
                    for line in f:
                        # Currently only have like 2 commands not including the comment but yea its still in beta so imma add more someday
                        if line.startswith("url ="):
                            currentframe.load_url(line.split("=", 1)[1].strip().strip('"'))
                        elif line.startswith("#"):
                            pass
                        elif line.startswith("btn ="):
                            partsname = line.split('"')
                            url = partsname[1]
                            name = partsname[3]
                            for widget in menubar.winfo_children():
                                if isinstance(widget, tk.Button) and widget.cget("text") == name:
                                    widget.destroy() # Hehe
                            buttons[name] = tk.Button(menubar, text=name, command=lambda url=url: currentframe.load_url(url))
                            buttons[name].pack(side='left')

    for file in os.listdir("custmod"): # This checks if a file is accepted or not so yea
        if file in accepted:
            parseFile()
            run(currentframe, menubar)
        else:
            consentShow(root, file)

