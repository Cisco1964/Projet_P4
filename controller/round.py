#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tinydb import TinyDB
from itertools import islice
from tkinter.messagebox import showinfo, showerror
from model.create_round import add_round

db = TinyDB('db/db.json')


def round(id_tournament, round):

    matchs = research_round_match(int(id_tournament))
    if matchs != []:
        showerror("Résultat", "il y a un tour en attente de saisie pour ce tournoi")
    else:
        players_table = db.table('players')
        serialized_players = players_table.all()
        # sort serialiazed players by ranking
        players_sorted = sorted(serialized_players, key=lambda x: x['classement'])

        array_players = []
        for item in players_sorted:
            players = [item['indice'], item['prenom'], item['nom'], item['classement']]
            array_players.append(players)

        list_players = []
        for item in array_players:
            # data extraction
            list_players.append(item)

        # first round
        my_players = []
        # print(id_tournament, round)
        if round == "round1":
            # sort the list by ranking
            i = len(players_sorted)//2
            for first, second in zip(list_players, islice(list_players, i, None)):
                match = (first[0], second[0])
                my_players.append(match)
            # writing of the round
            add_round(id_tournament, round, my_players)
        else:
            # research the other rounds
            other_round(id_tournament, players_sorted, my_players)
            # writing of the round
            add_round(id_tournament, round, my_players)
            # information message
            showinfo("Résultat", "le {} a été généré".format(round))


def other_round(id_tournament, players_sorted, my_players):

    # store matches already played
    result = research_score(id_tournament)
    list_match = list(map(lambda x: x['joueurs'], result))
    tup_players = {}
    match = []
    for item in result:
        for i, elem in enumerate(item['joueurs']):
            tup_players = elem, item['score'][i]
            match.append(tup_players)
        # Conversion to dictionnary
        tup = {i: 0 for i, v in match}
        # Consolidation des points par indice
        for key, value in match:
            tup[key] = tup[key]+value
        # using map
        resultat = list(map(tuple, tup.items()))
    res = []
    # research of player ranking
    for item in resultat:
        classement = search(item[0], players_sorted)
        add_classement = (classement,)
        tup = item + add_classement
        res.append(tup)
    # sort the list by point (reverse) and ranking
    a = sorted(res, key=lambda x: (-x[1], x[2]))
    # round génération
    array_ctl = []
    for item in a:
        if item[0] not in array_ctl:
            for i in a:
                if i[0] not in array_ctl:
                    if item[0] != i[0]:
                        m = [item[0], i[0]]
                        elem = compare(m, list_match)
                        # print(elem)
                        if elem is not False:
                            my_players.append(m)
                            array_ctl.append(i[0])
                            array_ctl.append(item[0])
                            break
    # print(array_ctl)


def compare(m, list_match):

    """ Recovery of player ranking"""
    for i in list_match:
        m = list(m)
        n = list(reversed(m))
        # print(m, n)
        if m == i or n == i:
            return False


def research_round_match(id_tournament):

        '''recherche s'il y a un tour en cours'''
        tournament_round = db.table('round_match')
        serialized_round_match = tournament_round.all()
        result = []
        for element in serialized_round_match:
            if element['id'] == id_tournament:
                result = element
                break
        return result

def search(i, players_sorted):

    """Reseach of player ranking """
    for element in players_sorted:
        if element['indice'] == i:
            return int(element['classement'])


def research_score(id_tournament):

    '''Research all the round'''
    score_round = db.table('score')
    serialized_score = score_round.all()
    score = []
    for element in serialized_score:
        if element['id'] == int(id_tournament):
            score.append(element)
    return score
