#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tinydb import TinyDB
from tkinter.constants import W
from view_tour2_alpha import *

db = TinyDB('db.json')
tournament_table = db.table('tournament')

class View_tour1_alpha(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Choisir un tournoi")
        self.construct()

    def construct(self):
        serialized_tournament = tournament_table.all()

        i = 0
        self.var = {}
        status = tk.StringVar()
        for item in serialized_tournament:
            self.var[item['name']] = status
            self.indice = tk.Radiobutton(self, text=item['name'], 
                        variable=status, value=item['name'], command=lambda: self.selection(status.get()))
            self.indice.pack(anchor=W)
            i += 1 

        self.bouton1 = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton1.pack()
        self.bouton2 = tk.Button(self, text="Valider", command=lambda: self.valid(status.get()))
        self.bouton2.pack()

    def selection(self, value):
        pass

    def valid(self, value):
        #mylabel = tk.Label(self, text=value)
        #mylabel.pack()
        name_tournament = value
        view_alpha(name_tournament)
            
    def quit(self):
        self.destroy()
    

if __name__ == "__main__":  

    app = View_tour1_alpha()


