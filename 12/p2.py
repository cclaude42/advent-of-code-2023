import re

# Pre-compute patterns for efficiency
patterns = {n: re.compile(f"[#?]{{{n}}}[\.?$]") for n in range(20)}
cache = dict()


def compute_arrangement(springs, config):
    # If no more springs to find, check if solution works (no more #)
    if not config:
        if springs.count("#") == 0:
            return 1
        else:
            return 0
    
    # Init and fetch regex pattern
    total = 0
    idx = 0
    pattern = patterns[config[0]]

    # While match
    while match := pattern.search(springs, idx):
        # If # before match, invalid configuration
        if "#" in springs[:match.start()]:
            return total

        # Else recurse to compute sub-ranges
        total += cache_compute_arrangement(springs[match.end():], config[1:])
        idx = match.start() + 1

    return total


def cache_compute_arrangement(springs, config):
    # Build a string for dict hashing
    h = f"{springs} {repr(config)}"
    
    # Return cached result
    if h in cache.keys():
        return cache[h]

    # Else cache result
    res = compute_arrangement(springs, config)
    cache[h] = res

    return res


def main():
    with open("input.txt") as f:
        total = 0

        for i, line in enumerate(f.readlines()):
            springs, config = line.strip().split()
            config = [int(n) for n in config.split(",")]

            springs = (springs + "?") * 5
            config = config * 5

            res = compute_arrangement(springs[:-1] + ".", config)
            total += res

        print("Total:", total)



if __name__ == "__main__":
    main()
