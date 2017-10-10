from interface.surface import Surface
from brain.brain import Brain
from brain.characterReader import CharacterReader
import time


brains = {
    "123ORM" : Brain(6),
    "4E0KZN" : Brain(6),
    "IFQXHW" : Brain(6),
    "TBCY5V" : Brain(6),
    "78GP9U" : Brain(6),
    "JA6LDS" : Brain(6)
}

characterReader = CharacterReader(brains)
#characterLines = open('data/characters_unknown.txt', 'r').readlines()
characterLines = open('data/characters.txt', 'r').readlines()

charCount = {}
characters1 = {}
characters2 = {}
characters3 = {}

#while True:
if True:
    for name in brains:
        brains[name].load("data/brains/%s.p" % name)


    characterReader = CharacterReader(brains)



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

        if expected not in charCount:
            charCount[expected] = 0
            characters1[expected] = 0
            characters2[expected] = 0
            characters3[expected] = 0


        #print("Expected: %s\tResult: %s" % (expected, result))
        first = result[0][0]
        second = result[1][0]
        third = result[2][0]

        charCount[expected] += 1

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

    """
    print("Good    : %d/%d (%.2f%%)" % (good, total, 100*good/total))
    print("First   : %d/%d (%.2f%%)" % (correct, total, 100*correct/total))
    print("Second  : %d/%d (%.2f%%)" % (seconds, total, 100*seconds/total))
    print("Third   : %d/%d (%.2f%%)" % (thirds, total, 100*thirds/total))
    print("Failed  : %d/%d (%.2f%%)" % (failed, total, 100*failed/total))
    """
    open('benchmark.txt','w').write("Char\t1er %\t2eme %\t3eme %\n")
    for char in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        open('benchmark.txt','a').write("%s\t%0.2f\t%0.2f\t%0.2f\n" % (char,
                                                          #charCount[char],
                                                          #characters1[char], characters2[char], characters3[char],
                                                          100.0*characters1[char]/charCount[char],
                                                          100.0*characters2[char]/charCount[char],
                                                          100.0*characters3[char]/charCount[char]))




