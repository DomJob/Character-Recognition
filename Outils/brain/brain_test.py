from ..brain.brain import Brain
import operator

#centralBrain = Brain(6)
brains = {
    "123ORM" : Brain(6),
    "LE0KZN" : Brain(6),
    "IFQXHW" : Brain(6),
    "TBCY5V" : Brain(6),
    "78GP9U" : Brain(6),
    "JA64DS" : Brain(6)
}

#centralBrain = Brain(6)
#centralBrain.load("../data/brainssimilaires/central.p")
for name in brains:
    brains[name].load("../data/brainssimilaires/%s.p" % name)

character = "0001111110000000000100001110000000010000001000000001000000010000000110000011000000001000001000000000000001000000000000001100000000000001100000000000001100000000000001100000000000000110000000000000000111100000000000000000000000000000000000000000000000000000"

#print(centralBrain.activate(character))

probs = {}

for charset in brains:
    output = brains[charset].activate(character)
    #print(charset, output )

    for i in range(len(charset)):
        char = charset[i]
        prob = output[i]

        probs[char] = (1-prob)**2

sorted_probs = sorted(probs.items(), key=operator.itemgetter(1))
for c in sorted_probs[::-1]:
    print(c[0], c[1])