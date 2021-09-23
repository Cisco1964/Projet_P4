#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tinydb import TinyDB
from tkinter.constants import W
from tkinter.messagebox import showinfo

db = TinyDB('db.json')

class View_clear_table(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("Choisir une table")
        self.construct()

    def construct(self):

        name_table = ['tournament', 'players', 'round_match', 'round', "score"]

        i = 0
        self.var = {}
        status = tk.StringVar()
        for item in name_table:
            self.var[item] = status
            self.indice = tk.Radiobutton(self, text=item, 
                        variable=status, value=item, command=lambda: self.selection(status.get()))
            self.indice.pack(anchor=W)
            i += 1 

        self.bouton1 = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton1.pack()
        self.bouton2 = tk.Button(self, text="Valider", command=lambda: self.valid(status.get()))
        self.bouton2.pack()

    def selection(self, value):
        pass

    def valid(self, value):
        name = value
        print(name)
        db.drop_table(name)
        showinfo("Drop table", "la table {} a été remise à blanc".format(name))
            
    def quit(self):
        self.destroy()
    

def clear_table():  
    View_clear_table()
