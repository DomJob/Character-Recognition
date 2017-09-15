from brain import Brain
import threading

"""
1LIT7J
3EFB8A
O0QCG6D9
RKXYP4
2ZS5
NMWVUH
"""

def trainBrain(name, brain):
    i = 0
    brain.loadTrainer()

    while True:
        print("Training brain %s" % (name.ljust(10)), end="\t")
        brain.train()

        if i % 10 == 0:
            print("Saving brain %s" % (name))
            brain.save("../data/brains/%s.p" % name)
        i+=1

centralBrain = Brain(6)


brains = {
    "1LIT7J"   : Brain(6),
    "3EFB8A"   : Brain(6),
    "O0QCG6D9" : Brain(8),
    "RKXYP4"   : Brain(6),
    "2ZS5"     : Brain(4),
    "NMWVUH"   : Brain(6)
}

centralBrain.load("../data/brains/Central.p")
for name in brains:
    brains[name].load("../data/brains/%s.p" % name)

characterLines = open('../data/characters.txt', 'r').readlines()

for line in characterLines:
    line = line.strip().split("\t")

    inputPixelString = line[1]
    outputLetter = line[0]

    brainIndex = 0
    for charset in brains:
        if outputLetter in charset:
            outputLetterIndex = charset.index(outputLetter)
            break
        brainIndex += 1

    centralBrainOutput = [0.0] * 6
    centralBrainOutput[brainIndex] = 1.0

    subBrain = brains[charset]
    subBrainOutput = [0.0] * len(charset)
    subBrainOutput[outputLetterIndex] = 1.0

    centralBrain.addToDataSet(inputPixelString, centralBrainOutput)
    subBrain.addToDataSet(inputPixelString, subBrainOutput)


threading.Thread(target=trainBrain, args=["Central", centralBrain]).start()

for charset in brains:
    brain = brains[charset]
    threading.Thread(target=trainBrain, args=[charset, brain]).start()