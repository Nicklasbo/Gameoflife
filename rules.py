def rule_1(cell_state, neighbors_alive):
    if cell_state:
        if neighbors_alive < 2 or neighbors_alive > 3:
            return 0
        else:
            return 1
    else:
        if neighbors_alive == 3:
            return 1
        else:
            return 0

def rule_2(cell_state, neighbors_alive):
    if cell_state:
        if neighbors_alive > 5:  # Cell dies from overpopulation
            return 0
        elif neighbors_alive < 3:  # Cell dies from underpopulation
            return 0
        else:  # Cells with healthy neighbours stays alive
            return 1
    else:
        if neighbors_alive >= 5:  # Dead cells with 3 or more neighbours comes to life
            return 1
        else:
            return 0

    return neighbors_alive