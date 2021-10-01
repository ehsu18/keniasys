import tkinter


class Widget(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)
        self.grid(row=2, column=0, sticky='nsew')

    def showmessage(self, m):
        print(m)