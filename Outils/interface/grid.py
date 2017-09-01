import pygame

class Grid:
    WIDTH = 32
    HEIGHT = 32
    PIXEL_SIZE = 10

    GRID_COLOR  = (180,180,180)
    PIXEL_COLOR = (0,0,0)

    def __init__(self, position, surface):
        self.grid = []
        self.position = position
        self.surface = surface

        self.reset()

    def reset(self):
        self.grid = []
        for y in range(self.HEIGHT):
            row = []

            for x in range(self.WIDTH):
                row.append(0)

            self.grid.append(row)

    def fillPixel(self, x, y):
        self.grid[y][x] = 1

    def erasePixel(self, x, y):
        self.grid[y][x] = 0

    def draw(self):
        # Dessiner la grille

        pygame.draw.rect(self.surface, self.GRID_COLOR,
                         (self.position[0], self.position[1], self.WIDTH * self.PIXEL_SIZE+1, self.HEIGHT * self.PIXEL_SIZE+1), 1)

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