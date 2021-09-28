#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tinydb import TinyDB
from tkinter.constants import W
from view_players_tour import view_tour
from view_round_tour import view_r_tour
from view_match_tour import view_m_tour

db = TinyDB('db.json')
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
                view_tour(id_tournament, my_choice)
            # list of rounds by tournament
            elif my_choice == 'round':
                view_r_tour(id_tournament)
            else:
                # list of matches by tournament
                view_m_tour(id_tournament)

    def quit(self):

        '''Exit'''
        self.destroy()


def view_choice(my_choice):

    View_choice_tour(my_choice)
