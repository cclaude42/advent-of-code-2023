def main():
    with open("input.txt") as f:
        times, distances = [s.split(":")[1].split() for s in f.readlines()]
        zipped = zip(times, distances)
        total = 1

        for time, distance in zipped:
            wins = 0

            for n in range(int(time) + 1):
                if n * (int(time) - n) > int(distance):
                    wins += 1

            total *= wins

        print(total)

if __name__ == "__main__":
    main()
