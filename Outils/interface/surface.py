import pygame, sys
from pygame.locals import *
from interface.grid import Grid
from interface.button import Button

class Surface:
    GRID_MARGIN = 25
    SCREEN_SIZE = (640, 400)
    WINDOW_TITLE = "Détecteur de caractère - LesDominics"

    def __init__(self):
        self.mouseDown = False

        pygame.font.init()

        # Icon
        icon = pygame.Surface((1, 1))
        icon.set_alpha(0)
        pygame.display.set_icon(icon)

        pygame.display.set_caption(self.WINDOW_TITLE)
        self.surface = pygame.display.set_mode(self.SCREEN_SIZE)

        self.grid = Grid(self.surface, (self.GRID_MARGIN, self.GRID_MARGIN))
        self.resetButton = Button(self.surface, (25, 350), "Reset")

    def getInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseDown = True
                self.mouseClick()
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouseDown = False
            if event.type == pygame.MOUSEMOTION and self.mouseDown:
                self.mouseDragged()

    def mouseClick(self):
        self.mouseDragged()

        if self.resetButton.isClicked():
            self.grid.reset()

    def mouseDragged(self):
        self.grid.mouseDragged()

    def display(self):
        while True:
            self.surface.fill((255,255,255))

            self.grid.draw()
            self.resetButton.draw()

            pygame.display.flip()
            self.getInput()