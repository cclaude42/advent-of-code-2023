import re, functools


def get_primes(cycle):
    primes = []
    n = 2

    while n < cycle:
        if cycle % n == 0:
            primes.append(n)
            cycle = cycle // n
            n = 2
        else:
            n += 1

    primes.append(cycle)
    return primes


def compute_cycle(nodemap, instructions, node):
    states = []
    ncopy = node
    nsteps = 0
    ilen = len(instructions)

    while not (ncopy, nsteps % ilen) in states:
        states.append((ncopy, nsteps % ilen))
        ncopy = nodemap[ncopy][instructions[nsteps % ilen]]
        nsteps += 1

    return nsteps - states.index((ncopy, nsteps % ilen))


def main():
    with open("input.txt") as f:
        lines = f.readlines()
        
        # Parse instructions
        instructions = lines[0].strip()
        ilen = len(instructions)
        
        # Parse nodes
        nodemap = dict()
        for line in lines[2:]:
            node, left, right = re.search("(...) = \((...), (...)\)", line).groups()
            nodemap[node] = {
                "L": left,
                "R": right
            }

        # Run through nodes
        nodes = [node for node in nodemap.keys() if node[-1] == "A"]
        cycles = [compute_cycle(nodemap, instructions, node) for node in nodes]

        # Primify
        primes = []
        for cycle in cycles:
            primes += get_primes(cycle)
        
        lcd = functools.reduce(lambda x, y: x * y, list(set(primes)))
        print(lcd)


if __name__ == "__main__":
    main()
