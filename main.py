#!/usr/bin/env python3

from os.path import basename, splitext
from tkinter import Scale, HORIZONTAL, Canvas, LEFT, S, Frame, Entry
import tkinter as tk

class Application(tk.Tk):
    name = basename(splitext(basename(__file__))[0])
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)

        self.frameR = Frame(self)
        self.frameR.pack()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.frameB = Frame(self)
        self.frameB.pack()

        self.labelR = tk.Label(self.frameR, text="R")
        self.labelR.pack(side=LEFT, anchor=S)
        self.scaleR = Scale(self.frameR, from_=0, to=255, orient=HORIZONTAL, length= 256, command=self.change)
        self.scaleR.pack(side=LEFT, anchor=S)
        self.entryR = Entry(self.frameR, width=4)
        self.entryR.pack(side=LEFT, anchor=S)

        self.labelG = tk.Label(self.frameG, text="G")
        self.labelG.pack(side=LEFT)
        self.scaleG = Scale(self.frameG, from_=0, to=255, orient = HORIZONTAL, length= 256, command=self.change)
        self.scaleG.pack(side=LEFT)
        self.entryG = Entry(self.frameG, width=4)
        self.entryG.pack(side=LEFT, anchor=S)

        self.labelB = tk.Label(self.frameB, text="B")
        self.labelB.pack(side=LEFT)
        self.scaleB = Scale(self.frameB, from_=0, to=255, orient = HORIZONTAL, length= 256, command=self.change)
        self.scaleB.pack(side=LEFT)
        self.entryB = Entry(self.frameB, width=4)
        self.entryB.pack(side=LEFT, anchor=S)

        self.canvasMain = Canvas(self, width=256, height=128, background= "#000000")
        self.canvasMain.pack()

        self.buttonExit = tk.Button(self, text="Exit", command=self.quit)
        self.buttonExit.pack()

    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvasMain.config(background=f"#{r:02x}{g:02x}{b:02x}")

    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()