# InkSquid - Rendering engine

---

## The plan
We will start making the first version of the renderer once we have around 5 contributors ready to help.
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
 