#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.messagebox import showerror, showwarning
from tinydb import TinyDB
from tkcalendar import DateEntry
import datetime

db = TinyDB('db.json')
players_table = db.table('players')


class Players(tk.Toplevel):

    def __init__(self):

        tk.Toplevel.__init__(self)
        self.title("Joueurs")
        self.creer_widgets()

    def valid(self):

        if (self.nom.get() == "" 
            or self.prenom.get() == "" 
            or self.datenaissance.get() == "" 
            or self.sex.get() == "" 
            or self.classement.get() == 0
            or self.classement.get() == ""):
                showerror("Résultat", "Saisir tous les champs.\nVeuillez recommencer !")
        else:
            bool = self.numberonly()
            if bool:
                elements = len(players_table)
                if elements < 8:
                    if elements == 0:
                        compteur = 1 
                    else:
                        compteur = elements + 1
                    print(compteur)
                    self.insert_user(compteur)
                else:
                    showwarning("Joueurs", "Vous avez déjà saisi 8 joueurs !")
                
    def insert_user(self, compteur):

        serialized_players = {
            'indice': compteur,
            'nom': self.nom.get(), 
            'prenom': self.prenom.get(),
            'datenaissance': self.datenaissance.get(),
            'sexe': self.sex.get(),
            'classement': int(self.classement.get()),
        }
        players_table.insert(serialized_players)
        self.reset()
        
    def reset(self):

        self.nom.set("")
        self.prenom.set("")
        self.datenaissance.set_date(datetime.date.today().strftime("%d/%m/%Y"))
        self.sex.set("")
        self.classement.set(0)

    def numberonly(self):

        if self.classement.get() in "123456789":    
            return True
        else:
            showerror("Classement invalide", "Veuillez recommencer !")
            return False
            
    def creer_widgets(self):

        self.label1 = tk.Label(self, text="Nom de famille").grid(row=0)
        self.label2 = tk.Label(self, text="Prénom").grid(row=1)
        self.label3 = tk.Label(self, text="Date de naissance").grid(row=2)
        self.label4 = tk.Label(self, text="Sexe").grid(row=3)
        self.label5 = tk.Label(self, text="Classement").grid(row=5)
                
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton.grid(row=10, padx=10, pady=10)
        self.bouton = tk.Button(self, text="Valider", command=self.valid)
        self.bouton.grid(row=10, column=1)
        self.bouton = tk.Button(self, text="Reset", command=self.reset)
        self.bouton.grid(row=10, column=2)

        self.nom = tk.StringVar()
        self.prenom = tk.StringVar()
        self.sex = tk.StringVar()
        self.classement = tk.StringVar()

        self.champ1 = tk.Entry(self, textvariable=self.nom)
        self.champ1.grid(row=0, column=1, padx=5, pady=5)
        self.champ2 = tk.Entry(self, textvariable=self.prenom)
        self.champ2.grid(row=1, column=1, padx=5, pady=5)
        
        self.datenaissance = DateEntry(self, width=12, background='darkblue',
                                       foreground='white', borderwidth=2)
        self.datenaissance.grid(row=2, column=1, padx=5, pady=5)

        self.champf = tk.Radiobutton(self, text="F", variable=self.sex, value="F")
        self.champf.grid(row=3, column=1)
        self.champm = tk.Radiobutton(self, text="M", variable=self.sex, value="M")
        self.champm.grid(row=4, column=1)

        self.champ4 = tk.Entry(self, textvariable=self.classement)
        self.champ4.grid(row=5, column=1, padx=5, pady=5)    

    def quit(self):

        ''' Exit'''
        self.destroy()


if __name__ == "__main__":
    app = Players()
    app = tk.Toplevel()
    app.lift()
    app.attributes('-topmost', True)
    app.after_idle(app.attributes, '-topmost', False)
