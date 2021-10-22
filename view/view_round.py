#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Visualiser les rounds en cours'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tinydb import TinyDB, Query

db = TinyDB('db/db.json')


class View_round(tk.Toplevel):

    def __init__(self, id_tournament, round, serialized_round):

        tk.Toplevel.__init__(self)
        # research the name of the tournament
        name_tournament = search_tournament(id_tournament)
        self.title("{} du tournoi de {}".format(round, name_tournament))
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.construct(serialized_round)

    def construct(self, serialized_round):

        """Construction du treeview"""
        tv = ttk.Treeview(self, columns=(1, 2, 3, 4, 5),
                          show='headings', height=4)
        tv.pack()

        tv.heading(1, text='nom')
        tv.heading(2, text='prénom')
        tv.heading(3, text='VS')
        tv.heading(4, text='nom')
        tv.heading(5, text='prénom')

        tournament_players = db.table('players')
        serialized_players = tournament_players.all()

        players = (serialized_round[0]['joueurs'])
        match = []
        table_match = []
        for item in players:
            for i in item:
                match.append(search(i, serialized_players))
            table_match.append(match)
            match = []

        i = 0
        for item in table_match:
            tv.insert(parent='', index=i, iid=i, values=(item[0]['nom'], item[0]['prenom'], "VS",
                      item[1]['nom'], item[1]['prenom']))
            i += 1


def search(i, serialized_players):

    """Collecting player items"""
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


def view_round(id_tournament):

    round_table = db.table('round_match')
    Round_table = Query()
    serialized_round = round_table.search(Round_table.id == int(id_tournament))
    if serialized_round == []:
        showerror("Résultat", "Aucun tour en attente pour ce tournoi")
    else:
        round = serialized_round[0]['round']
        View_round(id_tournament, round, serialized_round)
