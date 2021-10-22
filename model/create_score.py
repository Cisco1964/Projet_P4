#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' - Mise à jour de la date de fin du tour en question ROUND
    - Ecriture dans la table SCORE
    - Rmise à blanc de la table ROUND_MATCH'''

from tinydb import TinyDB, where
import datetime


db = TinyDB('db/db.json')


class Create_Score():
   
    def insert_score(self, id_tournament, round, line_score):

        """Writing the recording SCORE """
        score_table = db.table('score')
        players = (int(line_score[0]), int(line_score[3]))
        score = (float(line_score[6]), float(line_score[7]))
        serialized_score = {
            'id': int(id_tournament),
            'round': round,
            'joueurs': players,
            'score': score,
        }
        score_table.insert(serialized_score)
        print("ok")
        return

    def insert_round(self, players_round, id_tournament, round, datedebut):

        """Writing the recording ROUND"""
        round_table = db.table('round')
        datefin = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        serialized_round = {
            'id': int(id_tournament),
            'round': round,
            'joueurs': players_round,
            'datedebut': datedebut,
            'datefin': datefin
        }
        round_table.insert(serialized_round)
        return

    def update_round_match(self, id_tournament):

        ''' remove record of round_match'''
        tournament_round = db.table('round_match')
        tournament_round.remove(where('id') == int(id_tournament))
        db.clear_cache()
        return
