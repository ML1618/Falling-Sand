import random, colorsys

class Sand:
    def __init__(self):
        self.colour = self.random_colour()

    def random_colour(self):
        hue = random.uniform(0.1, 0.12)
        saturation = random.uniform(0.5, 0.7)
        value = random.uniform(0.6, 0.8)

        r, g, b, = colorsys.hsv_to_rgb(hue, saturation, value)
        return int(r * 255), int(g * 255), int(b * 255)
    
    def update(self, grid, row, col):
        # if grid.is_empty(row + 1, col):
        #     grid.set_cell(row + 1, col, self)
        #     grid.set_cell(row, col, None)
        # elif grid.is_empty(row + 1, col - 1):
        #     grid.set_cell(row + 1, col - 1, self)
        #     grid.set_cell(row, col, None)
        # elif grid.is_empty(row + 1, col + 1):
        #     grid.set_cell(row + 1, col + 1, self)
        #     grid.set_cell(row, col, None)

        if grid.cell_is_empty(row + 1, col):
            return row + 1, col
        else:
            offsets = [-1, 1]
            random.shuffle(offsets)
            for offset in offsets:
                if grid.cell_is_empty(row + 1, col + offset):
                    return row + 1, col + offset
        return row, col