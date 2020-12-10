## Hello there! this code helps you to fastly create small programs or projects with Tkinter,
## thus making your work much easier. Explaining on how it works accom

import sys
from tkinter.constants import END
import tkinter as tk

## Toplevel can be used for warnings or other extra features
from tkinter import Toplevel

WIDTH = 600
HEIGHT = 400

## This part makes sure that when you use the return part of the Tkinter buttons,
## it will return it as a string, so if you need entries that are int or float,
## you gotta use int() or float() on the those said entries for proper calculations.
class IntEntry(tk.Entry):
    def get(self):
        val = super().get()
        return int(val)


## The Clear function deletes all current widgets on the Frame, and executes the 
## function that will create new ones. 
def clear(frame, userfunction):
    for widget in frame.winfo_children():
        widget.destroy()
    userfunction()


## The program's main screen
def startScreen(root):
    global canvas
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    global frame
    frame = tk.Frame(root, bg="gray", bd=10)
    frame.place(relheight=1, relwidth=1)

    label = tk.Label(frame, text="This is the first Frame of the project.", font=20, bg="gray")
    label.pack()

    button = tk.Button(frame, text="Welcome!", font=20, command=lambda: clear(frame, newWindow))
    button.place(relx=0.5, rely=0.5, anchor="c")

    root.mainloop()

def newWindow():
    root.title("Frame redone")

    label = tk.Label(frame, text="This is how the button works!", font=20, bg="gray")
    label.pack()

    b = tk.Button(frame, text="Next", font=20, command=lambda: clear(frame, secondWindow))
    b.place(relx=0.95, rely=0.95, relwidth=0.15, relheight=0.12, anchor="se")

def secondWindow():
    root.title("Frame redone again")

    label = tk.Label(frame, text="And here is the frame redone again!", font=20, bg="gray")
    label.pack()

    b = tk.Button(frame, text="Back", font=20, command=lambda: clear(frame, newWindow))
    b.place(relx=0.95, rely=0.95, relwidth=0.15, relheight=0.12, anchor="se")

global root     
root = tk.Tk()
root.title("Your program")
startScreen(root)