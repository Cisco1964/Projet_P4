#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from tournament import Tournament
from players import Players
from update_players import Update_players
from score import Score
from view_players_alpha import Players_alpha
from view_players_class import Players_class
from view_tournament import View_tournament
from view_tour1_alpha import View_tour1_alpha
from view_tour1_class import View_tour1_class
from view_tour_round import *


class MyWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.create_menu_bar()

        self.geometry("400x300")
        self.title("Projet P4")

    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Sauvegarder", command=self.do_save)
        menu_file.add_separator()
        menu_file.add_command(label="Supprimer les tables", command=self.do_clear)
        menu_file.add_separator()
        menu_file.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Fichier", menu=menu_file)

        menu_tournament = Menu(menu_bar, tearoff=0)
        menu_tournament.add_command(label="Saisie d'un tournoi", command=self.do_tournament)
        menu_tournament.add_separator()
        menu_tournament.add_command(label="Visualiser round 1", command=self.do_round1)
        menu_tournament.add_command(label="Générer round 2", command=self.do_round2)
        menu_tournament.add_command(label="Générer round 3", command=self.do_round3)
        menu_tournament.add_command(label="Générer round 4", command=self.do_round4)
        menu_bar.add_cascade(label="Tournois", menu=menu_tournament)

        menu_players = Menu(menu_bar, tearoff=0)
        menu_players.add_command(label="Saisie des joueurs", command=self.do_players)
        menu_players.add_command(label="Mise à jour classement joueurs", command=self.do_maj_players)
        menu_bar.add_cascade(label="Joueurs", menu=menu_players)

        menu_score = Menu(menu_bar, tearoff=0)
        menu_score.add_command(label="Saisie des scores", command=self.do_score)
        menu_bar.add_cascade(label="Scores", menu=menu_score)

        menu_rapport = Menu(menu_bar, tearoff=0)
        menu_liste1 = Menu(menu_rapport, tearoff=0)
        menu_liste2 = Menu(menu_rapport, tearoff=0)

        menu_liste1.add_command(label="par ordre alphabétique", command=self.do_joueurs_alpha)
        menu_liste1.add_command(label="par classement", command=self.do_joueurs_class)
        menu_rapport.add_cascade(label="Liste des joueurs", underline=0, menu=menu_liste1)
        menu_rapport.add_separator()

        menu_liste2.add_command(label="par ordre alphabétique", command=self.do_view_joueurs_t_alpha)
        menu_liste2.add_command(label="par classement", command=self.do_view_joueurs_t_class)
        menu_rapport.add_cascade(label="Liste des joueurs d'un tournoi", menu=menu_liste2)
        menu_rapport.add_separator()

        menu_rapport.add_command(label="Liste des tournois", command=self.do_view_tournament)
        menu_rapport.add_command(label="Liste de tous les tours d'un tournoi", command=self.do_something)
        menu_rapport.add_command(label="Liste de tous les matches d'un tournoi", command=self.do_something)
        menu_bar.add_cascade(label="Rapports", menu=menu_rapport)

        self.config(menu=menu_bar)

    def do_something(self):
        print("Menu clicked")

    def do_tournament(self):
        Tournament()

    def do_round1(self):
        pass

    def do_round2(self):
        view_round("round2")

    def do_round3(self):
        view_round("round3")

    def do_round4(self):
        view_round("round4")

    def do_players(self):
        Players()

    def do_maj_players(self):
        Update_players()

    def do_score(self):
        Score()

    def do_joueurs_alpha(self):
        Players_alpha()

    def do_joueurs_class(self):
        Players_class()

    def do_view_tournament(self):
        View_tournament()

    def do_view_joueurs_t_alpha(self):
        View_tour1_alpha()

    def do_view_joueurs_t_class(self):
        View_tour1_class()

    def do_save(self):
        files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes = files, defaultextension = files)

    def do_clear(self):
        print("Menu clicked")
  

    def quit(self):
        self.destroy()


window = MyWindow()
window.mainloop()