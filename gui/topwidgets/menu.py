import tkinter


class Menu(tkinter.Menu):
    def __init__(self, master, *args, **kwargs):
        tkinter.Menu.__init__(self, master, *args, **kwargs)
        self.master = master

        # cascades below
        self.menu_test = tkinter.Menu(self)
        self.add_cascade(label='test', menu=self.menu_test)

        # including in root
        self.master.root.config(menu=self)
