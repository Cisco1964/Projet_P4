#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tinydb import TinyDB

db = TinyDB('db.json')
round_table = db.table('round')


class View_round_tour(tk.Toplevel):

    def __init__(self, id_tournament):

        tk.Toplevel.__init__(self)
        # research the name of the tournament
        name_tournament = search_tournament(id_tournament)
        self.title("Liste des tous les rounds du tournoi de {}".format(name_tournament))
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.construct(id_tournament)

    def construct(self, id_tournament):

        tv = ttk.Treeview(self, columns=(1, 2, 3), show='headings', height=4)
        tv.pack()

        tv.heading(1, text='round')
        tv.heading(2, text='date début')
        tv.heading(3, text='date fin')

        # research all the round for the tournament
        result = research_round(id_tournament)
        print(result)
        i = 0
        for item in result:
            tv.insert(parent='', index=i, iid=i, values=(item['round'], item['datedebut'],
                      item['datefin']))
            i += 1


def search_tournament(id_tournament):

    '''Research the name of the tournament'''
    tournament_table = db.table('tournament')
    serialized_tournament = tournament_table.all()
    for element in serialized_tournament:
        if element['id'] == int(id_tournament):
            return element['name']


def research_round(id_tournament):

    '''Research all the round'''
    serialized_round = round_table.all()
    round = []
    for element in serialized_round:
        if element['id'] == int(id_tournament):
            round.append(element)
    return round


def view_r_tour(id_tournament):

    View_round_tour(id_tournament)
