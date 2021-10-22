#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Mise à jour du classement des joueurs'''

import tkinter as tk
from tkinter.constants import DISABLED, END, NORMAL
from tinydb import TinyDB

db = TinyDB('db/db.json')
players_table = db.table('players')


class V_Maj_Players():

    def __init__(self, master):

        self.master = master
        serialized_players = players_table.all()
        self.total_columns = 4
        self.total_rows = len(serialized_players)
        # constitution of the table
        array_players = []
        for item in serialized_players:
            players = (item['indice'], item['prenom'], item['nom'], item['classement'])
            array_players.append(players)
        # Formatting the Table View
        self.data = list()
        for i in range(self.total_rows):
            line = list()
            for j in range(self.total_columns):
                self.e = tk.Entry(self.master, width=10)
                self.e.grid(row=i, column=j)
                self.e.configure(state=NORMAL)
                self.e.insert(END, array_players[i][j])
                if j < 3:
                    self.e.configure(state=DISABLED, disabledbackground='#6fedf8')
                line.append(self.e)
            self.data.append(line)
        self.quit_btn = tk.Button(self.master, text="Quitter")
        self.quit_btn.grid(row=10, column=1, padx=10, pady=10)
        self.valid_btn = tk.Button(self.master, text="Valider")
        self.valid_btn.grid(row=10, column=2)
