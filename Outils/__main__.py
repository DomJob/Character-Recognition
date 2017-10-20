from interface.surface import Surface
from brain.brain import Brain
from brain.characterReader import CharacterReader


brains = [
    Brain("0ODGCQ"),
    Brain("1IJ3B8"),
    Brain("2Z5SEF"),
    Brain("AHTKXW"),
    Brain("MNVUY7"),
    Brain("469LPR")
]
centralBrain = Brain("Central")
centralBrain.load("data/brains/Central.p")

for brain in brains:
    brain.load("data/brains/%s.p" % brain.charset)



characterReader = CharacterReader(brains, centralBrain)

surface = Surface(characterReader)
surface.display()