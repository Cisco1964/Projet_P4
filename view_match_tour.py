#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tinydb import TinyDB

db = TinyDB('db.json')


class View_match_tour(tk.Toplevel):

    def __init__(self, id_tournament):

        tk.Toplevel.__init__(self)

        # research the name of the tournament
        name_tournament = search_tournament(id_tournament)
        self.title("Liste des tous les matchs du tournoi de {}".format(name_tournament))
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.construct(id_tournament)

    def construct(self, id_tournament):

        tv = ttk.Treeview(self, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height=8)
        tv.pack()

        tv.heading(1, text='round')
        tv.heading(2, text='nom')
        tv.heading(3, text='prénom')
        tv.heading(4, text='score')
        tv.heading(5, text='nom')
        tv.heading(6, text='prénom')
        tv.heading(7, text='score')

        result = research_score(id_tournament)
        # key extraction: round, players, scores
        klist = ['round', 'joueurs', 'score']
        liste_match = extract_value(result, klist)
        # Search players for the tournament
        tournament_players = db.table('players')
        serialized_players = tournament_players.all()

        table = []
        match = []
        for item in liste_match:
            for v, i in enumerate(item[1]):
                detail_match = [item[0], search(i, serialized_players), item[2][v]]
                match.append(detail_match)
            table.append(match)
            match = []

        i = 0
        for item in table:
            tv.insert(parent='', index=i, iid=i, values=(item[0][0], item[0][1]['prenom'],
                      item[0][1]['nom'], item[0][2], item[1][1]['prenom'],
                      item[1][1]['nom'], item[1][2]))
            i += 1


def extract_value(result, klist):

    ''' Extracting and formatting the list'''
    liste = []
    for r in result:
        r2 = []
        for key in klist:
            r2.append(r[key])
        liste.append(r2)
    return liste


def search(i, serialized_players):

    '''Research the elements of the player'''
    for element in serialized_players:
        if element['indice'] == i:
            return element


def search_tournament(id_tournament):

    '''Research the name of the tournament'''
    tournament_table = db.table('tournament')
    serialized_tournament = tournament_table.all()
    for element in serialized_tournament:
        if element['id'] == int(id_tournament):
            return element['name']


def research_score(id_tournament):

    '''Research all the score'''
    score_table = db.table('score')
    serialized_score = score_table.all()
    score = []
    for element in serialized_score:
        if element['id'] == int(id_tournament):
            score.append(element)
    return score


def view_m_tour(id_tournament):

    View_match_tour(id_tournament)
