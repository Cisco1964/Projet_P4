#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from tournament import Tournament
from players import Players
from score import Score


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
        menu_file.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Fichier", menu=menu_file)

        menu_tournament = Menu(menu_bar, tearoff=0)
        menu_tournament.add_command(label="Saisie d'un tournoi", command=self.do_tournament)
        menu_tournament.add_separator()
        menu_tournament.add_command(label="Générer round 2", command=self.do_something)
        menu_tournament.add_command(label="Générer round 3", command=self.do_something)
        menu_tournament.add_command(label="Générer round 4", command=self.do_something)
        menu_bar.add_cascade(label="Tournois", menu=menu_tournament)

        menu_players = Menu(menu_bar, tearoff=0)
        menu_players.add_command(label="Saisie des joueurs", command=self.do_players)
        menu_bar.add_cascade(label="Joueurs", menu=menu_players)

        menu_score = Menu(menu_bar, tearoff=0)
        menu_score.add_command(label="Saisie des scores", command=self.do_score)
        menu_bar.add_cascade(label="Scores", menu=menu_score)

        menu_rapport = Menu(menu_bar, tearoff=0)
        menu_liste1 = Menu(menu_rapport, tearoff=0)
        menu_liste2 = Menu(menu_rapport, tearoff=0)

        menu_liste1.add_command(label="par ordre alphabétique")
        menu_liste1.add_command(label="par classement")
        menu_rapport.add_cascade(label="Liste des joueurs", underline=0, menu=menu_liste1)
        menu_rapport.add_separator()

        menu_liste2.add_command(label="par ordre alphabétique")
        menu_liste2.add_command(label="par classement")
        menu_rapport.add_cascade(label="Liste des joueurs d'un tournoi", menu=menu_liste2)
        menu_rapport.add_separator()

        menu_rapport.add_command(label="Liste des tournois", command=self.do_something)
        menu_rapport.add_command(label="Liste de tous les tours d'un tournoi", command=self.do_something)
        menu_rapport.add_command(label="Liste de tous les matches d'un tournoi", command=self.do_something)
        menu_bar.add_cascade(label="Rapports", menu=menu_rapport)

        self.config(menu=menu_bar)

    def do_something(self):
        print("Menu clicked")

    def do_tournament(self):
        Tournament()

    def do_players(self):
        Players()

    def do_score(self):
        Score()

    def do_save(self):
        files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes = files, defaultextension = files)
  

    def quit(self):
        self.destroy()


window = MyWindow()
window.mainloop()