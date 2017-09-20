import operator

class CharacterReader:
    def __init__(self, brains):
        self.brains = brains

    def read(self, pixelString):
        probs = {}

        for charset in self.brains:
            output = self.brains[charset].activate(pixelString)
            # print(charset, output )

            for i in range(len(charset)):
                char = charset[i]
                prob = output[i]

                probs[char] = (1 - prob) ** 2

        sorted_probs = sorted(probs.items(), key=operator.itemgetter(1))

        print(sorted_probs[:5])

        return sorted_probs[:5]