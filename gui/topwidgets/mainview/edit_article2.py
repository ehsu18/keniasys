from gui.tools import *
from gui.topwidgets.mainview import basetab
from PIL import ImageTk, Image
from tkinter import ttk, filedialog, messagebox
import tkinter
import os

class EditArticle(basetab.BaseTab):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(bg=color8)
        self.create_variables()
        self.create_widgets()

    def create_widgets(self):
        self.rowconfigure(0, weight=1)
        # self.rowconfigure(1)
        self.rowconfigure(3, weight=1)

        self.columnconfigure(0, weight=1)
        # self.columnconfigure(1)
        # self.columnconfigure(2)
        self.columnconfigure(3, weight=1)

        self.create_controls()
        self.details()
        self.more()

        # self.btn = tkinter.Button(self, command=self.close, text="Volver")
        # self.btn.grid(column=1, row=4, columnspan=2)

    def create_controls(self):
        self.controls = tkinter.Frame(self, bg=color8)
        self.controls.grid(column=1, row=1, columnspan=2, sticky='nsew', pady=15)

        self.prev_btn = tkinter.Button(self.controls, command=self.prev, width=8, text='Anterior', bg=color4, fg=color8, font=font6, relief='flat')
        self.prev_btn.pack(side='left', padx=0)
        self.next_btn = tkinter.Button(self.controls, command=self.next, width=8, text='Siguiente', bg=color4, fg=color8, font=font6, relief='flat')
        self.next_btn.pack(side='left', padx=(5, 0))
        self.title_label = tkinter.Label(self.controls, textvariable=self.title_var, font=font1, bg=color8)
        self.title_label.pack(expand=1, side='left', padx=20)
        self.save_btn = tkinter.Button(self.controls, command=self.save, width=8, text='Guardar', bg=color2, fg=color8, font=font6, relief='flat')
        self.save_btn.pack(side='left', padx=(0, 5))
        self.cancel_btn = tkinter.Button(self.controls, command=self.close, width=8, text='Volver', bg=color1, fg=color8, font=font6, relief='flat')
        self.cancel_btn.pack(side='left', padx=0)

    def details(self):
        self.details_frame = tkinter.Frame(self, bg=color8)
        self.details_frame.grid(column=1, row=2, sticky='nsew', pady=15, padx=(0,15))

        self.miniframe_u = tkinter.Frame(self.details_frame, bg=color8)
        self.miniframe_u.grid(column=0, row=0, columnspan=3, sticky='nsew')
        self.miniframe_u.columnconfigure(1, weight=1)
        self.name_tag = tkinter.Label(self.miniframe_u, text="Nombre", font=font7, bg=color8)
        self.name_tag.grid(column=0, row=0, sticky='w', padx=(0, 5))
        self.name_entry = tkinter.Entry(self.miniframe_u, textvariable=self.name_var, font=font3, relief='solid', bd=1)
        self.name_entry.grid(column=1, row=0, sticky='ew', padx=(15, 0))

        self.separator_1 = ttk.Separator(self.details_frame, orient='horizontal')
        self.separator_1.grid(column=0, row=1, sticky='ew', columnspan=3, pady=15)

        self.sellcop_tag = tkinter.Label(self.details_frame, font=font6, bg=color8, text="Precio de venta en pesos")
        self.sellcop_tag.grid(column=0, row=2, sticky='nsew')
        self.sellcop_entry = tkinter.Entry(self.details_frame, font=font5, textvariable=self.sellcop_var, relief='solid', bd=1, justify='right') # , validatecommand=(self.ckprc, '%P'), validate='key')
        self.sellcop_entry.grid(column=1, row=2, sticky='nsew', padx=15, pady=(0, 5))
        self.sellusd_tag = tkinter.Label(self.details_frame, font=font7, bg=color8, text="Precio de venta en dólares")
        self.sellusd_tag.grid(column=0, row=3, sticky='nsew')
        self.sellusd_entry = tkinter.Entry(self.details_frame, font=font5, textvariable=self.sellusd_var, relief='solid', bd=1, justify='right')
        self.sellusd_entry.grid(column=1, row=3, sticky='nsew', padx=15, pady=5)
        self.buycop_tag = tkinter.Label(self.details_frame, font=font6, bg=color8, text="Precio de compra en pesos")
        self.buycop_tag.grid(column=0, row=4, sticky='nsew')
        self.buycop_entry = tkinter.Entry(self.details_frame, font=font5, textvariable=self.buycop_var, relief='solid', bd=1, justify='right')
        self.buycop_entry.grid(column=1, row=4, sticky='nsew', padx=15, pady=5)
        self.buyusd_tag = tkinter.Label(self.details_frame, font=font7, bg=color8, text="Precio de compra en dólares")
        self.buyusd_tag.grid(column=0, row=5, sticky='nsew')
        self.buyusd_entry = tkinter.Entry(self.details_frame, font=font5, textvariable=self.buyusd_var, relief='solid', bd=1, justify='right')
        self.buyusd_entry.grid(column=1, row=5, sticky='nsew', padx=15, pady=5)

        self.details_note = tkinter.Label(self.details_frame, font=font7, bg=color7, fg=color6, text="""Use un punto para
los decimales, no use
caracteres para separar
los miles""")
        self.details_note.grid(column=2, row=2, rowspan=4, sticky='nsew')

        self.separator_2 = ttk.Separator(self.details_frame, orient='horizontal')
        self.separator_2.grid(column=0, row=6, sticky='ew', columnspan=3, pady=15)
    
        self.miniframe_l = tkinter.Frame(self.details_frame, bg=color8)
        self.miniframe_l.grid(column=0, row=7, sticky='nsew')
        self.units_tag = tkinter.Label(self.miniframe_l, text="Cantidad\ndisponible", font=font7, bg=color8)
        self.units_tag.grid(column=0, row=0)
        self.units_entry = tkinter.Entry(self.miniframe_l, font=font2, width=6, relief='solid', bd=1, textvariable=self.units_var, justify='center')
        self.units_entry.grid(column=1, row=0, sticky='ns')
        self.barcode_tag = tkinter.Label(self.miniframe_l, text="Código de barras", font=font7, bg=color8)
        self.barcode_tag.grid(column=0, columnspan=2, row=1, sticky='ew', pady=(10,0))
        self.barcode_entry = tkinter.Entry(self.miniframe_l, font=font5, relief='solid', bd=1, textvariable=self.barcode_var, justify='center')
        self.barcode_entry.grid(column=0, columnspan=2, row=2, sticky='nsew')

        self.miniframe_r = tkinter.Frame(self.details_frame, bg=color8)
        self.miniframe_r.grid(column=1, row=7, columnspan=2, sticky='nsew', padx=(50, 0))
        # ttk.Style().configure("miniframe_r.TCombobox", font=font5, background=color8)

        self.dept_tag = tkinter.Label(self.miniframe_r, text='Departamento', bg=color8)
        self.dept_tag.grid(column=0, row=0, padx=5)
        self.dept_select = ttk.Combobox(self.miniframe_r, textvariable=self.dept_var,
            values = ['motos', 'ferretería', 'electrodomésticos', 'refrigeración']) # TODO cargar esto de bd
        self.dept_select.grid(column=1, row=0, sticky='ew')
        # self.dept_plus = tkinter.Label(self.miniframe_r, text='+', font=font6)
        # self.dept_plus.grid(column=2, row=0)
        self.provider_tag = tkinter.Label(self.miniframe_r, text='Proveedor', bg=color8)
        self.provider_tag.grid(column=0, row=1, pady=(10,0), padx=5)
        self.provider_select = ttk.Combobox(self.miniframe_r, textvariable=self.provider_var,
            values = ['garcía motors'])
        self.provider_select.grid(column=1, row=1, sticky='ew', pady=(10,0))
        self.selling_tag = tkinter.Label(self.miniframe_r, text='Se vende por', bg=color8)
        self.selling_tag.grid(column=0, row=2, pady=(10,0), padx=5)
        self.selling_select = ttk.Combobox(self.miniframe_r, textvariable=self.selling_var,
            values = ['unidad', 'par', 'caja', 'bolsa', 'paquete'])
        self.selling_select.grid(column=1, row=2, sticky='ew', pady=(10,0))


    def more(self):
        self.more_frame = tkinter.Frame(self, bg=color8)
        self.more_frame.grid(column=2, row=2, sticky='nsew', pady=15, padx=0)
        self.more_frame.columnconfigure(0, minsize=170)
        self.more_frame.rowconfigure(0, minsize=170)

        self.img_label = tkinter.Label(self.more_frame, bg=color8, height=10, relief='raised', bd=3, image=self.img_file)
        self.img_label.grid(column=0, row=0, sticky='nsew')
        self.img_side = tkinter.Frame(self.more_frame, bg=color8)
        self.img_side.grid(column=1, row=0, sticky='nsew', padx=(15, 0))
        # TODO select solo los jpg y png
        self.select_img = tkinter.Button(self.img_side, bg=color4, fg=color8, font=font6, text="Seleccionar foto", relief='flat', command=self.select_img)
        self.select_img.pack(fill='x', expand=1)
        self.delete_img = tkinter.Button(self.img_side, bg=color1, fg=color8, font=font6, text="Eliminar foto", relief='flat', command=self.del_img)
        self.delete_img.pack(fill='x', expand=1, pady=(0,5))
        self.note_img = tkinter.Label(self.img_side, bg=color7, fg=color6, font=font7, 
            text="""Seleccione una imagen
en cualquier carpeta
del sistema, esta
será copiada""")
        self.note_img.pack(fill='both', expand=1)
        
        self.notes_tag = tkinter.Label(self.more_frame, text="Notas / Observaciones", font=font7, bg=color8)
        self.notes_tag.grid(column=0, row=1, sticky='w', pady=(15,0))
        self.notes_text = tkinter.Text(self.more_frame, font=font5, height=6, width=40, relief='solid', bd=1)
        self.notes_text.grid(column=0, row=2, columnspan=2, sticky='s')

    def close(self):
        self.app.mainview.tab_inventory.update_list()
        self.app.mainview.tab_inventory.clean_variables()
        self.app.mainview.set_tab('inventory')
        self.clear()

    def save(self):
        c = self.comprobe() # revisar si todos los valores estan bien puestos
        if c != True:
            messagebox.showerror(title="Error guardando artículo", message=c)
            return

        # crear plantilla 
        l = [None for x in range(11)]
        if self.id_var.get() > 0: l[0] = self.id_var.get()
        l[5] = 0
 
        # revisando cada valor y asignando
        if self.name_var.get() != '': l[1] = self.name_var.get()

        if self.buycop_var.get() == 0: l[2] = float(self.buyusd_var.get())
        else: l[2] = float(self.buycop_var.get()) / self.app.usd
        if l[2] == 0.0: l[2] = None


        if self.sellusd_var.get() != 0: l[3] = self.sellusd_var.get()
        if self.sellcop_var.get() != 0: l[4] = self.sellcop_var.get()

        if self.units_var.get() != 0: l[5] = self.units_var.get()
        if self.dept_var.get() != '': l[6] = self.dept_var.get()
        if self.provider_var.get() != '': l[7] = self.provider_var.get()
        if self.notes_text.get(0.0, 'end')[:-1] != '': l[8] = self.notes_text.get(0.0, 'end')[:-1]  # borra el salto de linea al final

        if self.copy_img(self.img_var.get()): l[9] = self.img_var.get().split('/')[-1] # para esto debe ser el path
        else: l[9] = None
        if self.barcode_var.get() != '': l[10] = self.barcode_var.get()
        

        # debugging
        for i in l:
            if i == 'None':
                messagebox.showerror(title='Error interno',
                                    message=f'No se podrá guardar el artículo por un error interno. \nNone detectado {l}')
                return

        try:
            if l[0] != None: self.app.products.update(*l)
            else:
                self.app.products.insert(*l[1:])
            messagebox.showinfo(title="Se guardó correctamente",
                                message=f"Se guardaron los datos del artículo \"{self.name_var.get()}\"")
        except Exception as e:
            messagebox.showerror(title="No se pudo guardar",
                                message=f"Hubo un error inesperado guardando: \"{self.name_var.get()}\"\n[{e}]\n{l}")

        if l[0] == None: self.clear()
    def prev(self):
        print('prev')
        if self.id_var.get() == 0: return
        l = [x for x in self.app.mainview.tab_inventory.list.get_children()][::-1]
        i = 0

        count = 0
        for i in l:
            count += 1
            item = self.app.mainview.tab_inventory.list.item(i)['text']
            if item == self.id_var.get():
                try:
                    self.charge(self.app.mainview.tab_inventory.list.item(l[count])['text'])
                    return
                except:
                    break

        messagebox.showinfo(title="Fin de la lista", message="No quedan artículos en la lista, realice otra búsqueda o recargue la lista principal para poder editar más artículos")

    def next(self):
        print('next')
        if self.id_var.get() == 0: return
        l = self.app.mainview.tab_inventory.list.get_children()
        i = 0

        count = 0
        for i in l:
            count += 1
            item = self.app.mainview.tab_inventory.list.item(i)['text']
            if item == self.id_var.get():
                try:
                    self.charge(self.app.mainview.tab_inventory.list.item(l[count])['text'])
                    return
                except:
                    break

        messagebox.showinfo(title="Fin de la lista", message="No quedan artículos en la lista, realice otra búsqueda o recargue la lista principal para poder editar más artículos")

    def del_img(self):
        self.img_var.set('')
        self.img_file = None

    def select_img(self):
        path = filedialog.askopenfilename()
        if path == '':
            print('no se recibio nada')
            self.img_var.set(None)
            return
        else:
            try:
                self.img_file = ImageTk.PhotoImage(Image.open(path).resize((165, 165), Image.ANTIALIAS))
            except Exception as e:
                self.img_file = None ; print('error cargando img', path, e)
                # TODO mensaje aqui
            else:
                self.img_label.config(image=self.img_file)
                self.img_var.set(path)
                # TODO copiar la imagen al directorio resources

    def create_variables(self):
        self.title_var = tkinter.StringVar()
        self.id_var = tkinter.IntVar()
        self.name_var = tkinter.StringVar()
        self.sellcop_var = tkinter.DoubleVar()
        self.sellusd_var = tkinter.DoubleVar()
        self.buycop_var = tkinter.DoubleVar()
        self.buyusd_var = tkinter.DoubleVar()
        self.units_var = tkinter.IntVar()
        self.dept_var = tkinter.StringVar()
        self.provider_var = tkinter.StringVar()
        self.selling_var = tkinter.StringVar()
        # self.notes_var = tkinter.StringVar()
        self.img_var = tkinter.StringVar()
        self.barcode_var = tkinter.StringVar()
        self.img_file = None
        # self.ckprc = self.app.root.register(checkprice)

    def clear(self):
        self.title_var.set('')
        self.id_var.set(0)
        self.name_var.set('')
        self.sellcop_var.set(0)
        self.sellusd_var.set(0)
        self.buycop_var.set(0)
        self.buyusd_var.set(0)
        self.units_var.set(0)
        self.dept_var.set('')
        self.provider_var.set('')
        self.selling_var.set('')
        # self.notes_var.set('')
        self.img_var.set('')
        self.barcode_var.set('')
        self.notes_text.delete(0.0,'end')
        self.img_file = None

    def charge(self, id):
        self.clear()
        l = [x for x in self.app.products.get(id)]
        self.id_var.set(int(id)) 
        self.title_var.set(f"Editando artículo - ID {id}")

        if l[1] != None: self.name_var.set(l[1])  # nombre
        try: self.sellcop_var.set(float(l[4]))    # precio de venta en pesos
        except: self.sellcop_var.set(0.0)         #  -
        try: self.sellusd_var.set(float(l[3]))    # precio de venta en usd
        except: self.sellusd_var.set(0.0)         #  -
        try: self.buycop_var.set(float(l[2]) * self.app.usd)
        except: self.buycop_var.set(0.0)          # precio de compra en pesos
        try: self.buyusd_var.set(float(l[2]))     # precio de compra en usd
        except: self.buyusd_var.set(0.0)          # -
        try: self.units_var.set(int(l[5]))        # cantidad disponible
        except: self.units_var.set(0)
        if l[6] != None: self.dept_var.set(l[6])
        if l[7] != None: self.provider_var.set(l[7])
        if l[8] != None: self.notes_text.insert('end', l[8])
        if l[9] != None: self.img_var.set(l[9])
        if l[10] != None: self.barcode_var.set(l[10])

        try:
            self.img_file = ImageTk.PhotoImage(Image.open('resources/' + l[9]).resize((165, 165), Image.ANTIALIAS))
        except TypeError as e: pass
        except Exception as e:
            self.img_file = None ; print('error en charge cargando img', e, l[9])
        finally:
            self.img_label.config(image=self.img_file)

    def create(self):
        self.clear()
        self.title_var.set("Añadiendo artículo")

    def comprobe(self):
        print('comprobe...')


        if self.name_var.get() == '': return "El nombre del artículo no puede estar vacío"
        
        if self.sellcop_entry.get().strip() == '': self.sellcop_var.set(0)
        if self.sellusd_entry.get().strip() == '': self.sellusd_var.set(0)
        if self.buycop_entry.get().strip() == '': self.buycop_var.set(0)
        if self.buyusd_entry.get().strip() == '': self.buyusd_var.set(0)
        if self.units_entry.get().strip() == '': self.units_var.set(0)

        try: float(self.sellcop_var.get())
        except Exception as e: return f"El precio de venta en pesos está mal escrito [{e}]"
        try: float(self.sellusd_var.get())
        except Exception as e: return f"El precio de venta en dólares está mal escrito [{e}]"
        try: float(self.buycop_var.get())
        except Exception as e: return f"El precio de compra en pesos está mal escrito [{e}]"
        try: float(self.buyusd_var.get())
        except Exception as e: return f"El precio de compra en dólares está mal escrito [{e}]"
        try: int(self.units_var.get())
        except Exception as e: return f"El número de unidades está mal escrito [{e}]"


        print("Todas las comprobaciones se hicieron y salió correcto")
        return True

    def copy_img(self, path):
        print('Debug: copy img')
        if path == '': return False
        if os.path.exists(self.app.resources + path.split('/')[-1]):
            print('\tya existe')
            return True

        r = self.resize(path)
        if r == True: return True
        else: 
            messagebox.showerror(title='Error al copiar la imagen', message=r)
            return False


    def resize(self, path):
        print('Debug: resize')
        name = path.split('/')[-1]
        try:
            img = Image.open(path)
            img.thumbnail((200, 200), Image.ANTIALIAS)
            print('resize:', path)

            if path.lower().endswith('.jpg'):
                img.save(self.app.resources + name, 'jpeg')
            elif path.lower().endswith('.jpeg'):
                img.save(self.app.resources + name, 'jpeg')
            elif path.lower().endswith('.png'):
                img.save(self.app.resources + name, 'png')
            else:
                return f'El archivo {path} no es del formato adecuado'

        except FileNotFoundError:
            return f'No se encontró el archivo {path}, puede haber sido borrado, el artículo se guardará sin imagen'
        except Exception as err:
            raise
            return err

        return True