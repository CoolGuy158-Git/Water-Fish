"""
Knotmeter
---
Calculates user's latency, download, upload, and internet speed.
Don't know if this should be a devopts feature or not, but I decided against it.
It's also the water-fish's repo 100th commit!!!
And since we literally don't have requests timeout just in case you are connected but just really slow,
I just use our checkonline module as to check if were online and only continue the process if so.
This module is very helpful as a mini internet speed test as many speed test websites just won't work because they have Js.
Why did I name knotmeter? Cuz knotmeter = speedometer for ships = water = waterfish.
"""

import requests
import time
from wfmodules.checkonline import checkonline

def knots(Framey, data):
    try:
        loading = """
        <html>
        <head>
        <title>Loading</title>
        <body bgcolor="lightblue">
        <hr>
        <h1>Checking connection</h1>
        <hr>
        </body>
        </html>
        """
        Framey.load_html(loading)
        if checkonline(url = "https://github.com", data = data): # Jst define url as this so that user doesn't have to type anything before using the knotmeter
            GOOOO = True
        else:
            GOOOO = False # NOOO DON'T GOOO!!!! PLEASEEEE DON'T LEAVE ME!!!
            speedhtml = f"""
                    <html>
                    <head>
                    <title>Knotmeter</title>
                    </head>
                    <body bgcolor="lightblue">
                    <h1><font color='red'>ERROR</font></h1>
                    <hr>
                    <h2>You seem to be offline.</h2>
                    </body>
                    </html>
                    """
            Framey.load_html(speedhtml)
        sites = [
            "https://www.google.com",
            "https://cloudflare.com",
            "https://duckduckgo.com",
            "https://wiby.me",
            "https://github.com"
        ]
        ElapsedTimey = []
        amount = 0
        if GOOOO:
            loading = """
                    <html>
                    <head>
                    <title>Loading</title>
                    <body bgcolor="lightblue">
                    <hr>
                    <h1>Checking latency</h1>
                    <hr>
                    <h3>Connection [OK]</h3>
                    </body>
                    </html>
                    """
            Framey.load_html(loading)
            for site in sites:
                timeStart = time.time()
                requests.get(site)
                timeEnd = time.time()
                ElapsedTimey.append(timeEnd - timeStart)
                amount = amount + 1

            latency = (sum(ElapsedTimey) / amount) * 1000
            latency = f"{latency:.2f} ms"

            loading = f"""
                    <html>
                    <head>
                    <title>Loading</title>
                    <body bgcolor="lightblue">
                    <hr>
                    <h1>Checking download speed</h1>
                    <hr>
                    <h3>Connection [OK]</h3>
                    <h3>Latency [{latency}]</h3>
                    </body>
                    </html>
                    """
            Framey.load_html(loading)
            downloadsSpeed = []
            for i in range(4): # Repeat four times just to get more accurate results
                timeStart = time.time() # Download 2.5 mb x 4 = uhh 10??? So you're downloading 10 mb to check if you're Usain Bolt.
                downloadr = requests.get("https://speed.cloudflare.com/__down?bytes=2500000", stream=True) # Imagine cloudflare crashes, pftt impossible, right?
                sizeB = 0
                for chunk in downloadr.iter_content(1024):
                    sizeB += len(chunk)
                endTime = time.time()
                downloadsSpeed.append(sizeB / (endTime - timeStart))
                time.sleep(1) # Pause for a bit cuz cloudflare keeps ghosting me
            avgdownloadSpeed = sum(downloadsSpeed) / len(downloadsSpeed)
            avgdownloadRaw = avgdownloadSpeed
            avgdownloadSpeed = f"{avgdownloadSpeed / (1024 * 1024):.2f} MB/s"

            loading = f"""
                    <html>
                    <head>
                    <title>Loading</title>
                    <body bgcolor="lightblue">
                    <hr>
                    <h1>Checking upload speed</h1>
                    <hr>
                    <h3>Connection [OK]</h3>
                    <h3>Latency [{latency}]</h3>
                    <h3>Download Speed [{avgdownloadSpeed}]</h3>
                    </body>
                    </html>
                    """
            Framey.load_html(loading)
            uploadsSpeed = []
            dada = b"x" * 1000000
            for i in range(4):
                timeStart = time.time()
                requests.post("https://speed.cloudflare.com/__up", data = dada)
                endTime = time.time()
                uploadsSpeed.append(len(dada) / (endTime - timeStart))
                time.sleep(1) # Pause for a bit cuz cloudflare keeps ghosting me
            avguploadSpeed = sum(uploadsSpeed) / len(uploadsSpeed)
            avguploadRaw = avguploadSpeed
            avguploadSpeed = f"{avguploadSpeed / (1024 * 1024):.2f} MB/s"

            loading = f"""
                    <html>
                    <head>
                    <title>Loading</title>
                    <body bgcolor="lightblue">
                    <hr>
                    <h1>Finalizing results</h1>
                    <hr>
                    <h3>Connection [OK]</h3>
                    <h3>Latency [{latency}]</h3>
                    <h3>Download Speed [{avgdownloadSpeed}]</h3>
                    <h3>Upload Speed [{avguploadSpeed}]</h3>
                    </body>
                    </html>
                    """
            Framey.load_html(loading)
            time.sleep(1)

            # Take all the frekin info and just like turn them to uhh make them look nice!
            # Ik there's a better way to do ts aka LOOP, but idk didn't feel like it.
            dloop1 = downloadsSpeed[0]
            dloop1 = f"{dloop1 / (1024 * 1024):.2f} MB/s"

            dloop2 = downloadsSpeed[1]
            dloop2 = f"{dloop2 / (1024 * 1024):.2f} MB/s"

            dloop3 = downloadsSpeed[2]
            dloop3 = f"{dloop3 / (1024 * 1024):.2f} MB/s"

            dloop4 = downloadsSpeed[3]
            dloop4 = f"{dloop4 / (1024 * 1024):.2f} MB/s"

            aloop1 = uploadsSpeed[0]
            aloop1 = f"{aloop1 / (1024 * 1024):.2f} MB/s"

            aloop2 = uploadsSpeed[1]
            aloop2 = f"{aloop2 / (1024 * 1024):.2f} MB/s"

            aloop3 = uploadsSpeed[2]
            aloop3 = f"{aloop3 / (1024 * 1024):.2f} MB/s"

            aloop4 = uploadsSpeed[3]
            aloop4 = f"{aloop4 / (1024 * 1024):.2f} MB/s"

            googleTime = ElapsedTimey[0] * 1000
            googleTime = f"{googleTime:.2f} ms"

            cloudflareTime = ElapsedTimey[1] * 1000
            cloudflareTime = f"{cloudflareTime:.2f} ms"

            duckduckgoTime = ElapsedTimey[2] * 1000
            duckduckgoTime = f"{duckduckgoTime:.2f} ms"

            wibyTime = ElapsedTimey[3] * 1000
            wibyTime = f"{wibyTime:.2f} ms"

            githubTime = ElapsedTimey[4] * 1000
            githubTime = f"{githubTime:.2f} ms"

            rawspeed = avgdownloadRaw + avguploadRaw
            # Create da HTML
            speedhtml = f"""
            <html>
            <head>
            <title>Knotmeter</title>
            </head>
            <body bgcolor="lightblue">
            <h1>Knotmeter</h1>
            <hr>
            <h2>Average latency:  {latency}</h2>
            <h2>Download speed:  {avgdownloadSpeed}</h2>
            <h2>Upload speed:  {avguploadSpeed}</h2>
            <h2>Internet speed: {rawspeed / (1024*1024):.2f} MB/s</h2>
            <hr>
            <h1>Latency for each site</h1>
            <hr>
            <p>Google: {googleTime}</p>
            <p>Cloudflare: {cloudflareTime}</p>
            <p>DuckDuckGo: {duckduckgoTime}</p>
            <p>Wibby: {wibyTime}</p>
            <p>Github: {githubTime}</p>
            <hr>
            <h1>Download/Upload loops</h1>
            <hr>
            <table border="1">
            <tr>
            <th colspan="2">Download</th>
            <th colspan="2">Upload</th>
            </tr>
            <tr>
            <td>Loop 1</td>
            <td>{dloop1}</td>
            <td>Loop 1</td>
            <td>{aloop1}</td>
            </tr>
            <tr>
            <td>Loop 2</td>
            <td>{dloop2}</td>
            <td>Loop 2</td>
            <td>{aloop2}</td>
            </tr>
            <tr>
            <td>Loop 3</td>
            <td>{dloop3}</td>
            <td>Loop 3</td>
            <td>{aloop3}</td>
            </tr>
            <tr>
            <td>Loop 4</td>
            <td>{dloop4}</td>
            <td>Loop 4</td>
            <td>{aloop4}</td>
            </tr>
            </table>
            </body>
            </html>
            """
            Framey.load_html(speedhtml)
    except Exception as e:
        speedhtml = f"""
                    <html>
                    <head>
                    <title>Knotmeter</title>
                    </head>
                    <body bgcolor="lightblue">
                    <h1><font color='red'>ERROR</font></h1>
                    <hr>
                    <h2>{e}</h2>
                    <p>Try restarting the browser or report the bug in github or discord.</p>
                    </body>
                    </html>
                    """
        Framey.load_html(speedhtml)

