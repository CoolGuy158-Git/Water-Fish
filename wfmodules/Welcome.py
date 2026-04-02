"""
Welcome message
---
This is the Welcomer module for when it's the user's first time of using WaterFish
Its meant as a fun way to get started with WaterFish
It also gives the user a tour around the browser to make sure anyone who's just starting off knows the basics to waterfish.
It's a module that focuses on improving user experience.
---
Under General Public License Version 3
"""
import tkinter as tk
from tkinterweb import HtmlFrame
welcome = """
<!DOCTYPE html>
<html>
<html>
<head>
<title>Welcome</title>
</head>
<body bgcolor='lightblue'>
<h1>Welcome</h1>
<hr>
<p>Have a look around!</p>
<p>We've got a simple yet nice interface, complete tabs etc.</p>
<p>Right click the top of the browser to open options!</p>
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
    if data.get("assistant") != "True":
        return

    if data.get("devopts") == "True":
        print("assistant features off")
    elif data.get("devopts") == "False":
        pass
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





