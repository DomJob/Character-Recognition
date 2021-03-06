import numpy as np
import pickle

#
# Transfer functions
#

def sgm(x,Derivative=False):
    if not Derivative:
        return 1.0 / (1.0+np.exp(-x))
    else:
        out = sgm(x)
        return out*(1.0-out)

def linear(x, Derivative=False):
    if not Derivative:
        return x
    else:
        return 1.0
        
def gaussian(x, Derivative=False):
    if not Derivative:
        return np.exp(-x**2)
    else:
        return -2*x*np.exp(-x**2)

def tanh(x, Derivative=False):
    if not Derivative:
        return np.tanh(x)
    else:
        return 1.0 - np.tanh(x)**2
       
        
class BackPropagationNetwork:
    """A back-propagation network"""
    layerCount = 0
    shape = None
    weights = []
    tFuncs = []


    def __init__(self,layerSize, layerFunctions=None):
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
        for (l1,l2) in zip(layerSize[:-1],layerSize[1:]):
            self.weights.append(np.random.normal(scale=0.5,size = (l2,l1+1)))
            self._previousWeightDelta.append(np.zeros((l2,l1+1)))
        
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
            
    def TrainEpoch(self, input, target, trainingRate = 0.2, momentum = 0.5):
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
                error = np.sum(output_delta**2)
                delta.append(output_delta * self.tFuncs[index](self._layerInput[index], True))
            else:
                # Compare to the following layer's delta
                delta_pullback = self.weights[index+1].T.dot(delta[-1])
                delta.append(delta_pullback[:-1,:] * self.tFuncs[index](self._layerInput[index], True))
                
        # Compute weight deltas
        for index in range(self.layerCount):
            delta_index = self.layerCount - 1 - index
            
            if index==0:
                layerOutput = np.vstack([input.T, np.ones([1, lnCases])])
            else:
                layerOutput = np.vstack([self._layerOutput[index - 1], np.ones([1, self._layerOutput[index - 1].shape[1]])])
        
            curWeightDelta = np.sum(\
                                  layerOutput[None,:,:].transpose(2,0,1)*delta[delta_index][None,:,:].transpose(2, 1, 0)\
                                  , axis = 0)
            
            weightDelta = trainingRate * curWeightDelta + momentum * self._previousWeightDelta[index]
            
            self.weights[index] -= weightDelta
            self._previousWeightDelta[index] = weightDelta
        
        
        return error

            
#
# If run as a script, create a test object
#
if __name__ == "__main__":
    charset="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    inputList = []
    outputList = []

    charsetLines = open('characters.txt','r').readlines()
    i=0
    for line in charsetLines:
        i+=1
        #if i==5:
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
    
    bpn = BackPropagationNetwork((1024,5,36))
    print(bpn.shape)
    
    lnMax = 1000000
    lnErr = 1e-6
    deltaErr = 0
    lastErr = 0
    for i in range(lnMax+1):
        err = bpn.TrainEpoch(lvInput, lvTarget, trainingRate = 0.0002, momentum=0.1)
        deltaErr = lastErr - err
        
        
        if i % 10 == 0:
            print("{0}\t{1:0.6f}".format(i,err))
            f = open('errordata.txt','a')
            f.write("{0}\t{1:0.6f}\n".format(i,err))
            f.close()
        if i % 100 == 0:
            file = open('trained.p','wb')
            pickle.dump([bpn.layerCount, bpn.shape, bpn.tFuncs, bpn.weights], file)
            file.close()
        if err <= lnErr:
            print("Minimum error reached at iteration {0}\tError: {1:0.6f}".format(i, err))
            break
    
    lvOutput = bpn.Run(lvInput)
    for i in range(lvInput.shape[0]):
        print("Input: {0} Output: {1}".format(lvInput[i],lvOutput[i]))
    
    