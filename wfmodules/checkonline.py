"""
Check Online
---
Modularized og checkonline func on main.py.
Helped reduce main.py size.
As well as helping maintainers improve and make changes to checkonline easily.
Checking steps (Skips the rest if one of them returns True):
    Checks if known addresses are found.
    Waits an additional 3 secs for the site you're trying to access (url) to respond.
    Checks if wiby.me is online.
"""

import requests
import psutil
def checkonline(url, data):
    knowns = [
        "https://www.google.com",
        "https://cloudflare.com",
        "https://duckduckgo.com"
        # Add more sites later on
    ]
    knownon = False
    for known in knowns:
        """
        Ts checks if known sites are online, 
        why? Well if popular and almost never down pages are up 
        that must mean that hopefully the internet is alive! Right?
        """
        try:
            requests.get(known, timeout=1)
            knownon = True
            break
        except:
            pass

    if knownon:
        if data['devopts'] == 'True':
            print("Known sites are online.")
        return True
    else:
        if data['devopts'] == 'True':
            print("Known sites are not online.")
            print("Checking for current page response...")
            print()
    try:
        """
        Wait's exactly 3 more seconds for the page to respond.
        Helps in case the server is just freaking slow.
        """
        requests.get(url, timeout=3)
        if data['devopts'] == 'True':
            print("Page responded.")
        return True
    except:
        if data['devopts'] == 'True':
            print("Page didn't responded.")
            print("Checking if WiBy is online...")
            print()
        pass

    try:
        """
        The last resort.
        Checks if wiby.me is online.
        Also if the browser's freaking search engine is down then basically the browser is down.
        """
        requests.get('https://wiby.me', timeout=6) # Long ahh timeout, im giving wiby as much time as it needs. That's why it's not together with the known sites.
        if data['devopts'] == 'True':
            print("WiBy is online.")
            return True
    except:
        if data['devopts'] == 'True':
            print("WiBy is offline. It's highly unlikely you're connected to the internet.")
            return False

    return False


