import operator

lines = open('data/characters.txt','r').readlines()

nb = {}

for line in lines:
    info = line.split("\t")

    character = info[0]

    if character not in nb:
        nb[character] = 1
    else:
        nb[character] += 1

sorted_nb = sorted(nb.items(), key=operator.itemgetter(1))

for data in sorted_nb:
    print(data[0], data[1])