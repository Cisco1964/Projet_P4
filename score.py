#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' - Lecture de la table ROUND_MATCH
    - Saisie des scores
    - Mise à jour de la date de fin du round dans la table ROUND
    - Ecriture des scores dans la table SCORE
    - Remise à blanc de la table ROUND_MATCH'''

import tkinter as tk
from tkinter import font
from tkinter.constants import DISABLED, END, NORMAL
from tkinter.font import BOLD
from tkinter.messagebox import showerror
from tinydb import TinyDB
import datetime

db = TinyDB('db.json')
score_table = db.table('score')


class Score(tk.Toplevel):

    def __init__(self):

        tk.Toplevel.__init__(self)

        tournament_round = db.table('round_match')
        serialized_round_match = tournament_round.all()

        tournament_players = db.table('players')
        serialized_players = tournament_players.all()

        global tournament
        global round
        global datedebut
        tournament = (serialized_round_match[0]['tournament'])
        round = (serialized_round_match[0]['round'])
        datedebut = (serialized_round_match[0]['datedebut'])
        joueurs = (serialized_round_match[0]['joueurs'])

        self.title("Saisir les scores du {} pour le tournoi de {}".format(round, tournament))
        self.construct(joueurs, serialized_players)

    def construct(self, joueurs, serialized_players):

        match = []
        table_match = []
        for item in joueurs:
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

        """Contrôle de la saisie"""
        my_bool = True
        for i in range(total_rows):
            result = float(0)
            result = float(self.data[i][6].get()) + float(self.data[i][7].get())
            print(result)
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
                joueurs = (int(line_score[0]), int(line_score[3]))
                players_round.append(joueurs)
                line_score = []
            self.update_round(players_round)
            db.drop_table('round_match')
            self.quit()

    def insert_score(self, line_score):

        """Ecriture de l'enregistrement SCORE """
        joueurs = (int(line_score[0]), int(line_score[3]))
        score = (float(line_score[6]), float(line_score[7]))
        serialized_score = {
            'tournament': tournament,
            'round': round,
            'joueurs': joueurs,
            'score': score,
        }
        score_table.insert(serialized_score)

    def update_round(self, players_round):

        """Ecriture de l'enregistrement ROUND"""
        round_table = db.table('round')
        datefin = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        serialized_round = {
            'tournament': tournament,
            'round': round,
            'joueurs': players_round,
            'datedebut': datedebut,
            'datefin': datefin

        }
        round_table.insert(serialized_round)

    def search(self, i, serialized_players):

        """Récupération des éléments du joueur"""
        for element in serialized_players:
            if element['indice'] == i:
                return element

    def quit(self):

        """Exit"""
        self.destroy()


def update_score():

    tournament_round = db.table('round_match')
    serialized_round_match = tournament_round.all()
    try:
        serialized_round_match[0]['tournament'] == ""
    except IndexError:
        showerror("Résultat", "Aucun tour en attente de saisie!")
    else:
        Score()
