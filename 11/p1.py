import itertools

def get_vertical_empty_lines(grid):
    indexes = []
    for i in range(len(grid[0])):
        indexes.append(all(l[i] == '.' for l in grid))
    return indexes


def get_horizontal_empty_lines(grid):
    return [len(set(line)) == 1 for line in grid]


def expand_grid(grid):
    new_grid = []
    v_indexes = get_vertical_empty_lines(grid)
    h_indexes = get_horizontal_empty_lines(grid)

    for line, is_h in zip(grid, h_indexes):
        newline = ""

        for c, is_v in zip(line, v_indexes):
            if is_v:
                newline += c
            newline += c

        if is_h:
            new_grid.append(newline)
        new_grid.append(newline)

    return new_grid


def compute_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_galaxies(grid):
    galaxies = []
    h_len = len(grid[0])
    v_len = len(grid)

    for i in range(v_len):
        for j in range(h_len):
            if grid[i][j] == "#":
                galaxies.append((i, j))

    return galaxies


def main():
    with open("input.txt") as f:
        grid = [l.strip() for l in f.readlines()]
        total = 0

        grid = expand_grid(grid)
        galaxies = get_galaxies(grid)

        for galaxyA, galaxyB in itertools.combinations(galaxies, 2):
            total += compute_distance(galaxyA, galaxyB)

        print(total)



if __name__ == "__main__":
    main()
