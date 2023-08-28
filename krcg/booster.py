from . import vtes
from. import cards

RARITY = [
    'Rare',
    'Uncommon',
    'Common'
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
        self.set = set_name
        self.num_rares = NUM_RARES
        self.num_uncommons = NUM_UNCOMMON[set_name]
        self.num_commons = NUM_COMMON[set_name]
        self.num_vampires = NUM_VAMPS
        self.num_rarity = {'Rare' : self.num_rares, 'Uncommon' : self.num_uncommons, 'Common' : self.num_commons, 'Vampire' : self.num_vampires}

def get_booster():
    booster_library = []
    booster_crypt = []
    
    # for each rarity
    for rarity in RARITY:
        # get a number of cards at the rarty
        get_cards(rarity)
        # add the cards to booster_library

    get_cards('Vampire')
    # add the cards to booster_crypt
    

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