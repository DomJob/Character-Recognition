import pygame, sys
from pygame.locals import *

mouseDown = False

def get_input():
    global mouseDown
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
            mouseDragged()
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        if event.type == pygame.MOUSEMOTION and mouseDown:
            mouseDragged()

def mouseDragged():
    global grid, MARGIN, PIXEL_SIZE, GRID_WIDTH, GRID_HEIGHT
    
    x, y = pygame.mouse.get_pos()
    
    x -= MARGIN
    y -= MARGIN
    
    if x >= GRID_WIDTH * PIXEL_SIZE or y >= GRID_HEIGHT * PIXEL_SIZE or x<0 or y<0:
        return
        
    gridX = x // PIXEL_SIZE
    gridY = y // PIXEL_SIZE
    
    grid[gridY][gridX] = 1
    
    
    
            
pygame.font.init()

GRID_WIDTH  = 32
GRID_HEIGHT = 32
PIXEL_SIZE = 15
MARGIN = 25

screen_size = [800,800]
icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
pygame.display.set_caption("Dessin")
surface = pygame.display.set_mode(screen_size)

grid = []
for y in range(GRID_HEIGHT):
    row = []
    
    for x in range(GRID_WIDTH):
        row.append(0)
    
    grid.append(row)
    
while True:
    surface.fill((255,255,255))
    
    # Dessiner la grille
    
    for x in range(0, PIXEL_SIZE * GRID_WIDTH + 1, PIXEL_SIZE):
        pygame.draw.line(surface, (0,0,0), (MARGIN + x, MARGIN), (MARGIN + x, MARGIN + PIXEL_SIZE * GRID_HEIGHT))
    for y in range(0, PIXEL_SIZE * GRID_HEIGHT + 1, PIXEL_SIZE):
        pygame.draw.line(surface, (0,0,0), (MARGIN, MARGIN + y), (MARGIN + PIXEL_SIZE * GRID_WIDTH, MARGIN + y))
    
    # Remplir les pixels noirs
    
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pixel = grid[y][x]
            if pixel == 1:
                pygame.draw.rect(surface, (0,0,0), (MARGIN+x*PIXEL_SIZE, MARGIN+y*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    
    
    pygame.display.flip()
    get_input()