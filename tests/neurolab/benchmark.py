import numpy as np
import neurolab as nl
import pickle

charset = '123ORM'

f = open('b/'+charset+'.p', 'rb')
net = pickle.load(f)
f.close()

charLines = open('characters_unknown.txt','r').readlines()
for line in charLines:
    line = line.strip()
    info = line.split("\t")
    
    expectedLetter = info[0]
    if expectedLetter not in charset:
        continue
    
    pixelString = info[1]
    
    input = np.array( [[float(p) for p in pixelString]] )
    
    print("Expected :", expectedLetter)
    
    output = net.sim(input)
    print("Output   :", output)