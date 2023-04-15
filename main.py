from tkinter import *
from tkinter import ttk

import calculator

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Calculator')
        self.geometry("272x300")
        self.pack_propagate(0)


        c = calculator.Controller(self)
        c.pack(side=TOP, fill=BOTH)

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()