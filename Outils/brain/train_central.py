from brain import Brain

brain = Brain(6)

charsets = [
    "0ODGCQ",
    "1IJ3B8",
    "2Z5SEF",
    "AHTKXW",
    "MNVUY7",
    "469LPR"
]

brain.load("../data/brains/Central.p")

characterLines = open('../data/characters.txt', 'r').readlines()

print("Loading samples")

for line in characterLines:
    line = line.strip().split("\t")

    inputPixelString = line[1]
    outputLetter = line[0]
    
    brainIndex = 0
    for charset in charsets:
        if outputLetter in charset:
            break
        brainIndex += 1
        
    brainOutput = [-1.0] * 6
    brainOutput[brainIndex] = 1.0
    
    brain.addToDataSet(inputPixelString, brainOutput)
    
print("Starting training...")

i = 0
while True:
    name = "Central"
    
    print(name, brain.train())
    
    if i % 10 == 0:
        print("Saving brain %s" % (name))
        brain.save("../data/brains/%s.p" % name)
    i+=1