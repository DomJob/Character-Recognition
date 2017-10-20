import pygame


class CharList:
    BORDER_COLOR = (93, 93, 93)
    MAX_LENGTH = 10
    WIDTH = 26
    HEIGHT = 20
    FONT_SIZE = 14
    FONT = 'Calibri'
    COLOR = (200, 200, 200)
    EMPTY = ""
    NUMBER_OF_CELLS = 7

    def __init__(self, surface, position):
        self.position = position
        self.surface = surface
        self.clean()
        self.font = pygame.font.SysFont(self.FONT, self.FONT_SIZE)

    def draw(self):
        y_position = self.position[1]
        for i in range(self.NUMBER_OF_CELLS):
            rectX = self.position[0]
            rectY = y_position

            textX = self.position[0] + 10
            textY = y_position + 3

            pygame.draw.rect(self.surface, self.BORDER_COLOR, (rectX, rectY, self.WIDTH, self.HEIGHT), 1)
            pygame.draw.rect(self.surface, self.COLOR, (rectX+1, rectY+1, self.WIDTH-2, self.HEIGHT-2))

            textsurface = self.font.render(self.text[i], False, (0, 0, 0))

            self.surface.blit(textsurface, (textX, textY))
            y_position += self.HEIGHT

    def get_result(self, results):
        stack = 0
        for result in results:
            for string in result:
                print(string)
                self.text[stack] = string
                self.draw()
                break
            stack += 1

    def clean(self):
        self.text = [self.EMPTY] * self.NUMBER_OF_CELLS
