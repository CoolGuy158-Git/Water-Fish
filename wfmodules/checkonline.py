"""
Check Online
---
Modularized og checkonline func on main.py.
Helped reduce main.py size.
As well as helping maintainers improve and make changes to checkonline easily.
Checking steps (Skips the rest if one of them returns True):
    Checks if known addresses are found.
    Waits an additional 3 secs for the site you're trying to access (url) to respond.
    Asks OS for info regarding network such us  as if Wi-Fi is on etc.
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
            print("Checking if Os's WiFi interface is on...")
        pass
    try:
        """
        Checks if Os's WiFi interface is on.
        Basically also the final one cuz its buggy and messy and ignores Ethernet users.
        There's not much else to be said that's all it really does.
        This my first time trynna actually make docs OK.
        Don't judge me, hmph~ 
        """
        stats = psutil.net_if_stats()
        for iface, stat in stats.items():
            name = iface.lower()
            if stat.isup and ("wi" in name or "wlan" in name or "wireless" in name):
                print("OS's WiFi interface is on.")
                return True

        if data['devopts'] == 'True':
            print("OS's WiFi interface is off.")

    except:
        return False
    return False


