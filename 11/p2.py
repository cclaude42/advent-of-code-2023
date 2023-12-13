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


def get_galaxies(grid, expansion_size):
    galaxies = []
    v_indexes = get_vertical_empty_lines(grid)
    h_indexes = get_horizontal_empty_lines(grid)

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[i][j] == "#":
                x = i + h_indexes[:i].count(True) * (expansion_size - 1)
                y = j + v_indexes[:j].count(True) * (expansion_size - 1)
                galaxies.append((x, y))

    return galaxies


def main(expansion_size):
    total = 0

    with open("input.txt") as f:
        grid = [line.strip() for line in f.readlines()]

        galaxies = get_galaxies(grid, expansion_size)

        for galaxyA, galaxyB in itertools.combinations(galaxies, 2):
            total += compute_distance(galaxyA, galaxyB)

    return total


if __name__ == "__main__":
    for s in [2, 10, 100, 1000, 1000000]:
        res = main(s)
        print(f"{s}: {res}")
