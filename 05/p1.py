def main():
    with open("input.txt") as f:
        seeds = [int(s) for s in f.readline().split(": ")[1].split()]
        results = []
        conversions = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
        conversion_dict = dict()

        # For each type of conversion
        for conversion in conversions:
            conversion_dict[conversion] = []
            # Watch for header
            while not conversion in f.readline():
                pass
            # Loop through numbers
            while True:
                line = f.readline()
                if line.strip():
                    dst, src, length = [int(n) for n in line.strip().split()]
                    node = {
                        "dst": dst,
                        "src": src,
                        "length": length
                    }
                    conversion_dict[conversion].append(node)
                # Stop when empty line
                else:
                    break

        # Iterate through seeds
        for seed in seeds:
            n = seed
            # Convert each step
            for conversion in conversions:
                for rng in conversion_dict[conversion]:
                    if n in range(rng["src"], rng["src"] + rng["length"]):
                        n = rng["dst"] + (n - rng["src"])
                        break
                # If not converted, ignore and move to next
            results.append(n)

        print(min(results))


if __name__ == "__main__":
    main()
