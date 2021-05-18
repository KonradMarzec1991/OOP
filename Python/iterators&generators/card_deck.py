from collections import namedtuple


Card = namedtuple('Card', 'rank suit')
SUITS = ('Spades', 'Heats', 'Diamonds', 'Clubs')
RANKS = tuple(range(2, 11)) + tuple('JQKA')


def card_gen():
    for i in range(len(SUITS) * len(RANKS)):
        suit = SUITS[i // len(RANKS)]
        rank = RANKS[i % len(RANKS)]
        card = Card(rank, suit)
        yield card


for card in card_gen():
    print(card)