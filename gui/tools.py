import tkinter

# fonts
font1 = 'Roboto 22 bold'
font2 = 'Roboto 18 bold'
font3 = 'Roboto 18'
font4 = 'Roboto 12 bold'
font5 = 'Roboto 12'
font6 = 'Roboto 10 bold'
font7 = 'Roboto 10'

# color palette
color1 = '#F00' # rojo
color2 = '#008000' # verde oscuro
color3 = '#FF0' # amarillo
color4 = '#403e39' # gris kenia
color5 = '#000' # negro
color6 = '#999999' # Gris oscuro
color7 = '#F2F2F2' # Gris claro
color8 = '#FFF' # blanco

def checkprice(key):
    print('key =', key)
    if key == '.': return True
    elif key.isdigit(): return True
    else: return False

# class AutoScrollbar(tkinter.Scrollbar):
#     """A class that inherits from Scrollbar for make it auto-hiding"""
#
#     def set(self, lo, hi):
#         if float(lo) <= 0.0 and float(hi) >= 1.0:
#             self.tk.call("grid", "remove", self)
#         else:
#             self.grid()
#         tkinter.Scrollbar.set(self, lo, hi)
#
#     def pack(self, **kw):
#         raise tkinter.TclError
#
#     def place(self, **kw):
#         raise tkinter.TclError
#
#
# class ListboxWithAutoscroll(tkinter.Frame):
#     """
#     """
#
#     def __init__(self, master, list_bind=None, *args, **kwargs):
#         """"""
#         tkinter.Frame.__init__(self, master, bd=0)
#
#         # making list expandable
#         self.rowconfigure(0, weight=1)
#         self.columnconfigure(0, weight=1)
#
#         self.xscroll = AutoScrollbar(self, orient='horizontal')
#         self.yscroll = AutoScrollbar(self)
#         self.listbox = tkinter.Listbox(self, *args, **kwargs)
#
#         self.xscroll.grid(row=1, column=0, sticky='ew')
#         self.yscroll.grid(column=1, row=0, sticky='ns')
#         self.listbox.grid(row=0, column=0, sticky='nsew')
#
#         self.xscroll.configure(command=self.listbox.xview)
#         self.yscroll.configure(command=self.listbox.yview)
#         self.listbox.configure(yscrollcommand=self.yscroll.set,
#                                xscrollcommand=self.xscroll.set)
#
#         try:
#             self.listbox.bind('<<ListboxSelect>>', list_bind)
#         except Exception:
#             # print(f'Error trying to call {list_bind} function')
#             raise
#
#
# class AutoScrolledFrame(tkinter.Frame):
#
#     def __init__(self, master, *args, **kwargs):
#         """Creating and configuring the basic of a tab
#         and making the container (self) whit the canvas
#         and autoscrollbars"""
#         tkinter.Frame.__init__(self, master, bd=0)
#
#         self.rowconfigure(0, weight=1)
#         self.columnconfigure(0, weight=1)
#
#         self.xscroll = AutoScrollbar(self, orient='horizontal')
#         self.xscroll.grid(row=1, column=0, sticky='ew')
#         self.yscroll = AutoScrollbar(self)
#         self.yscroll.grid(column=1, row=0, sticky='ns')
#         self.canvas = tkinter.Canvas(
#             self, bg='#000',
#             yscrollcommand=self.yscroll.set,
#             xscrollcommand=self.xscroll.set,
#             *args, **kwargs)
#         self.canvas.grid(row=0, column=0, sticky='nsew')
#
#         self.creeate_widgets()
#
#         self.xscroll.config(command=self.canvas.xview)
#         self.yscroll.config(command=self.canvas.yview)
#         self.canvas.config(scrollregion=self.canvas.bbox("all"))
#
#     def creeate_widgets(self):
#         """This method need to be rewrited on a child
#         class to make all widgets from each tab.
#         All these widgets must be made in the self.canvas
#         element."""
#         pass


# def resize_photo(file, size=500):
#     try:
#         img = Image.open(file)
#     except:
#         raise
#     else:
#         return img.thumbnail((size,size), Image.ANTIALIAS)
