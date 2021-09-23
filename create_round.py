#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query, where
from tinydb.operations import add
from itertools import islice, groupby
import datetime


db = TinyDB('db.json')


def round(name_tournament, round):
  print(name_tournament)
  print(round)
  players_table = db.table('players')
  serialized_players = players_table.all()
  tableau_joueurs = []
  for item in serialized_players:
    players = [item['indice'], item['prenom'], item['nom'], item['classement']]
    #print(players)
    tableau_joueurs.append(players)

  liste_joueurs = []
  for item in tableau_joueurs:
    # extraction des données 
    liste_joueurs.append(item)

  # premier round
  if round == "round1":
    i = len(serialized_players)//2
    joueurs = []
    for first, second in zip(liste_joueurs, islice(liste_joueurs, i, None)):
        match = (first[0], second[0])
        joueurs.append(match)
    # écriture du round
    add_round(name_tournament, round, joueurs)
  else:
    # écriture les autres tours
    joueurs = []
    other_round(name_tournament, round, serialized_players, joueurs)
    # écriture du round
    add_round(name_tournament, round, joueurs)
    # mise à jour du tournoi pour le round
    update_tournament(name_tournament, round)

def other_round(name_tournament, round, serialized_players, joueurs):
  score_round = db.table('score')
  Round = Query()
  result = score_round.search(Round.tournament == name_tournament)

  # stocker les matchs dejà joué
  serialized_score = score_round.all()
  liste_match = list(map(lambda x : x['joueurs'], serialized_score))

  tup_joueur = {}
  match = []
  for item in result:
    for i, id in enumerate(item['joueurs']):
      tup_joueur = id, item['score'][i]
      print(tup_joueur)
      match.append(tup_joueur)

  # Convertion en dictionnaire
  tup = {i:0 for i, v in match}

  # Consolidation des points par indice
  for key, value in match:
    tup[key] = tup[key]+value

  # using map
  resultat = list(map(tuple, tup.items()))

  # recherche du classement du joueur
  res = []
  for item in resultat:
    classement = search(item[0], serialized_players)
    add_classement = (classement,)
    tup = item + add_classement
    print(tup)
    res.append(tup)

  # tri de la liste par points (reverse) et par classement
  a = sorted(res, key=lambda x: (-x[1],x[2]))

  # generation du round
  array_ctl = []
  for item in a:
    if item[0] not in array_ctl:
      for i in a:
        if i[0] not in array_ctl:
          if item[0] != i[0]:
            m = [item[0], i[0]]
            elem = compare(m, liste_match)
            if elem != False:
              joueurs.append(m)
              array_ctl.append(i[0])
              array_ctl.append(item[0])
            break
        
  print("joueurs", joueurs)

def compare(m, liste_match):
    """Récupération du classement du joueur"""
    for i in liste_match:
        m = list(m)
        n = list(reversed(m))
        if m == i or n == i:
          return False

def search(i, serialized_players):
  """Récupération du classement du joueur"""
  for element in serialized_players:
    if element['indice'] == i:
      return int(element['classement'])

def add_round(name_tournament, round, joueurs):
  """ création du round """
  datedeb = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
  serialized_match = {
      'tournament': name_tournament,
      'round': round, 
      'datedebut' : datedeb,
      'joueurs': joueurs,
      }
  db.table('round_match').insert(serialized_match)

def update_tournament(name_tournament, round):
  print(name_tournament, round)
  tournament_table = db.table('tournament')
  tournament_db = Query()
  tournament_table.update(add('round', round), tournament_db.tournament == name_tournament)


