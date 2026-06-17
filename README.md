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

Controls:
- Quit
    - To quit the simulation, press `Esc` or 
- Restart
    - To restart the simulation, press `r` or `R`.
- Erase
    - To erase particles, press `e` or `E`.
- Sand
    - To swap to sand particles, press `1`.
- Rock
    - To swap to rock particles, press `2`.

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