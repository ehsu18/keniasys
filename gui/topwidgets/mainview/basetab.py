from gui.tools import *


class ScrolledBaseTab(tkinter.Frame):
    """
    Base tab is a template of all tabs. Each tab is a frame that
    contains all sub-widgets in a canvas and is packaged to the
    mainview frame at the end. Whit the create_widget method is
    how the sub-widgets must to be created.
    """

    def __init__(self, master, *args, **kwargs):
        """Creating and configuring the basic of a tab
        and making the container (self) whit the canvas
        and autoscrollbars"""
        tkinter.Frame.__init__(self, master, bd=0, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.xscroll = AutoScrollbar(self, orient='horizontal')
        self.xscroll.grid(row=1, column=0, sticky='ew')
        self.yscroll = AutoScrollbar(self)
        self.yscroll.grid(column=1, row=0, sticky='ns')
        self.canvas = tkinter.Canvas(
            self, bg='#000',
            yscrollcommand=self.yscroll.set,
            xscrollcommand=self.xscroll.set,
            *args, **kwargs)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        self.create_widgets()

        self.xscroll.config(command=self.canvas.xview)
        self.yscroll.config(command=self.canvas.yview)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def create_widgets(self):
        """This method need to be rewrited on a child
        class to make all widgets from each tab.
        All these widgets must be made in the self.canvas
        element."""
        pass


class BaseTab(tkinter.Frame):

    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)
        self.app = master.app
        # self.products = self.app.products
