import tkinter
import time

class Login(tkinter.Frame):
    def __init__(self, app):
        self.app = app
        tkinter.Frame.__init__(self, self.app.root, bg='#FFF')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.frame = tkinter.Frame(self, bg='#FFF')

        self.name_label = tkinter.Label(self.frame, text="Login", font='Roboto 22 bold', bg='#FFF')
        self.name_label.grid(column=0, row=0, sticky='we', pady=5)
        self.name_var = tkinter.StringVar(value='Nombre')
        self.name_entry = tkinter.Entry(self.frame, width=14, textvariable=self.name_var, font='Roboto 16', relief='solid', borderwidth=1, fg='#888')
        self.name_entry.grid(column=0, row=1, pady=5)
        def f(e):
            print(e)
            self.name_entry.config(fg='#000')
            self.name_var.set('')
        self.name_entry.bind('<1>', f)

        self.password_var = tkinter.StringVar(value='Contraseña')
        self.password_entry = tkinter.Entry(self.frame, width=14, textvariable=self.password_var, font='Roboto 16', relief='solid', borderwidth=1, fg='#888')
        self.password_entry.grid(column=0, row=2, pady=5)
        def g(e):
            print(e)
            self.password_var.set('')
            self.password_entry.config(show='*', fg='#000')
        self.password_entry.bind('<1>', g)

        self.button = tkinter.Button(self.frame, text='Ingresar', command=self.check, font='Roboto 16 bold', bg='#403E39', relief='flat', bd=3, fg='#FFF')
        self.button.grid(column=0, row=3, pady=10)

        self.message_var = tkinter.StringVar(value='')
        self.message_lbl = tkinter.Label(self.frame, textvariable=self.message_var, bg='#FFF', font='Roboto 12', fg='#A00')
        self.message_lbl.grid(column=0, row=4)

        self.frame.pack(expand=True) 
        self.password_entry.bind('<Return>', self.check)

        # esto genera bugs con el placeholder
        # self.name_entry.bind('<Return>', lambda e: self.password_entry.focus())
        # self.name_entry.focus() 

    def check(self, *e):
        c = self.app.users.check(self.name_var.get())
        if c != []:
            print('** se encontró un usuario con el username', self.name_var.get()) # TODO borar esto debugging
            if self.password_var.get() == c[0][2]:
                print('contraseña Correcta')
                self.app.user = c[0]
                self.pack_forget()
                self.app.charge_topwidgets()
                self.app.pack(fill='both', expand=1)
                return 
        self.message_var.set('Vuelva a intentarlo')

            
