import pygame, sys
from pygame.locals import *
from interface.grid import Grid
from interface.button import Button
from interface.proposedCharList import CharList


class Surface:
    GRID_MARGIN = 25
    SCREEN_SIZE = (640, 315)
    WINDOW_TITLE = "Détecteur de caractère - LesDominics"

    def __init__(self, characterReader):
        self.mouseDown = False
        self.characterReader = characterReader

        pygame.font.init()

        # Icon
        icon = pygame.Surface((1, 1))
        icon.set_alpha(0)
        pygame.display.set_icon(icon)

        pygame.display.set_caption(self.WINDOW_TITLE)
        self.surface = pygame.display.set_mode(self.SCREEN_SIZE)

        # Elements
        self.grid = Grid(self.surface, (self.GRID_MARGIN, self.GRID_MARGIN))
        self.resetButton = Button(self.surface, (25, 275), "Reset")
        self.char_list = CharList(self.surface, (300, self.GRID_MARGIN))

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
            if event.type == pygame.KEYDOWN:
                if event.key == K_TAB:
                    self.grid.resize()

                if (event.key >= K_0 and event.key <= K_9) or (event.key >= K_a and event.key <= K_z):
                    keyPressed = chr(event.key)
                    keyPressed = keyPressed.upper()

                    #self.grid.saveState(keyPressed)

                    self.grid.loadAverage(keyPressed)
                    #pygame.image.save(self.surface, "./images/after/" + keyPressed + ".png")

    def mouseClick(self):
        self.mouseDragged()

        if self.resetButton.isClicked():
            self.grid.reset()
            self.char_list.clean()

    def mouseDragged(self):
        if self.grid.mouseDragged():
            state = self.grid.getState()
            self.grid.resize()
            resizedState = self.grid.getState()
            self.grid.setState(state)
                
            if self.characterReader.readFailed(resizedState):
                self.char_list.get_result(None)
            else:
                results = self.characterReader.read(resizedState)
                self.char_list.get_result(results)


    def display(self):
        while True:
            self.surface.fill((255,255,255))

            self.grid.draw()
            self.resetButton.draw()
            self.char_list.draw()

            pygame.display.flip()
            self.getInput()