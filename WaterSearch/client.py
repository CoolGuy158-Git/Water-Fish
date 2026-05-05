"""
Client
---
Idk what else to name it but this does almost everything,
It takes the knownsites maps the words and yea.
Like for example user searches:
    Search: Dog
The program finds the knownsites where Dog is mentioned and shows the sites with the most mention of dogs first.
Honestly just use wiby over this.
"""
import requests
from bs4 import BeautifulSoup
import warnings
from bs4 import XMLParsedAsHTMLWarning
import time
import ast
from urllib.parse import urlparse

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def clientSTART(search, load):
    """
    Very, very slow, goes through each line of knownsites,
    then checks if search is in line,
    if so it downloads the file
    in order to get stuff such as phar, title, etc.
    """
    timeStart = time.time()
    file = open("system/knownsites.txt", "r")
    timesDone = 0
    titles = []
    links = []
    scores = []
    previews = []
    searchishere = False
    for line in file:
        if search in line:
            url, data = line.split(",", 1)
            links.append(line.split(",", 1)[0])
            html = requests.get(line.split(",", 1)[0]).text
            score = dict(ast.literal_eval(data)).get(search.lower(), 0)
            soup = BeautifulSoup(html, "lxml")
            phar = soup.find_all("p")
            txt = "\n".join(p.get_text() for p in phar)
            words = txt.split()
            preview = " ".join(words[:10])
            if len(words) > 80:
                preview += "..."
            previews.append(preview)
            if soup.title and soup.title.string:
                title = soup.title.string
            else:
                title = urlparse(url).netloc.replace("www.", "")
            titles.append(title)
            scores.append(score)
            timesDone += 1
            searchishere = True
    timeEnd = time.time()
    timeElapsed = timeEnd - timeStart

    combined = list(zip(links, titles, scores, previews))
    combined.sort(key=lambda x: x[2], reverse=True)
    if not searchishere:
        waterFishSearchOut = f"""
        <html>
        <head>
        <title>{search}</title>
        <body>
        <h1>Wf-Search query: {search}</h1>
        <hr>
        <h2>No results found</h2>
        <h3>Try crawling again to know more pages!</h3>
        <hr>
        <h2>How to crawl?</h2>
        <p>Go over to crawler.py run it and follow the following steps.</p>
        <ul>
        <li>In starting url, paste your desired url or leave blank to default to https://vlib.org/</li>
        <li>In max url type a number (e.g. 10) to make it stop crawling after you've hit the desired amount of sites crawled.</li>
        <li>Then it will ask or confirmation to crawl, type Y if you're willing to do so.</li>
        </ul>
        <p><b>Note:</b> Make sure you use starting point that has no js and ensure that the links in there are mostly html only, as you may know wf and it's renderer tkinterweb doesn't have a dedicated js engine</p>
        <p><b>I recommend crawling around 5 starting url's each one place a max of 30 that'd give you enough pages to work with I believe</b></p>
        """
        load.load_html(waterFishSearchOut)
        return
    waterFishSearchOut = f"""
    <html>
    <head>
    <title>Wf-Search query: {search}</title>
    </head>
    <body>
    <h1>Wf-Search query: {search}</h1> <br>
    <h6>Loaded {str(timesDone)} results in {str(round(timeElapsed))} seconds.</h6>
    """

    for link, title, score, preview in combined:
        waterFishSearchOut += "<hr>"
        waterFishSearchOut += f'<a href="{link}">{title}</a><br>'
        waterFishSearchOut += f'<a style = "color: black" href="{link}">{preview}</a><br>'

    waterFishSearchOut += """
    </body>
    </html>
    """

    load.load_html(waterFishSearchOut)
