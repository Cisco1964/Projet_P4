#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tinydb import TinyDB, Query

db = TinyDB('db.json')


class View_tour(tk.Toplevel):

    def __init__(self, name_tournament, choice):
        tk.Toplevel.__init__(self)
        self.title("Liste des joueurs du tournoi de {} par {}".format(name_tournament, choice))
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.construct(name_tournament, choice)

    def construct(self, name_tournament, choice):
        tv = ttk.Treeview(
        self, 
        columns=(1, 2, 3, 4, 5), 
        show='headings', 
        height=5
        )
        tv.pack()

        tv.heading(1, text='nom')
        tv.heading(2, text='prénom')
        tv.heading(3, text='date naissance')
        tv.heading(4, text='sexe')
        tv.heading(5, text='classement')

        tournament_table = db.table('tournament')

        Tournament = Query()
        result = tournament_table.search(Tournament.name == name_tournament)
    
        joueurs = (result[0]['joueurs'])
        print(joueurs)

        ''' Recherche des joueurs pour le tournoi'''

        tournament_players = db.table('players')
        serialized_players = tournament_players.all()

        table = []
        for i in joueurs:
            table.append(search(i, serialized_players))
       
        table_sorted = sorted(table, key=lambda k: k[choice])

        i = 0
        for item in table_sorted:
            tv.insert(parent='', index=i, iid=i, values=(item['nom'], item['prenom'],
                item['datenaissance'], item['sexe'], item['classement'])) 
            i = i + 1

def search(i, serialized_players):
    for element in serialized_players:
        if element['indice'] == i:
            return element

def view_tour(name_tournament, choice):

    View_tour(name_tournament, choice)

