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
from tinydb import TinyDB
import datetime

db = TinyDB('model/db.json')
score_table = db.table('score')


class Score(tk.Toplevel):

    def __init__(self):

        tk.Toplevel.__init__(self)

        tournament_round = db.table('round_match')
        serialized_round_match = tournament_round.all()

        tournament_players = db.table('players')
        serialized_players = tournament_players.all()

        global id_tournament
        global round
        global datedebut
        id_tournament = (serialized_round_match[0]['id'])
        round = (serialized_round_match[0]['round'])
        datedebut = (serialized_round_match[0]['datedebut'])
        players = (serialized_round_match[0]['joueurs'])
        # research the name of the tournament
        name_tournament = self.search_tournament(id_tournament)
        self.title("Saisir les scores du {} pour le tournoi de {}".format(round, name_tournament))
        self.construct(players, serialized_players)

    def construct(self, players, serialized_players):

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

        global total_rows
        global total_columns
        total_rows = len(liste_match)
        total_columns = len(liste_match[0])
        self.data = list()
        for i in range(total_rows):
            line = list()
            for j in range(total_columns):
                self.e = tk.Entry(self, width=20)
                self.e.grid(row=i, column=j)
                self.e.configure(state=NORMAL)
                # self.e.configure(font=("Helvetica", 10, BOLD))
                self.e.insert(END, liste_match[i][j])
                if j < 6:
                    self.e.configure(state=DISABLED)
                line.append(self.e)
            self.data.append(line)
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton.grid(row=10, column=3, padx=10, pady=10)
        self.bouton = tk.Button(self, text="Valider", command=self.valid)
        self.bouton.grid(row=10, column=4)

    def valid(self):

        """Data entry control"""
        my_bool = True
        for i in range(total_rows):

            try:
                float(self.data[i][6].get())
            except ValueError:
                showerror("Résultat", "Score invalide.\nVeuillez recommencer !")
                my_bool = False
                break

            try:
                float(self.data[i][7].get())
            except ValueError:
                showerror("Résultat", "Score invalide.\nVeuillez recommencer !")
                my_bool = False
                break

            result = float(self.data[i][6].get()) + float(self.data[i][7].get())
            if result > 1 or result == 0:
                showerror("Résultat", "Score invalide.\nVeuillez recommencer !")
                my_bool = False
                break

        if my_bool:
            line_score = []
            players_round = []
            for i in range(total_rows):
                for j in range(total_columns):
                    line_score.append(self.data[i][j].get())
                self.insert_score(line_score)
                players = (int(line_score[0]), int(line_score[3]))
                players_round.append(players)
                line_score = []
            self.update_round(players_round)
            db.drop_table('round_match')
            self.quit()

    def insert_score(self, line_score):

        """Writing the recording SCORE """
        players = (int(line_score[0]), int(line_score[3]))
        score = (float(line_score[6]), float(line_score[7]))
        serialized_score = {
            'id': int(id_tournament),
            'round': round,
            'joueurs': players,
            'score': score,
        }
        score_table.insert(serialized_score)

    def update_round(self, players_round):

        """Writing the recording ROUND"""
        round_table = db.table('round')
        datefin = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        serialized_round = {
            'id': int(id_tournament),
            'round': round,
            'joueurs': players_round,
            'datedebut': datedebut,
            'datefin': datefin
        }
        round_table.insert(serialized_round)

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
        self.destroy()


def update_score():

    tournament_round = db.table('round_match')
    serialized_round_match = tournament_round.all()
    if len(serialized_round_match) == 0:
        showerror("Résultat", "Aucun tour en attente de saisie")
    else:
        Score()
