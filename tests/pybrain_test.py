from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import *
import pickle



net = buildNetwork(256, 10, 36)
#f = open('brain.p','rb')
#net = pickle.load(f)

ds = SupervisedDataSet(256, 36)

charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

charsetLines = open('characters.txt', 'r').readlines()
i = 0
print("Loading dataset...")
for line in charsetLines:
    outputLetter = line[0]

    letterIndex = charset.index(outputLetter)

    output = [0.0] * 36
    output[letterIndex] = 1.0

    line = line.strip().split("\t")

    pixelString = line[1]

    pixels = [float(p) for p in pixelString]

    input = tuple(pixels)
    output = tuple(output)
    print(letterIndex, output)

    ds.addSample(input, output)

print("Done")
trainer = RPropMinusTrainer(net, learningrate=5, momentum=1, verbose=True)
#trainer = BackpropTrainer(net, learningrate=0.01, momentum=0.5, verbose=True)

err = 3



while True:
    err = trainer.trainOnDataset(ds)


    f = open('brain.p','wb')
    pickle.dump(net, f)
    f.close()
