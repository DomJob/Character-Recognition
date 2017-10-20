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
    
    backupRead = characterReader.backupRead(pixelString)
    
    failed = characterReader.readFailed(pixelString)
    
    if failed:
        print(i, expected, backupRead[:3])
        i+=1

sys.exit()
i=-1
for line in characterLines:
    i+=1
    
    line = line.strip().split("\t")
    expected = line[0]
    pixelString = line[1]
    
    detectedCharsets = characterReader.getCharset(pixelString)
    detectedCharset = detectedCharsets[0][0]
    
    output = characterReader.read(pixelString)
    backupRead = characterReader.backupRead(pixelString)
    
    if expected not in detectedCharset:
        if output[0][1] > 0.6:
            print(i, expected, "not in charset:", detectedCharset, "mixed with", output[0])
