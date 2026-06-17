from grid import Grid
from particle import Sand

class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)

    def draw(self, window):
        self.grid.draw(window)

    def add_particle(self, row, col):
        self.grid.add_particle(row, col, Sand)

    def remove_particle(self, row, col):
        self.grid.remove_particle(row, col)