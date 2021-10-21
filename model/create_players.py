#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tinydb import TinyDB


class Create_Players():

    def __init__(self):

        global players_table
        db = TinyDB('db/db.json')
        self.players_table = db.table('players')

    def insert_user(self, compteur, arg1, arg2, arg3, arg4, arg5):
        serialized_players = {
            'indice': compteur,
            'nom': arg1,
            'prenom': arg2,
            'datenaissance': arg3,
            'sexe': arg4,
            'classement': int(arg5),
        }
        self.players_table.insert(serialized_players)

        return
