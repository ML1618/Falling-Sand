import pygame, sys
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                simulation.restart()
            elif event.key == pygame.K_e:
                print("erase mode")
            elif event.key == pygame.K_1:
                print("sand mode")
            elif event.key == pygame.K_2:
                print("rock mode")
            

    buttons = pygame.mouse.get_pressed()
    if buttons[0]: # Left mouse button
        pos = pygame.mouse.get_pos()
        mouse_y = pos[0] // CELL_SIZE
        mouse_x = pos[1] // CELL_SIZE
        simulation.add_particle(mouse_x, mouse_y)
    # Updating state
    simulation.update()

    # Drawing
    window.fill(DARK_GREY)
    simulation.draw(window)

    pygame.display.flip()
    clock.tick(FPS_CAP)