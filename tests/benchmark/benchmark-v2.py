from interface.surface import Surface
from brain.brain import Brain
from brain.characterReader import CharacterReader
import time


brains = {
    "0ODGCQ" : Brain(6),
    #"1IJ3B8" : Brain(6),
    #"2Z5SEF" : Brain(6),
    #"AHTKXW" : Brain(6),
    "MNVUY7" : Brain(6),
    #"469LPR" : Brain(6)
}

characterReader = CharacterReader(brains)
#characterLines = open('data/characters.txt', 'r').readlines()
characterLines = open('data/characters_unknown.txt', 'r').readlines()

for name in brains:
    brains[name].load("data/brains-similaire-plus-0/%s.p" % name)

file = open('bench-v2.txt','w')
for line in characterLines:
    line = line.strip().split("\t")

    inputPixelString = line[1]

    expected = line[0]
    
    
    
    for charset in brains:
        if expected in charset:
            line = charset + "\t"
            line += expected + "\t"
            bOutput = brains[charset].activate(inputPixelString)
            
            maxProb = -1
            for i in range(6):
                if bOutput[i] > maxProb:
                    result = charset[i]
                    maxProb = bOutput[i]
                
            
            line += result + "\t"
            line += "\t".join([ str(round(p,5)) for p in bOutput])
            
            if expected != result:
                print(line)
            file.write(line + '\n')
