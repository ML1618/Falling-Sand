import pygame, sys
from simulation import Simulation

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CELL_SIZE = 20 # Size of each cell in pixels

BLACK = (0, 0, 0)

FPS_CAP = 60

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Falling sands simulation")

clock = pygame.time.Clock()

simulation = Simulation(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
simulation.add_particle(0, 0)
simulation.add_particle(1, 1)
simulation.remove_particle(0, 0)

#####################
# Simulation loop
#####################

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Updating state

    # Drawing
    window.fill(BLACK)
    simulation.draw(window)

    pygame.display.flip()
    clock.tick(FPS_CAP)