#! venv/bin/python

# Main file of the inventory manager
# begin at feb 02 of 2021

import tkinter
from tkinter import messagebox
from gui import *
from db import *
from PIL import ImageTk, Image


class App(tkinter.Frame):
    """" The main class of the app
    Methods defined here:
    - __init__()
    - configure_root()
    - configure_self()
    """

    def __init__(self):
        """Making all the app before mainloop"""
        
        # Variables
        self.logo = 'gui/img/logo.png'
        self.icon = 'gui/img/logo.ico'
        self.user = (-1, 'debugging', 'mode', 0, 'youshouldn\'t', 'seethisxd')
        self.usd = 3800.00
        self.ganancia = 0.30
        self.resources = 'resources/'

        # Tk window
        self.root = tkinter.Tk()
        self.configure_root()        

        # initializing in tk and making main frame
        tkinter.Frame.__init__(self, self.root)
        self.configure_self()

        # Making Database Objects
        self.products = ProductsDB()
        self.ventas = VentasDB(self)
        self.users = UsersDB()
        self.configurations = None
        self.providers = None
        self.clients = None

        # Making main widgets
        # self.menubar = MenuBar(self)
        self.login = Login(self)
        # self.pack(fill='both', expand=True) # TODO debuggin mode
        # self.charge_topwidgets()

    def charge_topwidgets(self):
        self.navbar = NavBar(self, bg='#403E39')
        self.mainview = MainView(self, bg='#FFF') # this should not be visible TODO change color when finish
        self.statusbar = StatusBar(self, bg='#403E39')
        

    def configure_root(self):
        """Main window configuration"""
        # TODO config icons and size and title
        self.root.geometry('1000x540')
        self.root.iconbitmap(self.icon)
        self.root.title('Sistema de gestión de inventario')

    def configure_self(self):
        """All main container (self) configuration"""
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, minsize=60)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, minsize=20)


if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        messagebox.showerror(title='Error en el programa', message=e)
