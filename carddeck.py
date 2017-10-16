#!/usr/bin/env python 
import requests
import json

# This abstracts 1 deck of cards
#
# 

class cardDeck:
    #def __init__(self):

    @staticmethod
    def __httpRequest(url):
        response = requests.get(url)
        return response 
 
    def startRound(self):
        response = self.__httpRequest("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
        deck_id = response.json()['deck_id']
        return deck_id
 
    def draw(self, deck_id):
        r = self.__httpRequest("https://deckofcardsapi.com/api/deck/%s/draw/?count=1" % deck_id)
        if (r.status_code == requests.codes.ok) and (r.json()['success'] == True):
            value = r.json()['cards'][0]['value']
            suit = r.json()['cards'][0]['suit']
            return {'value': value, 'suit': suit, 'image': r.json()['cards'][0]['images']['png']}

    def shuffle(self, deck_id):
        r = self.__httpRequest("https://deckofcardsapi.com/api/deck/%s/shuffle/" % deck_id)
