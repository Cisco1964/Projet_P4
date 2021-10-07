#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Choix du tournoi pour la génération du round suivant'''

import tkinter as tk
from tinydb import TinyDB
from tkinter.constants import W
from tkinter.messagebox import showerror
from controller.create_round import round as add_round

db = TinyDB('model/db.json')
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
                                         variable=status, value=item['id'])
            self.indice.pack(anchor=W)
            i += 1

        self.bouton1 = tk.Button(self, text="Valider",
                                 command=lambda: self.valid(status.get()))
        self.bouton1.pack()
        self.bouton2 = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton2.pack()

    def valid(self, value):

        ''' Validate selection'''
        if value != "":
            id = int(value)
            # search for rounds already generated
            result = self.research_round(id)
            if result == []:
                showerror("Résultat", "Aucun tour n'a été généré")
            else:
                round = ["round1", "round2", "round3", "round4"]
                # search for the non-generated round
                res = [x for x in round if x not in result]
                if res == []:
                    showerror("Résultat", "Tous les tours ont été générés")
                else:
                    # recovery of the next round
                    next_round = res[0]
                    # generation of the next round
                    add_round(value, next_round)

    def research_round(self, id):

        '''Research all the round'''
        table_round = db.table('round')
        serialized_round = table_round.all()
        round = []
        for element in serialized_round:
            if element['id'] == id:
                item = element['round']
                round.append(item)
        return round

    def quit(self):

        '''Exit'''
        self.destroy()
