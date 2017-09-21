from interface.surface import Surface
from brain.brain import Brain
from brain.characterReader import CharacterReader

"""
brains = {
    "123ORM" : Brain(6),
    "LE0KZN" : Brain(6),
    "IFQXHW" : Brain(6),
    "TBCY5V" : Brain(6),
    "78GP9U" : Brain(6),
    "JA64DS" : Brain(6)
}"""

brains = {
    "RKXYP4" : Brain(6),
    "O0QCG6D9" : Brain(8),
    "NMWVUH" : Brain(6),
    "3EFB8A" : Brain(6),
    "2ZS5" : Brain(4),
    "1LIT7J" : Brain(6)
}


for name in brains:
    brains[name].load("data/brains/%s.p" % name)


characterReader = CharacterReader(brains)
"""
characterLines = open('data/characters.txt', 'r').readlines()

total = 1.0
correct = 0.0
seconds = 0.0
thirds = 0.0
failed = 0.0

for line in characterLines:
    line = line.strip().split("\t")

    inputPixelString = line[1]

    expected = line[0]
    result = characterReader.read(inputPixelString)

    #print("Expected: %s\tResult: %s" % (expected, result))
    first = result[0][0]
    second = result[1][0]
    third = result[2][0]

    if first==expected:
        correct += 1
    if second==expected:
        seconds += 1
    if third==expected:
        thirds += 1
    if expected not in [result[n][0] for n in range(7)]:
        failed += 1

    total += 1

print("First   : %d/%d (%.2f%%)" % (correct, total, 100*correct/total))
print("Second  : %d/%d (%.2f%%)" % (seconds, total, 100*seconds/total))
print("Third   : %d/%d (%.2f%%)" % (thirds, total, 100*thirds/total))
print("Failed  : %d/%d (%.2f%%)" % (failed, total, 100*failed/total))
#"""
surface = Surface(characterReader)
surface.display()