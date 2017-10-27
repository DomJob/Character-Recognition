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
        
        return letters[:6]
        
    def getCharset(self, pixelString):
        networkOutput = self.centralBrain.sortOutputs(pixelString)
        
        charsets = []
        for index, score in networkOutput:
            charsets.append( (self.brains[index].charset, score) )
        charsets.sort(key=operator.itemgetter(1), reverse=True)
        
        return charsets[0][0]
        
    def read(self, pixelString):
        charset = self.getCharset(pixelString)

        for brain in self.brains:
            if brain.charset == charset:
                goodBrain = brain
                break
        
        brainOutput = brain.sortOutputs(pixelString)
        
        letters = []
        
        for index, score in brainOutput:
            letter = brain.charset[index]
            letters.append( (letter, score) )
            
        letters.sort(key=operator.itemgetter(1), reverse=True)
        
        if letters[0][1] < self.FAILURE_TRESHOLD:
            return self.backupRead(pixelString)
        
        return letters