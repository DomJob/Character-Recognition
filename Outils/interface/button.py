import pygame

class Button:
    BORDER_COLOR = (93,93,93)
    COLOR = (200,200,200)

    def __init__(self, surface, position, text):
        self.text = text
        self.position = position
        self.surface = surface

        self.height = 20
        self.width = 20 + len(text) * 6

        self.font = pygame.font.SysFont('Calibri', 14)

    def isClicked(self):
        x, y = pygame.mouse.get_pos()

        if x >= self.position[0] and x < self.position[0] + self.width:
            if y >= self.position[1] and y < self.position[1] + self.height:
                return True

        return False

    def draw(self):
        rectX = self.position[0]
        rectY = self.position[1]

        textX = self.position[0] + 10
        textY = self.position[1] + 3

        pygame.draw.rect(self.surface, self.BORDER_COLOR, (rectX, rectY, self.width, self.height), 1)
        pygame.draw.rect(self.surface, self.COLOR, (rectX+1, rectY+1, self.width-2, self.height-2))

        textsurface = self.font.render(self.text, False, (0, 0, 0))

        self.surface.blit(textsurface, (textX, textY))