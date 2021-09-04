#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.constants import CENTER, DISABLED, END, N, NORMAL
from tkinter.font import BOLD
from tkinter.messagebox import showwarning
from tinydb import TinyDB, Query
from first_round import First_round

db = TinyDB('db.json')
players_table = db.table('players')
  
class Update_players(tk.Toplevel):

    def __init__(self): 
        tk.Toplevel.__init__(self)
        self.title("Mise à jour classement joueurs")
   
        global total_rows
        global total_columns
        total_columns = 4

        players_table = db.table('players')

        if players_table == "":
            showwarning("Résultat", "veuillez saisir des joueurs !")
        else:
            serialized_players = players_table.all()

        total_rows = len(serialized_players)
        print(serialized_players)

        tableau_joueurs = []
        for item in serialized_players:
            players = (item['indice'], item['prenom'], item['nom'], item['classement'])
            tableau_joueurs.append(players) 

        self.data = list()          
        for i in range(total_rows): 
            line = list()
            for j in range(total_columns): 
                self.e = tk.Entry(self, width=10)
                self.e.grid(row=i, column=j)
                self.e.configure(state=NORMAL)
                self.e.insert(END, tableau_joueurs[i][j]) 
                if j < 3:
                    self.e.configure(state=DISABLED)
                line.append(self.e) 
            self.data.append(line)
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton.grid(row=10, column=1, padx=10, pady=10)
        self.bouton = tk.Button(self, text="Valider", command=self.valid)
        self.bouton.grid(row=10, column=2)

    def valid(self):
        my_bool = True
        for i in range(total_rows):   
            if float(self.data[i][3].get()) == 0:
                showwarning("Résultat", "Classement invalide !")
                my_bool = False
                break
        if my_bool:
            line_player = []
            for i in range(total_rows):   
                for j in range(total_columns): 
                    line_player.append(self.data[i][j].get())
                self.update(line_player)
                line_player = []

    def update(self, line_player):
        #serialized_players = {
            #'nom': self.nom.get(), 
            #'prenom': self.prenom.get(),
            #'classement': self.classement.get(),
        #}
        #print(serialized_players)
        #players_table.update(serialized_players)
        #players_table.update({'classement':self.classement.get()})
        joueurs = Query()
        db.search(joueurs.classement.get() == 1)
        print('coucou')
        self.quit()

    def quit(self):
        self.destroy()
  
if __name__ == "__main__":  
    
    app = Update_players()
    app.title("Mise à jour classement joueurs")
    app.mainloop()