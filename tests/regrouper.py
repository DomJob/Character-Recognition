from random import randint, choice
import sys

characterLines = open('data/characters.txt', 'r').readlines()

total = {}
nb = {}
averages = {}

for line in characterLines:
    line = line.strip().split("\t")

    character = line[0]
    pixelString = line[1]
    
    if character not in total:
        nb[character] = 0.0
        total[character] = [0.0] * 256
        
    nb[character] += 1
    
    i = 0
    for p in pixelString:
        total[character][i] += float(p)
        i+=1
        

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in chars:
    averages[char] = [ total[char][i] / nb[char] for i in range(256) ]


def getAvgDiff(chars):
    done = []
    totalDiff = 0.0
    i = 0
    for char1 in chars:
        for char2 in chars:
            if char1 == char2:
                continue
            diff = 0
            for i in range(256):
                diff += abs(averages[char1][i] - averages[char2][i])
            diff = diff / 256
            
            if char1+"-"+char2 not in done:
                totalDiff += diff
                i += 1
                done.append(char2+"-"+char1)
    return totalDiff / i
    
bestFitness = 1e4
bestSets = "012345 6789AB CDEFGH IJKLMN OPQRST UVWXYZ".split(" ")
bestFitness = sum([ getAvgDiff(set) for set in bestSets ])

print("%.6f" % bestFitness, bestSets)



while True:
    sets = list(bestSets)
    
    for _ in range(randint(0,100)):
        while True:
            i1 = randint(0, 5)
            i2 = randint(0, 5)
            if i1 != i2: break
            
        set1 = sets[i1]
        set2 = sets[i2]
        
        letter1 = choice(set1)
        letter2 = choice(set2)
        
        sets[i1] = sets[i1].replace(letter1, letter2)
        sets[i2] = sets[i2].replace(letter2, letter1)
    
    
    totalDiff = sum([ getAvgDiff(set) for set in sets ])
    
    if totalDiff < bestFitness:
        bestFitness = totalDiff
        bestSets = list(sets)
        
        print("%.6f" % bestFitness, bestSets)

        
    
    

