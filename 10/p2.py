import math

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

def clean_grid(grid, prev_pos, pos):
    main_pipe = {pos, prev_pos}

    while get_pipe(grid, pos) != "S":
        pipe = get_pipe(grid, pos)
        dir1, dir2 = pipes[pipe]

        if go_to(pos, dir1) == prev_pos:
            dir1, dir2 = dir2, dir1

        prev_pos = pos
        pos = go_to(pos, dir1)
        main_pipe.add(pos)

    for point in [(x, y) for x in range(len(grid)) for y in range(len(grid[0]))]:
        if get_pipe(grid, point) != "." and not point in main_pipe:
            x, y = point
            grid[x] = grid[x][:y] + "." + grid[x][y + 1:]


def go_to(pos, direction):
    x1, y1 = pos
    x2, y2 = directions[direction]
    return x1 + x2, y1 + y2


def get_pipe(grid, pos):
    x, y = pos
    return grid[x][y]


def get_angle(fixed_point, old_pos, new_pos):
    old_tan = math.atan2(old_pos[1] - fixed_point[1], old_pos[0] - fixed_point[0])
    new_tan = math.atan2(new_pos[1] - fixed_point[1], new_pos[0] - fixed_point[0])
    ang = math.degrees(old_tan - new_tan)
    return - math.copysign(360 - abs(ang), ang) if abs(ang) > 180 else ang


def main():
    with open("input.txt") as f:
        # Parse grid and start position
        grid = [l.strip() for l in f.readlines()]
        s_index = ["S" in line for line in grid].index(True)
        start_pos = (s_index, grid[s_index].index("S"))

        # Find first connected pipe
        for any_dir in directions.keys():
            pos = go_to(start_pos, any_dir)
            pipe_dirs = pipes[get_pipe(grid, pos)]
            pipe_outs = [go_to(pos, pipe_dir) == start_pos for pipe_dir in pipe_dirs]

            if any(pipe_outs):
                break

        clean_grid(grid, start_pos, pos)
        print("done cleaning!")

        number_inside = 0
        backup_pos = pos
        all_points = [(x, y) for x in range(len(grid)) for y in range(len(grid[0]))]
        erg = [point for point in all_points if get_pipe(grid, point) == "."]
        for i, fixed_point in enumerate(erg):
            prev_pos, pos = start_pos, backup_pos
            winding = get_angle(fixed_point, prev_pos, pos)

            # Run through pipes until back to start
            while get_pipe(grid, pos) != "S":
                pipe = get_pipe(grid, pos)
                dir1, dir2 = pipes[pipe]

                if go_to(pos, dir1) == prev_pos:
                    dir1, dir2 = dir2, dir1

                prev_pos = pos
                pos = go_to(pos, dir1)
                winding += get_angle(fixed_point, prev_pos, pos)

            winding = int(round(winding, 0))
            if winding == 360 or winding == -360:
                number_inside += 1
                print(f"found inside at {fixed_point} ({i}/{len(erg)})")
            else:
                print(f"found nothin ({i}/{len(erg)})")

        print(number_inside)



if __name__ == "__main__":
    main()
