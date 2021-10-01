from gui.tools import ListboxWithAutoscroll, font1
from gui.topwidgets.mainview import basetab
import tkinter


class Inventory(basetab.BaseTab):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # List frame and list controls
        self.list_frame = tkinter.Frame(self, bg='#EEEEEE')
        self.list = ListboxWithAutoscroll(self.list_frame, self.charge_article)  # TODO list_bind
        self.list_order_var = tkinter.StringVar()
        self.list_order_btn = tkinter.OptionMenu(self.list_frame, self.list_order_var,
                                                 *["nombre", "precio", "cantidad", "tienda"])
        self.list_update_btn = tkinter.Button(self.list_frame, text="Actualizar",
                                              command=lambda: self.update_list(self.list_order_var.get()))

        # details and text boxes
        self.details_frame = tkinter.Frame(self, bg='#EEE', bd=5)

        self.details_name_frm = tkinter.Frame(self.details_frame, bg="#EEE")
        self.details_name_var = tkinter.StringVar()
        self.details_name_lbl = tkinter.Label(self.details_name_frm, text='Nombre:', bg='#EEE', font=font1)
        self.details_name_box = tkinter.Entry(self.details_name_frm, textvariable=self.details_name_var, bd=0)

        self.details_provider_frm = tkinter.Frame(self.details_frame, bg="#EEE")
        self.details_provider_var = tkinter.StringVar()
        self.details_provider_lbl = tkinter.Label(self.details_provider_frm, text='Proveedor:', bg='#EEE', font=font1)
        self.details_provider_box = tkinter.Entry(self.details_provider_frm, textvariable=self.details_provider_var, bd=0)

        self.details_shop_frm = tkinter.Frame(self.details_frame, bg="#EEE")
        self.details_shop_var = tkinter.StringVar()
        self.details_shop_lbl = tkinter.Label(self.details_shop_frm, text='Tienda:', bg='#EEE', font=font1)
        self.details_shop_box = tkinter.OptionMenu(self.details_shop_frm, self.details_shop_var,
                                                   *["ferreteria", "motos", "refrigeracion", "otro"])

        self.details_units_frm = tkinter.Frame(self.details_frame, bg="#EEE")
        self.details_units_var = tkinter.StringVar()
        self.details_units_lbl = tkinter.Label(self.details_units_frm, text='Unidades:', bg='#EEE', font=font1)
        self.details_units_box = tkinter.Entry(self.details_units_frm, textvariable=self.details_units_var, bd=0)

        self.details_notes_frm = tkinter.Frame(self.details_frame, bg="#EEE")
        self.details_notes_var = tkinter.StringVar()
        self.details_notes_lbl = tkinter.Label(self.details_notes_frm, text='Anotaciones:', bg='#EEE', font=font1)
        self.details_notes_box = tkinter.Entry(self.details_notes_frm, textvariable=self.details_notes_var, bd=0)

        self.price_buy_frm = tkinter.Frame(self.details_frame, bg="#EEE")
        self.price_buy_var = tkinter.StringVar()
        self.price_buy_lbl = tkinter.Label(self.price_buy_frm, text='Precio de compra (USD):', bg='#EEE', font=font1)
        self.price_buy_box = tkinter.Entry(self.price_buy_frm, textvariable=self.price_buy_var, bd=0)
        self.price_buy_box.bind("<KeyRelease>", self.update_price)

        self.price_usd_frm = tkinter.Frame(self.details_frame, bg="#EEE")
        self.price_usd_var = tkinter.StringVar()
        self.price_usd_lbl = tkinter.Label(self.price_usd_frm, text='Precio de venta (USD):', bg='#EEE', font=font1)
        self.price_usd_box = tkinter.Label(self.price_usd_frm, textvariable=self.price_usd_var, bd=0, bg="#EEE", fg='#595')

        self.price_cop_frm = tkinter.Frame(self.details_frame, bg="#EEE")
        self.price_cop_var = tkinter.StringVar()
        self.price_cop_lbl = tkinter.Label(self.price_cop_frm, text='Precio de venta (COP):', bg='#EEE', font=font1)
        self.price_cop_box = tkinter.Label(self.price_cop_frm, textvariable=self.price_cop_var, bd=0, bg="#EEE", fg='#595')

        # frame for controls
        self.controls_frame = tkinter.Frame(self, bg="#EEE")
        self.controls_new_btn = tkinter.Button(self.controls_frame, bd=0, bg="#FFF",
                                               text="Guardar datos como nuevo articulo")
        self.controls_del_btn = tkinter.Button(self.controls_frame, bd=0, bg="#FFF", text="Borrar este articulo")
        self.controls_sel_btn = tkinter.Button(self.controls_frame, bd=0, bg="#FFF", text="Vender una unidad")
        self.controls_upd_btn = tkinter.Button(self.controls_frame, bd=0, bg="#FFF",
                                               text="Guardar cambios en este articulo")

        self.charge_inventory()
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.config(bg='#EEEEEE')

        # List frame and list controls
        self.list_frame.grid(row=0, column=0, sticky='nsew', rowspan=2, padx=5, pady=5)

        self.list.listbox.config(bd=0, relief='flat', bg='#FFF')
        self.list.pack(fill='both', expand=1)

        self.list_order_var.set("nombre")
        self.list_order_btn.config(bg='#FFF', bd=0, relief='flat')
        self.list_order_btn.pack(side='left', fill='x', expand=1, pady=(5, 0), padx=(0, 2))

        self.list_update_btn.config(bg='#FFF', bd=0, relief='flat')
        self.list_update_btn.pack(side='right', fill='x', expand=1, pady=(5, 0))

        # details and text boxes
        self.details_frame.columnconfigure(0, weight=1)
        self.details_frame.columnconfigure(1, weight=1)
        self.details_frame.columnconfigure(2, weight=1)
        self.details_frame.grid(column=1, row=0, sticky='nsew', padx=(0, 5), pady=5)

        self.details_name_frm.grid(column=0, row=0, columnspan=3, sticky='nsew')
        self.details_name_frm.columnconfigure(1, weight=1)
        self.details_name_lbl.grid(column=0, row=0, padx=(0, 5), pady=5)
        self.details_name_box.grid(column=1, row=0, sticky='nsew', pady=5)

        self.details_provider_frm.grid(column=0, row=1, sticky='nsew')
        self.details_provider_frm.columnconfigure(1, weight=1)
        self.details_provider_lbl.grid(column=0, row=0, padx=(0, 5), pady=5)
        self.details_provider_box.grid(column=1, row=0, sticky='nsew', pady=5)

        self.details_shop_frm.grid(column=1, row=1, sticky='nsew')
        self.details_shop_frm.columnconfigure(1, weight=1)
        self.details_shop_var.set("otro")  # TODO delete this after do db
        self.details_shop_lbl.grid(column=0, row=0, padx=(10, 5), pady=5)
        self.details_shop_box.config(bd=0, bg='#FFF')
        self.details_shop_box.grid(column=1, row=0, sticky='nsew', pady=5)

        self.details_units_frm.grid(column=2, row=1, sticky='nsew')
        self.details_units_frm.columnconfigure(1, weight=1)
        self.details_units_lbl.grid(column=0, row=0, padx=(10, 5), pady=5)
        self.details_units_box.grid(column=1, row=0, sticky='nsew', pady=5)

        self.details_notes_frm.grid(column=0, row=4, columnspan=3, sticky='nsew')
        self.details_notes_frm.columnconfigure(0, weight=1)
        self.details_notes_lbl.grid(column=0, row=0, pady=(20, 5), sticky='ew')
        self.details_notes_box.grid(column=0, row=1, sticky='nsew', pady=(0, 5))

        self.price_buy_frm.grid(column=0, row=3, sticky='nsew')
        self.price_buy_frm.columnconfigure(0, weight=1)
        self.price_buy_lbl.grid(column=0, row=0, pady=(20, 5), sticky='ew')
        self.price_buy_box.grid(column=0, row=1, sticky='ns', pady=(0, 5))

        self.price_usd_frm.grid(column=1, row=3, sticky='nsew')
        self.price_usd_frm.columnconfigure(0, weight=1)
        self.price_usd_lbl.grid(column=0, row=0, pady=(20, 5), sticky='ew')
        self.price_usd_box.grid(column=0, row=1, sticky='ns', pady=(0, 5))

        self.price_cop_frm.grid(column=2, row=3, sticky='nsew')
        self.price_cop_frm.columnconfigure(0, weight=1)
        self.price_cop_lbl.grid(column=0, row=0, pady=(20, 5), sticky='ew')
        self.price_cop_box.grid(column=0, row=1, sticky='ns', pady=(0, 5))

        # Controls
        self.controls_frame.grid(column=1, row=1, sticky='nsew', pady=(0, 5))
        self.controls_frame.columnconfigure(0, weight=1)
        self.controls_frame.columnconfigure(1, weight=1)
        self.controls_sel_btn.grid(column=0, row=0, sticky='nsew', padx=(0, 5))
        self.controls_upd_btn.grid(column=1, row=0, sticky='nsew', padx=(0, 5))
        self.controls_del_btn.grid(column=0, row=1, sticky='nsew', padx=(0, 5), pady=(5, 0))
        self.controls_new_btn.grid(column=1, row=1, sticky='nsew', padx=(0, 5), pady=(5, 0))

    def update_list(self, by):
        print(f"updated list by: {by}")

    def update_price(self, *e):
        try:
            n = float(self.price_buy_var.get().replace(',', '.'))
        except ValueError:
            self.app.statusbar.showmessage("Revisa el precio. Incluye solo numeros y puntos en el precio de compra.")
        else:
            x = n + (n * 0.3)  # TODO make this a global variable at app
            self.price_usd_var.set("{0:.2f}$".format(x))
            self.price_cop_var.set("{0:,.2f}cop".format(x * 3200))  # TODO make this a global variable at app

    def charge_article(self, *e):
        print(e)  # TODO FIX SELECTING WITH KEYBOARD
        try:
            article = self.list.listbox.get('anchor')
            id = int(article.split(' - ')[0])  # obtain the id from the text
        except ValueError:
            raise  # TODO There can be a show info message
        else:
            article = self.app.products.get(id)[0]
            print(article)
            if article:
                self.details_name_var.set(article[1])
                self.details_units_var.set(article[2])
                self.price_buy_var.set(article[3])
                self.details_shop_var.set(article[4])
                self.details_provider_var.set(article[5])
                self.details_notes_var.set(article[6])
                self.update_price()


    def insert_into_list(self, *args):
        self.list.listbox.delete(0, 'end')
        for i in args:
            self.list.listbox.insert('end', "{0} - {1} ({2} disponibles)".format(
                i[0], i[1], i[2]))

    def charge_inventory(self):
        products = self.app.products.get_all()
        if products:
            self.insert_into_list(*products)
            return
        self.list.listbox.insert('end', "No hay articulos")
