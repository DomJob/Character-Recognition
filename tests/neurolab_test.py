import numpy as np
import neurolab as nl

charset="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

inputList = []
outputList = []

charsetLines = open('characters.txt', 'r').readlines()
i = 0
for line in charsetLines:
    i += 1
    # if i==5:
    #    break

    outputLetter = line[0]

    line = line.strip().split("\t")
    pixelString = line[1]
    pixels = [float(p) for p in pixelString]
    inputList.append(pixels)

    letterIndex = charset.index(outputLetter)

    output = [0.0] * 36
    output[letterIndex] = 1.0

    outputList.append(output)

lvInput = np.array(inputList)
lvTarget = np.array(outputList)

net = nl.net.newff([[0,1]]*1024, [15, 36])

# print(lvInput, lvTarget)
err = net.train(lvInput, lvTarget, show=15)

print(net.sim([[0.2, 0.1]]))