import pygame

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
                state += str(pixel)

        return state

    def saveState(self, character):
        state = self.getState()

        file = open('data/characters.txt','a')
        file.write("%s\t%s\n" % (character, state))

        self.reset()

    def mouseDragged(self):
        x, y = pygame.mouse.get_pos()

        if x<self.position[0] or x>=self.position[0]+self.PIXEL_SIZE*self.WIDTH:
            return
        if y<self.position[1] or y>=self.position[1]+self.PIXEL_SIZE*self.HEIGHT:
            return

        x -= self.position[0]
        y -= self.position[1]

        gridX = x // self.PIXEL_SIZE
        gridY = y // self.PIXEL_SIZE

        self.fillPixel(gridX, gridY)

    def fillPixel(self, x, y):
        self.grid[y][x] = 1

    def erasePixel(self, x, y):
        self.grid[y][x] = 0

    def draw(self):
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

        # Remplir les pixels

        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                pixel = self.grid[y][x]

                rectX = self.position[0] + x * self.PIXEL_SIZE
                rectY = self.position[1] + y * self.PIXEL_SIZE
                size = self.PIXEL_SIZE

                if pixel==1:
                    pygame.draw.rect(self.surface, (0, 0, 0),
                                 (rectX, rectY, size, size), 0)