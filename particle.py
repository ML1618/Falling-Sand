import random, colorsys


class Sand:
    def __init__(self):
        self.colour = random_colour((0.1, 0.12), (0.5, 0.7), (0.7, 0.9))

    def update(self, grid, row, col):
        # Move down a cell, if it's open
        if grid.cell_is_empty(row + 1, col):
            return row + 1, col
        else:
            # Pick a cell down a row, randomly to diagonal left/right
            offsets = [-1, 1]
            random.shuffle(offsets)
            for offset in offsets:
                if grid.cell_is_empty(row + 1, col + offset):
                    return row + 1, col + offset
        # No options, so stay still
        return row, col


class Rock:
    def __init__(self):
        self.colour = random_colour((0.0, 0.1), (0.1, 0.3), (0.3, 0.5))


class Wood:
    def __init__(self):
        self.colour = random_colour((0.055, 0.11), (0.5, 0.8), (0.3, 0.65))


class Water:
    def __init__(self):
        self.colour = random_colour((0.5, 0.5), (0.5, 0.9), (0.7, 0.9))

    def update(self, grid, row, col):
        # Fall straight down when possible
        if grid.cell_is_empty(row + 1, col):
            return row + 1, col

        # Prefer diagonal fall before filling side gaps
        offsets = [-1, 1]
        random.shuffle(offsets)
        for offset in offsets:
            if grid.cell_is_empty(row + 1, col + offset):
                return row + 1, col + offset

        # Spread evenly along the current row when supported
        side_offsets = [-1, 1]
        random.shuffle(side_offsets)
        for offset in side_offsets:
            if grid.cell_is_empty(row, col + offset) and not grid.cell_is_empty(
                row + 1, col + offset
            ):
                return row, col + offset

        return row, col


def random_colour(hue_range, saturation_range, value_range):
    hue = random.uniform(*hue_range)
    saturation = random.uniform(*saturation_range)
    value = random.uniform(*value_range)

    (
        r,
        g,
        b,
    ) = colorsys.hsv_to_rgb(hue, saturation, value)
    return int(r * 255), int(g * 255), int(b * 255)
