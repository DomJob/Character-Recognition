from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import RPropMinusTrainer
import pickle

class Brain:
    def __init__(self, nbOutputs):
        self.net = buildNetwork(256, 10, nbOutputs)

    def load(self, file):
        f = open(file, 'rb')
        self.net = pickle.load(f)
        f.close()

    def save(self, file):
        f = open(file, 'wb')
        pickle.dump(self.net, f)
        f.close()

    def loadDataSet(self, inputs, outputs):
        self.ds = SupervisedDataSet(256, 6)

        self.trainer = RPropMinusTrainer(self.net, learningrate=5, momentum=1)

    def train(self, inputs, outputs):
        error = self.trainer.trainOnDataset(self.ds)
        return error

    def activate(self, pixelString):
        inputs = [float(p) for p in pixelString]
        outputs = self.net.activate(inputs)

        return outputs
