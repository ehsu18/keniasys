import tkinter
from PIL import ImageTk, Image


class NavBar(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)
        self.app = master
        self.grid(row=0, column=0, sticky='nsew')

        # creating logo label
        try:
            self.logo_img = ImageTk.PhotoImage(Image.open(self.app.logo).resize((50, 50), Image.ANTIALIAS))
        except Exception as e:
            print(e)
        else:
            self.logo_label = tkinter.Label(self, image=self.logo_img, bd=0, relief='flat', bg='#403E39')
            self.logo_label.pack(side='left', padx=5, pady=5)

        # creating label
        self.upper_label = tkinter.Label(self, fg='#FFF', bg='#403E39', text="FERROMOTOS KENIA\'S SYSTEM",
                                         font='Oswald 16 bold')
        self.upper_label.pack(side='left', padx=5)

        nav_btn_style = {
            'fg': '#403E39',
            'bg': '#FF0',
            'relief': 'flat',
            'bd': 0,
            'font': 'Roboto 12 bold'
        }
        self.inventory_button = tkinter.Button(self, text="FACTURACIÓN",
                                               command=lambda: self.app.mainview.set_tab('facturation'),
                                               **nav_btn_style)
        self.inventory_button.pack(side='right', padx=10, pady=5)

        self.inventory_button = tkinter.Button(self, text="INVENTARIO",
                                               command=lambda: self.app.mainview.set_tab('inventory'),
                                               **nav_btn_style)
        self.inventory_button.pack(side='right', pady=5)

    # def change_tab(self, t: str):
    #     self.app.mainview.set_tab(t)
