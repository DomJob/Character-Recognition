import operator, pickle, random
import pygame, sys
from pygame.locals import *

def get_input():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()


def activate(net, input):
    charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    output = net.activate(input)
    probsDict = {}

    for i in range(36):
        letter = charset[i]
        probs = output[i]
        probsDict[letter] = probs

    sorted_probs = sorted(probsDict.items(), key=operator.itemgetter(1))
    final = {}
    for i in range(35, -1, -1):
        l = sorted_probs[i]

        final[l[0]] = "%.3f" % l[1]

    return final

inputs = [0] * 256


target = "A"

inputs = [float(p) for p in "0000000000000000000000011000000000000001100000000000001010000000000000101100000000000100010000000000010001000000000010000100000000001000001000000001111111100000000100000010000000010000000100000010000000010000001000000001100000000000000000000000000000000000"]

f = open('abcdef.p','rb')
net = pickle.load(f)

pygame.font.init()

GRID_WIDTH = 16
GRID_HEIGHT = 16
PIXEL_SIZE = 20
MARGIN = 25

screen_size = [370, 370]
icon = pygame.Surface((1, 1));
icon.set_alpha(0);
pygame.display.set_icon(icon)
pygame.display.set_caption("Dessin")
surface = pygame.display.set_mode(screen_size)

grid = []
for y in range(GRID_WIDTH):
    row = []

    for x in range(GRID_WIDTH):
        row.append(0)

    grid.append(row)

maxFitness = 0.0

while True:
    surface.fill((255, 255, 255))

    # Dessiner les pixels

    x, y = 0, 0

    for i in range(256):
        c = int((1-inputs[i])*255)
        if c < 0:
            c = 0
        if c > 255:
            c = 255

        pygame.draw.rect(surface, (c,c,c), (MARGIN + x * PIXEL_SIZE, MARGIN + y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

        x += 1
        if x == 16:
            x = 0
            y += 1

    # Dessiner la grille

    for x in range(0, PIXEL_SIZE * GRID_HEIGHT + 1, PIXEL_SIZE):
        pygame.draw.line(surface, (0, 0, 0), (MARGIN + x, MARGIN), (MARGIN + x, MARGIN + PIXEL_SIZE * GRID_HEIGHT))
    for y in range(0, PIXEL_SIZE * GRID_WIDTH + 1, PIXEL_SIZE):
        pygame.draw.line(surface, (0, 0, 0), (MARGIN, MARGIN + y), (MARGIN + PIXEL_SIZE * GRID_WIDTH, MARGIN + y))

    oldInputs = inputs[:]

    for _ in range(random.randint(1,1)):
        pick = random.randint(0,255)
        inputs[pick] += random.uniform(-0.1, 0.1)
        #inputs[pick] *= random.uniform(0.90,1.1)
        if inputs[pick] < 0: inputs[pick] = 0
        if inputs[pick] > 1: inputs[pick] = 1

    net_output = activate(net, inputs)

    targetFitness = float(net_output[target])

    rank = 36
    for letter in net_output:
        if letter != target:
            rank-=1

    targetFitness *= rank
    if targetFitness > maxFitness:
        maxFitness = targetFitness
        print(maxFitness, net_output)
    else:
        inputs = oldInputs[:]

    pygame.display.flip()
    get_input()