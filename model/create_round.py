#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query
from tinydb.operations import add
import datetime

''' Création des rounds'''

db = TinyDB('db/db.json')


def add_round(id_tournament, round, my_players):

    """ create round """
    datedeb = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    serialized_match = {'id': int(id_tournament),
                        'round': round,
                        'datedebut': datedeb,
                        'joueurs': my_players}
    db.table('round_match').insert(serialized_match)
    db.table('round_match').clear_cache()

    ''''update value round'''
    tournament_table = db.table('tournament')
    Tournament_db = Query()
    if round != "round1":
        tournament_table.update(add('round', round.split()), Tournament_db.id == int(id_tournament))
    return
