#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tinydb import TinyDB, where
from tkinter.constants import W
from tkinter.messagebox import showerror, showinfo
from create_round import *

db = TinyDB('db.json')
tournament_table = db.table('tournament')

class View_choice_round(tk.Toplevel):

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
        table_round = db.table('round')
        Round = Query()
        # extraction round
        result = table_round.search(Round['tournament'] == value)
        if result == []:
            showerror("Résultat", "Aucun tour n'a été généré")
        else:    
            round = ["round1", "round2", "round3", "round4"]
            # recherche des rounds déjà générés
            list_round = [item['round'] for item in result]
            print(list_round)
            # recherche du round non généré
            res = [x for x in round if x not in list_round]
            if res == []:
                showerror("Résultat", "Tous les tours ont été générés")
            else:
                next_round = res[0]
                # génération du tour suivant
                round(value, next_round)

            
    def quit(self):
        '''Exit'''
        self.destroy()
    
def view_gen_round():  
    View_choice_round()


