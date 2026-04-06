"""
Welcome message
---
This is the Welcomer module for when it's the user's first time of using WaterFish
Its meant as a fun way to get started with WaterFish
It also gives the user a tour around the browser to make sure anyone who's just starting off knows the basics to waterfish.
It's a module that focuses on improving user experience.
"""
import tkinter as tk
from tkinterweb import HtmlFrame
welcome = """
<!DOCTYPE html>
<html>
<head>
<title>Welcome</title>
</head>
<body bgcolor='lightblue'>
<h1>Welcome</h1>
<hr>
<p>Have a look around!</p>
<p>We've got a simple yet nice interface, complete tabs etc.</p>
<p>Type /cmds (to customize) and /cmds fav (to change favorite url's)</p>
<p>For navigation, click the home button to return to the homepage</p>
<p>As for the tabs it's simple but effective click the '+' to add a tab and click '-' to remove a tab</p>
<p>If you have anymore questions, you can join the community on discord!</p>
<p>https://discord.gg/sHxdjFxuhk</p>
<p>We hope you'll love Water-Fish!</p>
<hr>
<font size=2>GNU3 License | CoolGuy158-Git | Water Fish Browser</font></p>
<hr>
</body>
</html>
"""
def start(root, data):
    """
    For those checking blame and wondering wtf is "Assistant".
    And probably asking 'ARE YOU PLANNING TO IMPLEMENT AI???'
    Don't worry I won't implement AI or at least Machine Learning.
    But it'd pretty cool if I added a Rule Based model.
    Don't worry it won't learn from user stuff and won't collect data.
    Rather it has a bunch of responses and stuff hardcoded.
    It's closer to Clippy than ChatGPT, heck it might even be considered Eliza.
    But yea, im still planning on how to implement this, if you have any questions.
    Join the Discord! Just ask about what the duck a Rule Based model is.
    And if you really, really don't want AI in anything, just say it on the server, it's not yet final if I'll add it.
    """
    def welcomeshow():
        if data.get("firstime") == "True":
            app = tk.Toplevel(root)
            app.title("Welcome")
            app.geometry("300x300")
            frame = HtmlFrame(app)
            frame.pack(fill="both", expand=True)
            frame.load_html(welcome)
            with open("system/settings.txt", "r") as f:
                lines = f.readlines()
            with open("system/settings.txt", "w") as f:
                for line in lines:
                    if line.startswith("firstime ="):
                        f.write("firstime = False\n")
                    else:
                        f.write(line)
        else:
            pass
    welcomeshow()





