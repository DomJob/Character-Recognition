from grid import Grid

grid = Grid(None, None)

characterLines = open('../data/characters_unresized.txt', 'r').readlines()
newCharFile = open('../data/characters.txt','w')

i = 0
for line in characterLines:
    line = line.strip().split("\t")

    inputPixelString = line[1]

    expected = line[0]

    grid.setState(inputPixelString)
    grid.resize()
    newState = grid.getState()

    newCharFile.write("%s\t%s\n" % (expected, newState))
    print(i)
    i+=1