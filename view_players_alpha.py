#from tkinter import *
import tkinter as tk
from tkinter import ttk
from tinydb import TinyDB

db = TinyDB('db.json')
players_table = db.table('players')

class Players_alpha(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Liste des joueurs par nom")
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.construct()

    def construct(self):
        tv = ttk.Treeview(
        self, 
        columns=(1, 2, 3, 4, 5), 
        show='headings', 
        height=len(players_table)
        )
        tv.pack()

        tv.heading(1, text='nom')
        tv.heading(2, text='prénom')
        tv.heading(3, text='date naissance')
        tv.heading(4, text='sexe')
        tv.heading(5, text='classement')

        serialized_players = players_table.all()
        serialized_players = sorted(serialized_players, key=lambda k: k['nom'])
        
        i = 0
        for item in serialized_players:
            tv.insert(parent='', index=i, iid=i, values=(item['nom'], item['prenom'],
                item['datenaissance'], item['sexe'], item['classement'])) 
            i += 1
    

if __name__ == "__main__":  

    ws = Players_alpha()

