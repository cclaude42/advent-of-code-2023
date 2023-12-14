def compute_load(grid):
    load = 0
    for n, line in enumerate(grid[::-1]):
        load += line.count("O") * (n + 1)
    return load


def tilt_up(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                x = i
                while x > 0 and grid[x - 1][j] == ".":
                    x -= 1
                if i != x:
                    grid[x] = grid[x][:j] + "O" + grid[x][j + 1:]
                    grid[i] = grid[i][:j] + "." + grid[i][j + 1:]
    return grid


def main():
    with open("input.txt") as f:
        grid = [l.strip() for l in f.readlines()]
        grid = tilt_up(grid)
        load = compute_load(grid)
        print(load)


if __name__ == "__main__":
    main()
