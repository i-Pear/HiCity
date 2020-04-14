from HiCity import HiCity, version
from tkinter import *
from tkinter import simpledialog
from Weather import getWeather
from tkinter.messagebox import *


class HiCityApp:
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 200
    HINT_DISPLAY_LIMIT = 4

    def __init__(self):
        self.core = HiCity()
        self.core.loadFullData()
        self.canvas = []

        self.window = Tk()
        self.window.title(version)
        self.set_center(self.window, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.window.resizable(False, False)

        self.cname = StringVar()

        self.cnameEntry = Entry(self.window)
        self.cnameEntry.place(width=375, height=20, x=10, y=32, anchor=NW)
        self.cnameEntry.config(textvariable=self.cname)
        self.cnameEntry.bind('<KeyRelease>', self.textChanged)
        self.cnameEntry.bind('<Key-Return>', self.keyENTERPressed)

        Label(self.window, text="Type city's name here, press ENTER to get info :").place(x=7, y=5, anchor=NW)

        Button(self.window, text='Import from database', command=self.buttonImportClicked) \
            .place(x=245, y=80, width=140, height=40)
        Button(self.window, text='Extract to excel', command=self.buttonExportClicked) \
            .place(x=245, y=140, width=140, height=40)

    def buttonImportClicked(self):
        self.core.db.loadDataFromExternal(silent=True)
        showinfo('Result', 'Data loaded successfully.')

    def buttonExportClicked(self):
        r = simpledialog.askstring('HiCity', 'Input filename')
        if r:
            self.core.db.backupDataToExcel(r)
            showinfo('Result', 'Saved 2586 records to excel file.')

    def keyENTERPressed(self, key):
        # showinfo('Answer', self.core.query(self.cname.get()))
        code = self.core.db.getCitiesByName(self.cname.get())
        title = None
        if len(code) >= 2:
            info = "Multiple cities with the same name!"
        elif len(code) == 0:
            info = "City not found!"
        else:
            weather = getWeather(code[0].code)
            title = weather.cityName + "天气"
            info = "{0}，最高气温{1}，最低气温{2}\n风力：{3}\n感冒指数：{4}" \
                .format(weather.type, weather.low, weather.high, weather.wind, weather.ganmao)
        showinfo('Weather' if title is None else title, info)

    def textChanged(self, event):
        # TODO:Should be rewritten with IoC
        self.displayHints(self.core.completer.get_completions(self.cname.get()))

    def displayHints(self, hints):
        for hint in self.canvas:
            hint.place_forget()
        self.canvas = []
        count = 0
        for hint in hints:
            if count >= self.HINT_DISPLAY_LIMIT:
                return
            self.canvas.append(Label(text=hint.text, bg="SkyBlue"))
            self.canvas[-1].place(x=10, y=60 + count * 25, width=100, height=25)
            count += 1

    def set_center(self, root, Width: int, Height: int):
        scn_w, scn_h = root.maxsize()
        cen_x = (scn_w - Width) // 2
        cen_y = (scn_h - Height) // 2
        size_xy = '{0}x{1}+{2}+{3}'.format(Width, Height, cen_x, cen_y)
        root.geometry(size_xy)

    def mainloop(self):
        self.window.mainloop()


app = HiCityApp()
app.mainloop()
