def main():
    with open("input.txt") as f:
        total = 0

        for l in f.readlines():
            subtotal = 0
            _, game = l.split(":")
            winning, scratched = (g.strip().split() for g in game.split("|"))

            for num in scratched:
                if num in winning:
                    if subtotal:
                        subtotal *= 2
                    else:
                        subtotal = 1

            total += subtotal

        print(total)


if __name__ == "__main__":
    main()
