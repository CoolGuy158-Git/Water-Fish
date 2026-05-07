"""
Web Crawler
---
Simple web crawler which well crawls the web,
it then takes the top word that shows up (excluding filler words and focusing mostly on nouns)
Then it maps that word to a url.
It places those in a file locaated in system/knownurl.txt.
The structure looks like:
    https://www.url.com | keyword

It is a very simple search engine it's not teh default wiby is still the default,
but it's there if you want to try,
also its fully local meaning you'd have to crawl the web yourself letting it grow the known url's list.

And the crawler is mostly based off of this I just added my own stuff.
https://www.zenrows.com/blog/web-crawler-python#follow-all-links-on-website
"""


from bs4 import BeautifulSoup
import requests
from collections import Counter
import re
import os

os.chdir("..")
with open("system/knownsites.txt", "r") as f:
    knownsites = f.read()
startingURL = input("Starting Url: ")
if startingURL == "" or "https://" not in startingURL:
    startingURL = "https://vlib.org/"
    print("Starting Url is: " + startingURL)

# Init the list of discovered URL's
urlToVisit = [startingURL]
max = int(input("Max URL: "))
def crawler():
    crawlCount = 0
    results = []
    visited = set()

    while urlToVisit and crawlCount < max:
        currentURL = urlToVisit.pop()
        if currentURL in visited:
            continue
        visited.add(currentURL)

        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(currentURL, headers=headers)

        if response.status_code != 200:
            print(f"[ERROR {response.status_code}] Skipping: {currentURL}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        words = re.findall(r'\b[a-z]+\b', soup.get_text().lower())
        filler = {"the", "and", "of", "to", "a", "in", "is", "was", "by", "that", "you", "your", "you're", "are", "we", "they", "them", "he", "she", "it"}
        words = [w for w in words if w not in filler]
        top = Counter(words).most_common(10)
        results.append((currentURL, top))

        print(currentURL, top)
        crawlCount += 1
        with open("system/knownsites.txt", "a") as f:
            f.write(f"\n{currentURL}, {top}")

        links = soup.select("a[href]")
        for link in links:
            url = link.get("href")
            if not url:
                continue
            absoluteURL = requests.compat.urljoin(currentURL, url)
            absoluteURL = absoluteURL.split("#")[0].strip()
            if not absoluteURL.startswith("http"):
                continue
            if any(absoluteURL.startswith(x) for x in ["mailto:", "javascript:"]):
                continue
            if absoluteURL not in knownsites and visited:
                urlToVisit.append(absoluteURL)
execute = input("Start crawler? Y/n ").lower()
if execute == "y":
    crawler()
elif execute == "n":
    pass
else:
    print("Unrecognized command, aborting crawl.")



