#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tinydb import TinyDB, where
from tkinter.constants import W
from view_players_tour import *

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
        self.control_round(value)

    def control_round(self, value):
        round = db.table('round')
        Round = Query()
        print(round.search(Round.tournament == value))
        list_round = ["round1", "round2", "round3", "round4"]

            
    def quit(self):
        '''Exit'''
        self.destroy()
    
def view_gen_round():  
    View_choice_round()


