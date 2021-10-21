#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Mise à jour du classement des joueurs'''

import tkinter as tk
from tkinter.constants import DISABLED, END, NORMAL
from tkinter.messagebox import showwarning
from model.update_players import Update_Players
from view.v_maj_players import V_Maj_Players


class Maj_Players(tk.Toplevel):

    def __init__(self):

        self.root = tk.Toplevel()
        self.root.title("Mise à jour classement joueurs")
        self.model = Update_Players()
        self.view = V_Maj_Players(self.root)
        self.view.quit_btn.config(command=self.quit)
        self.view.valid_btn.config(command=self.valid)

    def main(self):
        self.view.main()

    def valid(self):

        ''' controle de la saisie
        si my_bool == True , on valide la mise à jour
        '''
        my_bool = True
        for i in range(self.view.total_rows):
            if float(self.view.data[i][3].get()) == 0:
                showwarning("Résultat", "Classement invalide !")
                my_bool = False
                break
        if my_bool:
            line_player = []
            for i in range(self.view.total_rows):
                for j in range(self.view.total_columns):
                    line_player.append(self.view.data[i][j].get())
                self.model.update(line_player)
                line_player = []

    def quit(self):

        ''' Exit'''
        self.root.destroy()


if __name__ == '__main__':
    c = Maj_Players()
    c.main()
