from interface.surface import Surface
from brain.brain import Brain
from brain.characterReader import CharacterReader
import time


brains = {
    "1LIT7J" : Brain(6),
    "2ZS5" : Brain(6),
    "RKXYP4" : Brain(6),
    "NMWVUH" : Brain(6),
    "3EFB8A" : Brain(6),
    "O0QCG6D9" : Brain(6)
}
characterReader = CharacterReader(brains)

characters1 = {}
characters2 = {}
characters3 = {}

#while True:
if True:
    for name in brains:
        brains[name].load("data/brains/%s.p" % name)


    characterReader = CharacterReader(brains)

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

        if expected not in characters1:
            characters1[expected] = 0
            characters2[expected] = 0
            characters3[expected] = 0


        #print("Expected: %s\tResult: %s" % (expected, result))
        first = result[0][0]
        second = result[1][0]
        third = result[2][0]

        if first==expected:
            correct += 1
            characters1[expected] += 1

        if second==expected:
            seconds += 1
            characters2[expected] += 1

        if third==expected:
            thirds += 1
            characters3[expected] += 1

        if expected not in [result[n][0] for n in range(7)]:
            failed += 1

        total += 1


    good = correct+seconds+thirds


    line = time.strftime("%Y-%m-%d %H:%M") + "\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n" % (100*good/total, 100*correct/total, 100*seconds/total, 100*thirds/total, 100*failed/total)
    f = open("stats.txt","a")
    f.write(line)
    f.close()

    print("Good    : %d/%d (%.2f%%)" % (good, total, 100*good/total))
    print("First   : %d/%d (%.2f%%)" % (correct, total, 100*correct/total))
    print("Second  : %d/%d (%.2f%%)" % (seconds, total, 100*seconds/total))
    print("Third   : %d/%d (%.2f%%)" % (thirds, total, 100*thirds/total))
    print("Failed  : %d/%d (%.2f%%)" % (failed, total, 100*failed/total))

    print(characters1, characters2, characters3 )
    time.sleep(280)

