#!/usr/bin/env python3

from os.path import basename, splitext
from tkinter import Scale, HORIZONTAL, Canvas
import tkinter as tk

class Application(tk.Tk):
    name = basename(splitext(basename(__file__))[0])
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)

        self.labelR = tk.Label(self, text="Red")
        self.labelR.pack()
        self.scaleR = Scale(self, from_=0, to=255, orient = HORIZONTAL, length= 256, command=self.change)
        self.scaleR.pack()

        self.labelG = tk.Label(self, text="Green")
        self.labelG.pack()
        self.scaleG = Scale(self, from_=0, to=255, orient = HORIZONTAL, length= 256, command=self.change)
        self.scaleG.pack()

        self.labelB = tk.Label(self, text="Blue")
        self.labelB.pack()
        self.scaleB = Scale(self, from_=0, to=255, orient = HORIZONTAL, length= 256, command=self.change)
        self.scaleB.pack()

        self.canvasMain = Canvas(self, width=256, height=128, background= "#000000")
        self.canvasMain.pack()

        self.buttonExit = tk.Button(self, text="Exit", command=self.quit)
        self.buttonExit.pack()

    def change(self, event):
        r=self.scaleR.get()
        g=self.scaleG.get()
        b=self.scaleB.get()
        self.canvasMain.config(background=f"#{r:02x}{g:02x}{b:02x}")

    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()