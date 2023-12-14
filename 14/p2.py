import copy

goal = 1000000000
records = []

def compute_load(grid):
    load = 0
    for n, line in enumerate(grid[::-1]):
        load += line.count("O") * (n + 1)
    return load


def in_bounds(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    else:
        return True


def move_rock(grid, i, j, idir, jdir):
    xi = i
    xj = j

    # Look for empty space in the desired direction
    while in_bounds(grid, xi + idir, xj + jdir) and grid[xi + idir][xj + jdir] == ".":
        xi += idir
        xj += jdir

    # Rewrite to move rock if found new pos
    if i != xi or j != xj:
        grid[xi] = grid[xi][:xj] + "O" + grid[xi][xj + 1:]
        grid[i] = grid[i][:j] + "." + grid[i][j + 1:]

    return grid


def tilt(grid, direction):
    # Define values for each direction
    match direction:
        case "west":
            idir, jdir, skiprange = 0, -1, 1
        case "east":
            idir, jdir, skiprange = 0, 1, -1
        case "north":
            idir, jdir, skiprange = -1, 0, 1
        case "south":
            idir, jdir, skiprange = 1, 0, -1

    # For each square of the grid
    for i in range(len(grid))[::skiprange]:
        for j in range(len(grid[0]))[::skiprange]:
            # Find round rocks
            if grid[i][j] == "O":
                grid = move_rock(grid, i, j, idir, jdir)

    return grid


def run_cycle(grid):
    # Compute tilt
    for direction in ["north", "west", "south", "east"]:
        grid = tilt(grid, direction)

    # Cache in records
    records.append(repr(grid))

    return grid


def find_starting_cycle():
    start = 0
    gap = 0

    rev = records[::-1]
    rlen = len(records)
    for item in records:
        i, ri = records.index(item), rlen - rev.index(item) - 1
        if ri - i > gap:
            start = i
            gap = ri - i

    return start + goal // gap * gap


def main():
    with open("input.txt") as f:
        grid = [l.strip() for l in f.readlines()]
        cycle = 0

        # Run cycles to get gaps
        for _ in range(1000):
            grid = run_cycle(grid)

        # Jump through cycles and compute the last ones
        cycle = find_starting_cycle()
        while cycle < goal:
            grid = run_cycle(grid)
            cycle += 1
        
        # Compute the load
        load = compute_load(grid)
        print(load)


if __name__ == "__main__":
    main()
