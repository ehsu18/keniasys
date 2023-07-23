import tkinter


class Widget(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)
        self.app = master
        self.grid(row=2, column=0, sticky='nsew')
        self.create_widgets()
        

    def create_widgets(self):
        self.user_name = tkinter.Label(self, text=(self.app.user[4] + ' ' + self.app.user[5]), font='Roboto 10', fg='#AAA', bg='#403E39')
        self.user_name.pack(side='left') # TODO asignar color6
        self.ganancia = tkinter.Label(self, text=self.app.ganancia, font='Roboto 10', fg='#AAA', bg='#403E39')
        self.ganancia.pack(side='right')
        self.dolar = tkinter.Label(self, text=self.app.usd, font='Roboto 10', fg='#AAA', bg='#403E39')
        self.dolar.pack(side='right')


    def showmessage(self, m):
        print(m)