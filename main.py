#! venv/bin/python

# Main file of the inventory manager
# begin at feb 02 of 2021

try:
    import tkinter
    from gui import *
    from db import *
except ModuleNotFoundError as e:
    print(f"Can't initialize, missing module: {e}")
    raise
except Exception:
    raise


class App(tkinter.Frame):
    """" The main class of the app
    Methods defined here:
    - __init__()
    - configure_root()
    - configure_self()
    """

    def __init__(self):
        """Making all the app before mainloop"""
        # Tk window
        self.root = tkinter.Tk()
        self.configure_root()

        # initializing in tk and making main frame
        tkinter.Frame.__init__(self, self.root)
        self.configure_self()

        # Making Database Objects
        self.products = ProductsDB()
        self.configurations = None
        self.providers = None
        self.clients = None

        # Making main widgets
        # self.menubar = MenuBar(self)
        self.navbar = NavBar(self, bg='#403E39')
        self.mainview = MainView(self, bg='#00F') # this don't should be visible
        self.statusbar = StatusBar(self, bg='#DDD')

        self.pack(fill='both', expand=1)

    def configure_root(self):
        """Main window configuration"""
        # TODO config icons and size and title
        self.root.geometry('1000x500')

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
    except:
        raise
        input()
