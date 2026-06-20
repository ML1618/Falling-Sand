import pygame
from simulation import Simulation

pygame.init()
# Hide the mouse so we can use our own indicator for what particle is active
pygame.mouse.set_visible(False)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

CELL_SIZE = 6  # Size of each cell in pixels

DARK_GREY = (29, 29, 29)

FPS_CAP = 60

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling sands simulation")

clock = pygame.time.Clock()

simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation loop
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
