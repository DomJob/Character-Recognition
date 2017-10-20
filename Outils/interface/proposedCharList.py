import pygame


class CharList:
    BORDER_COLOR = (10, 10, 10)
    MAX_LENGTH = 10
    WIDTH = 26
    HEIGHT = 20
    DATA_FONT_SIZE = 14
    DATA_FONT = 'Calibri'
    TITLE_FONT_SIZE = 28
    COLOR = (10, 170, 0)
    EMPTY = ""
    NUMBER_OF_CELLS = 7
    LIST_TITLE = "Caractères possibles"

    def __init__(self, surface, position):
        self.position = position
        self.surface = surface
        self.clean()
        self.data_font = pygame.font.SysFont(self.DATA_FONT, self.DATA_FONT_SIZE)
        self.title_font = pygame.font.SysFont(self.DATA_FONT, self.TITLE_FONT_SIZE)

    def draw(self):
        text_x = self.position[0] + 10
        text_y = self.position[1] + 3

        text_surface = self.title_font.render(self.LIST_TITLE, False, (0, 0, 0))

        self.surface.blit(text_surface, (text_x, text_y))

        y_position = self.position[1] + 32
        for i in range(self.NUMBER_OF_CELLS):
            rect_x = self.position[0]
            rect_y = y_position

            text_x = self.position[0] + 10
            text_y = y_position + 3

            pygame.draw.rect(self.surface, self.BORDER_COLOR, (rect_x, rect_y, self.WIDTH, self.HEIGHT), 1)
            pygame.draw.rect(self.surface, self.COLOR, (rect_x+1, rect_y+1, self.WIDTH-2, self.HEIGHT-2))

            text_surface = self.data_font.render(self.text[i], False, (0, 0, 0))

            self.surface.blit(text_surface, (text_x, text_y))
            y_position += self.HEIGHT - 1

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
