# Falling-Sand
This is a falling sand simulation, built with Pygame and Python.

Particle effects:
- Sand
    - If cell below is empty, move down.
    - If either cells to diagonal down left/right are empty, move to one of them. If both are empty, pick one at random.
    - If neither of the above happen, don't move anywhere.
- Rock
    - No special interactions with any other particles.
    - Floats in midair.
- Wood
    - FLoats in midair.
    - Burns in contact with Fire.
- Water
    - Falls down.

Controls:
- Quit
    - To quit the simulation, press `Esc` or 
- Restart
    - To restart the simulation, press `r` or `R`.
- Increase brush size
    - To increase brush size, press `.`. Maximum brush size is capped at 10.
- Decrease brush size
    - To decrease brush size, press `,`. Minimum brush size is capped at 1.
- Erase
    - To erase particles, press `e` or `E`.
- Sand
    - To swap to Sand particles, press `1`.
- Rock
    - To swap to Rock particles, press `2`.
- Wood
    - To swap to Wood particles, press `3`.

To-Do:
- At some point, maybe add other things like Fire, Wood, Greenery, Flowers, Smoke, Steam, Water...
    - Fire
        - Consumes Wood.
        - Spreads on Wood and Greenery.
        - Put out by Sand and Water.
        - Produces Smoke.
    - Wood
        - Produces Greenery.
        - Burns slowly in contact with Fire.
    - Greenery
        - Produces Flowers.
        - Spreads quickly.
        - Burns quickly.
        - Floats in midair.
    - Flowers
        - Burns instantly.
    - Smoke
        - Floats upward.
        - Trapped by Wood and Stone.
    - Steam
        - Floats upward.
        - Trapped by Wood and Stone.
    - Water
        - Produces Steam when in contact with fire.
        - Falls.
        - Fits shape of container.

Issues:
- Water particles fritz on the top of the surface. Unsure how to fix. Maybe delete them? Don't know how to check.
- Water particles pool on the sides. For each particle, go through and check if there are any empty particles on the row beneath, then move to fill?