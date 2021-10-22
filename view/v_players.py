#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Création des joueurs'''

import tkinter as tk
from tkcalendar import DateEntry


class V_Players():

    def __init__(self, master):

        self.master = master
        self.nom = tk.StringVar()
        self.prenom = tk.StringVar()
        self.sex = tk.StringVar()
        self.classement = tk.StringVar()

        self.label1 = tk.Label(self.master, text="Nom de famille").grid(row=0)
        self.label2 = tk.Label(self.master, text="Prénom").grid(row=1)
        self.label3 = tk.Label(self.master, text="Date de naissance").grid(row=2)
        self.label4 = tk.Label(self.master, text="Sexe").grid(row=3)
        self.label5 = tk.Label(self.master, text="Classement").grid(row=5)

        self.quit_btn = tk.Button(self.master, text="Quitter")
        self.quit_btn.grid(row=10, padx=10, pady=10)
        self.valid_btn = tk.Button(self.master, text="Valider")
        self.valid_btn.grid(row=10, column=1)
        self.reset_btn = tk.Button(self.master, text="Reset")
        self.reset_btn.grid(row=10, column=2)

        self.champ1 = tk.Entry(self.master, textvariable=self.nom)
        self.champ1.grid(row=0, column=1, padx=5, pady=5)
        self.champ2 = tk.Entry(self.master, textvariable=self.prenom)
        self.champ2.grid(row=1, column=1, padx=5, pady=5)

        self.datenaissance = DateEntry(self.master, width=12, background='darkblue',
                                       foreground='white', borderwidth=2)
        self.datenaissance.grid(row=2, column=1, padx=5, pady=5)

        self.champf = tk.Radiobutton(self.master, text="F", variable=self.sex, value="F")
        self.champf.grid(row=3, column=1)
        self.champm = tk.Radiobutton(self.master, text="M", variable=self.sex, value="M")
        self.champm.grid(row=4, column=1)

        self.champ4 = tk.Entry(self.master, textvariable=self.classement)
        self.champ4.grid(row=5, column=1, padx=5, pady=5)
