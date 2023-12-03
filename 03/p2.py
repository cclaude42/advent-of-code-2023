import re

def has_gear_at (engine, x, y):
    # Return false if negative (out of range)
    if x < 0 or y < 0:
        return False
    # Return false if exception (out of range)
    try:
        c = engine[x][y]
    except IndexError:
        return False
    # Else return gear position
    else:
        if engine[x][y] is '*':
            return (x, y)
        else:
            return False


def find_gears_around (engine, match, x):
    # Check left and right
    results = [
        has_gear_at(engine, x, match.start() - 1),
        has_gear_at(engine, x, match.end()),
    ]

    # Check up and down for each pos, from left to right
    for y in range(match.start() - 1, match.end() + 1):
        results.append(has_gear_at(engine, x - 1, y))
        results.append(has_gear_at(engine, x + 1, y))

    # Return gear positions
    return [r for r in results if r]


def main ():
    with open("input.txt") as f:
        engine = f.readlines()
        pattern = re.compile("\d+")
        gears = dict()
        total = 0

        # For each line
        for x, line in enumerate(engine):
            pos = 0
            # Find each gear
            while match := pattern.search(line, pos):
                # Record numbers next to gears
                for gear in find_gears_around(engine, match, x):
                    gears.setdefault(gear, []).append(int(match.group(0)))
                # Move pos to find next gear
                pos = match.end()

        for gear in gears.values():
            if len(gear) == 2:
                total += gear[0] * gear[1]

        print(total)

if __name__ == "__main__":
    main()
