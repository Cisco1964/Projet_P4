#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' - Lecture de la table ROUND_MATCH
    - saisie les scores du tour
    - Mise à jour de la date de fin du tour en question ROUND
    - Ecriture dans la table SCORE
    - Rmise à blanc de la table ROUND_MATCH'''

import tkinter as tk
from tkinter.constants import DISABLED, END, NORMAL
from tkinter.messagebox import showerror
from tinydb import TinyDB, Query, where
import datetime
from model.create_score import Create_Score
from view.v_score import V_Score


db = TinyDB('db/db.json')
score_table = db.table('score')


class Control_Score:

    def __init__(self, result):

        serialized_round_match = result
        global round
        global datedebut
        global id_tournament
        round = (serialized_round_match[0]['round'])
        datedebut = (serialized_round_match[0]['datedebut'])
        id_tournament = (serialized_round_match[0]['id'])
        name_tournament = self.search_tournament(id_tournament)
        self.root = tk.Toplevel()
        self.root.title("Saisir les scores du {} pour le tournoi de {}".format(round, name_tournament))

        self.model = Create_Score()
        self.view = V_Score(self.root, serialized_round_match)
        self.view.quit_btn.config(command=self.quit)
        self.view.valid_btn.config(command=self.valid)

    def valid(self):

        """Data entry control"""
        my_bool = True
        for i in range(self.view.total_rows):

            try:
                float(self.view.data[i][6].get())
            except ValueError:
                showerror("Résultat", "Score invalide.\nVeuillez recommencer !")
                my_bool = False
                break

            try:
                float(self.view.data[i][7].get())
            except ValueError:
                showerror("Résultat", "Score invalide.\nVeuillez recommencer !")
                my_bool = False
                break

            result = float(self.view.data[i][6].get()) + float(self.view.data[i][7].get())
            if result > 1 or result == 0:
                showerror("Résultat", "Score invalide.\nVeuillez recommencer !")
                my_bool = False
                break

        if my_bool:
            line_score = []
            players_round = []
            for i in range(self.view.total_rows):
                for j in range(self.view.total_columns):
                    line_score.append(self.view.data[i][j].get())
                self.model.insert_score(id_tournament, round, line_score)
                players = (int(line_score[0]), int(line_score[3]))
                players_round.append(players)
                line_score = []
            # remove the record
            self.model.insert_round(players_round, id_tournament, round, datedebut)
            # remove the record
            self.model.update_round_match(id_tournament)
            self.quit()

    def search(self, i, serialized_players):

        """Collecting player items"""
        for element in serialized_players:
            if element['indice'] == i:
                return element

    def search_tournament(self, id_tournament):

        '''Research the name of the tournament'''
        tournament_table = db.table('tournament')
        serialized_tournament = tournament_table.all()
        for element in serialized_tournament:
            if element['id'] == id_tournament:
                return element['name']

    def quit(self):

        """Exit"""
        self.root.destroy()
