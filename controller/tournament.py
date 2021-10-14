#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' - Saisie d'un tournoi et génération du premier tour par le module create_round'''

import tkinter as tk
from tkinter.constants import DISABLED, EW
from tkinter.messagebox import showerror, showinfo
from tinydb import TinyDB
from tkcalendar import DateEntry
from datetime import date
from controller.round import round

db = TinyDB('db/db.json')
tournament_table = db.table('tournament')


class Tournament(tk.Toplevel):

    def __init__(self):

        tk.Toplevel.__init__(self)
        self.players = list()
        self.checkbuttons = list()
        self.title("Tournoi")
        self.lift()
        self.creer_widgets()

    def creer_widgets(self):

        self.label1 = tk.Label(self, text="Nom").grid(row=0)
        self.label2 = tk.Label(self, text="Lieu").grid(row=1)
        self.label3 = tk.Label(self, text="Date début").grid(row=2)
        self.label4 = tk.Label(self, text="Date fin").grid(row=3)
        self.label5 = tk.Label(self, text="Nombre de tours").grid(row=4)
        self.label6 = tk.Label(self, text="Tournées").grid(row=5)
        self.label7 = tk.Label(self, text=" Sélectionner les joueurs").grid(row=6)
        self.label8 = tk.Label(self, text=" Contrôle du temps").grid(row=9, pady=10)
        self.label9 = tk.Label(self, text="Description").grid(row=11)

        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton.grid(row=16, column=1, pady=30)
        self.bouton = tk.Button(self, text="Valider", command=self.valid)
        self.bouton.grid(row=16, column=2)
        self.bouton = tk.Button(self, text="Reset", command=self.reset)
        self.bouton.grid(row=16, column=3)

        self.nom = tk.StringVar()
        self.lieu = tk.StringVar()
        self.tour = tk.IntVar(self, value=4)
        self.tournees = tk.StringVar(self, value="round1")
        self.time = tk.StringVar()
        self.description = tk.StringVar()

        self.champs1 = tk.Entry(self, textvariable=self.nom)
        self.champs1.grid(row=0, column=1, columnspan=2, sticky=EW,
                          padx=5, pady=5)
        self.champs2 = tk.Entry(self, textvariable=self.lieu)
        self.champs2.grid(row=1, column=1, columnspan=2, sticky=EW,
                          padx=5, pady=5)

        self.datedeb = DateEntry(self, width=12, background='darkblue',
                                 foreground='white', borderwidth=2)
        self.datedeb.grid(row=2, column=1, padx=5, pady=5)

        self.datefin = DateEntry(self, width=12, background='darkblue',
                                 foreground='white', borderwidth=2)
        self.datefin.grid(row=3, column=1, padx=5, pady=5)

        self.champs5 = tk.Entry(self, textvariable=self.tour)
        self.champs5.grid(row=4, column=1, padx=5, pady=5)
        self.champs6 = tk.Entry(self, textvariable=self.tournees, state=DISABLED)
        self.champs6.grid(row=5, column=1, padx=5, pady=5)

        # player clues
        self.alim_players()

        self.time1 = tk.Radiobutton(self, text='bullet', variable=self.time,
                                    value="bullet", command=self.ctltime)
        self.time1.grid(row=9, column=1)
        self.time2 = tk.Radiobutton(self, text='blitz', variable=self.time,
                                    value="blitz", command=self.ctltime)
        self.time2.grid(row=9, column=2)
        self.time3 = tk.Radiobutton(self, text='coup rapide  ', variable=self.time,
                                    value="coup rapide", command=self.ctltime)
        self.time3.grid(row=9, column=3)
        self.description = tk.Text(self, width=20, height=10)
        self.description.grid(row=11, column=1, columnspan=2, sticky=EW, padx=5, pady=5)

    def ctltime(self):
        pass

    def check_players(self):

        ''' players verification'''
        self.players = []
        for item, status in self.var.items():
            if status.get():
                self.players.append(item)

    def valid(self):

        resdate = self.datedeb.get() <= self.datefin.get()
        print(resdate)
        ''' control of the entry and validation if all ok '''
        if (self.nom.get() == ""
           or self.lieu.get() == ""
           or self.datedeb.get() == ""
           or self.datefin.get() == ""
           or self.tour.get() == 0
           or self.players == []
           or self.tournees.get() == ""):
            # error message
            showerror("Résultat", "Saisir tous les champs.\nVeuillez recommencer !")
        elif not resdate:
            showerror("Résultat", "Date de fin > date début")
        else:
            # tournament creation
            name_tournament = self.nom.get()
            # search for the last tournament created
            num_tournament = self.last_id()
            self.insert_tournament(num_tournament)
            # call of the script to generate the first round
            round(num_tournament, "round1")
            # information message
            showinfo("Résultat", "Le tournoi de {} a été créé et\n"
                     "le premier tour a été généré !".format(name_tournament))

    def insert_tournament(self, num_tournament):

        ''' record creation '''
        nom_round = ['round1']
        serialized_tournament = {
            'id': num_tournament,
            'name': self.nom.get(),
            'lieu': self.lieu.get(),
            'datedebut': self.datedeb.get(),
            'datefin': self.datefin.get(),
            'tour': self.tour.get(),
            'round': nom_round,
            'joueurs': self.players,
            'time': self.time.get(),
            'description': self.description.get("1.0", "end")
        }
        tournament_table.insert(serialized_tournament)
        self.reset()

    def reset(self):

        ''' initialization of input fields '''
        self.nom.set("")
        self.lieu.set("")
        self.datedeb.set_date(date.today().strftime("%d/%m/%Y"))
        self.datefin.set_date(date.today().strftime("%d/%m/%Y"))
        self.tour.set("4")
        self.tournees.set("round1")
        self.time.set("")
        self.checkbuttons.clear()
        self.description.delete("1.0", "end")

    def alim_players(self):

        ''' fill in the table of players for selection '''
        players_table = db.table('players')
        serialized_players = players_table.all()
        ''' initialization of line (r) and position (c) counters '''
        r = 6
        c = 1
        self.var = {}
        for item in serialized_players:
            status = tk.BooleanVar()
            self.var[item['indice']] = status
            self.indice = tk.Checkbutton(self, text=item['indice'],
                                         variable=status, onvalue=True, offvalue=False,
                                         command=self.check_players)
            self.indice.grid(row=r, column=c, sticky=EW)
            self.checkbuttons.append(self.indice)
            c += 1
            if c > 3:
                r += 1
                c = 1

    def last_id(self):

        ''' Research the last id of tournament'''
        if len(tournament_table) == 0:
            num = 1
        else:
            table_sorted = sorted(tournament_table, key=lambda x: x['id'], reverse=True)
            num = table_sorted[0]['id'] + 1
        return num

    def quit(self):

        '''Exit'''
        self.destroy()
