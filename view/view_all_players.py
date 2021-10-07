#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Liste de tous les joueurs qui sont dans la table players'''

import tkinter as tk
from tkinter import ttk
from tinydb import TinyDB

db = TinyDB('db/db.json')
players_table = db.table('players')


class View_all_players(tk.Toplevel):

    def __init__(self, my_choice):

        tk.Toplevel.__init__(self)
        self.title("Liste des joueurs par {}".format(my_choice))
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.construct(my_choice)

    def construct(self, my_choice):

        tv = ttk.Treeview(self, columns=(1, 2, 3, 4, 5),
                          show='headings', height=len(players_table))
        tv.pack()

        tv.heading(1, text='nom')
        tv.heading(2, text='prénom')
        tv.heading(3, text='date naissance')
        tv.heading(4, text='sexe')
        tv.heading(5, text='classement')

        serialized_players = players_table.all()
        serialized_players = sorted(serialized_players, key=lambda k: k[my_choice])

        i = 0
        for item in serialized_players:
            tv.insert(parent='', index=i, iid=i, values=(item['nom'], item['prenom'],
                                                         item['datenaissance'],
                                                         item['sexe'], item['classement']))
            i += 1
