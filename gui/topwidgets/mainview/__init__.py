from gui.tools import *
from gui.topwidgets.mainview import facturation, inventory


class MainView(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)
        self.app = master

        # creating tabs
        self.actual_tab = None
        self.tab_inventory = inventory.Inventory(self, bg="#FFF")
        self.tab_facturation = facturation.Facturation(self)
        self.set_tab('inventory')  # this put the inventory tab

        self.grid(row=1, column=0, sticky='nsew')

    def set_tab(self, t):
        """This method receives a string whit a name of
        an tab to set in MainView widget"""
        tab_list = {
            'inventory': self.tab_inventory,
            'facturation': self.tab_facturation
        }
        if self.actual_tab == t:
            print("Se seleccionó la pestaña actual")
        elif t in tab_list:
            print('Cambiando a:', t)
            try: tab_list[self.actual_tab].pack_forget()  # remove last tab
            except: pass
            tab_list[t].pack(fill="both", expand=1)
            self.actual_tab = t
        else:
            raise Exception(f'Not found this tab. Must be one of {tab_list}')
