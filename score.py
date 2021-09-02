#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.constants import CENTER, DISABLED, END, N, NORMAL
from tkinter.font import BOLD
from tkinter.messagebox import showwarning
from tinydb import TinyDB, Query

db = TinyDB('db.json')
score_table = db.table('score')
  
class Score(tk.Toplevel):

    def __init__(self): 
        tk.Toplevel.__init__(self)
        self.title("Saisir les scores")
        lst = [
        ("001", "Celine", 'Durand', '005' , "Karim", "Zidour", 0, 0), 
        ("002", "Francis", "Dupond", "006", "Karen", "Durand", 0, 0), 
        ("003", "Albert", "Londres", "007", "Josepha", "Clarisse", 0, 0), 
        ("004", "Ahmed", "Lustre", "008", "Celine", "Howard", 0, 0)] 

        resultList = [
        ("A", "round1", ("001", "005"), 0, 0),
        ("A", "round1", ("002", "006"), 0, 0),
        ("A", "round1", ("003", "007"), 0, 0),
        ("A", "round1", ("004", "008"), 0, 0)]
   
        global total_rows
        global total_columns
        total_rows = 4
        total_columns = 8

        round_table = db.table('round')
        players_table = db.table('players')

        if round_table == "":
            showwarning("Résultat", "veuillez générer le prochain round !")
        else:
            serialized_round = round_table.all()
            serialized_players = players_table.all()

        match_joueurs = []
        for item in serialized_round:

            Name = Query()
            round_table.search(Name.indice == item['joueurs'][0])

            #players = Joueur(item['indice'], item['prenom'], item['nom'], item['classement'])
            #tableau_joueurs.append(players)

        self.data = list()          
        for i in range(total_rows): 
            line = list()
            for j in range(total_columns): 
                self.e = tk.Entry(self, width=20)
                self.e.grid(row=i, column=j)
                self.e.configure(state=NORMAL)
                self.e.insert(END, lst[i][j]) 
                if j < 6:
                    self.e.configure(state=DISABLED)
                line.append(self.e) 
            self.data.append(line)
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton.grid(row=10, column=3, padx=10, pady=10)
        self.bouton = tk.Button(self, text="Valider", command=self.valid)
        self.bouton.grid(row=10, column=4)

    def valid(self):
        my_bool = True
        for i in range(total_rows):    
            result = float(0)
            result = float(self.data[i][6].get()) + float(self.data[i][7].get()) 
            print(result)
            if result > 1 or result == 0:
                showwarning("Résultat", "Score invalide.\nVeuillez recommencer !")
                my_bool = False
                break
        if my_bool:
            line_score = []
            for i in range(total_rows):   
                for j in range(total_columns): 
                    line_score.append(self.data[i][j].get())
                self.insert_score(line_score)
                line_score = []

    def insert_score(self, line_score):
        joueurs = (line_score[0], line_score[3])
        score = (line_score[6], line_score[7])
        serialized_score = {
            'tournament': resultList[0][0], 
            'round': resultList[0][1], 
            'joueurs': joueurs,
            'score': score,
        }
        score_table.insert(serialized_score)
        self.quit()

    def quit(self):
        self.destroy()
  
if __name__ == "__main__":  
    
    app = Score()
    app.title("Saisir les scores")
    app.mainloop()