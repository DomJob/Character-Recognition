import pygame, sys
from pygame.locals import *
from interface.grid import Grid

class Surface:
    GRID_MARGIN = 25
    SCREEN_SIZE = (640, 360)
    WINDOW_TITLE = "Détecteur de caractère - LesDominics"

    def __init__(self):
        #icon = pygame.Surface((1, 1))
        #icon.set_alpha(0)
        #pygame.display.set_icon(icon)

        pygame.display.set_caption(self.WINDOW_TITLE)
        self.surface = pygame.display.set_mode(self.SCREEN_SIZE)

        self.grid = Grid((self.GRID_MARGIN, self.GRID_MARGIN), self.surface)

    def getInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            """if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
                mouseDragged()
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False
            if event.type == pygame.MOUSEMOTION and mouseDown:
                mouseDragged()
            """

    def display(self):
        while True:
            self.surface.fill((255,255,255))

            self.grid.draw()

            pygame.display.flip()
            self.getInput()