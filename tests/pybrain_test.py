from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import operator, pickle


# net = buildNetwork(1024, 15, 36)

net = buildNetwork(256, 15, 36)
ds = SupervisedDataSet(256, 36)

charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

charsetLines = open('characters.txt', 'r').readlines()
i = 0
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



    ds.addSample(input, output)

trainer = BackpropTrainer(net, ds)

err = 3



while True:
    err = trainer.train()
    print(err)

    f = open('brain.p','wb')
    pickle.dump(net, f)
    f.close()
