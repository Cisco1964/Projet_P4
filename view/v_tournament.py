#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.constants import DISABLED, EW
from tinydb import TinyDB
from tkcalendar import DateEntry


class V_Tournament():

    def __init__(self, master):

        self.master = master
        self.label1 = tk.Label(self.master, text="Nom").grid(row=0)
        self.label2 = tk.Label(self.master, text="Lieu").grid(row=1)
        self.label3 = tk.Label(self.master, text="Date début").grid(row=2)
        self.label4 = tk.Label(self.master, text="Date fin").grid(row=3)
        self.label5 = tk.Label(self.master, text="Nombre de tours").grid(row=4)
        self.label6 = tk.Label(self.master, text="Tournées").grid(row=5)
        self.label7 = tk.Label(self.master, text=" Sélectionner les joueurs").grid(row=6)
        self.label8 = tk.Label(self.master, text=" Contrôle du temps").grid(row=9, pady=10)
        self.label9 = tk.Label(self.master, text="Description").grid(row=11)

        self.quit_btn = tk.Button(self.master, text="Quitter")
        self.quit_btn.grid(row=16, column=1, pady=30)
        self.valid_btn = tk.Button(self.master, text="Valider")
        self.valid_btn.grid(row=16, column=2)
        self.reset_btn = tk.Button(self.master, text="Reset")
        self.reset_btn.grid(row=16, column=3)

        self.nom = tk.StringVar()
        self.lieu = tk.StringVar()
        self.tour = tk.IntVar(self.master, value=4)
        self.tournees = tk.StringVar(self.master, value="round1")
        self.time = tk.StringVar()
        self.description = tk.StringVar()

        self.champs1 = tk.Entry(self.master, textvariable=self.nom)
        self.champs1.grid(row=0, column=1, columnspan=2, sticky=EW,
                          padx=5, pady=5)
        self.champs2 = tk.Entry(self.master, textvariable=self.lieu)
        self.champs2.grid(row=1, column=1, columnspan=2, sticky=EW,
                          padx=5, pady=5)

        self.datedeb = DateEntry(self.master, width=12, background='darkblue',
                                 foreground='white', borderwidth=2)
        self.datedeb.grid(row=2, column=1, padx=5, pady=5)

        self.datefin = DateEntry(self.master, width=12, background='darkblue',
                                 foreground='white', borderwidth=2)
        self.datefin.grid(row=3, column=1, padx=5, pady=5)

        self.champs5 = tk.Entry(self.master, textvariable=self.tour)
        self.champs5.grid(row=4, column=1, padx=5, pady=5)
        self.champs6 = tk.Entry(self.master, textvariable=self.tournees, state=DISABLED)
        self.champs6.grid(row=5, column=1, padx=5, pady=5)

        # player clues
        self.players = []
        self.alim_players()

        self.time1 = tk.Radiobutton(self.master, text='bullet', variable=self.time,
                                    value="bullet")
        self.time1.grid(row=9, column=1)
        self.time2 = tk.Radiobutton(self.master, text='blitz', variable=self.time,
                                    value="blitz")
        self.time2.grid(row=9, column=2)
        self.time3 = tk.Radiobutton(self.master, text='coup rapide  ', variable=self.time,
                                    value="coup rapide")
        self.time3.grid(row=9, column=3)
        self.description = tk.Text(self.master, width=20, height=10)
        self.description.grid(row=11, column=1, columnspan=2, sticky=EW, padx=5, pady=5)

    def alim_players(self):

        self.checkbuttons = list()
        ''' fill in the table of players for selection '''
        db = TinyDB('db/db.json')
        players_table = db.table('players')
        serialized_players = players_table.all()
        ''' initialization of line (r) and position (c) counters '''
        r = 6
        c = 1
        self.var = {}
        for item in serialized_players:
            status = tk.BooleanVar()
            self.var[item['indice']] = status
            self.indice = tk.Checkbutton(self.master, text=item['indice'],
                                         variable=status, onvalue=True, offvalue=False,
                                         command=self.check_players)
            self.indice.grid(row=r, column=c, sticky=EW)
            self.checkbuttons.append(self.indice)
            c += 1
            if c > 3:
                r += 1
                c = 1
        return self.players

    def check_players(self):

        ''' players verification'''
        self.players = []
        for item, status in self.var.items():
            if status.get():
                self.players.append(item)
        return self.players
