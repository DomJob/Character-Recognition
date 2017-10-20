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
    "0ODGCQ" : Brain(6),
    "1IJ3B8" : Brain(6),
    "2Z5SEF" : Brain(6),
    "AHTKXW" : Brain(6),
    "MNVUY7" : Brain(6),
    "469LPR" : Brain(6)
}


for name in brains:
    brains[name].load("../data/brains/%s.p" % name)


characterLines = open('../data/characters.txt', 'r').readlines()

print("Loading samples")

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
    
    
    #for name in brains:
    #    if name == brainCharset:
    #        continue
    #    subBrain = brains[name]
    #    subBrain.addToDataSet(inputPixelString, [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0])
    
    if brainCharset == None:
        continue
    
    subBrain = brains[brainCharset]
    
    subBrainOutput = [-1.0] * (len(brainCharset) )
    subBrainOutput[outputLetterIndex] = 1.0

    subBrain.addToDataSet(inputPixelString, subBrainOutput)


print("Starting training")

for charset in brains:
    brain = brains[charset]
    threading.Thread(target=trainBrain, args=[charset, brain]).start()