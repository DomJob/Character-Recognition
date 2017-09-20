from brain import Brain
import threading


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

#centralBrain = Brain(6)
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

# centralBrain.load("../data/brains/Central.p")
#for name in brains:
#    brains[name].load("../data/brains/%s.p" % name)



characterLines = open('../data/characters.txt', 'r').readlines()

for line in characterLines:
    line = line.strip().split("\t")

    inputPixelString = line[1]
    outputLetter = line[0]

    #brainIndex = 0
    for charset in brains:
        if outputLetter in charset:
            outputLetterIndex = charset.index(outputLetter)
            break
        #brainIndex += 1

    #centralBrainOutput = [0.0] * 6
    #centralBrainOutput[brainIndex] = 1.0

    subBrain = brains[charset]
    subBrainOutput = [0.0] * len(charset)
    subBrainOutput[outputLetterIndex] = 1.0

    #centralBrain.addToDataSet(inputPixelString, centralBrainOutput)
    subBrain.addToDataSet(inputPixelString, subBrainOutput)


#threading.Thread(target=trainBrain, args=["Central", centralBrain]).start()

for charset in brains:
    brain = brains[charset]
    threading.Thread(target=trainBrain, args=[charset, brain]).start()