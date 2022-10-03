from . import vtes
from. import cards

RARITY = [
    'Rare',
    'Uncommon',
    'Common',
    'Vampire'
]

NUM_RARE = {
    'third edition' : 1,
    'sword of caine' : 1,
    'lords of the night' : 1,
    'twilight rebellion' : 1,
    'keepers of tradition' : 1,
    'ebony kingdom' : 1,
    'heirs to the blood' : 1
}

NUM_UNCOMMON = {
    'third edition' : 2,
    'sword of caine' : 0,
    'lords of the night' : 0,
    'twilight rebellion' : 0,
    'keepers of tradition' : 2,
    'ebony kingdom' : 0,
    'heirs to the blood' : 0
}

NUM_COMMON = {
    'third edition' : 5,
    'sword of caine' : 7,
    'lords of the night' : 7,
    'twilight rebellion' : 7,
    'keepers of tradition' : 2,
    'ebony kingdom' : 7,
    'heirs to the blood' : 7
}

NUM_VAMPIRE = {
    'third edition' : 3,
    'sword of caine' : 3,
    'lords of the night' : 3,
    'twilight rebellion' : 3,
    'keepers of tradition' : 3,
    'ebony kingdom' : 3,
    'heirs to the blood' : 3
}

class Booster:
    def __init__(self, set_name):
        self.set = set_name
        self.num_rares = NUM_RARE[set_name]
        self.num_uncommons = NUM_UNCOMMON[set_name]
        self.num_commons = NUM_COMMON[set_name]
        self.num_vampires = NUM_VAMPIRE[set_name]
        self.num_rarity = {'Rare' : self.num_rares, 'Uncommon' : self.num_uncommons, 'Common' : self.num_commons, 'Vampire' : self.num_vampires}

def get_booster():
    booster = []
    
    # for each rarity
    for rarity in RARITY:
        # get a number of cards at the rarty
        get_cards(rarity)
        # add the cards to the booster

def get_cards(self, rarity):
    cards = []
    
    # get number of cards of given rarity in the set
    num_cards_in_rarity = 0
    
    # if num_cards_in_rarity != 0
    while len(cards) < self.num_rarity[rarity]:
        # get random card from that rarity
        # if that card is not in the collection of cards
            # add it to the cards[]
        pass

    #return cards[]