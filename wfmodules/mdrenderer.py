"""
Simple Markdown renderer
---
Markdown renderer for Water-Fish.
Used when user wants to create simple markdown files and check what it looks like via Water-Fish.
It can however, only render the following stuff:
    Bold **text**
    Italic *text*
    headers eg:
        # header 1
        ## header 2
        and so till header 6
    horizontal rule ---
    br are just spaces
    and the rest of the stuff is just turned to a <p>text</p> because im lazy to add those complex stuff hehe.
It's probably closer to a compiler (markdown -> html) though.
"""

import re

def rendermd(currentframe, content, file):
    output = []
    for lines in content.splitlines():
        lines = lines.lstrip()
        # Remove the cute little \, there's probably a better way to do this but for now, this is fine.
        lines = lines.replace("\\#", "#")
        lines = lines.replace("\\---", "---")
        lines = lines.replace("\\*", "*")

        # Why's i, and b not in if/elif? So that even if you do ## *Italic header 2* it still works.
        lines = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", lines)
        lines = re.sub(r"\*(.*?)\*", r"<i>\1</i>", lines)
        if lines.startswith("# "):
            text = lines[2:]
            lines = "<h1>" + text + "</h1>"
        elif lines.startswith("## "):
            text = lines[3:]
            lines = "<h2>" + text + "</h2>"
        elif lines.startswith("### "):
            text = lines[4:]
            lines = "<h3>" + text + "</h3>"
        elif lines.startswith("#### "):
            text = lines[5:]
            lines = "<h4>" + text + "</h4>"
        elif lines.startswith("##### "):
            text = lines[6:]
            lines = "<h5>" + text + "</h5>"
        elif lines.startswith("###### "):
            text = lines[7:]
            lines = "<h6>" + text + "</h6>"
        elif lines.strip() == "---":
            lines = "<hr>"
        elif lines.strip() == "":
            lines = "<br>"
        else:
            lines = "<p>" + lines + "</p>"
        # Just add more stuff later for now this is pretty good

        output.append(lines)
    # The final page (Not sure if it's needed but better safe than sorry)
    finpage = f""" 
    <!DOCTYPE html>
    <html>
    <head>
    <title>{file}</title>
    </head>
    <body>
    """ + "\n".join(output) + """
    </body>
    </html>
    """
    currentframe.load_html(finpage)
