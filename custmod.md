# Custom Modules BETA

---
## The info
Allows users to create custom modules.
User created modules are stored in custmod/ and must have the .wfmd extension.
Currently the custmods only have 2 commands (url, btn).
Url -> Transfers the user to a certain url
Btn -> Creates a button in menubar

---
## How to use one
Using a custom mod is straight forward.
You first have to create one or use the ones created by other users,
you must then add it to the custmod dir making sure it has the .wfmd extension.
Then you must make sure to read the source code.

---
## How to make one
Open your editor of choice, create a new file with a .wfmd extension. Make sure it follows a format like this one.
source: [example](custmod/Example.wfmd)
```wfmd
name: Example
consent:"""
This is a simple demo mod.
It takes you to the example domain.
By clicking agree you agree that:
    This mod shall take you to example domain.
    That you've read this terms and conditions.
    And that you've read the source code and fully,
    understood what this mod does.
"""
license: MIT
repository: https://github.com/example/hello-mod
code:"""
btn = "https://example.com" "example"
"""
```
Make sure your consent isn't too long as it may overflow from the pop-up.

---
## Why doesn't it show?
Well as you may know it's a beta feature so you may have to first go into system/settings.txt,
locate custmodBETA and switch it to True.