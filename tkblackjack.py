#!/usr/bin/env python 

import requests
import Tkinter as tk
from carddeck import cardDeck

root = tk.Tk()
root.title("some cards")


deck = cardDeck()
id = deck.startRound()
resp = deck.draw(id)

response = requests.get(resp['image'])
with open('/tmp/tmp.png', 'wb') as f:
    f.write(response.content)

photo = tk.PhotoImage(file= r"/tmp/tmp.png")
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=photo, anchor='nw')
root.mainloop()






#!/usr/bin/env python 

from carddeck import cardDeck

# our game is like:
# 4 cards are drawn automatically
# up to 1 additional card(s) can be drawn
# deck will be reshuffled

startingCards = 2
additionalCards = 3
rankedcards = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']

class simpleGame():
 
    def __init__(self):
        self.deck = cardDeck()
        self.vals = {}

    def drawcard(self, id):
        card = self.deck.draw(id) 

        self.vals[card['value']] = self.vals.setdefault(card['value'], 0) + 1 
        print "%(value)s of %(suit)s" % (card)

    def run(self):
        id = self.deck.startRound()

        for _ in range(0,startingCards):
            self.drawcard(id)

        for _ in range(0,additionalCards):
            answer = raw_input("would you like to draw another card (y/n)?")
            if answer.lower().startswith('n'):
                break
            card = self.drawcard(id)
           
    def report(self): 
        cardsummary = []
        for key in rankedcards:
            count = self.vals.get(key)
            if count is not None:
                cardsummary.append("%s:%s" % (key,count))
        print ", ".join(cardsummary)

if __name__ == '__main__':
    game = simpleGame()
    game.run()
    game.report()
