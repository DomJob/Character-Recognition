from interface.surface import Surface
from brain.brain import Brain
from brain.characterReader import CharacterReader

"""
brains = {
    "123ORM" : Brain(6),
    "LE0KZN" : Brain(6),
    "IFQXHW" : Brain(6),
    "TBCY5V" : Brain(6),
    "78GP9U" : Brain(6),
    "JA64DS" : Brain(6)
}
"""

brains = {
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" : Brain(36)
}

for name in brains:
    brains[name].load("data/brains/%s.p" % name)

characterReader = CharacterReader(brains)

surface = Surface(characterReader)

surface.display()