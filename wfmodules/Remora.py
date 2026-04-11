"""
Remora
---
Rule-Based Assistant for Water-Fish.
It doesn't collect any data, and all responses are predefined and hard coded.

Named after the Remora fish, which travels attached to larger sea creatures,
assisting them as they move through the waters.
"""
import tkinter as tk

userinputs = [
    "What is Water-Fish?",
    "How to add/close tabs?",
    "What are some Easter Eggs?",
    "How to open customize?",
    "How do I change the theme?",
    "What can Remora do?"
]

def initRemora(root, data):
    if data['remora'] == 'True':
        assis = tk.Toplevel(root)
        assis.title("Remora")
        assis.resizable(False, False)
        assis.geometry("400x400")

        remoraSay = tk.Label(assis, text="Hello Im Remora", font=("Arial", 30), relief='ridge')
        remoraSay.pack()

        def respond(text): # Ik it's a big and messy if/else statement but ehh good enough
            if text == "What is Water-Fish?":
                remoraSay.config(text = "Water-Fish is a lightweight Python based web browser.", font=("Arial", 10))
            if text == "How to add/close tabs?":
                remoraSay.config(text = "Click the '+' to open tabs and '-' to close tabs.", font=("Arial", 10))
            if text == "What are some Easter Eggs?":
                remoraSay.config(text = "Type '/egg' on the search bar and see if you can find out!", font=("Arial", 10))
            if text == "How to open customize?":
                remoraSay.config(text = "Type '/cmds customize' on search bar additionally type '/cmds fav' to\nchange the links the pops up on homepage!", font=("Arial", 10))
            if text == "How do I change the theme?":
                remoraSay.config(text = "By opening customize.", font=("Arial", 20))
            if text == "What can Remora do?":
                remoraSay.config(text = "I can provide answers to FAQ! You can disable me if you want \nby going to customize and set Remora to False", font=("Arial", 10))

        inputs = tk.Frame(assis, width=400, height=400, bg='lightblue')
        inputs.pack(fill='both', expand=True)

        buttons = []
        for item in userinputs:
            input = tk.Button(inputs, text=item, command=lambda x=item: respond(x))
            input.pack(pady=5)
            buttons.append(input)
    else:
        pass