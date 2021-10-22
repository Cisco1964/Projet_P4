#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Controller du tournoi'''

import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from tinydb import TinyDB
from datetime import date
from controller.round import round
from model.create_tournament import Create_Tournament
from view.v_tournament import V_Tournament


class Control_Tournament:

    def __init__(self):

        db = TinyDB('db/db.json')
        global tournament_table
        tournament_table = db.table('tournament')

        self.root = tk.Toplevel()
        self.root.title("Tournoi")
        self.model = Create_Tournament()
        self.view = V_Tournament(self.root)
        self.view.quit_btn.config(command=self.quit)
        self.view.valid_btn.config(command=self.valid)
        self.view.reset_btn.config(command=self.reset)
        self.run()

    def valid(self):

        ''' Validation'''
        print("v_tournament", self.view.players)
        resdate = self.view.datedeb.get() <= self.view.datefin.get()
        ''' control of the entry and validation if all ok '''
        if (self.view.nom.get() == ""
           or self.view.lieu.get() == ""
           or self.view.datedeb.get() == ""
           or self.view.datefin.get() == ""
           or self.view.tour.get() == 0
           or self.view.players == []
           or self.view.time.get() == ""):
            # error message
            showerror("Résultat", "Saisir tous les champs.\nVeuillez recommencer !")
        elif not resdate:
            showerror("Résultat", "Date de fin < date début")
        elif len(self.view.players) != 8:
            showerror("Résultat", "Vous devez selectionné 8 joueurs")
        else:
            # tournament creation
            name_tournament = self.view.nom.get()
            # search for the last tournament created
            num_tournament = self.last_id()
            self.model.insert_tournament(num_tournament, self.view.nom.get(),
                                         self.view.lieu.get(),
                                         self.view.datedeb.get(),
                                         self.view.datefin.get(),
                                         self.view.tour.get(),
                                         self.view.players,
                                         self.view.time.get(),
                                         self.view.description.get("1.0", "end"))
            # call of the script to generate the first round
            round(num_tournament, "round1")
            # information message
            showinfo("Résultat", "Le tournoi de {} a été créé et\n"
                     "le premier tour a été généré !".format(name_tournament))
            self.reset()

    def last_id(self):

        ''' Research the last id of tournament'''
        if len(tournament_table) == 0:
            num = 1
        else:
            table_sorted = sorted(tournament_table, key=lambda x: x['id'], reverse=True)
            num = table_sorted[0]['id'] + 1
        return num

    def reset(self):

        ''' initialization of input fields '''
        self.view.nom.set("")
        self.view.lieu.set("")
        self.view.datedeb.set_date(date.today().strftime("%d/%m/%Y"))
        self.view.datefin.set_date(date.today().strftime("%d/%m/%Y"))
        self.view.tour.set("4")
        self.view.tournees.set("round1")
        self.view.players = []
        self.view.time.set("")
        self.view.checkbuttons.clear()
        self.view.description.delete("1.0", "end")

    def run(self):

        self.root.mainloop()

    def quit(self):

        '''Exit'''
        self.root.destroy()


if __name__ == '__main__':
    Control_Tournament()
