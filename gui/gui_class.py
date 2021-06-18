from tkinter import *


class Gui:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.window = Tk()
        self.window.geometry(str(self.width) + "x" + str(self.height))
        self.window.title(self.title)

    def start_gui(self):
        self.window.mainloop()
