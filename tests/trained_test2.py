from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import pickle, operator, time

def activate(net, pixelString):
    input = [float(p) for p in pixelString]
    charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    output = net.activate(input)
    probsDict = {}

    for i in range(36):
        letter = charset[i]
        probs = output[i]
        probsDict[letter] = probs

    sorted_probs = sorted(probsDict.items(), key=operator.itemgetter(1))
    final = {}
    for i in range(35, -1, -1):
        l = sorted_probs[i]

        final[l[0]] = "%.3f" % l[1]

    return final

char = "0000000000000000000000011000000000000001100000000000001010000000000000101100000000000100010000000000010001000000000010000100000000001000001000000001111111100000000100000010000000010000000100000010000000010000001000000001100000000000000000000000000000000000"


f = open('brain.p','rb')
net = pickle.load(f)

charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

charsetLines = open('characters.txt', 'r').readlines()
i = 0
for line in charsetLines:
    outputLetter = line[0]

    line = line.strip().split("\t")

    pixelString = line[1]

    pixels = [float(p) for p in pixelString]

    input = tuple(pixels)
    output = activate(net, pixelString)
    print("Expect", outputLetter, "Got : ", output)

print(activate(net, char))

time.sleep(3)