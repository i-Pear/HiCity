from HiCity import HiCity
from tkinter import *
from AutoComplete import CNameCompleter

class App:
    WINDOW_WIDTH = 756
    WINDOW_HEIGHT = 470

    def __init__(self):
        self.core=HiCity()

        self.window = Tk()
        self.window.title("HiCity v0.4")
        self.window.geometry('{0}x{1}'.format(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.window.resizable(False, False)

        self.cname = StringVar()

        self.cnameEntry = Entry(self.window)
        self.cnameEntry.config(textvariable=self.cname)
        self.cnameEntry.bind('<KeyRelease>', self.textChanged)
        self.cnameEntry.place(x=10, y=10)

    def textChanged(self, event):
        print(self.cname.get())

    def mainloop(self):
        self.window.mainloop()


app = App()
app.mainloop()
