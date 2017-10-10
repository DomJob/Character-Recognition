import pygame
from PIL import Image

class Grid:
    WIDTH = 16
    HEIGHT = 16
    PIXEL_SIZE = 15

    GRID_COLOR  = (180,180,180)
    PIXEL_COLOR = (0,0,0)

    def __init__(self, surface, position):
        self.position = position
        self.surface = surface

        self.grid = []
        self.reset()

    def reset(self):
        self.grid = []
        for y in range(self.HEIGHT):
            row = []

            for x in range(self.WIDTH):
                row.append(0)

            self.grid.append(row)

    def getState(self):
        state = ""

        for row in self.grid:
            for pixel in row:
                state += str(round(int(pixel)))

        return state

    def setState(self, pixelString):
        self.reset()
        i = 0
        for row in range(self.WIDTH):
            for col in range(self.HEIGHT):
                self.grid[row][col] = float(pixelString[i])
                i+=1

    def loadAverage(self, character, file='data/characters.txt'):
        characterLines = open(file, 'r').readlines()

        averageState = [0] * 256
        i = 0

        for line in characterLines:
            line = line.strip().split("\t")
            if line[0] != character:
                continue
            inputPixelString = line[1]
            pixelIndex = 0
            for p in inputPixelString:
                averageState[pixelIndex] += float(p)
                pixelIndex += 1

            i += 1
        self.setState([total/i for total in averageState])


    def saveState(self, character):
        self.resize()
        state = self.getState()

        file = open('data/characters.txt','a')
        file.write("%s\t%s\n" % (character, state))

        self.reset()

    def mouseDragged(self):
        x, y = pygame.mouse.get_pos()

        if x<self.position[0] or x>=self.position[0]+self.PIXEL_SIZE*self.WIDTH:
            return False
        if y<self.position[1] or y>=self.position[1]+self.PIXEL_SIZE*self.HEIGHT:
            return False

        x -= self.position[0]
        y -= self.position[1]

        gridX = x // self.PIXEL_SIZE
        gridY = y // self.PIXEL_SIZE

        self.fillPixel(gridX, gridY)
        return True

    def fillPixel(self, x, y):
        self.grid[y][x] = 1

    def erasePixel(self, x, y):
        self.grid[y][x] = 0

    def draw(self):

        # Remplir les pixels

        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                pixel = 1 - float(self.grid[y][x])

                rectX = self.position[0] + x * self.PIXEL_SIZE
                rectY = self.position[1] + y * self.PIXEL_SIZE
                size = self.PIXEL_SIZE


                pygame.draw.rect(self.surface, (pixel * 255, pixel * 255, pixel * 255),
                             (rectX, rectY, size, size), 0)

        # Dessiner la grille

        pygame.draw.rect(self.surface, self.GRID_COLOR,
                         (self.position[0], self.position[1],
                          self.WIDTH * self.PIXEL_SIZE+1, self.HEIGHT * self.PIXEL_SIZE+1), 1)

        for x in range(1, self.HEIGHT):
            lineX = self.position[0] + x * self.PIXEL_SIZE

            lineY1 = self.position[1]
            lineY2 = self.position[1] + self.HEIGHT * self.PIXEL_SIZE

            pygame.draw.line(self.surface, self.GRID_COLOR, (lineX, lineY1), (lineX, lineY2))

        for y in range(1, self.WIDTH):
            lineY = self.position[1] + y * self.PIXEL_SIZE

            lineX1 = self.position[0]
            lineX2 = self.position[0] + self.WIDTH * self.PIXEL_SIZE

            pygame.draw.line(self.surface, self.GRID_COLOR, (lineX1, lineY), (lineX2, lineY))

    def crop(self):
        while self.grid[0] == [0] * self.WIDTH:
            self.grid.pop(0)
            self.grid.append([0] * self.WIDTH)

        while True:
            empty = True
            for row in self.grid:
                if row[0] == 1:
                    empty = False
                    break

            if empty:
                for row in self.grid:
                        row.pop(0)
                        row.append(0)
            else:
                break

    def getSize(self):
        # Determiner les dimensions
        height = 0
        width = 0

        i = 0
        for c in range(self.HEIGHT):
            i+=1
            row = self.grid[c]
            line = []

            for r in range(self.WIDTH):
                pixel = self.grid[r][c]
                line.append(pixel)

            if line != [0] * self.WIDTH:
                width = i

        i = 0
        for row in self.grid:
            i += 1
            if row != [0] * self.WIDTH:
                height = i

        return width, height

    def resize(self):
        self.crop()
        width, height = self.getSize()
        if height == 16:
            self.centerHorizontally()
            return

        newSize = (width * int(16/height), 16)

        state = self.getState()

        im = Image.new("1", (width, height), 1)

        for y in range(0,height):
            for x in range(0,width):
                pixel = "0" if str(round(self.grid[y][x]))=="1" else "1"

                im.putpixel((x, y), int(pixel))

        im = im.resize(newSize)

        newState = ""

        for y in range(16):
            for x in range(16):
                try:
                    newState += "0" if im.getpixel((x,y)) == 1 else "1"
                except:
                    newState += "0"

        self.reset()
        self.setState(newState)

        self.centerHorizontally()

    def centerHorizontally(self):
        width, height = self.getSize()

        blankSides = (16 - width) // 2
        tmpGrid = self.grid

        self.reset()

        for y in range(0,height):
            for x in range(0,width):
                self.grid[y][x+blankSides] = str(int(tmpGrid[y][x]))

