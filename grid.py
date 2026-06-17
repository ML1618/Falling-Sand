import pygame

class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.cols = width // cell_size
        self.cell_size = cell_size

        # Create a 2D list to represent the grid, initialised with None values
        self.cells = [[None for _ in range(self.cols)] for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for col in range(self.cols):
                particle = self.cells[row][col]
                if particle is not None:
                    colour = particle.colour
                    pygame.draw.rect(
                        window,
                        colour,
                        (
                            col * self.cell_size,
                            row * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        ),
                    )

    def add_particle(self, row, col, particle_type):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.cells[row][col] = particle_type()

    def remove_particle(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.cells[row][col] = None

    def cell_is_empty(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col] is None
        return False

    def set_cell(self, row, col, particle):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return
        self.cells[row][col] = particle

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col]
        return None

    def clear(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.remove_particle(row, col)