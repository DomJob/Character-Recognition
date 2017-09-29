from interface.surface import Surface
from brain.brain import Brain
from brain.characterReader import CharacterReader

'''
brains = {
    "123ORM" : Brain(6),
    "LE0KZN" : Brain(6),
    "IFQXHW" : Brain(6),
    "TBCY5V" : Brain(6),
    "78GP9U" : Brain(6),
    "JA64DS" : Brain(6)
}
'''

brains = {
    #"1LIT7J" : Brain(6),
    #"2ZS5" : Brain(6),
    "RKXYP4" : Brain(6),
    #"NMWVUH" : Brain(6),
    #"3EFB8A" : Brain(6),
    #"O0QCG6D9" : Brain(6)
}

characterReader = CharacterReader(brains)


for name in brains:
    brains[name].load("data/brains/%s.p" % name)


characterReader = CharacterReader(brains)


surface = Surface(characterReader)
surface.display()