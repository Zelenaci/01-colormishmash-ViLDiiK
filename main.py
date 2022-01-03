#!/usr/bin/env python3

from os.path import basename, splitext
from tkinter import Scale, StringVar, HORIZONTAL, Canvas, LEFT, S, Frame, Entry, END
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

        self.varR = StringVar()
        self.labelR = tk.Label(self.frameR, text="R")
        self.labelR.pack(side=LEFT, anchor=S)
        self.scaleR = Scale(self.frameR, from_=0, to=255, orient=HORIZONTAL, length= 256, variable=self.varR
        )
        self.scaleR.pack(side=LEFT, anchor=S)
        self.entryR = Entry(self.frameR, width=8, textvariable=self.varR)
        self.entryR.pack(side=LEFT, anchor=S)

        self.varG = StringVar()
        self.labelG = tk.Label(self.frameG, text="G")
        self.labelG.pack(side=LEFT)
        self.scaleG = Scale(self.frameG, from_=0, to=255, orient = HORIZONTAL, length= 256, variable=self.varG
        )
        self.scaleG.pack(side=LEFT)
        self.entryG = Entry(self.frameG, width=8, textvariable=self.varG)
        self.entryG.pack(side=LEFT, anchor=S)

        self.varB = StringVar()
        self.labelB = tk.Label(self.frameB, text="B")
        self.labelB.pack(side=LEFT)
        self.scaleB = Scale(self.frameB, from_=0, to=255, orient = HORIZONTAL, length= 256, variable=self.varB
        )
        self.scaleB.pack(side=LEFT)
        self.entryB = Entry(self.frameB, width=8, textvariable=self.varB)
        self.entryB.pack(side=LEFT, anchor=S)

        self.varR.trace("w", self.change)
        self.varB.trace("w", self.change)
        self.varG.trace("w", self.change)

        self.canvasMain = Canvas(self, width=256, height=128, background= "#000000")
        self.canvasMain.pack()
        self.canvasMain.bind("<Button-1>", self.clickHandler)
        self.entryMain = Entry(self, text="#000000")
        self.entryMain.pack()

        self.buttonExit = tk.Button(self, text="Exit", command=self.quit)
        self.buttonExit.pack()

        self.buttonChange = tk.Button(self, text="Change", command=self.change)
        self.buttonChange.pack()

        self.frameMem = Frame(self)
        self.frameMem.pack()
        self.canvasMem = []
        for row in range(3):
            for column in range(7):
                canvas = Canvas(self.frameMem, width=50, height=50, background="#abcdef")
                canvas.bind("<Button-1>", self.clickHandler)
                canvas.grid(row=row,column=column)
                self.canvasMem.append(canvas)

    def change(self, var=None, index=None, mode=None):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        colorcode = f"#{r:02x}{g:02x}{b:02x}"
        self.canvasMain.config(background=colorcode)
        self.entryMain.delete(0, END)
        self.entryMain.insert(0, colorcode)

    def clickHandler(self, event):
        if self.cget("cursor") != "pencil":
            self.config(cursor="pencil")
            self.color = event.widget.cget("background")
        else:
            self.config(cursor="")
            event.widget.config(background=self.color)

    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()