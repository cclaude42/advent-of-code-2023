directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

pipes = {
    ".": (),
    "-": ("left", "right"),
    "|": ("up", "down"),
    "L": ("up", "right"),
    "J": ("up", "left"),
    "F": ("down", "right"),
    "7": ("down", "left")
}


def go_to(pos, direction):
    x1, y1 = pos
    x2, y2 = directions[direction]
    return x1 + x2, y1 + y2


def get_pipe(grid, pos):
    x, y = pos
    return grid[x][y]


def main():
    with open("input.txt") as f:
        # Parse grid and start position
        grid = f.readlines()
        s_index = ["S" in line for line in grid].index(True)
        prev_pos = (s_index, grid[s_index].index("S"))
        pos = None
        n = 1

        # Find first connected pipe
        for any_dir in directions.keys():
            pos = go_to(prev_pos, any_dir)
            pipe_dirs = pipes[get_pipe(grid, pos)]
            pipe_outs = [go_to(pos, pipe_dir) == prev_pos for pipe_dir in pipe_dirs]

            if any(pipe_outs):
                break

        # Run through pipes until back to start
        while get_pipe(grid, pos) != "S":
            pipe = get_pipe(grid, pos)
            dir1, dir2 = pipes[pipe]

            if go_to(pos, dir1) == prev_pos:
                dir1, dir2 = dir2, dir1

            prev_pos = pos
            pos = go_to(pos, dir1)
            n += 1

        print(n // 2)


if __name__ == "__main__":
    main()
