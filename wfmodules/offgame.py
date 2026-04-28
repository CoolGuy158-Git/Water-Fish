"""
Offline game | Gamble-Core
---
Lets users play a "gambling" game (no money/rewards/payment involved) game.
Lets users interact with the browser while their connection is dying!
So users can pass the time just clicking search over and over again!
"""

import random

def error_internet():
    things = ["apple", "orange", "banana"]

    thing1 = random.choice(things)
    thing2 = random.choice(things)
    thing3 = random.choice(things)

    if thing1 == thing2 and thing3 == thing1:
            result = "Win"
    else:
            result = "Lose"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Error</title>
    </head>
    <body>
    <h1>Error Loading Page</h1>
    <hr>
    <p>Please check your internet connection</p>
    <p>If error persists, file an issue on the <a href='https://github.com/CoolGuy158-Git/Water-Fish'>official github repo</a></p>
    <p>your feedback truly matters</p>
    <hr>
    <h1>{result}</h1>
    <hr>
    <p>Thing1: {thing1}</p>
    <p>Thing2: {thing2}</p>
    <p>Thing3: {thing3}</p>
    """