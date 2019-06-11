import pygame
from random import random
import default
import cfg
import cells_alive as ca
import rules

# Initilizes pygame
pygame.init()

# Sets the screen to the size parsed
screen = pygame.display.set_mode(cfg.size)

# Sets the caption for the window
pygame.display.set_caption("Game of Life")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


w, h = (100, 100)
game_state = [[0 for x in range(w)] for y in range(h)]
game_paused = True
first_run = True
next_step = False
drawing = False

rule = rules.rule_1

pixel_w = 800 / w
pixel_h = 800 / h

# draw buttons
pygame.draw.rect(screen, (169, 169, 169), [
                 800, 0, 200, 100], 0)  # start button
pygame.draw.rect(screen, (128, 128, 128), [
                 800, 100, 200, 100], 0)  # pause button
pygame.draw.rect(screen, (169, 169, 169), [
                 800, 200, 200, 100], 0)  # next step button
# clear game_state button
pygame.draw.rect(screen, (128, 128, 128), [800, 300, 200, 100], 0)
# glider game_state button
pygame.draw.rect(screen, (169, 169, 169), [800, 400, 200, 100], 0)
# random game_state button
pygame.draw.rect(screen, (128, 128, 128), [800, 500, 200, 100], 0)
pygame.draw.rect(screen, (169, 169, 169), [
                 800, 600, 200, 100], 0)  # rule_1  button
pygame.draw.rect(screen, (128, 128, 128), [
                 800, 700, 200, 100], 0)  # rule_2  button

# draw text
font = pygame.font.SysFont("comicsansms", 32)
start_text = font.render("Start", True, (cfg.BLACK))
pause_text = font.render("Pause", True, (cfg.BLACK))
next_text = font.render("Next", True, (cfg.BLACK))
clear_text = font.render("Clear", True, (cfg.BLACK))
glider_text = font.render("Glider", True, (cfg.BLACK))
random_text = font.render("Random", True, (cfg.BLACK))
rule1_text = font.render("Rule 1", True, (cfg.BLACK))
rule2_text = font.render("Rule 2", True, (cfg.BLACK))

screen.blit(start_text, (850, 30))
screen.blit(pause_text, (850, 130))
screen.blit(next_text, (850, 230))
screen.blit(clear_text, (850, 330))
screen.blit(glider_text, (850, 430))
screen.blit(random_text, (850, 530))
screen.blit(rule1_text, (850, 630))
screen.blit(rule2_text, (850, 730))

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        # If the user clicks with the mouse, get the position
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse coordinates
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cfg.mouse_pos = (int(mouse_x // pixel_w), int(mouse_y // pixel_h))

            # check for button presses
            if mouse_x >= 800:
                if mouse_y < 100:
                    game_paused = False
                elif mouse_y < 200:
                    game_paused = True
                elif mouse_y < 300:
                    next_step = True
                elif mouse_y < 400:
                    game_state = [[0 for x in range(w)] for y in range(h)]
                    next_step = True
                elif mouse_y < 500:
                    game_state = default.state
                    next_step = True
                elif mouse_y < 600:
                    for i in range(w):
                        for j in range(h):
                            if random() < 0.1:
                                game_state[i][j] = 1
                    next_step = True
                elif mouse_y < 700:
                    rule = rules.rule_1
                elif mouse_y < 800:
                    rule = rules.rule_2
            else:
                game_state[cfg.mouse_pos[1]][cfg.mouse_pos[0]
                                             ] = 1 if game_state[cfg.mouse_pos[1]][cfg.mouse_pos[0]] == 0 else 0
                drawing = True
                next_step = True

        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    if game_paused:
        if first_run:
            first_run = False
        elif next_step:
            next_step = False
        else:
            continue

    # clear game state
    next_game_state = [[0 for x in range(w)] for y in range(h)]

    for i in range(w):
        for j in range(h):
            if game_state[i][j] == 1:
                pygame.draw.rect(screen, cfg.BLACK, [
                                 j * pixel_w, i * pixel_h, pixel_w, pixel_h], 0)
            else:
                pygame.draw.rect(screen, cfg.WHITE, [
                                 j * pixel_w, i * pixel_h, pixel_w, pixel_h], 0)

            next_game_state[i][j] = rule(
                game_state[i][j], ca.neighbors_alive(list(game_state), j, i))

    if not drawing:
        game_state = next_game_state.copy()
    else:
        drawing = False

    # Draws the screen
    pygame.display.update()

# Be IDLE friendly
pygame.quit()
