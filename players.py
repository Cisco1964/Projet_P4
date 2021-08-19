#!/usr/bin/env python3
import tkinter as tk
from tkinter.messagebox import showwarning
from tinydb import TinyDB

db = TinyDB('db.json')
players_table = db.table('players')


class Players(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()

    def valid(self):
        if (self.nom.get() == "" 
        or self.prenom.get() == "" 
        or self.datenaissance.get() == "" 
        or self.sex.get() == "" 
        or self.classement.get() == 0):
            showwarning("Résultat", "Saisir tous les champs.\nVeuillez recommencer !")
        else:
            elements = len(players_table)
            if elements < 8:
                if elements == 0:
                    compteur = 1 
                else:
                    compteur = elements + 1
                print(compteur)
                self.insert_user(compteur)
            else:
                showwarning("Résultat", "Vous avez déjà saisi 8 joueurs !")
                
    def insert_user(self, compteur):
        serialized_players = {
            'indice': compteur,
            'name': self.nom.get(), 
            'prenom': self.prenom.get(),
            'datenaissance': self.datenaissance.get(),
            'sexe': self.sex.get(),
            'classement': self.classement.get(),
        }
        print(serialized_players)
        players_table.insert(serialized_players)
        self.reset()
        
    def reset(self):
        self.nom.set("")
        self.prenom.set("")
        self.datenaissance.set("")
        self.sex.set("")
        self.classement.set(0)
        print("reset")

    def sexe(self):
        print(self.sex.get())

    def valid_classement(self):
        if self.classement.isnotdigit():
            showwarning("Résultat", "le classement doit être numérique et > à 0 \nVeuillez recommencer !")
            return False
            self.classement.set("")
        else:
            return True

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
        self.datenaissance = tk.StringVar()
        self.sex = tk.StringVar()
        self.classement = tk.IntVar()

        self.champ1 = tk.Entry(self, textvariable=self.nom)
        self.champ1.grid(row=0, column=1, padx=5, pady=5)
        self.champ2 = tk.Entry(self, textvariable=self.prenom)
        self.champ2.grid(row=1, column=1, padx=5, pady=5)
        self.champ3 = tk.Entry(self, textvariable=self.datenaissance)
        self.champ3.grid(row=2, column=1, padx=5, pady=5)
        self.champf = tk.Radiobutton(self, text="F", variable=self.sex, value="F", command=self.sexe)
        self.champf.grid(row=3, column=1)
        self.champm = tk.Radiobutton(self, text="M", variable=self.sex, value="M", command=self.sexe)
        self.champm.grid(row=4, column=1)
        self.champ4 = tk.Entry(self, textvariable=self.classement, validate='key', validatecommand=(self.valid_classement, '% P'))
        self.champ4.grid(row=5, column=1, padx=5, pady=5)             

if __name__ == "__main__":
    app = Players()
    app.title("Joueurs")
    app.mainloop()
