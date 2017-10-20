import operator

class CharacterReader:
    FAILURE_TRESHOLD = -0.5
    
    def __init__(self, brains, centralBrain):
        self.brains = brains
        self.centralBrain = centralBrain

    def readFailed(self, pixelString):
        return self.backupRead(pixelString)[0][1] < self.FAILURE_TRESHOLD
        
    def backupRead(self, pixelString):
        letters = []
        
        for brain in self.brains:
            outputs = brain.sortOutputs(pixelString)
            
            for index, score in outputs:
                letter = brain.charset[index]
                letters.append( (letter, score) )
                
        letters.sort(key=operator.itemgetter(1), reverse=True)
        
        return letters
        
 
        
    def getCharset(self, pixelString):
        networkOutput = self.centralBrain.sortOutputs(pixelString)
        
        charsets = []
        for index, score in networkOutput:
            charsets.append( (self.brains[index].charset, score) )
        charsets.sort(key=operator.itemgetter(1), reverse=True)
        
        return charsets
        
    def read(self, pixelString):
        networkOutput = self.centralBrain.sortOutputs(pixelString)
        
        brain = self.brains[ networkOutput[0][0] ]
        charset = brain.charset
        
        outputs = brain.sortOutputs(pixelString)
        
        letters = []
        for index, score in outputs:
            letter = brain.charset[index]
            letters.append( (letter, score) )
        letters.sort(key=operator.itemgetter(1), reverse=True)
        
        return letters