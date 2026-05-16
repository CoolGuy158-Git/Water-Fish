"""
Safemode
----
Blocks specific url's.
By default, it's on and blocks url's that are yk.
It can be set to off in settings just toggle safemode to False.
"""

def block(currentframe):
    blockedHTML = """
    <html>
    <head>
    <title>Oops!</title>
    <body bgcolor="lightblue">
    <hr>
    <h1>Oops!</h1>
    <hr>
    <p>This url seems to be blocked</p>
    <p>Reason: safemode</p>
    </body>
    </html>
    """
    currentframe.load_html(blockedHTML)

def safemode(url, currentframe):
    unsafeKeyWords = [
        "xxx",
        "nsfw",
        "p" + "corn"[1:], # Introducing, SOURCE CODE CENSORING YEAAAA
        "not safe for work"
    ]
    for word in unsafeKeyWords:
        if word in url.lower():
            block(currentframe)
            return
