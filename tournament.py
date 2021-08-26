#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.constants import CENTER, DISABLED, END, EW, W
from tkinter.messagebox import showwarning
from tinydb import TinyDB
from tkcalendar import DateEntry
import datetime

db = TinyDB('db.json')
tournament_table = db.table('tournament')


class Tournament(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.joueurs = list()
        self.creer_widgets()

    def ctltime(self):
        pass
        #print(self.time.get())

    def check_joueurs(self):
        self.joueurs = []
        for item, status in self.var.items():
            if status.get(): 
                self.joueurs.append(item)

    def valid(self):
        if (self.nom.get() == ""
        or self.lieu.get() == ""
        or self.datedeb.get() == ""
        or self.datefin.get() == ""
        or self.tour.get() == 0
        or self.tournees.get() == ""):
            showwarning("Résultat", "Saisir tous les champs.\nVeuillez recommencer !")
        else: 
            self.insert_tournament()

    def insert_tournament(self):
        serialized_tournament = {
            'name': self.nom.get(), 
            'lieu': self.lieu.get(),
            'datedebut': self.datedeb.get(),
            'datefin': self.datefin.get(),
            'tour': self.tour.get(),
            'tournees': self.tournees.get(),
            'joueurs': self.joueurs,
            'time': self.time.get(),
            'description': self.description.get("1.0", "end")
        }
        #print(serialized_tournament)
        tournament_table.insert(serialized_tournament)
        self.reset()

    def reset(self):
        self.nom.set("")
        self.lieu.set("")
        self.datedeb.set_date(datetime.date.today().strftime("%d/%m/%Y"))
        self.datefin.set_date(datetime.date.today().strftime("%d/%m/%Y"))
        self.tour.set("4")
        self.tournees.set("")
        self.time.set("")
        for item, status in self.var.items():
            if status.get(): 
                status = ""
        self.description.delete("1.0", "end")

    def alim_joueurs(self):
        ''' remplir la table des joueurs pour sélection '''
        players_table = db.table('players')
        serialized_players = players_table.all()
        ''' initialisation compteurs ligne(r) et position(c) '''
        r = 6
        c = 1
        self.var = {}
        for item in serialized_players:
            status = tk.BooleanVar()
            self.var[item['indice']] = status
            self.indice = tk.Checkbutton(self, text=item['indice'], 
                        variable=status, command=self.check_joueurs)
            self.indice.grid(row=r, column=c, sticky=EW)
            c += 1 
            if c > 3:
               r += 1  
               c = 1

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
        self.bouton.grid(row=14, column=1, pady=5)
        self.bouton = tk.Button(self, text="Valider", command=self.valid)
        self.bouton.grid(row=14, column=2)
        self.bouton = tk.Button(self, text="Reset", command=self.reset)
        self.bouton.grid(row=14, column=3)

        self.nom = tk.StringVar()
        self.lieu = tk.StringVar()
        self.tour = tk.IntVar(self, value=4)
        self.tournees = tk.StringVar()
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
        self.champs6 = tk.Entry(self, textvariable=self.tournees)
        self.champs6.grid(row=5, column=1, padx=5, pady=5)

        ''' indices des joueurs'''       
        self.alim_joueurs()

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
        self.description.grid(row=11, column=1, columnspan=2, sticky='ew', padx=5, pady=5)
          
       
if __name__ == "__main__":
    app = Tournament()
    app.title("Tournoi")
    app.mainloop()
