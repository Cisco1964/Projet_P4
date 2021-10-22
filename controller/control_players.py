#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.messagebox import showerror, showwarning
from tinydb import TinyDB
import datetime
from model.create_players import Create_Players
from view.v_players import V_Players


class Control_Players:

    def __init__(self):

        db = TinyDB('db/db.json')
        global players_table
        players_table = db.table('players')

        self.root = tk.Toplevel()
        self.root.title('Joueurs')

        self.model = Create_Players()
        self.view = V_Players(self.root)
        self.view.quit_btn.config(command=self.quit)
        self.view.valid_btn.config(command=self.valid)
        self.view.reset_btn.config(command=self.reset)

    def valid(self):

        ''' Validation saisie'''
        print(self.view.nom.get())
        if (self.view.nom.get() == ""
            or self.view.prenom.get() == ""
            or self.view.datenaissance.get() == ""
            or self.view.sex.get() == ""
            or self.view.classement.get() == 0
                or self.view.classement.get() == ""):
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
                    self.model.insert_user(compteur, self.view.nom.get(),
                                           self.view.prenom.get(), self.view.datenaissance.get(),
                                           self.view.sex.get(), self.view.classement.get())
                    self.reset()
                else:
                    showwarning("Joueurs", "Vous avez déjà saisi 8 joueurs !")

    def numberonly(self):

        '''Ranking control'''
        if self.view.classement.get() in "123456789":
            return True
        else:
            showerror("Classement invalide", "Veuillez recommencer !")
            return False

    def reset(self):
        self.view.nom.set("")
        self.view.prenom.set("")
        self.view.datenaissance.set_date(datetime.date.today().strftime("%d/%m/%Y"))
        self.view.sex.set("")
        self.view.classement.set(0)

    def quit(self):

        '''Exit'''
        self.root.destroy()


if __name__ == '__main__':
    c = Control_Players()
