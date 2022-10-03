from . import vtes

NUM_RARES = {
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
        self.num_rares = NUM_RARES[set_name]
        self.num_uncommons = NUM_UNCOMMON[set_name]
        self.num_commons = NUM_COMMON[set_name]
        self.num_vampires = NUM_VAMPIRE[set_name]