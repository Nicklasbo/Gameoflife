import pygame
import default
import cfg
import cell_state

'''
To do
Lav knapper til Start, Next og Stop
Lav drop-down til user defined states
Lav visuelt grid
Unit test
'''

# Initilizes pygame
pygame.init()

# Sets the screen to the size parsed
screen = pygame.display.set_mode(cfg.size)

# Sets the caption for the window
pygame.display.set_caption("Game of Life")

#game_state = [[0 for _ in range(100)] for _ in range(100)]
game_state = default.state
next_game_state = game_state

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        # If the user clicks with the mouse, get the position
        if event.type == pygame.MOUSEBUTTONDOWN:
            cfg.mouse_pos = pygame.mouse.get_pos()
            cc = cell_state.cell_coords(cfg.mouse_pos)
            # Swaps the cell from alive to dead, or dead to alive
            game_state[cc['x']][cc['y']
                                ] = 1 if game_state[cc['x']][cc['y']] == 0 else 0
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(cfg.WHITE)

    # Iterates over the rows
    for i, row in enumerate(game_state):
        # Iterates over the cells in the row
        for j, cell in enumerate(row):

            next_game_state[j][i] = cell_state.rule_one(
                game_state, {'x': j, 'y': i})
            # If the cell is alive, it gets drawns as a black rectangle
            if cell == 1:
                pygame.draw.rect(screen, cfg.BLACK, [j * 8, i * 8, 8, 8], 0)
            # If the cell is dead we draw a white rectangle
            else:
                pygame.draw.rect(screen, cfg.WHITE, [j * 8, i * 8, 8, 8], 0)

    game_state = next_game_state

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
