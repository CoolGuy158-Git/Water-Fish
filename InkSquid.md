# InkSquid - Rendering engine

---

## The plan
I'm currently making a few prototypes (Currently I'm making the networker and parser) not full renderers yet, I'll do that once there's around 5 devs helping.
The first version shall include the following:

- Render simple html only pages (Support for headers, paragraph, break line, and horizontal rule)
- No CSS support
- No Js support 
- Must have a similar namespace to tkinterweb
- Must be able to do networking, parsing, and rendering.

---

## Structure and Data Flow
The renderer must be modular for ease of maintenance and must be inside a folder named InkSquid.
It shall look something like this:

```txt
InkSquid\
    Networker.py (Input: URL or HTML String | Output: raw HTML srting)
    Parser.py (Input: raw HTML string | Output: DOM-like tree nested Python objects)
    HTMLFrame.py (Input: DOM tree | Output: drawn elements on canvas / tkinter frame)
    HTMLRenderer.py (load_html() | load_url())
```
---

## Dev Note - Why am I doing this

---

Soo yea this is big and slightly unrealistic but here's the thing, im not planning to build a full renderer.
Mine is meant to be simple not compete with Chrome. Also yes I get it adding JS support means you need all these security features.
Well guess what im not planning on adding JS till I figure out how to add security and sandboxing and whatnot, and if I don't, bye bye JS!
Also, the reason I made this in python apart from the fact im bad at other langs is cuz of modules!!!
We can use stuff like requests the beautiful soup thing, and lots of modules that just do the stuff for us.
Also, some people are asking "Why aren't you using chromium?", well if you want a browser that uses a nice and polished engine, don't look at an experimental, hobbyist browser meant to learn how browsers work.
Cuz another reason I made this is to explore the idea of just making your own browser and try to not rely on all these big tech stuff.
InkSquid is literally made to just renderer html pages and maybe a few basic CSS, yes it's still pretty hard, but no im not planning to go head to head with Blink, Gecko, or Webkit.
It's a toy browser not the next "Chrome Killer".
