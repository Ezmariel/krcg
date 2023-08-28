import random

from . import vtes
from. import cards

RARITY = [
    'Rare',
    'Uncommon',
    'Common',
    'Vampire'
]

SET_LIST = [
    'Third Edition',
    'Sword of Caine',
    'Lords of the Night',
    'Twilight Rebellion',
    'Keepers of Tradition',
    'Ebony Kingdom',
    'Heirs to the Blood'
]

NUM_VAMPS = 3

NUM_RARES = 1

NUM_UNCOMMON = {
    'Third Edition' : 2,
    'Sword of Caine' : 0,
    'Lords of the Night' : 0,
    'Twilight Rebellion' : 0,
    'Keepers of Tradition' : 2,
    'Ebony Kingdom' : 0,
    'Heirs to the Blood' : 0
}

NUM_COMMON = {
    'Third Edition' : 5,
    'Sword of Caine' : 7,
    'Lords of the Night' : 7,
    'Twilight Rebellion' : 7,
    'Keepers of Tradition' : 5,
    'Ebony Kingdom' : 7,
    'Heirs to the Blood' : 7
}

class Booster:
    def __init__(self, set_name):
        self.set_booster = set_name
        self.num_rares = NUM_RARES
        self.num_uncommons = NUM_UNCOMMON[set_name]
        self.num_commons = NUM_COMMON[set_name]
        self.num_vampires = NUM_VAMPS
        self.num_rarity = {'Rare' : self.num_rares, 'Uncommon' : self.num_uncommons, 'Common' : self.num_commons, 'Vampire' : self.num_vampires}

def get_booster(self):
    booster = []
    
    # for each rarity
    for rarity in RARITY:
        if(self.num_rarity[rarity]) != 0:
            # add the cards to booster
            booster.append(get_cards(rarity))

def get_cards(self, card_rarity):    
    cards_for_booster = []
    
    # get list of cards, by name, as an array
    search = cards.CardSearch()
    search.set_dimensions(rarity = card_rarity, set = self.set_booster)
    
    # if num_cards_in_rarity != 0
    while len(cards_for_booster) > self.num_rarity[card_rarity]:
        # remove a random card from the cards array
        cards_for_booster.pop(random.randint(0, len(cards_for_booster) - 1))

    return cards_for_booster