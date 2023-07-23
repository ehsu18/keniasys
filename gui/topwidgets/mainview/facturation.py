from gui.topwidgets.mainview import basetab
from gui.tools import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import tkinter


class Facturation(basetab.BaseTab):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, weight=1, minsize=600)
        self.columnconfigure(2, minsize=400)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, minsize=50)
        self.create_variables()
        self.create_widgets()
        self.update_list()
        self.normal_mode()

    def create_widgets(self):
        self.__createlist()
        self.__createcontrols() 

    def __createlist(self):
        style = ttk.Style(self)
        style.configure("Treeview", background=color8, fieldbackground=color8, foreground=color4, font=font5, relief='flat')

        self.list = ttk.Treeview(self, columns=(1, 2, 3, 4, 5), padding=[0,0,0,0])
        self.list.column("#0", stretch=0, width=0)
        self.list.heading("#0", text="id")
        self.list.column(1, stretch=0, width=90, anchor='center')
        self.list.heading(1, text="Fecha")
        self.list.heading(2, text="Artículo")
        self.list.column(3, stretch=0, width=40, anchor='e')
        self.list.heading(3, text="Cant.")
        self.list.column(4, stretch=0, width=100, anchor='e')
        self.list.heading(4, text="Total")
        self.list.column(5, stretch=0, width=100, anchor='w')
        self.list.heading(5, text="Nota")


        self.list.grid(column=0, row=0, sticky='nsew', padx=15, pady=15)
        self.list.bind('<ButtonRelease-1>',self.list_select)

        # ------------------------------

        self.list_controls = tkinter.Frame(self, bg=color8)

        self.search_entry = tkinter.Entry(self.list_controls, width=30, relief='solid', bg=color8, bd=1, font=font5, fg=color5) # , textvar=self.search_var)
        self.search_entry.pack(side='left', fill='y')
        self.search_entry.bind('<Return>', self.search)


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

        self.del_button = tkinter.Button(self.list_controls, text='Eliminar', bg=color1, font=font6, fg=color8, relief='flat', command=self.delete_venta) #, command=self.create_article)
        self.del_button.pack(side='right', padx=5)
        self.edit_button = tkinter.Button(self.list_controls, text='Editar', bg=color4, font=font6, fg=color8, relief='flat', command=self.charge_venta) #, command=self.create_article)
        self.edit_button.pack(side='right')

        self.list_controls.grid(column=0, row=1, sticky='nsew', pady=(0, 15), padx=15)

    def __createcontrols(self):
        self.article_details = tkinter.Frame(self, bg=color8)
        self.article_details.columnconfigure(0, weight=1)
        # self.article_details.columnconfigure(1, weight=1)
        self.article_details.columnconfigure(2, weight=1)
        self.article_details.columnconfigure(3, weight=1)
        self.article_details.columnconfigure(5, weight=1)
        #self.article_details.rowconfigure(0, weight=1)
        self.article_details.rowconfigure(7, weight=1)
        # self.article_details.columnconfigure(0, weight=1)
        # self.article_details.rowconfigure(5, weight=1)

        self.title = tkinter.Label(self.article_details, bg=color8, text="Añadiendo venta", font=font1)
        self.title.grid(column=0, row=0, sticky='sw', columnspan=5)

        # ------------------------------------

        self.description_tag = tkinter.Label(self.article_details, bg=color8, text='Descripción', font=font7)
        self.description_tag.grid(column=0, row=1, sticky='w', pady=10)
        self.description_entry = tkinter.Entry(self.article_details, bg=color8, font=font4, textvariable=self.description_var)
        self.description_entry.grid(column=1, row=1, sticky='nsew', columnspan=4, pady=(0, 10))

        # ------------------------------------

        self.cant_tag = tkinter.Label(self.article_details, bg=color8, text="Cantidad", font=font7)
        self.cant_tag.grid(column=0, row=2, sticky='w', pady=(0, 0))
        self.cant_entry = tkinter.Entry(self.article_details, bg=color8, font=font7, width=10, textvariable=self.cant_var)
        self.cant_entry.grid(column=1, row=2, sticky='ns', pady=(0, 0))

        self.total_tag = tkinter.Label(self.article_details, bg=color8, text="Total", font=font7)
        self.total_tag.grid(column=2, row=2, sticky='w', pady=(0, 0), padx=(10, 0))
        self.total_entry = tkinter.Entry(self.article_details, bg=color8, font=font7, textvariable=self.total_var)
        self.total_entry.grid(column=3, row=2, columnspan=2, sticky='nsew', pady=(0, 0))

        # ------------------------------------

        self.separator = ttk.Separator(self.article_details, orient='horizontal')
        self.separator.grid(column=0, row=3, sticky='ew', columnspan=5, pady=10)

        # ------------------------------------

        self.date_tag = tkinter.Label(self.article_details, bg=color8, text="Fecha", font=font7)
        self.date_tag.grid(column=0, row=4, sticky='w')
        self.date_entry = tkinter.Entry(self.article_details, bg=color8, font=font7, width=10, textvariable=self.date_var)
        self.date_entry.grid(column=1, row=4, sticky='nsew', pady=0)

        # -------------------------------------

        self.notes_frame = tkinter.Frame(self.article_details, bg=color8)
        self.notes_frame.columnconfigure(0, weight=1)
        self.notes_frame.rowconfigure(1, weight=1)
        self.notes_tag = tkinter.Label(self.notes_frame, text="Notas / Observaciones", font=font7, bg=color8)
        self.notes_tag.grid(column=0, row=0, sticky='w', pady=(0, 5))
        self.notes_text = tkinter.Text(self.notes_frame, font=font5, height=3, width=42, relief='solid', bd=1)
        self.notes_text.grid(column=0, row=1, columnspan=5, sticky='n')
        self.notes_frame.grid(column=0, row=5, columnspan=5, sticky='nsew', pady=10)

        
        # self.notes_lbl = tkinter.Label(self.notes_frame, wraplength=400, justify='center', bg=color7, fg=color6) #, textvariable=self.notes_var)
        # self.notes_lbl.pack(expand=True)
        # s
        # self.notes_lbl['text'] = 'Prueba de texto'

        # -------------------------------------

        self.btn_frame = tkinter.Frame(self.article_details, bg=color8)
        self.btn_frame.grid(row=6, column=0, columnspan=5, sticky='nsew', pady=(5, 0))
        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)

        self.save_btn = tkinter.Button(self.btn_frame, text='Añadir', bg=color2, relief='flat', fg=color8, font=font6)
        self.save_btn.grid(row=0, column=0, sticky='ew', pady=(0, 0))
        self.cancel_btn = tkinter.Button(self.btn_frame, text='Cancelar', bg=color1, relief='flat', fg=color8, font=font6, command=self.cancel)
        self.cancel_btn.grid(row=0, column=1, sticky='ew', pady=(0, 0), padx=(5, 0))

        # -------------------------------------

        self.article_details.grid(column=2, row=0, rowspan=2, sticky='nsew', pady=15, padx=(0, 15))


    def list_select(self, *e):
        if self.list.focus() == None or self.list.focus() == '':
            self.list_focus_id = None
        else:
            self.list_focus_id = int(self.list.item(self.list.focus())['text'])

    def charge_venta(self, *e):
        print('FACTURATION: charge_venta', self.list.focus())
        if self.list.focus() == None or self.list.focus() == '':
            print("charge_venta entro en if")
            # self.clean_variables()
            self.cancel()
            messagebox.showinfo(title="Seleccione una venta", message="Debe seleccionar una venta anterior en la tabla para poder editarla")
            return
        else:
            print("\tcargando venta de la lista")

            self.edit_mode()
            self.clean_variables()
            self.list_focus_id = int(self.list.item(self.list.focus())['text'])
            self.update_variables()

    def edit_mode(self):
        self.save_btn['text'] = "Guardar"
        self.save_btn['command'] = self.update_venta
        self.title['text'] = "Editando venta"

    def normal_mode(self):
        self.save_btn['text'] = "Añadir"
        self.save_btn['command'] = self.insert_venta
        self.title['text'] = "Nueva venta"        

    def cancel(self):
        self.clean_variables()
        self.normal_mode()
        self.update_list()
        self.list_focus_id = None

    def delete_venta(self):
        if self.list_focus_id == None: 
            messagebox.showinfo(title='No se pudo elminar', message="Debe seleccionar primero una venta")
            return

        try: self.app.ventas.delete(self.list_focus_id)
        except Exception as e: messagebox.showerror(title="No se pudo eliminar", message=e)
        else: messagebox.showinfo(title="Venta eliminada", message="La venta se eliminó satisfactoriamente")

        self.cancel()

    def update_venta(self): # TODO reformat
        
        c = self.check_variables()
        if c != True:
            messagebox(title="No se pudo guardar", message=c)
            return

        print('updating venta id:', self.list_focus_id)
        l = [x for x in self.app.ventas.get(self.list_focus_id)]

        if l[1] != None:
            if self.description_var.get() != self.app.products.get(l[1]):
                pass
            else:
                l[1] = None
                l[2] = self.description_var.get()
        else:
            l[2] = self.description_var.get()

        l[3] = self.cant_var.get()
        l[4] = self.total_var.get()
        l[5] = self.date_var.get()
        l[6] = self.notes_text.get(0.0, 'end')[:-1]

        try:
            self.app.ventas.update(*l)
        except Exception as e:
            # raise 
            messagebox.showerror(title="Error interno", message=f"No se pudieron guardar los cambios a esta venta debido a un error interno, se quedará como estaba.\n[{e}]")
        else:
            messagebox.showinfo(title="Venta actualizada", message="Los datos de la venta se actualizaron correctamente")
            self.cancel()

    def insert_venta(self):
        c = self.check_variables()
        if c != True:
            messagebox.showerror(title='No se pudo agregar la venta', message=c)
            return

        l = [
            None,
            self.description_var.get(),
            self.cant_var.get(),
            self.total_var.get(),
            self.date_var.get(),
        ]

        if self.notes_text.get(0.0, 'end')[:-1] == '': l.append(None)
        else: l.append(self.notes_text.get(0.0, 'end')[:-1])

        try: self.app.ventas.insert(*l); self.cancel()
        except Exception as e: messagebox.showerror(title='Error guardando', message=e)
        else: messagebox.showinfo(title="Venta añadida", message=f"Se guardó correctamente la venta del {l[1]}")

    def create_variables(self):
        print('Debug: create_variables Facturation')
        self.list_focus_id = None
        self.description_var = tkinter.StringVar()
        self.cant_var = tkinter.IntVar()
        self.total_var = tkinter.DoubleVar()
        self.notes_var = tkinter.StringVar()
        self.date_var = tkinter.StringVar()
        self.search_var = tkinter.StringVar()

    def update_variables(self):
        print('update', type(self.list_focus_id))
        print('update_variables', self.list_focus_id)

        l = self.app.ventas.get(self.list_focus_id)

        if l[1] != None: self.description_var.set(self.app.products.get(l[1])[1])        
        else: self.description_var.set(l[2])

        if l[3] == None: self.cant_var.set(0)
        else: self.cant_var.set(l[3])

        if l[4] == None: self.total_var.set(0)
        else: self.total_var.set(l[4])

        if l[5] == None: self.date_var.set("Sin fecha")
        else: self.date_var.set(l[5])

        if l[6] != None: self.notes_text.insert('end', l[6])

    def check_variables(self):
        return True

    def clean_variables(self):
        print('clean')
        # self.list_focus_id = None
        self.description_var.set('')
        self.cant_var.set(0)
        self.total_var.set(0)
        # self.notes_var.set('')
        self.notes_text.delete(0.0,'end')
        self.date_var.set('')
        # self.search_var.set('')

    def update_list(self):
        print('facturation: update_list')
        self.clear_list()
        for i in self.app.ventas.get_all():
            if i[1] == None :
                self.list.insert("", 'end', text=i[0], values=(i[5], i[2], i[3], i[4], i[6]))
            else:
                self.list.insert("", 'end', text=i[0], values=(i[5], self.app.products.get(i[1])[1], i[3], i[4], i[6]))

    def clear_list(self):
        print('Debug: clear_list')
        for item in self.list.get_children():
            self.list.delete(item)

    def search(self, *e):
        print('facturation: search')
        if self.search_entry.get() == '':
            messagebox.showinfo(title="Búsqueda", message='Escriba primero un texto muy corto en el cuadro de búsqueda.')
            # self.update_list()
            return

        l = self.app.ventas.search(self.search_entry.get())
        if l == []: messagebox.showerror(title="Sin resultados", message="Intente escribiendo sólo las primeras letras del nombre del artículo o con otras formas de llamarle.")
            # self.update_list()
        else:
            self.clear_list()
            for i in l:
                if i[1] == None: self.list.insert("", 'end', text=i[0], values=(i[5], i[2], i[3], i[4], i[6]))
                else: self.list.insert("", 'end', text=i[0], values=(i[5], self.app.products.get(i[1])[1], i[3], i[4], i[6]))

        self.search_var.set('')
        self.clean_variables()
