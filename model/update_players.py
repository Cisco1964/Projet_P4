#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Mise à jour du classement des joueurs'''

from tinydb import TinyDB, Query

db = TinyDB('db/db.json')


class Update_Players():

    def update(self, line_player):

        ''' Update player rankings'''
        players_table = db.table('players')
        players_table.update({'classement': int(line_player[3])}, Query().indice == int(line_player[0]))
