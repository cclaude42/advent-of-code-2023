import re

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
        node = "AAA"
        nsteps = 0
        while node != "ZZZ":
            node = nodemap[node][instructions[nsteps % ilen]]
            nsteps += 1

        print(nsteps)


if __name__ == "__main__":
    main()
