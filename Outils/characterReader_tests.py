from brain.brain import Brain
from brain.characterReader import CharacterReader
import sys

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
characterLines = open('data/characters_unknown.txt', 'r').readlines()

i = 1
for line in characterLines:
    line = line.strip().split("\t")
    expected = line[0]
    pixelString = line[1]
    
    if characterReader.readFailed(pixelString):
        print(expected, "Failed")
        continue
    
    read = characterReader.read(pixelString)
    if read[0][0] != expected and read[1][0] != expected:
        print(expected, read[:3])