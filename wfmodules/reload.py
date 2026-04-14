"""
Reload/Refresh module
---
WfModule used for reloading the page.
Useful for when you're staring at a blank screen,
contemplating every life decision and just want to hit a button.
All jokes asides its useful when:
    A page is half loaded due to network issue mid-load.
    When the page stores the old data, and you need to reload it to see the changes,
    Along with many more.
"""

import sys
import os

# Must be the shortest module made, but I expected it to be longer then I found out tkinterweb has reload, so pretty cool, it saved me some time.
def reload(currentframe):
    currentframe.reload()
def reloadmain(root):
    root.destroy()
    os.system(f'"{sys.executable}" main.py')

