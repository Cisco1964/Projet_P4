#!/usr/bin/env python3
import tkinter as tk
from tkinter.constants import CENTER, DISABLED, END, N, NORMAL
from tkinter.font import BOLD
from tkinter.messagebox import showwarning
from tinydb import TinyDB

db = TinyDB('db.json')
score_table = db.table('score')
  
class Score(tk.Tk): 

    def __init__(self): 
        tk.Tk.__init__(self)
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
        serialized_score = {
            'tournament': resultList[0][0], 
            'round': resultList[0][1], 
            'indice1': line_score[0],
            'prenom1': line_score[1],
            'nom1': line_score[2],
            'indice2': line_score[3],
            'prenom2': line_score[4],
            'nom2': line_score[5],
            'score1': line_score[6],
            'score2': line_score[7]
        }
        score_table.insert(serialized_score)
        self.quit()
  

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

playerList = [
    ("001", "Celine", "Durand" , "29/10/2003", "F", "7"),
    ("002", "Francis", "Dupond", "01/12/1995", "M", "6"),
    ("003", "Albert", "Londres", "10/12/1984", "F", "3"),
    ("004", "Ahmed", "Lustre", "15/01/1978", "M", "5"),
    ("005", "Karim", "Zidour" , "29/04/1995", "M", "2"),
    ("006", "Karen", "Durand", "22/06/2010", "F", "8"),
    ("007", "Josepha", "Clarisse", "03/02/2001", "F", "4"),
    ("008", "Celine", "Howard", "14/08/2005", "F", "1")]

   
total_rows = len(lst) 
total_columns = len(lst[0]) 

print(total_rows)
print(total_columns)

app = Score()
app.title("Saisir les scores")
app.mainloop()