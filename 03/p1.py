import re


def has_symbol_at (engine, x, y):
    # Return false if negative (out of range)
    if x < 0 or y < 0:
        return False
    # Return false if exception (out of range)
    try:
        c = engine[x][y]
    except IndexError:
        return False
    # Else return char 
    else:
        return engine[x][y] not in ".0123456789"


def has_symbol_around (engine, match, x):
    # Check left and right
    results = [
        has_symbol_at(engine, x, match.start() - 1),
        has_symbol_at(engine, x, match.end()),
    ]

    # Check up and down for each pos, from left to right
    for y in range(match.start() - 1, match.end() + 1):
        results.append(has_symbol_at(engine, x - 1, y))
        results.append(has_symbol_at(engine, x + 1, y))

    # Return true if any match
    return any(results)


def main ():
    with open("input.txt") as f:
        engine = f.readlines()
        pattern = re.compile("\d+")
        total = 0

        # For each line
        for x, line in enumerate(engine):
            pos = 0
            # Find each number
            while match := pattern.search(line, pos):
                # Add to total if number has a symbol around
                if has_symbol_around(engine, match, x):
                    total += int(match.group(0))
                # Move pos to find next number
                pos = match.end()

        print(total)

if __name__ == "__main__":
    main()