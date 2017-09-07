import numpy as np
import pickle
import operator

def sgm(x, Derivative=False):
    if not Derivative:
        return 1.0 / (1.0 + np.exp(-x))
    else:
        out = sgm(x)
        return out * (1.0 - out)


def linear(x, Derivative=False):
    if not Derivative:
        return x
    else:
        return 1.0


def gaussian(x, Derivative=False):
    if not Derivative:
        return np.exp(-x ** 2)
    else:
        return -2 * x * np.exp(-x ** 2)


def tanh(x, Derivative=False):
    if not Derivative:
        return np.tanh(x)
    else:
        return 1.0 - np.tanh(x) ** 2

class BackPropagationNetwork:
    """A back-propagation network"""
    layerCount = 0
    shape = None
    weights = []
    tFuncs = []

    def __init__(self, layerSize, layerFunctions=None):
        """Initialize the network"""

        self.layerCount = len(layerSize) - 1
        self.shape = layerSize

        if layerFunctions is None:
            lFuncs = []
            for i in range(self.layerCount):
                if i == self.layerCount - 1:
                    lFuncs.append(linear)
                else:
                    lFuncs.append(sgm)
        else:
            if len(layerSize) != len(layerFunctions):
                raise ValueError("Incompatible list of transfer functions")
            elif layerFunctions[0] is not None:
                raise ValueError("Input layer cannot have a transfer function")
            else:
                lFuncs = layerFunctions[1:]

        self.tFuncs = lFuncs

        # Data from last Run
        self._layerInput = []
        self._layerOutput = []
        self._previousWeightDelta = []

        # Create the weights array
        for (l1, l2) in zip(layerSize[:-1], layerSize[1:]):
            self.weights.append(np.random.normal(scale=0.5, size=(l2, l1 + 1)))
            self._previousWeightDelta.append(np.zeros((l2, l1 + 1)))

    def Run(self, input):
        """Run the network based on the input data"""

        lnCases = input.shape[0]

        # Clear out the previous intermediate value lists
        self._layerInput = []
        self._layerOutput = []

        # Run it!
        for index in range(self.layerCount):
            # Determine layer input
            if index == 0:
                layerInput = self.weights[0].dot(np.vstack([input.T, np.ones([1, lnCases])]))
            else:
                layerInput = self.weights[index].dot(np.vstack([self._layerOutput[-1], np.ones([1, lnCases])]))

            self._layerInput.append(layerInput)
            self._layerOutput.append(self.tFuncs[index](layerInput))

        return self._layerOutput[-1].T

    def TrainEpoch(self, input, target, trainingRate=0.2, momentum=0.5):
        """ This method trains the network for one epoch"""

        delta = []
        lnCases = input.shape[0]

        # First run the network
        self.Run(input)

        # Calculate our deltas
        for index in reversed(range(self.layerCount)):
            if index == self.layerCount - 1:
                # Compare to the target values
                output_delta = self._layerOutput[index] - target.T
                error = np.sum(output_delta ** 2)
                delta.append(output_delta * self.tFuncs[index](self._layerInput[index], True))
            else:
                # Compare to the following layer's delta
                delta_pullback = self.weights[index + 1].T.dot(delta[-1])
                delta.append(delta_pullback[:-1, :] * self.tFuncs[index](self._layerInput[index], True))

        # Compute weight deltas
        for index in range(self.layerCount):
            delta_index = self.layerCount - 1 - index

            if index == 0:
                layerOutput = np.vstack([input.T, np.ones([1, lnCases])])
            else:
                layerOutput = np.vstack(
                    [self._layerOutput[index - 1], np.ones([1, self._layerOutput[index - 1].shape[1]])])

            curWeightDelta = np.sum( \
                layerOutput[None, :, :].transpose(2, 0, 1) * delta[delta_index][None, :, :].transpose(2, 1, 0) \
                , axis=0)

            weightDelta = trainingRate * curWeightDelta + momentum * self._previousWeightDelta[index]

            self.weights[index] -= weightDelta
            self._previousWeightDelta[index] = weightDelta

        return error

bpn = BackPropagationNetwork((1024,15,36))

attributes = pickle.load(open('trained.p', 'rb'))
# [bpn.layerCount, bpn.shape, bpn.tFuncs, bpn.weights]

bpn.layerCount = attributes[0]
bpn.shape = attributes[1]
bpn.tFuncs = attributes[2]
bpn.weights = attributes[3]

pixelString = "1111111111111110000000000000000000000000000000111000000000000000000000000000000100000000000000000000000000000010000000000000000000000000000001100000000000000000000000000000110000000000000000000000000000001000000000000000000000000000000110000000000000000000000000000011000000000000000000000000000000100000000000000000000000000000010000000000000000000000000000000100000000000000000000000000000011000000000000000000000000000001100000000000000000000000000000010000000000000000000000000000001100000000000000000000000000000010000000000000000000000000000001100000000000000000000000000000010000000000000000000000000000001100000000000000000000000000000110000000000000000000000000000001000000000000000000000000000000011111111111111100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
pixels = [float(p) for p in pixelString]

lvInput = np.array([ pixels ])

lvOutput = bpn.Run(lvInput)

charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

probs = {}

for k in range(len(charset)):
    char = charset[k]
    probs[char] = lvOutput[0][k]

sorted_probs = sorted(probs.items(), key=operator.itemgetter(1))

for data in sorted_probs:
    print(data[0], data[1])