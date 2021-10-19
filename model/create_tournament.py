#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Création du tournoi'''

from tinydb import TinyDB


class Create_Tournament():

    def __init__(self):

        db = TinyDB('db/db.json')
        global tournament_table
        tournament_table = db.table('tournament')

    def insert_tournament(self, num_tournament, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):

        ''' record creation '''
        nom_round = ['round1']
        serialized_tournament = {
            'id': num_tournament,
            'name': arg1,
            'lieu': arg2,
            'datedebut': arg3,
            'datefin': arg4,
            'tour': arg5,
            'round': nom_round,
            'joueurs': arg6,
            'time': arg7,
            'description': arg8
        }
        tournament_table.insert(serialized_tournament)

        return
