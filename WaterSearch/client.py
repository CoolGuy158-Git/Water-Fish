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
import random
import requests
from bs4 import BeautifulSoup
import warnings
from bs4 import XMLParsedAsHTMLWarning
import time
import ast
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
def clientSTART(search, load, settings):
    """
    Very, very slow, goes through each line of knownsites,
    then checks if search is in line,
    if so it downloads the file
    in order to get stuff such as phar, title, etc.
    """
    timeStart = time.time()
    search = search.replace('%20', ' ')

    def loading():
        """
        Loading messages to keep the user kinda entertained.
        """
        elapsed = round(int(time.time() - timeStart))
        boredtext = ['Did you know? By clicking start song, you can choose a song to play?', 'You can ask Remora FAQs!','If you ever get bored, open a new tab and try to find all our hidden easter eggs!', 'The buggiest browser ever.', 'Is this even a browser?', '"I will feed you Ai." -Not my browser', 'Why are you using ts?', 'Magnificant browser', 'Slightly better than IE!', 'Fun fact this browser was made by a 13 yo!', 'Is using tkinterweb cheating?']
        fintext = random.choice(boredtext)
        return f"""
            <html>
            <head>
            <title>Searching for {search}</title>
            </head>
            <body>
            <h1>Searching for {search}</h1>
            <h2>Time: {elapsed}</h2>
            <hr>
            <h2>{fintext}</h2>
            </body>
            </html>
            """
    file = open("system/knownsites.txt", "r")
    timesDone = 0
    links = []
    previews = []
    searchishere = False
    load.load_html(loading())
    def wfSearchResults(line):
        """
        Turned this part into a func,
        so that I can use threading on it hehe.
        """
        urldatasplit = time.time()
        url, data = line.split(",", 1)

        if settings["devopts"] == "True":
            print("url data split: ", time.time() - urldatasplit)

        downloading = time.time()
        links.append(line.split(",", 1)[0])
        html = requests.get(line.split(",", 1)[0]).text
        score = dict(ast.literal_eval(data)).get(search.lower(), 0)
        if settings["devopts"] == "True":
            print("downloads: ", time.time() - downloading)
        makingpreview = time.time()
        soup = BeautifulSoup(html, "lxml")
        text = soup.get_text(" ", strip=True)
        preview = text[:30]
        if len(text) > 30:
            preview += "..."
        else:
            pass
        if settings["devopts"] == "True":
            print("preview: ", time.time() - makingpreview)
        previews.append(preview)
        makingtitle = time.time()
        if soup.title and soup.title.string:
            title = soup.title.string
        else:
            title = urlparse(url).netloc.replace("www.", "")
        if settings["devopts"] == "True":
            print("title:", time.time() - makingtitle)
        return url, title, score, preview

    results = []

    with ThreadPoolExecutor(max_workers=35) as executor:
        futures = []
        for line in file:  # Checks every line in knownsites
            if search.lower() in line.lower():
                """
                Then the ones which match the search ya, gets downloaded and stuff, 
                this also kinda means that the user's search has to be the exact same as to any top ten words in any url 
                thats in the knwosites which makes it kind dumb but ehh
                """
                futures.append(executor.submit(wfSearchResults, line))
        if not futures:
            searchishere = False
        else:
            searchishere = True
        for completedf in as_completed(futures):
            results.append(completedf.result())
            timesDone += 1
            load.load_html(loading())

    timeEnd = time.time()
    timeElapsed = timeEnd - timeStart

    combined = results
    combined.sort(key=lambda x: x[2], reverse=True)
    if not searchishere: # Checks if user's search matches any url in knownsites.txt
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
    for i in range(0, len(results), 10):
        batch = results[i:i + 10]
        for link, title, score, preview in batch:
            waterFishSearchOut += "<hr>"
            waterFishSearchOut += f'<a href="{link}">{title}</a><br>'
            waterFishSearchOut += f'<a style = "color: black" href="{link}">{preview}</a><br>'

    waterFishSearchOut += """
    <hr>
    <h5>Sorry, that's all I seem to know... Crawl more to make me smarter!</h5>
    </body>
    </html>
    """

    load.load_html(waterFishSearchOut)
