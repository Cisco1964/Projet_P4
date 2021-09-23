#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tinydb import TinyDB
from tkinter.constants import W
from view_players_tour import *

db = TinyDB('db.json')
tournament_table = db.table('tournament')

class View_choice_tour(tk.Toplevel):

    def __init__(self, choice):
        tk.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Choisir un tournoi")
        self.construct(choice)

    def construct(self, choice):
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
        self.bouton2 = tk.Button(self, text="Valider", command=lambda: self.valid(status.get(), choice))
        self.bouton2.pack()

    def selection(self, value):
        pass

    def valid(self, value, choice):
        name_tournament = value
        view_tour(name_tournament, choice)

            
    def quit(self):
        '''Exit'''
        self.destroy()
    
def view_choice(choice):  
    View_choice_tour(choice)


