import pygame


class CharList:
    BORDER_COLOR = (10, 10, 10)
    MAX_LENGTH = 10
    WIDTH = 26
    HEIGHT = 20
    DATA_FONT_SIZE = 14
    DATA_FONT = 'Calibri'
    TITLE_FONT_SIZE = 28
    GREEN_COLOR = (10, 210, 0)
    YELLOW_COLOR = (200, 210, 5)
    RED_COLOR = (210, 5, 5)
    BASE_COLOR = (200, 200, 200)
    EMPTY = ""
    NUMBER_OF_CELLS = 7
    LIST_TITLE_1 = "Caractères"
    LIST_TITLE_2 = "possibles"
    ERROR_MESSAGE = "Caractère inconnu"
    ALERT_MESSAGE = "Veuillez dessiner un caractère"
    MARGIN = 5
    ANY_CHAR = "  "

    def __init__(self, surface, position):
        self.position = position
        self.surface = surface
        self.clean()
        self.data_font = pygame.font.SysFont(self.DATA_FONT, self.DATA_FONT_SIZE)
        self.data_width, self.data_height = self.data_font.size(self.ANY_CHAR)
        self.title_font = pygame.font.SysFont(self.DATA_FONT, self.TITLE_FONT_SIZE)
        self.title_width_1, self.title_height_1 = self.title_font.size(self.LIST_TITLE_1)
        self.title_width_2, self.title_height_2 = self.title_font.size(self.LIST_TITLE_2)
        self.message_font = pygame.font.SysFont(self.DATA_FONT, self.DATA_FONT_SIZE)

    def draw(self):
        self.draw_header()
        if self.text[0] is None:
            self.draw_message(self.ERROR_MESSAGE)
        elif self.text[0] == self.EMPTY:
            self.draw_message(self.ALERT_MESSAGE)
        else:
            self.draw_list()

    def draw_message(self, message):
        text_x = self.position[0]
        text_y = self.position[1] + (self.title_height_1 * 2) + self.MARGIN

        text_surface = self.message_font.render(message, False, (0, 0, 0))
        self.surface.blit(text_surface, (text_x, text_y))

    def draw_header(self):
        text_x = self.position[0]
        text_y = self.position[1] + 3

        text_surface = self.title_font.render(self.LIST_TITLE_1, True, (0, 0, 0))
        self.surface.blit(text_surface, (text_x, text_y))

        if self.title_width_1 >= self.title_width_2:
            text_2_x = self.position[0] + self.title_width_1/2 - self.title_width_2/2
            text_y = self.position[1] + 3 + self.title_height_1
        else:
            text_2_x = self.position[0] + self.title_width_2/2 - self.title_width_1/2
            text_y = self.position[1] + 3 + self.title_height_1

        text_surface = self.title_font.render(self.LIST_TITLE_2, True, (0, 0, 0))
        self.surface.blit(text_surface, (text_2_x, text_y))

    def draw_list(self):
        if self.title_width_1 >= self.title_width_2:
            x_position = self.position[0] + self.title_width_1 / 2 - self.data_width * 2
        else:
            x_position = self.position[0] + self.title_width_2 / 2 - self.data_width * 2
        y_position = self.position[1] + (self.title_height_1 * 2) + self.MARGIN
        for i in range(self.NUMBER_OF_CELLS):

            rect_x = x_position
            rect_y = y_position

            text_x = x_position + 10
            text_y = y_position + 3

            pygame.draw.rect(self.surface, self.BORDER_COLOR, (rect_x, rect_y, self.WIDTH, self.HEIGHT), 1)
            pygame.draw.rect(self.surface, self.BASE_COLOR, (rect_x + 1, rect_y + 1, self.WIDTH - 2, self.HEIGHT - 2))

            text_surface = self.data_font.render(self.text[i], False, (0, 0, 0))

            self.surface.blit(text_surface, (text_x, text_y))
            y_position += self.HEIGHT - 1

    def get_result(self, results):
        if results is None:
            self.text[0] = None
        else:
            stack = 0
            for result in results:
                for string in result:
                    self.text[stack] = string
                    break
                stack += 1

    def clean(self):
        self.text = [self.EMPTY] * self.NUMBER_OF_CELLS
