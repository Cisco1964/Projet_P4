#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

class MyWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.create_menu_bar()

        self.geometry("400x300")
        self.title("Projet P4")

    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Sauvegarder", command=self.do_something)
        menu_file.add_separator()
        menu_file.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Application", menu=menu_file)

        menu_tournament = Menu(menu_bar, tearoff=0)
        menu_tournament.add_command(label="Saisie d'un tournoi", command=self.do_tournament)
        menu_tournament.add_separator()
        menu_tournament.add_command(label="Générer un tour", command=self.do_something)
        menu_bar.add_cascade(label="Tournois", menu=menu_tournament)

        menu_players = Menu(menu_bar, tearoff=0)
        menu_players.add_command(label="Saisie des joueurs", command=self.do_players)
        menu_bar.add_cascade(label="Joueurs", menu=menu_players)

        menu_score = Menu(menu_bar, tearoff=0)
        menu_score.add_command(label="Saisie des scores", command=self.do_score)
        menu_bar.add_cascade(label="Scores", menu=menu_score)

        self.config(menu=menu_bar)

    def do_something(self):
        print("Menu clicked")

    def do_tournament(self):
        import tournament
        tournament.Tournament()

    def do_players(self):
        import players
        players.Players()

    def do_score(self):
        import score
        score.Score()


window = MyWindow()
window.mainloop()