from gui.tools import *
from gui.topwidgets.mainview import basetab
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import tkinter


class Inventory(basetab.BaseTab):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, weight=1, minsize=600)
        self.columnconfigure(2, minsize=400)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, minsize=50)
        self.create_variables()
        self.create_widgets()
        self.update_list()

    def create_widgets(self):
        self.__createlist()
        self.__createcontrols()            

    def __createlist(self):
        style = ttk.Style(self)
        style.configure("Treeview", background=color8, fieldbackground=color8, foreground=color4, font=font5, relief='flat')

        self.list = ttk.Treeview(self, columns=(1, 2, 3, 4), padding=[0,0,0,0])
        self.list.column("#0", stretch=0, width=0)
        self.list.heading("#0", text="id")
        self.list.heading(1, text="Nombre")
        self.list.column(2, stretch=0, width=100, anchor='e')
        self.list.heading(2, text="Precio en pesos")
        self.list.column(3, stretch=0, width=60, anchor='center')
        self.list.heading(3, text="Cantidad")
        self.list.column(4, stretch=0, width=60, anchor='center')
        self.list.heading(4, text="Tienda")


        self.list.grid(column=0, row=0, sticky='nsew', padx=15, pady=15)
        self.list.bind('<ButtonRelease-1>',self.charge_article)

        # ------------------------------

        self.list_controls = tkinter.Frame(self, bg=color8)

        self.search_entry = tkinter.Entry(self.list_controls, width=30, relief='solid', bg=color8, bd=1, font=font5, fg=color5, textvar=self.search_var)
        self.search_entry.pack(side='left', fill='y')
        self.search_entry.bind('<Return>', lambda e: self.search())


        self.search_button = tkinter.Button(self.list_controls, bg=color4, font=font6, fg=color8, relief='flat', command=self.search) 
        try:
            self.search_image = ImageTk.PhotoImage(Image.open('gui/img/search_icon.png'))
        except Exception as e:
            print('no se pudo abrir la imagen', e)
            self.search_button.config(text='Buscar')
        else:
            self.search_button.config(image=self.search_image)
        finally:
            self.search_button.pack(side='left', padx=(5, 0))
    
        self.back_button = tkinter.Button(self.list_controls, bg=color4, font=font6, fg=color8, relief='flat', command=self.update_list)
        try:
            self.back_image = ImageTk.PhotoImage(Image.open('gui/img/back_icon.png'))
        except Exception as e:
            print('no se pudo abrir la imagen', e)
            self.back_button.config(text='Volver')
        else:
            self.back_button.config(image=self.back_image)
        finally:
            self.back_button.pack(side='left', padx=(5, 0))

        self.new_button = tkinter.Button(self.list_controls, text='+ Añadir artículo', bg=color4, font=font6, fg=color8, relief='flat', command=self.create_article)
        self.new_button.pack(side='right')

        self.list_controls.grid(column=0, row=1, sticky='nsew', pady=(0, 15), padx=15)

    def __createcontrols(self):
        self.article_details = tkinter.Frame(self, bg=color8)
        self.article_details.columnconfigure(1, minsize=170)
        self.article_details.rowconfigure(1, minsize=170)
        self.article_details.columnconfigure(0, weight=1)
        self.article_details.rowconfigure(4, weight=1)

        # -------------------------------

        self.name_lbl = tkinter.Label(self.article_details, textvariable=self.name_var, height=1, bg=color8, fg=color4, font=font1, width=22, justify='left')
        self.name_lbl.grid(column=0, row=0, sticky='w', columnspan=2, pady=(0,5))

        # -------------------------------

        self.img_file = None
        self.img_label = tkinter.Label(self.article_details, bg=color8, height=10, relief='raised', bd=3, image=self.img_file)
        self.img_label.grid(column=1, row=1, sticky='nsew')

        # -------------------------------

        self.price_frame = tkinter.Frame(self.article_details, bg=color8)
        self.price_frame.grid(column=0, row=1, sticky='nsew')
        # self.price_frame.columnconfigure(0, minsize=80)
        self.price_frame.columnconfigure(1, weight=1)
        self.price_frame.rowconfigure(0, weight=2)
        self.price_frame.rowconfigure(1, weight=1)
        self.price_frame.rowconfigure(2, weight=1)

        self.price_manual_frame = tkinter.LabelFrame(self.price_frame, text="Precio manual", bg=color8, foreground=color4, font=font6)
        self.price_manual_frame.grid(column=0, row=0, sticky='nsew', columnspan=2, padx=5)
        self.price_manual_lbl = tkinter.Label(self.price_manual_frame, textvariable=self.price_manual_var, bg=color8, font=font2, fg=color2)
        self.price_manual_lbl.pack(fill='both', expand=1)
        self.price_auto_lbl = tkinter.Label(self.price_frame, textvariable=self.price_auto_var, bg=color8, font=font6)
        self.price_auto_lbl.grid(column=1, row=1, sticky='nsew')
        self.price_auto_tag = tkinter.Label(self.price_frame, text="Precio automático", bg=color8, foreground=color4, font=font7)
        self.price_auto_tag.grid(column=0, row=1, sticky='nsew')
        self.cant_lbl = tkinter.Label(self.price_frame, textvariable=self.cant_var, bg=color8, font=font6)
        self.cant_lbl.grid(column=1, row=2, sticky='nsew')
        self.cant_tag = tkinter.Label(self.price_frame, text='Cantidad disponible', bg=color8, foreground=color4, font=font7)
        self.cant_tag.grid(column=0, row=2, sticky='nsew')

        # --------------------------------------

        self.separator = ttk.Separator(self.article_details, orient='horizontal')
        self.separator.grid(column=0, row=2, sticky='ew', columnspan=2, pady=10)

        # --------------------------------------

        self.more_frame = tkinter.Frame(self.article_details, bg=color8)
        self.selling_tag = tkinter.Label(self.more_frame, text='Se vende en:', fg=color4, bg=color8, font=font7)
        self.selling_tag.pack(side='left')
        self.selling_lbl = tkinter.Label(self.more_frame, text='unidad', fg=color4, bg=color8, font=font6)
        self.selling_lbl.pack(side='left')
        self.department_tag = tkinter.Label(self.more_frame, text='', fg=color4, bg=color8, font=font6)
        self.department_tag.pack(side='right')
        self.department_lbl = tkinter.Label(self.more_frame, text='Departamento:', fg=color4, bg=color8, font=font7)
        self.department_lbl.pack(side='right', padx=(80,0))
        self.more_frame.grid(column=0, row=3, columnspan=2)

        # --------------------------------------

        self.notes_var = tkinter.StringVar()
        self.notes_frame = tkinter.Frame(self.article_details, bg=color7)
        self.notes_lbl = tkinter.Label(self.notes_frame, wraplength=400, justify='center', bg=color7, fg=color6, textvariable=self.notes_var)
        self.notes_lbl.pack(expand=True)
        self.notes_frame.grid(column=0, row=4, columnspan=2, sticky='nsew', pady=10)

        # --------------------------------------

        btn_style = {
            'relief': 'flat',
            'font':font6,
            'fg':color8,
            'padx':10
            }
        self.details_buttons = tkinter.Frame(self.article_details, bg=color8)
        self.details_buttons.columnconfigure(2, weight=1)
        #self.details_buttons.columnconfigure(4, weight=1)
        self.sell_spin = ttk.Spinbox(self.details_buttons, from_ = 1, to=99, width=5, font=font5, textvariable=self.sell_var)
        self.sell_spin.grid(row=0, column=0)
        self.sell_btn = tkinter.Button(self.details_buttons, command=self.sell_article, text='Vender', bg=color2, **btn_style)
        self.sell_btn.grid(row=0, column=1, padx=2)
        self.delete_btn = tkinter.Button(self.details_buttons, command=self.delete_article, text='Borrar', bg=color1, **btn_style)
        self.delete_btn.grid(row=0, column=4, padx=2)
        self.edit_btn = tkinter.Button(self.details_buttons, command=self.edit_article, text='Editar', bg=color4, **btn_style)
        self.edit_btn.grid(row=0, column=3, padx=2)
        self.details_buttons.grid(column=0, row=5, sticky='we', columnspan=2, pady=(5,0))

        # --------------------------------------

        self.article_details.grid(column=2, row=0, rowspan=2, sticky='nsew', pady=15, padx=(0, 15))

    def update_list(self):
        print('Debug: update_list')
        self.clear_list()
        for i in self.app.products.get_all():
            self.list.insert("", 'end', text=i[0], values=(i[1], i[4], i[5], i[6]))

    def charge_article(self, *e):
        print('Debug: charge_article')
        if self.list.focus() == None or self.list.focus() == '':
            self.clean_variables()
            return
        else:
            self.list_focus_id = self.list.item(self.list.focus())['text']
            self.update_variables()

    def create_variables(self):
        print('Debug: create_variables')
        self.list_focus_id = None
        self.name_var = tkinter.StringVar()
        self.price_auto_var = tkinter.StringVar()
        self.price_manual_var = tkinter.StringVar()
        self.cant_var = tkinter.IntVar()
        self.department_var = tkinter.StringVar()
        self.sell_var = tkinter.StringVar(value='1')
        self.search_var = tkinter.StringVar()

    def update_variables(self):
        print('Debug: update_variables')
        # if self.list_focus_id == '' or self.list_focus_id == None :
        #     print('\tNo se detectó ningun articulo seleccionado')
        #     return

        print(f'\tid seleccionado: {self.list_focus_id}')
        l = self.app.products.get(self.list_focus_id)[1:]
        print(f'\tl = {l}')

        self.name_var.set(l[0][:22])
        self.cant_var.set(l[4])
        price = float(l[1])+(float(l[1]) * self.app.ganancia)   # Variable global del porcentaje de ganancia
        if True:# TODO comprobar si esta en modo pesos o usd
            try: self.price_manual_var.set('{:,.0f} COP'.format(l[3]))
            except: self.price_manual_var.set('Sin precio')
            try: self.price_auto_var.set('{:,.0f} COP'.format(price * self.app.usd))  # TODO ponerlo como variable global
            except: self.price_auto_var.set('Sin precio')
        else:
            try: self.price_manual_var.set('{:,.0f} USD'.format(l[2]))
            except: self.price_manual_var.set('Sin precio')
            try: self.price_auto_var.set('{:,.0f} USD'.format(price))  # TODO ponerlo como variable global
            except: self.price_auto_var.set('Sin precio')

        if l[5] != None:
            self.department_tag.config(text=l[5].capitalize())  # TODO comprobar
        else:
            self.department_tag.config(text='')

        if l[7] != None:
            self.notes_var.set(l[0] + '\n' + str(l[7]))
        else:
            self.notes_var.set(l[0])

        try:
            self.img_file = ImageTk.PhotoImage(Image.open(self.app.resources + l[8]).resize((165, 165), Image.ANTIALIAS))
        except:
            self.img_file = None
        else:
            self.img_label.config(image=self.img_file)

        print('\tYa se cargaron todos los elementos del articulo')

    def clean_variables(self):
        print('Debug: clean_variables')
        self.name_var.set('')
        self.price_auto_var.set('')
        self.price_manual_var.set('')
        self.cant_var.set(0)
        self.department_var.set('')
        self.notes_var.set('')
        self.img_file = None
        self.list_focus_id = None

    def sell_article(self):
        print('Debug: sell_article')
        if self.list_focus_id == None or self.list_focus_id == '':
            messagebox.showinfo(title="Seleccione un artículo", message="Primero seleccione el artículo en la lista y luego presione vender")
            print('\tNo se detectó ningun articulo seleccionado')
            return

        print(f'\tid seleccionado: {self.list_focus_id}')
        l = [x for x in self.app.products.get(self.list_focus_id)]
        try: s = int(self.sell_var.get())
        except: messagebox.showerror(title="Error al vender", message="ingrese un número válido para venta")
        if s < 1:
            print('\tno puedes vender 0')   # TODO messagebox aqui
            return
        try:
            if l[5] >= s: l[5] -= s
            elif l[5] <= s: l[5] = 0
        except Exception as e:
            messagebox.showerror(title='Error interno', message='No se ha podido vender el artículo debido a un error interno, quedará igual')
            print('Error', e, 'l =', l) # TODO mandar error
            return
        
        # agregar venta a lista de ventas en base de datos
        self.app.products.update(*l)
        messagebox.showinfo(title='Vendido', message=f'Se vendió {s} {l[1]}')
        self.update_list()
        self.clean_variables()
        # TODO recargar articulo en lista y en detalles
        self.sell_var.set(1) # limpiar tambien el spinbox

    def clear_list(self):
        print('Debug: clear_list')
        for item in self.list.get_children():
            self.list.delete(item)
        print('\tlisto')

    def delete_article(self):
        print('Debug: delete_article')
        if self.list_focus_id == None or self.list_focus_id == '':
            messagebox.showinfo(title="No se pudo elminiar", message="Seleccione primero un artículo de la lista para elminiarlo")
            print('\tno se detectó ningun articulo seleccionado')
            return
        self.app.products.delete(self.list_focus_id)
        self.update_list()
        self.clean_variables()
        print('\tlisto')

    def edit_article(self):
        print('Debug: edit_article')
        if self.list_focus_id == None or self.list_focus_id == '':
            messagebox.showinfo(title="Seleccione un artículo", message="Seleccione primero un artículo de la lista para editarlo")
            print('\tno se detectó articulo seleccionado')
            return # TODO mandar messagebox
        self.app.mainview.tab_edit_article.charge(self.list_focus_id)
        self.app.mainview.set_tab('edit_article')
        print('\tcargado edit_article')

    def create_article(self):
        print('Debug: create_article')
        self.app.mainview.tab_edit_article.create()
        self.app.mainview.set_tab('edit_article')

    def search(self):
        print('Debug: search')
        if self.search_var.get() == '':
            messagebox.showinfo(title="Búsqueda", message='Escriba primero un texto muy corto en el cuadro de búsqueda.')
            self.update_list()
            return

        self.clear_list()
        l = self.app.products.search(self.search_var.get())
        if l == []:
            print('no se consiguio nada')
            messagebox.showerror(title="Sin resultados", message="Intente escribiendo sólo las primeras letras del nombre del artículo o con otras formas de llamarle.")
            self.update_list()
        else:
            for i in l:
                self.list.insert("", 'end', text=i[0], values=(i[1], i[4], i[5], i[6]))
        self.search_var.set('')
        self.clean_variables()
        print('\tsearch listo')

