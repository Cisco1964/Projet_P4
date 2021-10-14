#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Choix du tournoi pour la génération du round suivant'''

import tkinter as tk
from tinydb import TinyDB, Query
from tkinter.constants import W
from tkinter.messagebox import showerror
from controller.round import round as call_round

db = TinyDB('db/db.json')
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
            matchs = self.research_round_match(id)
            print(matchs)
            if matchs != []:
                showerror("Résultat", "Il y a un tour en attente de saisie pour ce tournoi")
            else:
                # search for rounds already generated
                result = self.research_round(id)
                round = ["round1", "round2", "round3", "round4"]
                # search for the non-generated round
                res = [x for x in round if x not in result]
                if res == []:
                    showerror("Résultat", "Tous les tours ont déjà été générés pour ce tournoi ")
                else:
                    # recovery of the next round
                    next_round = res[0]
                    # generation of the next round
                    call_round(value, next_round)

    def research_round_match(self, id):

        '''recherche s'il y a un tour en cours'''
        tournament_round = db.table('round_match')
        Round_table = Query()
        result = tournament_round.search(Round_table.id == int(id))
        return result

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
