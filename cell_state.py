def cell_coords(cc):
    return{
        'y': int([0] / 8),
        'x': int([1] / 8)
    }


'''
def surrounding_cells(game_state, cc):
    num_cells = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i >= 0 & i < len(game_state) & j >= 0 & j < len(game_state[i]) & game_state[i][j] == 1:
                num_cells += 1

    return num_cells


def cell_status(game_state, cc):
    cells_alive = surrounding_cells(game_state, cc)

    if cells_alive < 2:
        return 0
    elif cells_alive > 3:
        return 0
    elif cells_alive == 3 and game_state[cc['x']][cc['y']] == 0:
        return 1
    elif (cells_alive == 2 or cells_alive == 3) and game_state[cc['x']][cc['y']] == 1:
        return 1
    else:
        return 0
'''


def surrounding_cells(game_state, cc):
    num_cells = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                pass
            else:
                try:
                    if game_state[cc['x'] + j][cc['y'] + i] == 1:
                        num_cells += 1
                except IndexError:
                    pass

    return num_cells


def rule_one(game_state, cc):
    alive_cells = surrounding_cells(game_state, cc)

    if game_state[cc['x']][cc['y']] == 1:
        if alive_cells > 3:  # Cell dies from overpopulation
            return 0
        elif alive_cells < 2:  # Cell dies from underpopulation
            return 0
        elif alive_cells == 2 or alive_cells == 3:  # Cells with healthy neighbours stays alive
            return 1
    elif game_state[cc['x']][cc['y']] == 0:
        if alive_cells >= 3:  # Dead cells with 3 or more neighbours comes to life
            return 1

    return alive_cells


def rule_two(game_state, cc):
    alive_cells = surrounding_cells(game_state, cc)

    if game_state[cc['x']][cc['y']] == 1:
        if alive_cells > 5:  # Cell dies from overpopulation
            return 0
        elif alive_cells < 3:  # Cell dies from underpopulation
            return 0
        elif alive_cells == 3 or alive_cells == 4 or alive_cells == 5:  # Cells with healthy neighbours stays alive
            return 1
    elif game_state[cc['x']][cc['y']] == 0:
        if alive_cells >= 5:  # Dead cells with 3 or more neighbours comes to life
            return 1

    return alive_cells
