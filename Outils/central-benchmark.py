from brain.brain import Brain

charsets = [
    "0ODGCQ",
    "1IJ3B8",
    "2Z5SEF",
    "AHTKXW",
    "MNVUY7",
    "469LPR"
]

brains = {
    "0ODGCQ" : Brain(6),
    "1IJ3B8" : Brain(6),
    "2Z5SEF" : Brain(6),
    "AHTKXW" : Brain(6),
    "MNVUY7" : Brain(6),
    "469LPR" : Brain(6)
}

central = Brain(6)

badNetwork = 0
badNetworkDetected = 0
badNetworkDetectedFP = 0
goodNetwork = 0
correct = 0
bad = 0


central.load("data/brains/Central.p")
for name in brains:
    brains[name].load("data/brains/%s.p" % name)

characterLines = open('data/characters_unknown.txt', 'r').readlines()
#characterLines = open('data/characters.txt', 'r').readlines()

o=0

for line in characterLines:
    line = line.strip().split("\t")

    inputPixelString = line[1]

    expected = line[0]
    
    centralOutput = central.activate(inputPixelString)

    maxScore = -10
    maxI = 0
    for i in range(6):
        if centralOutput[i] > maxScore:
            maxScore = centralOutput[i]
            maxI = i
    
    brainCharset = charsets[maxI]
    networkOutput = brains[brainCharset].activate(inputPixelString)
    
    if expected not in brainCharset:
        badNetwork += 1
        print(o, expected, "Bad network.")
    else:
        goodNetwork += 1
        
    maxScore = -10
    maxI = 0
    
    for i in range(6):
        if networkOutput[i] > maxScore:
            maxScore = networkOutput[i]
            maxI = i
    
    if maxScore < 0:
        print(o, expected, "Score: ",maxScore," - Most likely bad network ("+brainCharset+") Backup...")
        # ect
        
        if expected not in brainCharset: 
            badNetworkDetected += 1
        else:
            badNetworkDetectedFP += 1
        
        print()
        continue
    
    detectedCharacter = brainCharset[maxI]
        
    if detectedCharacter != expected:
        bad += 1
        print(o, "Expected:", expected, "Detected:", detectedCharacter, maxScore)
        print()
    else:
        correct += 1
    #    print(o, "Got it! ", expected, detectedCharacter)
    o += 1
    
    
print("Bad network:     ", badNetwork)
print(" Detected:       ", badNetworkDetected)
print(" False positive: ", badNetworkDetectedFP)
print("Good network:    ", goodNetwork)
print(" Correct guess:  ", correct)
print(" Bad guess:      ", bad)


