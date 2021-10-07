#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tinydb import TinyDB, Query

db = TinyDB('db.json')


class View_tour(tk.Toplevel):

    def __init__(self, id_tournament, my_choice):

        tk.Toplevel.__init__(self)

        # research the name of the tournament
        name_tournament = search_tournament(id_tournament)
        self.title("Liste des joueurs du tournoi de {} par {}".format(name_tournament, my_choice))
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.construct(id_tournament, my_choice)

    def construct(self, id_tournament, my_choice):

        tv = ttk.Treeview(self, columns=(1, 2, 3, 4, 5), show='headings', height=8)
        tv.pack()

        tv.heading(1, text='nom')
        tv.heading(2, text='prénom')
        tv.heading(3, text='date naissance')
        tv.heading(4, text='sexe')
        tv.heading(5, text='classement')

        tournament_table = db.table('tournament')
        Tournament = Query()
        result = tournament_table.search(Tournament.id == int(id_tournament))
        players = (result[0]['joueurs'])
        # Search players for the tournament
        tournament_players = db.table('players')
        serialized_players = tournament_players.all()

        table = []
        for i in players:
            table.append(search(i, serialized_players))
        # sort the list by choice
        table_sorted = sorted(table, key=lambda k: k[my_choice])

        i = 0
        for item in table_sorted:
            tv.insert(parent='', index=i, iid=i, values=(item['nom'], item['prenom'],
                                                         item['datenaissance'],
                                                         item['sexe'], item['classement']))
            i += 1


def search(i, serialized_players):

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
