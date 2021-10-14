#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Choix du tournoi puis appel du module suivant le paramètre d'entré
    - my_choice = nom ou classement : liste des joueurs par tournoi
    - my_choice = round : liste des rounds par tournoi
    - my_choice = match : liste tous les matchs par tournoi
'''

import tkinter as tk
from tinydb import TinyDB
from tkinter.constants import W
from controller.score import update_score
from view.view_players_tour import View_tour
from view.view_round_tour import View_round_tour
from view.view_match_tour import View_match_tour
from view.view_round import view_round

db = TinyDB('db/db.json')
tournament_table = db.table('tournament')


class View_choice_tour(tk.Toplevel):

    def __init__(self, my_choice):

        tk.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Choisir un tournoi")
        self.construct(my_choice)

    def construct(self, my_choice):

        ''' Window construction'''
        serialized_tournament = tournament_table.all()
        i = 0
        self.var = {}
        status = tk.StringVar()
        for item in serialized_tournament:
            self.var[item['name']] = status
            self.indice = tk.Radiobutton(self, text=item['name'], variable=status, value=item['id'])
            self.indice.pack(anchor=W)
            i += 1

        self.bouton1 = tk.Button(self, text="Valider",
                                 command=lambda: self.valid(status.get(), my_choice))
        self.bouton1.pack()
        self.bouton2 = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton2.pack()

    def valid(self, value, my_choice):

        if value != "":
            ''' Validation of the selection '''
            id_tournament = value
            # list of players by tournament
            if my_choice in ['nom', 'classement']:
                View_tour(id_tournament, my_choice)
            # list of rounds by tournament
            elif my_choice == 'round':
                View_round_tour(id_tournament)
            elif my_choice == 'match':
                # list of matches by tournament
                View_match_tour(id_tournament)
            elif my_choice == 'view_round':
                # view round in treatement
                view_round(id_tournament)
            else:
                # saisie des scores
                update_score(id_tournament)

    def quit(self):

        '''Exit'''
        self.destroy()
