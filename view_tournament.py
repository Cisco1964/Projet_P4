import tkinter as tk
from tkinter import ttk
from tinydb import TinyDB

db = TinyDB('db.json')
tournament_table = db.table('tournament')

class View_tournament(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Liste des tournois")
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.construct()

    def construct(self):
        tv = ttk.Treeview(
        self, 
        columns=(1, 2, 3, 4, 5), 
        show='headings', 
        height=len(tournament_table)
        )

        tv.pack()

        tv.heading(1, text='nom')
        tv.heading(2, text='lieu')
        tv.heading(3, text='date début')
        tv.heading(4, text='date fin')
        tv.heading(5, text='tournées')

        serialized_tournament = tournament_table.all()
        serialized_tournament = sorted(serialized_tournament, key=lambda k: k['name'])

        i = 0
        for item in serialized_tournament:
            tv.insert(parent='', index=i, iid=i, values=(item['name'], item['lieu'],
                item['datedebut'], item['datefin'], item['tournees'])) 
            i += 1
    

if __name__ == "__main__":  

    ws = View_tournament()


