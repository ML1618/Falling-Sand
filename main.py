import pygame
from simulation import Simulation

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CELL_SIZE = 6 # Size of each cell in pixels

BLACK = (0, 0, 0)
DARK_GREY = (29, 29, 29)

FPS_CAP = 60

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Falling sands simulation")

clock = pygame.time.Clock()

simulation = Simulation(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)

#####################
# Simulation loop
#####################

while True:
    # Event handling
    simulation.handle_controls()

    # Updating state
    simulation.update()

    # Drawing
    window.fill(DARK_GREY)
    simulation.draw(window)

    pygame.display.flip()
    clock.tick(FPS_CAP)