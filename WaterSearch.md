# WaterSearch

---
## What is it?
WaterSearch is a simple crawler + search engine,
It's not the default one however it can be used by toggling wfsearch to True in settings.txt
It's meant for people experimenting with search engines.
However, it only works locally meaning no server.
This also means you'll have to crawl manually.

---
## How to crawl?
Go over to crawler.py run it and follow the following steps.

- In starting url, paste your desired url or leave blank to default to https://vlib.org/
- In max url type a number (e.g. 10) to make it stop crawling after you've hit the desired amount of sites crawled.
- Then it will ask or confirmation to crawl, type Y if you're willing to do so.

**Note: Make sure you use starting point that has no js and ensure that the links in there are mostly html only, as you may know wf and it's renderer tkinterweb doesn't have a dedicated js engine**
**I recommend crawling around 5 starting url's each one place a max of 30 that'd give you enough pages to work with I believe**

---
## How to search?
As mentioned before you'll have to toggle wfsearch to True in settings otherwise it shall use the far superior wiby.
Then after that you have to type ypur search in the search bar hit enter,
due to bad design the search engine is going to be very slow around 5 secs for 15 results on average,
you can de see the total time it took to load, the amount of results showns, your results and ofcourse previews!

---
## But why?
As you may know this browser is also just a fun hobbyist project,
and so is this search engine,
it's meant especially for people who wanna tinker with search engines.

The search engine itself is very simple meaning anyone with adequate python experience can change and mod the engine to their likings.
Also I just think it's pretty fun to crawl and act like Google hehe.
