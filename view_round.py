#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tinydb import TinyDB, Query

db = TinyDB('db.json')


class View_round(tk.Toplevel):

    def __init__(self, tournament, round, serialized_round):
        tk.Toplevel.__init__(self)
        self.title("{} du tournoi de {}".format(round, tournament))
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.construct(tournament, serialized_round)

    def construct(self, tournament, serialized_round):
        """Construction du treeview"""
        tv = ttk.Treeview(
        self, 
        columns=(1, 2, 3, 4, 5), 
        show='headings', 
        height=4
        )
        tv.pack()

        tv.heading(1, text='nom')
        tv.heading(2, text='prénom')
        tv.heading(3, text='VS')
        tv.heading(4, text='nom')
        tv.heading(5, text='prénom')

        tournament_players = db.table('players')
        serialized_players = tournament_players.all()

        joueurs = (serialized_round[0]['joueurs'])
        match = []
        table_match = []
        for item in joueurs:
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
    """Récupération des éléments du joueur"""
    for element in serialized_players:
        if element['indice'] == i:
            return element

def view_round():
    round_table = db.table('round_match')
    serialized_round = round_table.all()
    try:
        serialized_round == []
    except IndexError:
        showerror("Résultat", "Aucun tour en attente !")
    else:
        tournament = serialized_round[0]['tournament']
        round = serialized_round[0]['round']
        View_round(tournament, round, serialized_round)

        