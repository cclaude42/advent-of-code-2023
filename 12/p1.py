import re

def compute_arrangement(springs, config):
    if not config:
        if springs.count("#") == 0:
            return 1
        else:
            return 0

    pattern = re.compile(f"[#?]{{{config[0]}}}[\.?$]")
    total = 0
    idx = 0

    while match := pattern.search(springs, idx):
        if "#" in springs[:match.start()]:
            return total
        total += compute_arrangement(springs[match.end():], config[1:])
        idx = match.start() + 1

    return total


def main():
    with open("input.txt") as f:
        total = 0

        for line in f.readlines():
            springs, config = line.strip().split()
            config = [int(n) for n in config.split(",")]

            total += compute_arrangement(springs + ".", config)

        print(total)



if __name__ == "__main__":
    main()
