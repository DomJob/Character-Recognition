from brain import Brain
import threading


def trainBrain(name, brain):
    i = 0
    brain.loadTrainer()

    while True:
        print(name.ljust(10), brain.train())

        if i % 10 == 0:
            print("Saving brain %s" % (name))
            brain.save("../data/brains/%s.p" % name)
        i+=1

brains = {
    "123ORM" : Brain(6),
    "4E0KZN" : Brain(6),
    "IFQXHW" : Brain(6),
    "TBCY5V" : Brain(6),
    "78GP9U" : Brain(6),
    "JA6LDS" : Brain(6)
}

for name in brains:
    brains[name].load("../data/brains/%s.p" % name)


characterLines = open('../data/characters.txt', 'r').readlines()

for line in characterLines:
    line = line.strip().split("\t")

    inputPixelString = line[1]
    outputLetter = line[0]

    #brainIndex = 0
    brainCharset = None

    for charset in brains:
        if outputLetter in charset:
            outputLetterIndex = charset.index(outputLetter)
            brainCharset = charset
        #else:
            #hashtagOutput = [0] * (len(charset) + 1)
            #hashtagOutput[-1] = 1
            #brains[charset].addToDataSet(inputPixelString, hashtagOutput)

    if brainCharset is None:
        print(outputLetter, "break")
        continue

    subBrain = brains[brainCharset]
    subBrainOutput = [0.0] * (len(brainCharset) )

    subBrainOutput[outputLetterIndex] = 1.0

    subBrain.addToDataSet(inputPixelString, subBrainOutput)



for charset in brains:
    brain = brains[charset]
    threading.Thread(target=trainBrain, args=[charset, brain]).start()