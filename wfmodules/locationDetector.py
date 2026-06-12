"""
Location detector
---
A simple wfmodule that detects user location,
so that it can show results which are fit for the user's location.
It is off by default but can be turned on by toggling location in settings.txt

It works by pinging ipapi then getting the country.
Then back in main.py it adds the country to search query.
Thus, wiby starts showing results with the country name on it.
It's not the most elegant way to show region based results. But hey it kinda works.
"""

import requests

def getLoc(dataopts):
    data = requests.get("https://ipapi.co/json/").json()
    if dataopts["devopts"] == "True":
        print(f"Location: {dataopts['location']}")
    return data["country_name"]


