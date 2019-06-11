def neighbors_alive(game_state, x, y):
    cells_alive = 0
    
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i or j:
                try:
                    if y + i < 0 or x + j < 0:
                        pass
                    else:
                        cells_alive += game_state[y + i][x + j]
                except IndexError:
                    pass 
    
    return cells_alive

[-3]