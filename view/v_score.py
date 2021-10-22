#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' - Lecture de la table ROUND_MATCH
    - saisie les scores du tour
    - Mise à jour de la date de fin du tour en question ROUND
    - Ecriture dans la table SCORE
    - Rmise à blanc de la table ROUND_MATCH'''

import tkinter as tk
from tkinter.constants import DISABLED, END, NORMAL
from tinydb import TinyDB


db = TinyDB('db/db.json')
score_table = db.table('score')


class V_Score():

    def __init__(self, master, serialized_round_match):

        self.master = master

        tournament_players = db.table('players')
        serialized_players = tournament_players.all()

        global id_tournament
        id_tournament = (serialized_round_match[0]['id'])
        players = (serialized_round_match[0]['joueurs'])

        match = []
        table_match = []
        for item in players:
            for i in item:
                match.append(self.search(i, serialized_players))
            table_match.append(match)
            match = []

        liste_match = []
        for item in table_match:
            match = (item[0]['indice'], item[0]['prenom'], item[0]['nom'],
                     item[1]['indice'], item[1]['prenom'], item[1]['nom'], 0, 0)
            liste_match.append(match)

        self.total_rows = len(liste_match)
        self.total_columns = len(liste_match[0])
        self.data = list()
        for i in range(self.total_rows):
            line = list()
            for j in range(self.total_columns):
                self.e = tk.Entry(self.master, width=20)
                self.e.grid(row=i, column=j)
                self.e.configure(state=NORMAL)
                self.e.insert(END, liste_match[i][j])
                if j < 6:
                    self.e.configure(state=DISABLED, disabledbackground='#6fedf8')
                line.append(self.e)
            self.data.append(line)
        self.quit_btn = tk.Button(self.master, text="Quitter")
        self.quit_btn.grid(row=10, column=3, padx=10, pady=10)
        self.valid_btn = tk.Button(self.master, text="Valider")
        self.valid_btn.grid(row=10, column=4)

    def search(self, i, serialized_players):

        """Collecting player items"""
        for element in serialized_players:
            if element['indice'] == i:
                return element
