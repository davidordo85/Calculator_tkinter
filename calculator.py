from tkinter import *
from tkinter import ttk

class Controller(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=300)
        d = Display(self)
        d.grid(column=0, row=0, columnspan=4)

class Display(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=50)
        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 30', background='black', foreground='white')

        lbl = ttk.Label(self, text="0", anchor=E, style='my.TLabel')
        lbl.pack(side=TOP, fill=BOTH, expand=True)


class Selector(ttk.Radiobutton):
    pass

class CalcButton(ttk.Button):
    pass