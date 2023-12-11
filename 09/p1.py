def main():
    with open("input.txt") as f:
        total = 0

        for line in f.readlines():
            nums = [int(n) for n in line.split()]
            matrix = [nums]

            # While last row isn't zeroes
            while any(matrix[-1]):
                new_row = []
                # Create next row by subtracting zipped pairs
                for a, b in zip(matrix[-1], matrix[-1][1:]):
                    new_row.append(b - a)
                matrix.append(new_row)

            # Add up all end-of-row values
            total += sum(row[-1] for row in matrix)

        print(total)


if __name__ == "__main__":
    main()
