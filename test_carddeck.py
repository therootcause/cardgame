#!/usr/bin/env python 

import unittest
from carddeck import cardDeck

class CardDeckTestClass(unittest.TestCase):

    def test_52cards(self):
        vals = {}
        deck = cardDeck()
        id = deck.startRound()

        # verify we can draw 52 cards
        for _ in range(52):
            card = deck.draw(id) 
            vals[card['value']] = vals.setdefault(card['value'], 0) + 1

        # a deck should have 13 values 
        self.assertEqual(len(vals), 13)
        # each should have 4 cards
        self.assertTrue(all(count == 4 for count in vals.values()))

        # an aditional draw should fail
        self.assertRaises(Exception, deck.draw(id))

    def test_randomness(self):
        # we expect uniform distribution of first card drawn
        count=130
        min = 5
        max = 15

        vals = {}
        for _ in range(count):
            deck = cardDeck()
            id = deck.startRound()
            card = deck.draw(id)
            index=card['value']+card['suit']
            vals[index] = vals.setdefault(index,0) + 1

        for key,value in vals.items():
            if (value < min) or (value > max):
                print "%s %d" % (key, value) 

if __name__ == '__main__':
    unittest.main()
