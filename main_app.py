#!/usr/bin/python3

from tkinter import *
from tkinter.filedialog import asksaveasfile
from tournament import Tournament
from players import Players
from update_players import Update_players
from score import update_score
from view_all_players import view_all
from view_tournament import View_tournament
from view_choice_tour import view_choice
from view_choice_round import view_gen_round
from view_round import view_round
from view_clear_table import clear_table


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
        menu_file.add_command(label="Remise à blanc des tables", command=self.do_clear)
        menu_file.add_separator()
        menu_file.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Fichier", menu=menu_file)

        menu_tournament = Menu(menu_bar, tearoff=0)
        menu_tournament.add_command(label="Saisie d'un tournoi", command=self.do_tournament)
        menu_tournament.add_separator()
        menu_tournament.add_command(label="Générer tour suivant", command=self.do_other_round)
        menu_tournament.add_command(label="Visualiser le tour en cours", command=self.do_round)
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
        menu_rapport.add_command(label="Liste de tous les tours d'un tournoi", command=self.do_view_round_tour)
        menu_rapport.add_command(label="Liste de tous les matches d'un tournoi", command=self.do_view_match_tour)
        menu_bar.add_cascade(label="Rapports", menu=menu_rapport)

        self.config(menu=menu_bar)

    def do_tournament(self):

        ''' Tournois'''
        Tournament()

    def do_round(self):

        ''' Visualiser un round '''
        view_round()

    def do_other_round(self):

        ''' Générer le tour suivant '''
        view_gen_round()

    def do_players(self):

        ''' Saisie des joueurs '''
        Players()

    def do_maj_players(self):

        ''' Mise à jour du classement des joueurs '''
        Update_players()

    def do_score(self):

        ''' Saisie des scores '''
        update_score()

    def do_joueurs_alpha(self):

        ''' Liste des joueurs par nom '''
        view_all("nom")

    def do_joueurs_class(self):

        ''' Liste des joueurs par classement '''
        view_all("classement")

    def do_view_tournament(self):

        ''' Liste des tournois '''
        View_tournament()

    def do_view_joueurs_t_alpha(self):

        ''' Liste des joueurs d'un tournoi par nom '''
        view_choice("nom")

    def do_view_joueurs_t_class(self):

        ''' Liste des joueurs d'un tournoi par classement '''
        view_choice("classement")

    def do_view_round_tour(self):

        ''' Liste de tous les rounds d'un tournoi '''
        view_choice("round")

    def do_view_match_tour(self):

        ''' Liste de tous les matchs d'un tournoi '''
        view_choice("match")

    def do_save(self):

        ''' Sauvegarde des fichiers'''
        files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes = files, defaultextension = files)

    def do_clear(self):

        ''' Clear table'''
        clear_table()
  
    def quit(self):

        ''' Exit '''
        self.destroy()


window = MyWindow()
window.mainloop()