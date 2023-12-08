def main():
    with open("input.txt") as f:
        seeds = [int(s) for s in f.readline().split(": ")[1].split()]
        conversions = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
        conversion_dict = dict()
        results = []

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

        # For each set of seeds...
        iter_seeds = iter(seeds)
        paired_seeds = zip(iter_seeds, iter_seeds)
        for start, length in paired_seeds:
            seedranges = [range(start, start+length)]

            # And for each conversion type...
            for conversion in conversions:
                converted_seedranges = []

                # Iterate through a subrange
                for seedrange in seedranges:
                    for rng in conversion_dict[conversion]:
                        conversion_range = range(rng["src"], rng["src"] + rng["length"])

                        # If ranges intersect...
                        if seedrange[0] <= conversion_range[-1] and conversion_range[0] <= seedrange[-1]:
                            r = range(max(seedrange[0], conversion_range[0]), min(seedrange[-1], conversion_range[-1]) + 1)

                            # Convert and record the range
                            diff = rng["dst"] - rng["src"]
                            converted_seedranges.append(range(r[0] + diff, r[-1] + diff + 1))

                            # And cut it from prev range
                            if conversion_range[0] > seedrange[0]:
                                seedranges.append(range(seedrange[0], conversion_range[0]))
                            if conversion_range[-1] < seedrange[-1]:
                                seedranges.append(range(conversion_range[-1] + 1, seedrange[-1] + 1))

                            # Return to loop
                            seedrange = None
                            break

                    # If no match, leave range as it is
                    if seedrange:
                        converted_seedranges.append(seedrange)

                seedranges = converted_seedranges

            results += [min(r) for r in seedranges]

        print(min(results))


if __name__ == "__main__":
    main()
