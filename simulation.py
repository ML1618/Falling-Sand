import pygame, sys
from grid import Grid
from particle import Sand, Rock

class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.cell_size = cell_size
        self.mode = "sand"
        self.brush_size = 3

    def draw(self, window):
        self.grid.draw(window)

    def add_particle(self, row, col):
        if self.mode == "sand":
            particle = Sand
        elif self.mode == "rock":
            particle =  Rock

        self.grid.add_particle(row, col, particle)

    def remove_particle(self, row, col):
        self.grid.remove_particle(row, col)

    def update(self):
        for row in range(self.grid.rows - 2, -1, -1):
            for col in range(self.grid.cols):
                particle = self.grid.get_cell(row, col)
                if isinstance(particle, Sand):
                    new_pos = particle.update(self.grid, row, col)
                    if new_pos != (row, col):
                        self.grid.set_cell(new_pos[0], new_pos[1], particle)
                        self.grid.remove_particle(row, col)
    
    def restart(self):
        self.grid.clear()

    def handle_controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key(event)

        self.handle_mouse()

    def handle_key(self, event):
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
            print("exiting simulation")
        elif event.key == pygame.K_r:
            print("reset simulation")
            self.restart()
        elif event.key == pygame.K_PERIOD:
            if self.brush_size < 10:
                print("brush size increasing by 1")
                self.brush_size += 1
            else:
                print("brush size is already at max")
        elif event.key == pygame.K_COMMA:
            if self.brush_size > 1:
                print("brush size decreasing by 1")
                self.brush_size -= 1
            else:
                print("brush size is already at min")
        elif event.key == pygame.K_e:
            print("erase mode")
            self.mode = "erase"
        elif event.key == pygame.K_1:
            print("sand mode")
            self.mode = "sand"
        elif event.key == pygame.K_2:
            print("rock mode")
            self.mode = "rock"

    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed()
        if buttons[0]: # Left mouse button
            pos = pygame.mouse.get_pos()
            col = pos[0] // self.cell_size
            row = pos[1] // self.cell_size
            
            self.apply_brush(row, col)
    
    def apply_brush(self, row, col):
        for i in range(self.brush_size):
            for j in range(self.brush_size):
                current_row = row + i
                current_col = col + j

                if self.mode == "erase":
                    self.grid.remove_particle(current_row, current_col)
                else:
                    self.add_particle(current_row, current_col)