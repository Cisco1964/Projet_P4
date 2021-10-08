#!/usr/bin/python3

from tkinter import Menu, Tk
from tkinter.constants import END
from controller.tournament import Tournament
from controller.players import Players
from controller.update_players import Update_players
from controller.score import update_score
from view.view_all_players import View_all_players
from view.view_tournament import View_tournament
from view.view_choice_tour import View_choice_tour
from view.view_choice_round import View_choice_round
from view.view_round import view_round
from view.view_clear_table import View_clear_table


class MyWindow(Tk):

    def __init__(self):

        Tk.__init__(self)
        self.create_menu_bar()

        self.geometry("400x300")
        self.title("Projet P4")

    def create_menu_bar(self):

        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Remise à blanc des tables", command=self.do_clear)
        menu_file.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Fichier", menu=menu_file)

        menu_players = Menu(menu_bar, tearoff=0)
        menu_players.add_command(label="Saisie des joueurs", command=self.do_players)
        menu_players.add_command(label="Mise à jour classement joueurs", command=self.do_update_players)
        menu_bar.add_cascade(label="Joueurs", menu=menu_players)

        menu_tournament = Menu(menu_bar, tearoff=0)
        menu_tournament.add_command(label="Saisie d'un tournoi", command=self.do_tournament)
        menu_tournament.add_separator()
        menu_tournament.add_command(label="Générer tour suivant", command=self.do_other_round)
        menu_tournament.add_command(label="Visualiser le tour en cours", command=self.do_round)
        menu_bar.add_cascade(label="Tournois", menu=menu_tournament)

        menu_score = Menu(menu_bar, tearoff=0)
        menu_score.add_command(label="Saisie des scores", command=self.do_score)
        menu_bar.add_cascade(label="Scores", menu=menu_score)

        menu_rapport = Menu(menu_bar, tearoff=0)
        menu_liste1 = Menu(menu_rapport, tearoff=0)
        menu_liste2 = Menu(menu_rapport, tearoff=0)

        menu_liste1.add_command(label="par ordre alphabétique", command=self.do_players_name)
        menu_liste1.add_command(label="par classement", command=self.do_players_ranking)
        menu_rapport.add_cascade(label="Liste des joueurs", underline=0, menu=menu_liste1)
        menu_rapport.add_separator()

        menu_liste2.add_command(label="par ordre alphabétique", command=self.do_view_players_t_name)
        menu_liste2.add_command(label="par classement", command=self.do_view_players_t_ranking)
        menu_rapport.add_cascade(label="Liste des joueurs d'un tournoi", menu=menu_liste2)
        menu_rapport.add_separator()

        menu_rapport.add_command(label="Liste des tournois", command=self.do_view_tournament)
        menu_rapport.add_command(label="Liste de tous les tours d'un tournoi", command=self.do_view_round_tour)
        menu_rapport.add_command(label="Liste de tous les matches d'un tournoi", command=self.do_view_match_tour)
        menu_bar.add_cascade(label="Rapports", menu=menu_rapport)

        self.config(menu=menu_bar)

    def do_tournament(self):

        ''' Tournament'''
        Tournament()

    def do_round(self):

        ''' View a round '''
        view_round()

    def do_other_round(self):

        ''' Generate the next round '''
        View_choice_round()

    def do_players(self):

        ''' Entering players '''
        Players()

    def do_update_players(self):

        ''' Update player rankings '''
        Update_players()

    def do_score(self):

        ''' Entering scores '''
        update_score()

    def do_players_name(self):

        ''' List of players by name '''
        View_all_players("nom")

    def do_players_ranking(self):

        ''' List of players by ranking '''
        View_all_players("classement")

    def do_view_tournament(self):

        ''' List of tournaments '''
        View_tournament()

    def do_view_players_t_name(self):

        ''' List of tournament players by name '''
        View_choice_tour("nom")

    def do_view_players_t_ranking(self):

        ''' List of players in a tournament by ranking '''
        View_choice_tour("classement")

    def do_view_round_tour(self):

        ''' List of all rounds in a tournament'''
        View_choice_tour("round")

    def do_view_match_tour(self):

        ''' List of all matches in a tournament '''
        View_choice_tour("match")

    def do_clear(self):

        ''' Clear table'''
        View_clear_table()

    def quit(self):

        ''' Exit '''
        self.destroy()


window = MyWindow()
window.mainloop()
