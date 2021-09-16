#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tinydb import TinyDB
from itertools import islice
import datetime


db = TinyDB('db.json')


def round(name_tournament):
  print(name_tournament)
  players_table = db.table('players')
  serialized_players = players_table.all()
  tableau_joueurs = []
  for item in serialized_players:
    players = [item['indice'], item['prenom'], item['nom'], item['classement']]
    print(players)
    tableau_joueurs.append(players)

  liste_joueurs = []
  for item in tableau_joueurs:
    ''' extraction des données '''
    liste_joueurs.append(item)

  ''' écriture du premier round '''
  i = len(serialized_players)//2
  
  joueurs = []
  match_table = db.table('round_match')
  for first, second in zip(liste_joueurs, islice(liste_joueurs, i, None)):
      match = (first[0], second[0])
      joueurs.append(match)

  datedeb = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
  serialized_match = {
      'tournament': name_tournament,
      'round': "round1", 
      'datedebut' : datedeb,
      'datefin' : 0,
      'joueurs': joueurs,
      }
  match_table.insert(serialized_match)
